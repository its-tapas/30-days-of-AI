# Day 2 — Lab 2 Guide (step-by-step)

## Mini-theory (2–5 minutes)
- A “mode” is just a named *system prompt preset*.
- Modes reduce repetition and make behavior consistent.

## 1) Open the starter code
File: `day2/lab2/prompt_modes.py`

You’ll implement:
- `get_system_prompt(mode)`

## 2) Implement the TODO
Rules:
- mode lookup is case-insensitive
- strip whitespace
- raise `ValueError` if mode is unknown

Implementation hint:
- Convert `mode` to a normalized key: `mode.strip().lower()`
- Then look it up in `PROMPT_MODES`

## 3) Run tests
From repo root:

```powershell
python -m pytest -q day2/lab2/tests
```

## If you get stuck
- Check the reference solution in `day2/solution/solution_lab2/`.
