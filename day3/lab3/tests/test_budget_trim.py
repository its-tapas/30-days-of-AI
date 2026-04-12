from __future__ import annotations

from day3.lab3.budget_trim import trim_messages_by_chars


def test_trim_by_chars_keeps_system_and_recent_messages() -> None:
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "1234"},        # 4
        {"role": "assistant", "content": "aaaaa"},  # 5
        {"role": "user", "content": "xx"},          # 2
        {"role": "assistant", "content": "yyy"},    # 3
    ]

    trimmed = trim_messages_by_chars(messages, max_chars=5)

    assert trimmed == [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "xx"},
        {"role": "assistant", "content": "yyy"},
    ]


def test_trim_by_chars_budget_too_small_still_keeps_latest_non_system() -> None:
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "this-is-long"},
    ]

    trimmed = trim_messages_by_chars(messages, max_chars=1)

    assert trimmed == [
        {"role": "system", "content": "rules"},
        {"role": "assistant", "content": "this-is-long"},
    ]


def test_trim_by_chars_max_chars_zero_returns_only_system() -> None:
    messages = [
        {"role": "system", "content": "rules"},
        {"role": "user", "content": "hi"},
    ]

    assert trim_messages_by_chars(messages, max_chars=0) == [{"role": "system", "content": "rules"}]
