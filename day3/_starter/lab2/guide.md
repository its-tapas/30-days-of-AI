# Day 3 — Lab 2 Guide (fully step-by-step)

## What you are building

You will add **session persistence**: saving a chat history to disk and loading it back later.

You will implement two functions in one file:

- `save_session(path, messages)`
- `load_session(path)`

The lab also includes a helper `_validate_messages(...)` that you should reuse.

## 0) Setup (PowerShell)

From the repo root:

1) (Optional) Allow activation scripts in this terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

2) Activate venv:

```powershell
& .\.venv\Scripts\Activate.ps1
```

3) Install deps (first time only):

```powershell
python -m pip install -r .\requirements.txt
```

## 1) Open the file you must edit

Open: `day3/lab2/session_store.py`

Find the two functions that currently raise `NotImplementedError`:

- `save_session(path, messages)`
- `load_session(path)`

Do not change tests.

## 2) Implement TODO #1 — `save_session(path, messages)`

Find this signature:

```python
def save_session(path: str | Path, messages: list[Message]) -> None:
```

Implement it in this exact order:

1) Convert `path` into a `Path`:

```python
path = Path(path)
```

2) Ensure the parent directory exists (so writing won’t fail):

```python
path.parent.mkdir(parents=True, exist_ok=True)
```

3) Build a JSON-serializable object with this shape:

```python
obj = {"version": 1, "messages": messages}
```

4) Convert it to JSON text:

- Use `indent=2` so it’s readable
- Use `ensure_ascii=False` so non-English characters don’t become `\uXXXX`

```python
text = json.dumps(obj, ensure_ascii=False, indent=2)
```

5) Write it as UTF-8:

```python
path.write_text(text, encoding="utf-8")
```

## 3) Implement TODO #2 — `load_session(path)`

Find this signature:

```python
def load_session(path: str | Path) -> list[Message]:
```

Implement it in this exact order:

1) Convert `path` into a `Path`.

2) If the file does not exist:

- return `[]`

3) If it exists:

- read text as UTF-8
- parse JSON using `json.loads`

4) Extract messages:

- The file should be a dict with a `"messages"` field
- If the JSON top-level is not a dict, raise `ValueError`

5) Validate messages using the provided helper:

- call `_validate_messages(value)`
- return its result

What “validate” means:

- `messages` must be a list
- each item must be a dict with a non-empty `role` string and a `content` string

If anything is invalid, raise `ValueError`.

## 4) Run the unit tests

From repo root:

```powershell
python -m pytest -q day3/lab2/tests
```

Expected result:

- All tests pass (exit code 0).

## 5) Quick manual sanity check (optional)

From repo root, run this one-liner:

```powershell
python -c "from day3.lab2.session_store import save_session, load_session; p='tmp/session.json'; save_session(p,[{'role':'user','content':'hi'},{'role':'assistant','content':'hello'}]); print(load_session(p))"
```

Expected result:

- It prints a Python list of messages with `role` and `content`.

## 6) Reset the lab back to starter (optional)

```powershell
python day3/submit_day.py --labs lab2
```

## Acceptance criteria (checklist)

- All tests pass
- Missing file returns `[]`
- Bad JSON shape raises `ValueError`
