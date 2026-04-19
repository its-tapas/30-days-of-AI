# Day 1 — Local LLM (Ollama) + First HTTP Call (2 Labs)

Time box: **2–3 hours**.

Day 1 has **2 Practical labs**:

- Lab 1: Build the HTTP URL + JSON payload pieces for a streaming `/api/generate` call.
- Lab 2: Build a tiny error-detail helper (real-world backend habit).

## Folder structure (Day 1)

- `day1/lab1/`
  - `problem_statement.md`
  - `guide.md`
  - lab files (starter code with TODOs)
  - `tests/`
- `day1/lab2/` (same idea)
- `day1/solution/`
  - `solution_lab1/` (complete reference)
  - `solution_lab2/` (complete reference)

## Pre-req

- Ollama installed + running.
- A model pulled (example): `ollama pull gemma2:2b`.
- (Optional) Copy `.env.example` to `.env` and set:
  - `OLLAMA_BASE_URL=http://localhost:11434`
  - `OLLAMA_MODEL=gemma2:2b`

## Lab 1

1) Read the problem:
- `day1/lab1/problem_statement.md`

2) Follow the step-by-step guide:
- `day1/lab1/guide.md`

3) Run tests (no Ollama required):

```powershell
python -m pytest -q day1/lab1/tests
```

4) Run the script (requires Ollama running):

```powershell
python day1/lab1/ollama_one_shot.py "Explain what an API is in 3 bullets"
```

If stuck, reference solution:
- `day1/solution/solution_lab1/`

## Lab 2

1) Read the problem:
- `day1/lab2/problem_statement.md`

2) Follow the step-by-step guide:
- `day1/lab2/guide.md`

3) Run tests:

```powershell
python -m pytest -q day1/lab2/tests
```

If stuck, reference solution:
- `day1/solution/solution_lab2/`

## Completion checklist

- Lab 1 tests pass
- Lab 2 tests pass
- You can run Lab 1 script successfully with Ollama running

## Save + reset (optional)

When you finish the day, verify tests and reset labs back to starter code:

Note: reset uses `day1/_starter/` so it works even outside git.

Reset overwrites only the lab’s editable starter code files from `day1/_starter/`.
It does **not** modify guides/tests/problem statements.

```powershell
python day1/submit_day.py

# Mode: verify tests before reset
python day1/submit_day.py --verify
```
