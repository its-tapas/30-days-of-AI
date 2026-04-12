from __future__ import annotations

import json
from pathlib import Path

import pytest

from day3.lab2.session_store import load_session, save_session


def test_load_session_missing_file_returns_empty(tmp_path: Path) -> None:
    missing = tmp_path / "missing.json"
    assert load_session(missing) == []


def test_save_and_load_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "session.json"
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "hello"},
    ]

    save_session(path, messages)
    loaded = load_session(path)
    assert loaded == messages


def test_load_session_rejects_invalid_shape(tmp_path: Path) -> None:
    path = tmp_path / "bad.json"
    path.write_text(json.dumps({"version": 1, "messages": [123]}), encoding="utf-8")

    with pytest.raises(ValueError):
        load_session(path)
