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

### What to type (line-by-line)

In `error_detail.py`, go into `extract_error_detail(...)` and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (only read JSON keys if JSON exists):
Explanation: If the server didn’t return JSON (or JSON parsing failed), `response_json` will be `None`.
Explanation: In that case we skip straight to the plain-text fallback at the end.
```python
if response_json is not None:
```

Step 2 (read the `error` field):
Explanation: Many APIs (including Ollama) put the best human-readable failure reason in an `error` field.
```python
    error = response_json.get("error")
```

Step 3 (if it’s a non-empty string, return it):
Explanation: We only accept real strings, and we treat whitespace-only values as “empty”.
```python
    if isinstance(error, str) and error.strip():
```

Step 4 (return stripped error text):
Explanation: Returning the stripped version keeps messages clean and avoids trailing newlines.
```python
        return error.strip()
```

Step 5 (read the `message` field):
Explanation: Some APIs use `message` instead of `error`, so this is our second-best source.
```python
    message = response_json.get("message")
```

Step 6 (if it’s a non-empty string, return it):
Explanation: Same rule: only non-empty strings count.
```python
    if isinstance(message, str) and message.strip():
```

Step 7 (return stripped message text):
Explanation: At this point we know `message` is a useful string, so return the cleaned version.
```python
        return message.strip()
```

Step 8 (fallback to response body text):
Explanation: If there was no useful JSON field, we fall back to raw response text (still stripped).
```python
return response_text.strip()
```

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
