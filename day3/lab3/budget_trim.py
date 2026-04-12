from __future__ import annotations

Message = dict[str, str]


def trim_messages_by_chars(messages: list[Message], max_chars: int) -> list[Message]:
    """Trim messages by an approximate character budget.

    Rules:
    - Keep all system messages
    - Keep as many non-system messages from the end as possible
    - Budget uses len(content)
    - If max_chars <= 0: keep only system messages
    - Always keep the most recent non-system message (even if it exceeds the budget)
    """
    # TODO (Practical): write your code here.
    raise NotImplementedError
