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

### What to type (line-by-line)

In `budget_trim.py`, go to the TODO function and **delete** the line:

```python
raise NotImplementedError
```

Then type the following lines **in order**.

Step 1 (keep all `system` messages):
Explanation: System messages are global rules/instructions; we always keep them and do not count them in the budget.
```python
system_messages = [m for m in messages if m.get("role") == "system"]
```

Step 2 (collect the non-system conversation messages):
Explanation: Only `user` and `assistant` messages compete for the character budget.
```python
conversation = [m for m in messages if m.get("role") != "system"]
```

Step 3 (edge case: zero/negative budget keeps only system messages):
Explanation: A non-positive budget means “keep no conversation”.
```python
if max_chars <= 0:
```

Step 4 (return early for the edge case):
Explanation: We return immediately because no conversation messages are allowed under this budget.
```python
    return system_messages
```

Step 5 (edge case: no conversation messages):
Explanation: If there are no non-system messages, the answer is just the system messages.
```python
if not conversation:
```

Step 6 (return system-only when conversation is empty):
Explanation: With no conversation messages, there is nothing to budget-trim.
```python
    return system_messages
```

Step 7 (running total of kept conversation character count):
Explanation: We track the total characters of the kept non-system messages.
```python
total_chars = 0
```

Step 8 (build the kept messages while walking backwards):
Explanation: We will scan from newest to oldest, so we temporarily store kept messages in reverse order.
```python
kept_reversed: list[Message] = []
```

Step 9 (always keep the newest non-system message):
Explanation: The rules require we keep the newest message even if it alone exceeds the budget.
```python
newest = conversation[-1]
```

Step 10 (append newest to kept list):
Explanation: This begins the kept set with the most recent message.
```python
kept_reversed.append(newest)
```

Step 11 (add its length to the budget counter):
Explanation: We count characters using `len(content)`; missing content counts as 0.
```python
total_chars += len(newest.get("content", ""))
```

Step 12 (iterate older messages from newest→oldest):
Explanation: Now we consider older messages one by one, keeping them only if they still fit.
```python
for message in reversed(conversation[:-1]):
```

Step 13 (compute this message’s character cost):
Explanation: This is the “price” of keeping this message in the conversation history.
```python
    message_chars = len(message.get("content", ""))
```

Step 14 (only keep it if it fits in the remaining budget):
Explanation: We keep a message only if adding it would not exceed `max_chars`.
```python
    if total_chars + message_chars <= max_chars:
```

Step 15 (keep the message):
Explanation: This message fits, so we include it.
```python
        kept_reversed.append(message)
```

Step 16 (update the running total):
Explanation: Update the running character count after keeping it.
```python
        total_chars += message_chars
```

Step 17 (reverse back to restore original order):
Explanation: We built the list backwards; reversing restores chronological order.
```python
kept = list(reversed(kept_reversed))
```

Step 18 (return system + trimmed conversation):
Explanation: Final output preserves system messages and includes as many recent messages as allowed.
```python
return system_messages + kept
```

### Common beginner mistakes (avoid these)

- Explanation: Don’t count characters for system messages.
- Explanation: Trim from the end (keep the newest messages), not from the front.
- Explanation: Always keep the newest non-system message, even if it exceeds `max_chars`.

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
