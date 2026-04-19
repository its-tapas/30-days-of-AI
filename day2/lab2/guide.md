# Day 2 — Lab 2 Guide (fully step-by-step)

## What you are building

You will implement **prompt modes**: a small helper that turns a user-chosen `mode` into a system prompt string.

The mapping is already provided in `PROMPT_MODES`. Your job is to implement:

- `get_system_prompt(mode)`

## 0) Prerequisites (do this once)

From the repo root in PowerShell:

1) (Optional) Allow activation scripts in this terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

2) Activate venv:

```powershell
& .\.venv\Scripts\Activate.ps1
```

3) Install dependencies (first time only):

```powershell
python -m pip install -r .\requirements.txt
```

## 1) Open the file you must edit

Open: `day2/lab2/prompt_modes.py`

Find the function `get_system_prompt(mode: str) -> str` that currently raises `NotImplementedError`.

Do not edit tests.

## 2) Understand the provided mapping

At the top of the file you will see something like:

```python
PROMPT_MODES = {
    "concise": "...",
    "teacher": "...",
    "reviewer": "...",
}
```

The keys are the valid modes.

## 3) Implement `get_system_prompt(mode)`

In `prompt_modes.py`, go into `get_system_prompt(...)` and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (strip + lowercase to make it case-insensitive):
Explanation: Users may type modes with extra spaces or different casing.
Explanation: Normalizing once keeps the rest of the function simple and predictable.
```python
mode_clean = (mode or "").strip().lower()
```

Step 2 (unknown mode should raise ValueError):
Explanation: We check membership first so we can raise a clear error instead of letting a `KeyError` happen.
```python
if mode_clean not in PROMPT_MODES:
```

Step 3 (raise ValueError with a helpful message):
Explanation: This message includes the original user input (before normalization) to aid debugging.
```python
    raise ValueError(f"Unknown mode: {mode!r}")
```

Step 4 (return the prompt for a known mode):
Explanation: If the mode exists, return the stored system prompt string.
```python
return PROMPT_MODES[mode_clean]
```

## 4) Run the unit tests

From repo root:

```powershell
python -m pytest -q day2/lab2/tests
```

Expected result:

- All tests pass (exit code 0).

## 5) Quick manual sanity check (optional)

From repo root:

```powershell
python -c "from day2.lab2.prompt_modes import get_system_prompt; print(get_system_prompt('  TEACHER  '))"
```

Expected result:

- It prints the teacher mode string.

## 6) Reset the lab back to starter (optional)

```powershell
python day2/submit_day.py --labs lab2
```

## Troubleshooting

- If tests fail with case/whitespace issues: make sure you did both `strip()` and `lower()`.
- If tests fail with a missing exception: ensure unknown modes raise `ValueError` (not `KeyError`).

## If you get stuck

- Reference solution: `day2/solution/solution_lab2/`
