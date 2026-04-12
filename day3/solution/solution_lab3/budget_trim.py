from __future__ import annotations

Message = dict[str, str]


def trim_messages_by_chars(messages: list[Message], max_chars: int) -> list[Message]:
    system_messages: list[Message] = []
    conversation: list[Message] = []

    for msg in messages:
        if msg.get("role") == "system":
            system_messages.append(msg)
        else:
            conversation.append(msg)

    if max_chars <= 0 or not conversation:
        return list(system_messages)

    kept_reversed: list[Message] = []
    total = 0

    # Always include the most recent non-system message.
    last = conversation[-1]
    kept_reversed.append(last)
    total += len(str(last.get("content", "")))

    for msg in reversed(conversation[:-1]):
        msg_len = len(str(msg.get("content", "")))
        if total + msg_len <= max_chars:
            kept_reversed.append(msg)
            total += msg_len

    kept = list(reversed(kept_reversed))
    return list(system_messages) + kept
