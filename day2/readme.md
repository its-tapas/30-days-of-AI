# Day 2 — Prompt Control (2 Labs)

Time box: **2–3 hours**.

Day 2 has **2 Practical labs**:

- Lab 1: Validate controls + build the Ollama request payload (`system`, `temperature`, `max-output-tokens`).
- Lab 2: Implement “system prompt modes” (reusable presets).

## Folder structure (Day 2)

- `day2/lab1/`
  - `problem_statement.md`
  - `guide.md`
  - lab files (starter code with TODOs)
  - `tests/`
- `day2/lab2/` (same idea)
- `day2/solution/`
  - `solution_lab1/` (complete reference)
  - `solution_lab2/` (complete reference)

## Pre-req

- Ollama installed.
- A model pulled (example): `ollama pull gemma2:2b`.

## Lab 1

1) Read the problem:
- `day2/lab1/problem_statement.md`

2) Follow the step-by-step guide:
- `day2/lab1/guide.md`

3) Run tests (no Ollama required):

```powershell
python -m pytest -q day2/lab1/tests
```

4) Run the script (requires Ollama running):

```powershell
python day2/lab1/prompt_playground.py --help
```

If stuck, reference solution:
- `day2/solution/solution_lab1/`

## Lab 2

1) Read the problem:
- `day2/lab2/problem_statement.md`

2) Follow the step-by-step guide:
- `day2/lab2/guide.md`

3) Run tests:

```powershell
python -m pytest -q day2/lab2/tests
```

If stuck, reference solution:
- `day2/solution/solution_lab2/`

## Completion checklist

- Lab 1 tests pass
- Lab 2 tests pass
- You can run Lab 1 script successfully with Ollama running

## Save + reset (optional)

When you finish the day, verify tests and reset labs back to starter code:

Note: reset uses `day2/_starter/` so it works even outside git.

```powershell
python day2/submit_day.py

# Mode: verify tests before reset
python day2/submit_day.py --verify
```
