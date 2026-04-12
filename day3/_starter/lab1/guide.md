# Day 3 — Lab 1 Guide (step-by-step)

## Mini-theory (2–5 minutes)

- A chat is a list of **messages**.
- Each message has:
  - `role`: who said it (`system`, `user`, `assistant`)
  - `content`: the text
- "Memory" is just **including previous messages** on every request.
- If you never trim history, your request grows forever (slower, less relevant, can exceed context limits).

## 0) Open the starter code

File: `day3/lab1/chat_memory.py`

You’ll implement 2 TODO functions:
- `trim_messages(messages, max_turns)`
- `build_chat_payload(model, messages, stream=False)`

## 1) Implement TODO #1 — `trim_messages`

Find:
- `def trim_messages(messages: list[Message], max_turns: int) -> list[Message]:`

Implement the rules exactly:

1) Split messages into:
   - **system** messages (role == `system`)
   - **conversation** messages (role != `system`)

2) Decide how many conversation messages to keep:
   - `keep_n = max_turns * 2`

3) If `max_turns <= 0`:
   - return only the system messages

4) Otherwise:
   - keep only the **last** `keep_n` conversation messages
   - return: `system_messages + kept_conversation_messages`

Important: return a **new list** (don’t mutate the input).

## 2) Implement TODO #2 — `build_chat_payload`

Find:
- `def build_chat_payload(...):`

Implement:
1) Strip `model` and validate it’s non-empty.
   - If empty, raise `ValueError("model must be non-empty")`
2) Return:

```python
{
  "model": model,
  "messages": messages,
  "stream": stream,
}
```

## 3) Run tests (does NOT require Ollama)

From repo root:

```powershell
python -m pytest -q day3/lab1/tests
```

If tests fail, read the assertion message — it tells you what shape is expected.

## 4) Run the script (requires Ollama running)

Start Ollama (if needed):
- `ollama serve`

Then run:

```powershell
python day3/lab1/chat_memory.py
```

Try 3 turns, then type `exit`.

## Acceptance criteria

- All tests pass
- Your chat keeps memory across turns (responses reflect earlier messages)
