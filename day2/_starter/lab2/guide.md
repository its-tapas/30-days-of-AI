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

Follow these rules exactly:

1) Normalize the input:

- `mode_clean = mode.strip().lower()`

2) Look up the normalized key in `PROMPT_MODES`.

3) If it exists:

- return the corresponding string

4) If it does not exist:

- raise `ValueError` (with a helpful message)

Suggested error message (any clear message is fine):

```python
raise ValueError(f"Unknown mode: {mode!r}")
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
