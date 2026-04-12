from __future__ import annotations

import json
from pathlib import Path
from typing import Any

Message = dict[str, str]


def save_session(path: str | Path, messages: list[Message]) -> None:
    """Save messages to a JSON file on disk."""
    # TODO (HackerRank-style): write your code here.
    raise NotImplementedError


def load_session(path: str | Path) -> list[Message]:
    """Load messages from a JSON file.

    Rules:
    - If file missing: return []
    - Validate shape; raise ValueError if invalid
    """
    # TODO (HackerRank-style): write your code here.
    raise NotImplementedError


def _validate_messages(value: Any) -> list[Message]:
    if not isinstance(value, list):
        raise ValueError("messages must be a list")

    out: list[Message] = []
    for i, item in enumerate(value):
        if not isinstance(item, dict):
            raise ValueError(f"messages[{i}] must be a dict")

        role = item.get("role")
        content = item.get("content")

        if not isinstance(role, str) or not role.strip():
            raise ValueError(f"messages[{i}].role must be a non-empty string")
        if not isinstance(content, str):
            raise ValueError(f"messages[{i}].content must be a string")

        out.append({"role": role, "content": content})

    return out
