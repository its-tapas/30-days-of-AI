from __future__ import annotations

import argparse
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"
DEFAULT_OLLAMA_MODEL = "gemma2:2b"

_SESSION = requests.Session()


def normalize_base_url(base_url: str) -> str:
    base_url = (base_url or "").strip()
    if not base_url:
        base_url = DEFAULT_OLLAMA_BASE_URL
    return base_url.rstrip("/")


def validate_controls(temperature: float, max_output_tokens: int) -> None:
    if not (0.0 <= temperature <= 1.0):
        raise ValueError("--temperature should be between 0.0 and 1.0")
    if max_output_tokens <= 0:
        raise ValueError("--max-output-tokens must be > 0")


def build_generate_payload(
    *,
    model: str,
    prompt: str,
    system: str,
    temperature: float,
    max_output_tokens: int,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_output_tokens,
        },
    }

    system = (system or "").strip()
    if system:
        payload["system"] = system

    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Day 2 Lab 1 solution: prompt controls playground (Ollama)"
    )
    parser.add_argument("--prompt", help="User prompt text")
    parser.add_argument("--system", default="", help="System prompt (rules/style)")
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-output-tokens", type=int, default=200)
    parser.add_argument("--model", default="", help="Override model (optional)")
    args = parser.parse_args()

    prompt = (args.prompt or "").strip() or input("Prompt> ").strip()
    if not prompt:
        print("[error] No prompt provided.")
        return 2

    base_url = normalize_base_url(os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL))
    model = (
        (args.model or "").strip()
        or os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL).strip()
        or DEFAULT_OLLAMA_MODEL
    )

    try:
        validate_controls(args.temperature, args.max_output_tokens)
    except ValueError as exc:
        print(f"[error] {exc}")
        return 2

    url = f"{base_url}/api/generate"
    payload = build_generate_payload(
        model=model,
        prompt=prompt,
        system=args.system,
        temperature=args.temperature,
        max_output_tokens=args.max_output_tokens,
    )

    try:
        resp = _SESSION.post(url, json=payload, timeout=60)
    except requests.exceptions.ConnectionError:
        print(f"[error] Ollama not reachable at {base_url}. Start Ollama (or run `ollama serve`).")
        return 1
    except requests.exceptions.Timeout:
        print(f"[error] Timed out calling {url}.")
        return 1

    if resp.status_code != 200:
        detail = (resp.text or "").strip()
        print(f"[error] Ollama returned HTTP {resp.status_code}: {detail or '<no details>'}")
        return 1

    data = resp.json()
    text = data.get("response")
    if not isinstance(text, str):
        print(f"[error] Unexpected response JSON: {data}")
        return 1

    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
