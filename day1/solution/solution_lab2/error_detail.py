from __future__ import annotations

from typing import Any


def extract_error_detail(*, response_text: str, response_json: dict[str, Any] | None) -> str:
    if response_json:
        error = response_json.get("error")
        if isinstance(error, str) and error.strip():
            return error.strip()

        message = response_json.get("message")
        if isinstance(message, str) and message.strip():
            return message.strip()

    return (response_text or "").strip()
