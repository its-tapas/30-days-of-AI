# Day 3 — Lab 1 Guide (beginner, step-by-step)

## Repo constraints (must follow)

- **OS:** Windows
- **Shell:** PowerShell
- **Runtime:** Free + local only (Ollama). **No API keys.**
- **Independence:** This lab is independent; do **not** import code from other days.
- **Tests:** `day3/lab1/tests`
- **Reference solution:** `day3/solution/solution_lab1`

## Mini-theory (2–5 minutes, then hands-on)

### 1) Multi-turn chat memory is just “send the whole history”
Every time you ask the model something, you send:
- your **system** rules (optional)
- the conversation **so far**
- the new user message

That full history is what makes the model “remember”.

### 2) Why trim history?
If you never trim:
- Requests get bigger and slower
- Old messages become irrelevant noise
- You can exceed a context window (a real LLM limit)

So you trim to keep only the most recent turns.

### 3) Message roles (you must understand these)
- `system`: instructions/rules for the assistant (tone, constraints). Usually placed at the start.
- `user`: the human’s message
- `assistant`: the model’s reply

## 0) Setup (PowerShell)

From the repo root:

1) (Optional) Allow activation scripts in this terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

2) Activate your venv (if not already):
```powershell
& .\.venv\Scripts\Activate.ps1
```

3) Install deps (only if you haven’t):
```powershell
python -m pip install -r .\requirements.txt
```

## 1) Open the starter file

Open `day3/lab1/chat_memory.py`.

You will implement exactly these functions (they currently raise `NotImplementedError`):
- `trim_messages(messages, max_turns)`
- `build_chat_payload(model, messages, stream=False)`

Do not change the tests.

## 2) Implement TODO #1 — `trim_messages(messages, max_turns)`

Find this function:
```python
def trim_messages(messages: list[Message], max_turns: int) -> list[Message]:
```

### Goal
Return a **new list** of messages that:
- keeps all `system` messages
- keeps only the last `max_turns` turns (turn = user+assistant = 2 non-system messages)
- if `max_turns <= 0`, keeps only system messages

### What to type (line-by-line)

In `chat_memory.py`, go into `trim_messages(...)` and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (collect all system messages):
Explanation: System messages are “global rules” and must always be preserved.
```python
system_messages = [m for m in messages if m.get("role") == "system"]
```

Step 2 (collect all non-system messages):
Explanation: A “turn” consists of user+assistant messages, so we only count non-system messages toward turns.
```python
non_system_messages = [m for m in messages if m.get("role") != "system"]
```

Step 3 (edge case: keep only system messages when `max_turns <= 0`):
Explanation: If `max_turns` is zero/negative, we keep conversation empty but still keep the system rules.
```python
if max_turns <= 0:
```

Step 4 (return early for the edge case):
Explanation: Returning here avoids any slicing math and guarantees only system messages remain.
```python
    return system_messages
```

Step 5 (convert turns → number of non-system messages to keep):
Explanation: 1 turn = 2 messages (user + assistant), so 2 turns = 4 messages.
```python
keep_n = max_turns * 2
```

Step 6 (slice to keep only the last `keep_n` non-system messages):
Explanation: Negative slicing keeps the newest messages and drops the oldest ones first.
```python
kept_non_system = non_system_messages[-keep_n:]
```

Step 7 (return system + trimmed conversation):
Explanation: The output order is: all system messages first, then the trimmed conversation.
```python
return system_messages + kept_non_system
```

### Common beginner mistakes (avoid these)

- Explanation: Don’t mutate the input list; return a new list.
- Explanation: One “turn” is **two** messages (user + assistant).
- Explanation: Never drop system messages.

## 3) Implement TODO #2 — `build_chat_payload(model, messages, stream=False)`

Find this function:
```python
def build_chat_payload(*, model: str, messages: list[Message], stream: bool = False) -> dict[str, Any]:
```

### Goal
Return a dict shaped like an Ollama `/api/chat` JSON payload:
```python
{
  "model": "...",
  "messages": [...],
  "stream": False,
}
```

### What to type (line-by-line)

In `chat_memory.py`, go into `build_chat_payload(...)` and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (strip and validate the model):
Explanation: A model name is required. Stripping avoids failures caused by trailing spaces.
```python
model_clean = (model or "").strip()
```

Step 2 (reject empty model):
Explanation: If it’s empty after stripping, we stop here with a clear error.
```python
if not model_clean:
```

Step 3 (raise ValueError for empty model):
Explanation: This makes failures obvious and matches the test expectation (a `ValueError` for empty model).
```python
    raise ValueError("model must be non-empty")
```

Step 4 (return the payload dict):
Explanation: This is the exact JSON shape Ollama `/api/chat` expects (and what the tests assert).
```python
return {"model": model_clean, "messages": messages, "stream": stream}
```

## 4) Run unit tests (no Ollama required)

From repo root:
```powershell
python -m pytest -q day3/lab1/tests
```

If a test fails:
- Read the assertion message carefully (it tells you what shape/value was expected)
- Re-check the rules in the docstring of the function you’re implementing

## 5) Optional: run the interactive chat (requires Ollama)

### 5.1 Start Ollama
In a separate PowerShell window:
```powershell
ollama serve
```

If you don’t have a model yet:
```powershell
ollama pull gemma2:2b
```

### 5.2 Run the script
From repo root:
```powershell
python day3/lab1/chat_memory.py
```

Type 2–3 messages. Then type `exit`.

### Troubleshooting

- If you see “Ollama not reachable…”, confirm `ollama serve` is running.
- If you want to override the model:
```powershell
$env:OLLAMA_MODEL="gemma2:2b"
python day3/lab1/chat_memory.py
```

## Acceptance criteria (checklist)

- `python -m pytest -q day3/lab1/tests` passes
- (Optional) Interactive chat runs and keeps context across turns
- You can explain what `system`, `user`, and `assistant` roles mean
