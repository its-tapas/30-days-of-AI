# Day 3 — Lab 3 Guide (beginner, step-by-step)

## Repo constraints (must follow)

- **OS:** Windows
- **Shell:** PowerShell
- **Runtime:** Free + local only (no API keys)
- **Independence:** This lab is independent; do **not** import code from other days.
- **Tests:** `day3/lab3/tests`
- **Reference solution:** `day3/solution/solution_lab3`

## Mini-theory (2–5 minutes, then hands-on)

### Why a budget?
LLMs have a limited context window. If you send too much:
- requests get slow
- the model pays attention to old, irrelevant text
- you can exceed limits and get errors

### Why characters, not tokens?
Tokens are what models actually count, but tokenization is extra complexity.
A **character budget** is a simple approximation that teaches the same trimming strategy:
- keep the newest messages
- drop the oldest messages first

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

Open `day3/lab3/budget_trim.py`.

You will implement:
- `trim_messages_by_chars(messages, max_chars)`

## 2) Implement `trim_messages_by_chars(messages, max_chars)`

Find:
```python
def trim_messages_by_chars(messages: list[Message], max_chars: int) -> list[Message]:
```

### Step-by-step algorithm (matches the tests)

1) Split messages into two lists:
- `system_messages`: all messages where `role == "system"`
- `conversation`: all messages where `role != "system"`

2) Handle the edge case first:
- If `max_chars <= 0`, return `system_messages`

3) Now decide which conversation messages to keep:
- Start from the **end** of `conversation` (newest → oldest)
- Maintain `total_chars = 0`
- Maintain `kept_reversed = []` (because you’re walking backwards)

4) Always keep the newest non-system message:
- Take the last element of `conversation`, append it to `kept_reversed`
- Add its `len(content)` to `total_chars`
- (Even if this exceeds `max_chars`, you keep it anyway — this is required.)

5) For each remaining message (moving backwards):
- Compute `message_chars = len(message["content"])`
- Only keep it if `total_chars + message_chars <= max_chars`
- If you keep it, add to `kept_reversed` and increase `total_chars`

6) Reverse back to restore original order:
- `kept = list(reversed(kept_reversed))`

7) Return the final trimmed list:
- `system_messages + kept`

### Common beginner mistakes (avoid these)

- Counting characters for system messages (don’t; system messages are always kept)
- Trimming from the front (you must keep the most recent messages)
- Dropping the newest message when the budget is tiny (tests require keeping it)

## 3) Run tests

From repo root:
```powershell
python -m pytest -q day3/lab3/tests
```

If a test fails, open `day3/lab3/tests/test_budget_trim.py` and compare the expected list to what your function returns.

## Acceptance criteria (checklist)

- `python -m pytest -q day3/lab3/tests` passes
- System messages are always present in the output
- Output keeps the most recent non-system messages possible within the budget
- The newest non-system message is always kept, even if over budget
