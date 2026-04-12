# Day 3 Notes — Chat Memory + Session Save/Load + Trimming

## Abbreviations / technical terms

| Term | Meaning |
|---|---|
| Message | A small object like `{ "role": "user", "content": "..." }`. |
| Role | Who said it: `system`, `user`, or `assistant`. |
| Turn | One pair of messages: `user` + `assistant` (2 messages). |
| Memory | Including prior messages on each request. |
| Context window | The max history a model can consider (token-limited). |
| Trimming | Dropping older messages to stay within a budget. |
| Budget | A limit like max turns, max tokens, or max characters. |
| Persistence | Saving session state to disk and loading it later. |
| Schema validation | Checking loaded data has the expected shape and types. |
| Summarization | Replacing old history with a short summary message. |

## Topics (1-liners)

| Topic | One-liner |
|---|---|
| Messages array | Chat input is a list of `{role, content}` objects. |
| System messages | Set rules/style once; keep them at the start. |
| Turn trimming | Keep system + last N turns to prevent unlimited growth. |
| Budget trimming | Keep recent messages under a size limit (tokens/chars). |
| Session persistence | Save/load the message list to resume conversations. |
| Validation | Treat disk input as untrusted; validate before using. |
| Summary strategy | Summarize older context instead of fully dropping it. |

## The practical chat mental model

A chat model does not “remember your session” automatically.

You provide memory by sending a message list every time:

1) Start with optional system message(s)
2) Append new user message
3) (Optionally) trim or summarize old history
4) Send `messages` to `/api/chat`
5) Append assistant response back into `messages`

## `/api/chat` payload shape (conceptual)

A typical payload looks like:

```json
{
  "model": "gemma2:2b",
  "messages": [
    {"role": "system", "content": "Be concise"},
    {"role": "user", "content": "What is an API?"}
  ],
  "stream": false
}
```

## Trimming strategies (you need one)

If you never trim, history grows forever.

### Strategy A — Trim by turns

Meaning:
- Keep system messages.
- Keep only the last `max_turns` turns.

Turn math:
- 1 turn ≈ 2 non-system messages
- Keep last `max_turns * 2` non-system messages

Edge cases:
- If `max_turns <= 0`, keep only system messages.

### Strategy B — Trim by budget (tokens or characters)

Meaning:
- Keep system messages.
- Keep as many recent messages as possible within a budget.

Important practical rule:
- Always keep the **most recent** user message (and often the most recent assistant message) even if it exceeds the budget.

### Strategy C — Summarize old messages

Meaning:
- Replace older history with one “summary” system or assistant message.

Why it works:
- Preserves important context while shrinking size.

## Session persistence (save/load)

A session is just:
- a version number
- the message list

Example file shape:

```json
{
  "version": 1,
  "messages": [
    {"role": "system", "content": "Be concise"},
    {"role": "user", "content": "hi"},
    {"role": "assistant", "content": "hello"}
  ]
}
```

When you load:
- If file missing → return empty list `[]`
- If file exists → parse JSON → validate → return messages

## Reusable helper functions (generic)

### `build_chat_payload(*, model: str, messages: list[dict], stream: bool = False, options: dict | None = None) -> dict`

Meaning:
- Builds request JSON for a chat call.

Key behaviors:
- Validate `model` non-empty
- Validate `messages` is a list
- Include `options` only if non-empty

### `trim_messages_by_turns(messages: list[dict], max_turns: int) -> list[dict]`

Meaning:
- Keeps system messages + the last N turns.

Rules:
- Split system vs non-system
- If `max_turns <= 0`: return system messages only
- Keep last `max_turns * 2` non-system messages

### `trim_messages_by_chars(messages: list[dict], max_chars: int) -> list[dict]`

Meaning:
- Keeps system messages + as many recent messages as fit in a char budget.

Rules:
- If `max_chars <= 0`: system only
- Walk from newest to oldest
- Always keep the newest non-system message

### `summarize_old_history(messages: list[dict]) -> dict`

Meaning:
- Converts older history into a compact summary message.

Typical output:
- `{ "role": "system", "content": "Summary: ..." }` or `{ "role": "assistant", "content": "Summary: ..." }`

### `save_session(path, messages: list[dict], version: int = 1) -> None`

Meaning:
- Writes `{version, messages}` as UTF-8 JSON.

Important details:
- Create parent folder(s)
- Consider atomic write (write temp file then rename) for reliability

### `load_session(path) -> list[dict]`

Meaning:
- Reads JSON and returns messages.

Rules:
- Missing file: return `[]`
- Invalid JSON/shape: raise `ValueError` with a clear message

### `validate_messages(value) -> list[dict]`

Meaning:
- Enforces message schema:
  - list of dicts
  - each dict has string `role` and string `content`

## Common pitfalls (and fixes)

- Forgetting to append assistant replies back to memory: always append both sides.
- Dropping system messages during trimming: preserve them.
- Trimming too aggressively: keep at least the newest user message.
- Loading corrupted sessions: validate shape before using.
- Using char budgets as “exact token budgets”: treat char budgets as an approximation.
