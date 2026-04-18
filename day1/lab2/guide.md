# Day 1 — Lab 2 Guide (fully step-by-step)

## What you are building

You will implement one helper function that extracts a useful error message from an HTTP failure.

You implement:
- `extract_error_detail(*, response_text: str, response_json: dict | None) -> str`

This lab is **pure Python** (no Ollama required).

## 0) Prerequisites (do this once)

From the repo root (`git-practice/`) in PowerShell:

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

Open: `day1/lab2/error_detail.py`

Find the function that currently raises `NotImplementedError`:

```python
def extract_error_detail(*, response_text: str, response_json: dict[str, Any] | None) -> str:
```

Do not change the tests.

## 2) Implement the function (exact rules)

You must implement the rules in this exact priority order:

1) If `response_json` exists AND contains key `"error"` with a **non-empty string** value:
- return that string (after stripping whitespace)

2) Else if `response_json` contains key `"message"` with a **non-empty string** value:
- return that string (after stripping whitespace)

3) Else:
- return `response_text.strip()` (can be empty)

What to do step-by-step:

1) If `response_json is None`, skip directly to step 3.
2) Read `error = response_json.get("error")`.
	- If it’s a `str` and `error.strip()` is not empty → return `error.strip()`.
3) Read `message = response_json.get("message")`.
	- If it’s a `str` and `message.strip()` is not empty → return `message.strip()`.
4) Return `response_text.strip()`.

## 3) Run the unit tests

From repo root:

```powershell
python -m pytest -q day1/lab2/tests
```

Expected result:
- `...` then `1 passed` with exit code 0.

## 4) Reset the lab back to starter (optional)

```powershell
python day1/submit_day.py --labs lab2
```

## If you get stuck

- Reference solution: `day1/solution/solution_lab2/`
