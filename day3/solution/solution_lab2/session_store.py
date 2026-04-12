from __future__ import annotations

import json
from pathlib import Path
from typing import Any

Message = dict[str, str]


def save_session(path: str | Path, messages: list[Message]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    obj = {
        "version": 1,
        "messages": _validate_messages(messages),
    }

    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def load_session(path: str | Path) -> list[Message]:
    path = Path(path)
    if not path.exists():
        return []

    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("session JSON must be an object")

    messages = data.get("messages")
    return _validate_messages(messages)


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
