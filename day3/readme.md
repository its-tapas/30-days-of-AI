# Day 3 — Chat Memory (3 Labs)

Time box: **2–3 hours**.

Day 3 has **3 Practical labs**:

- Lab 1: Maintain a multi-turn message history and build the Ollama `/api/chat` payload.
- Lab 2: Save and load a chat session (messages) to a JSON file.
- Lab 3: Trim memory by an approximate character budget.

## Folder structure (Day 3)

- `day3/lab1/`
  - `problem_statement.md`
  - `guide.md`
  - lab files (starter code with TODOs)
  - `tests/`
- `day3/lab2/` (same idea)
- `day3/lab3/` (same idea)
- `day3/solution/`
  - `solution_lab1/` (complete reference)
  - `solution_lab2/` (complete reference)
  - `solution_lab3/` (complete reference)

## Pre-req

- Ollama installed + running.
- A model pulled (example): `ollama pull gemma2:2b`.

## Lab 1

1) Read the problem:
- `day3/lab1/problem_statement.md`

2) Follow the step-by-step guide:
- `day3/lab1/guide.md`

3) Run tests (no Ollama required):

```powershell
python -m pytest -q day3/lab1/tests
```

4) Run the script (requires Ollama running):

```powershell
python day3/lab1/chat_memory.py
```

If stuck, reference solution:
- `day3/solution/solution_lab1/`

## Lab 2

1) Read the problem:
- `day3/lab2/problem_statement.md`

2) Follow the step-by-step guide:
- `day3/lab2/guide.md`

3) Run tests:

```powershell
python -m pytest -q day3/lab2/tests
```

If stuck, reference solution:
- `day3/solution/solution_lab2/`

## Lab 3

1) Read the problem:
- `day3/lab3/problem_statement.md`

2) Follow the step-by-step guide:
- `day3/lab3/guide.md`

3) Run tests:

```powershell
python -m pytest -q day3/lab3/tests
```

If stuck, reference solution:
- `day3/solution/solution_lab3/`

## Completion checklist

- Lab 1 tests pass
- Lab 2 tests pass
- Lab 3 tests pass
- You can run Lab 1 and chat for multiple turns

## Save + reset (optional)

When you finish the day, verify tests and reset labs back to starter code:

Note: reset uses `day3/_starter/` so it works even outside git.

```powershell
python day3/submit_day.py

# Mode: verify tests before reset
python day3/submit_day.py --verify
```
