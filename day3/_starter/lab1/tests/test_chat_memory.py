from __future__ import annotations

import pytest

from day3.lab1.chat_memory import build_chat_payload, trim_messages


def test_trim_messages_keeps_system_and_last_turns() -> None:
    messages = [
        {"role": "system", "content": "You are helpful"},
        {"role": "user", "content": "u1"},
        {"role": "assistant", "content": "a1"},
        {"role": "user", "content": "u2"},
        {"role": "assistant", "content": "a2"},
        {"role": "user", "content": "u3"},
        {"role": "assistant", "content": "a3"},
    ]

    trimmed = trim_messages(messages, max_turns=2)

    assert trimmed[0] == {"role": "system", "content": "You are helpful"}
    assert trimmed[1:] == [
        {"role": "user", "content": "u2"},
        {"role": "assistant", "content": "a2"},
        {"role": "user", "content": "u3"},
        {"role": "assistant", "content": "a3"},
    ]


def test_trim_messages_max_turns_zero_keeps_only_system() -> None:
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "u1"},
        {"role": "assistant", "content": "a1"},
    ]

    assert trim_messages(messages, max_turns=0) == [{"role": "system", "content": "rules"}]


def test_build_chat_payload_shape() -> None:
    payload = build_chat_payload(
        model="gemma2:2b",
        messages=[{"role": "user", "content": "hi"}],
        stream=False,
    )

    assert payload["model"] == "gemma2:2b"
    assert payload["messages"] == [{"role": "user", "content": "hi"}]
    assert payload["stream"] is False


def test_build_chat_payload_rejects_empty_model() -> None:
    with pytest.raises(ValueError):
        build_chat_payload(model="   ", messages=[], stream=False)
