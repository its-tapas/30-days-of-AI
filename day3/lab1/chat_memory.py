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

Message = dict[str, str]


def normalize_base_url(base_url: str) -> str:
    """Return a usable Ollama base URL without a trailing slash."""
    base_url = (base_url or "").strip() or DEFAULT_OLLAMA_BASE_URL
    return base_url.rstrip("/")


def build_chat_url(base_url: str) -> str:
    """Return the full /api/chat URL."""
    return f"{normalize_base_url(base_url)}/api/chat"


def trim_messages(messages: list[Message], max_turns: int) -> list[Message]:
    """Return a trimmed copy of messages keeping at most max_turns turns.

    Rules:
    - Keep system message(s)
    - Keep only the last max_turns turns
      (a turn is 2 non-system messages: user + assistant)
    - If max_turns <= 0, keep only system message(s)
    """
    # TODO (HackerRank-style): write your code here.
    raise NotImplementedError


def build_chat_payload(*, model: str, messages: list[Message], stream: bool = False) -> dict[str, Any]:
    """Build the JSON payload for a non-streaming /api/chat request."""
    # TODO (HackerRank-style): write your code here.
    # Requirements:
    # - Return a dict with keys: model, messages, stream
    # - model must be non-empty after strip, else raise ValueError
    raise NotImplementedError


def _extract_assistant_text(data: dict[str, Any]) -> str:
    message = data.get("message")
    if isinstance(message, dict):
        content = message.get("content")
        if isinstance(content, str):
            return content

    # Fallback (some endpoints/versions use "response")
    response = data.get("response")
    if isinstance(response, str):
        return response

    raise ValueError(f"Unexpected chat response JSON: {data}")


def chat_once(*, base_url: str, model: str, messages: list[Message]) -> str:
    url = build_chat_url(base_url)
    payload = build_chat_payload(model=model, messages=messages, stream=False)

    try:
        resp = _SESSION.post(url, json=payload, timeout=60)
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError(
            f"Ollama not reachable at {base_url}. Start Ollama (or run `ollama serve`)."
        ) from exc
    except requests.exceptions.Timeout as exc:
        raise RuntimeError(f"Timed out calling {url}.") from exc

    if resp.status_code != 200:
        detail = (resp.text or "").strip()
        raise RuntimeError(f"Ollama returned HTTP {resp.status_code}: {detail or '<no details>'}")

    data = resp.json()
    return _extract_assistant_text(data)


def main() -> int:
    parser = argparse.ArgumentParser(description="Day 3 Lab 1: multi-turn chat memory")
    parser.add_argument("--system", default="", help="System prompt (rules/style)")
    parser.add_argument("--max-turns", type=int, default=6, help="How many turns to keep")
    parser.add_argument("--model", default="", help="Override model (optional)")
    args = parser.parse_args()

    base_url = normalize_base_url(os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL))
    model = (
        (args.model or "").strip()
        or os.getenv("OLLAMA_MODEL", DEFAULT_OLLAMA_MODEL).strip()
        or DEFAULT_OLLAMA_MODEL
    )

    messages: list[Message] = []
    system = (args.system or "").strip()
    if system:
        messages.append({"role": "system", "content": system})

    print("Type a message. Type 'exit' to quit.\n")

    while True:
        user = input("You> ").strip()
        if user.lower() in {"exit", "quit"}:
            break
        if not user:
            continue

        messages.append({"role": "user", "content": user})
        messages = trim_messages(messages, args.max_turns)

        try:
            assistant = chat_once(base_url=base_url, model=model, messages=messages)
        except RuntimeError as exc:
            print(f"[error] {exc}")
            return 1

        print(f"Bot> {assistant}\n")
        messages.append({"role": "assistant", "content": assistant})
        messages = trim_messages(messages, args.max_turns)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
