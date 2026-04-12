from __future__ import annotations

import argparse
import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_OLLAMA_MODEL = "gemma2:2b"

_SESSION = requests.Session()


def normalize_base_url(base_url: str) -> str:
    """Return a usable Ollama base URL without a trailing slash."""
    # TODO: implement
    # Requirements:
    # - Strip whitespace
    # - If empty, use DEFAULT_OLLAMA_BASE_URL
    # - Remove trailing '/'
    raise NotImplementedError


def build_generate_url(base_url: str) -> str:
    """Return the full /api/generate URL."""
    # TODO: implement using normalize_base_url()
    raise NotImplementedError


def build_stream_payload(model: str, prompt: str) -> dict[str, Any]:
    """Build the JSON payload for a streaming /api/generate request."""
    # TODO: implement
    # Requirements:
    # - Must return a dict with keys: model, prompt, stream
    # - stream must be True
    raise NotImplementedError


def main() -> int:
    parser = argparse.ArgumentParser(description="One-shot Ollama prompt (Day 1 demo)")
    parser.add_argument("prompt", nargs="?", help="Prompt text to send")
    args = parser.parse_args()

    prompt = (args.prompt or "").strip()
    if not prompt:
        prompt = input("Prompt> ").strip()

    if not prompt:
        print("[error] No prompt provided.")
        return 2

    base_url = os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL)
    model = os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL).strip() or DEFAULT_OLLAMA_MODEL

    url = build_generate_url(base_url)
    payload = build_stream_payload(model, prompt)

    try:
        resp = _SESSION.post(url, json=payload, timeout=60, stream=True)
    except requests.exceptions.ConnectionError:
        print(
            f"[error] Ollama not reachable at {base_url}. "
            "Start Ollama (or run `ollama serve`) and retry."
        )
        return 1
    except requests.exceptions.Timeout:
        print(f"[error] Timed out calling {url}. Try again.")
        return 1

    with resp:
        if resp.status_code != 200:
            detail = ""
            try:
                data = resp.json()
                detail = str(data.get("error") or data.get("message") or "").strip()
            except ValueError:
                pass
            if not detail:
                detail = (resp.text or "").strip()

            if resp.status_code == 404 or (
                "model" in detail.lower() and "not found" in detail.lower()
            ):
                print(f"[error] Model '{model}' missing. Run: ollama pull {model}")
                return 1

            print(f"[error] Ollama returned HTTP {resp.status_code}: {detail or '<no details>'}")
            return 1

        for line in resp.iter_lines(decode_unicode=True):
            if not line:
                continue

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            error = event.get("error")
            if isinstance(error, str) and error.strip():
                print(f"[error] {error.strip()}")
                return 1

            chunk = event.get("response")
            if isinstance(chunk, str) and chunk:
                print(chunk, end="", flush=True)

            if event.get("done") is True:
                break

    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
