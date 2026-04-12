# Day 3 — Lab 3 Guide (step-by-step)

## Mini-theory (2–5 minutes)

- LLMs have context limits; too much history makes requests slower and less relevant.
- You rarely have exact token counts in a simple script, so a practical first step is a **character budget**.
- The usual strategy is: keep the most recent messages, drop the oldest.

## 0) Open the starter code

File: `day3/lab3/budget_trim.py`

You’ll implement:
- `trim_messages_by_chars(messages, max_chars)`

## 1) Implement the algorithm

Find the TODO function and implement this approach:

1) Split messages into:
   - `system_messages` where `role == "system"`
   - `conversation` where `role != "system"`

2) If `max_chars <= 0`:
   - return `system_messages`

3) Walk `conversation` backwards (from newest to oldest) and keep messages while you can:
   - Maintain a running `total` of character count.
   - Always include the newest non-system message.
   - After that, only include a message if adding its content length keeps `total <= max_chars`.

4) Reverse the kept messages back to the original order.

5) Return: `system_messages + kept_conversation`.

Important:
- Return a new list.
- Don’t mutate the input list.

## 2) Run tests

From repo root:

```powershell
python -m pytest -q day3/lab3/tests
```

## Acceptance criteria

- All tests pass
- System messages are never dropped
- Most recent messages are preferred over old ones
