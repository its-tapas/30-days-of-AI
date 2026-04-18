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

### Step-by-step implementation approach

1) Create a list of system messages:
- system messages are those where `m.get("role") == "system"`

2) Create a list of non-system messages:
- everything that is not role `system`

3) Handle the “zero/negative turns” case first:
- if `max_turns <= 0`, return `system_messages`

4) Compute how many non-system messages you’re allowed to keep:
- `keep_n = max_turns * 2`

5) Keep only the last `keep_n` non-system messages:
- in Python slicing: `non_system_messages[-keep_n:]`

6) Return:
- `system_messages + kept_non_system`

### Common beginner mistakes (avoid these)

- Mutating the original list (safer to return a new list)
- Forgetting that a “turn” is **2** messages
- Dropping system messages (you must always keep them)

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

### Step-by-step

1) Normalize and validate `model`:
- `model = (model or "").strip()`
- If `model` is empty after stripping: `raise ValueError(...)`

2) Return the payload dict with keys exactly:
- `model`
- `messages`
- `stream`

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
