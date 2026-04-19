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

Go into the function body and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (convert `path` into a `Path`):
Explanation: Converting early lets you use `.parent`, `.write_text()`, etc. consistently.
```python
path = Path(path)
```

Step 2 (ensure the parent directory exists):
Explanation: This prevents failures when the folder doesn’t exist yet (e.g., `tmp/session.json`).
```python
path.parent.mkdir(parents=True, exist_ok=True)
```

Step 3 (build the JSON object):
Explanation: Wrapping messages in an object lets you add versioning without changing the file shape later.
```python
obj = {"version": 1, "messages": messages}
```

Step 4 (serialize JSON; readable + keep unicode):
Explanation: `indent=2` makes it readable, and `ensure_ascii=False` keeps unicode characters intact.
```python
text = json.dumps(obj, ensure_ascii=False, indent=2)
```

Step 5 (write as UTF-8):
Explanation: UTF-8 is the standard encoding for JSON text files.
```python
path.write_text(text, encoding="utf-8")
```

## 3) Implement TODO #2 — `load_session(path)`

Find this signature:

```python
def load_session(path: str | Path) -> list[Message]:
```

Go into the function body and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (convert `path` into a `Path`):
Explanation: Accept both strings and `Path` objects for convenience, then normalize.
```python
path = Path(path)
```

Step 2 (missing file returns empty list):
Explanation: If there’s nothing saved yet, we treat that as “no session”.
```python
if not path.exists():
```

Step 3 (return for missing file):
Explanation: Returning `[]` is the simplest “no saved session yet” behavior.
```python
    return []
```

Step 4 (read file as UTF-8):
Explanation: Read the entire JSON file into memory as text.
```python
text = path.read_text(encoding="utf-8")
```

Step 5 (parse JSON):
Explanation: Convert JSON text into Python objects (dict/list/etc.).
```python
data = json.loads(text)
```

Step 6 (top-level must be a dict/object):
Explanation: We expect a JSON object like `{ "version": 1, "messages": [...] }`.
```python
if not isinstance(data, dict):
```

Step 7 (raise ValueError for invalid top-level):
Explanation: A non-dict top-level JSON means the file is corrupted or not in our expected format.
```python
    raise ValueError("session file must contain a JSON object")
```

Step 8 (extract `messages` field):
Explanation: Pull out just the stored messages list.
```python
messages = data.get("messages")
```

Step 9 (validate using the provided helper and return):
Explanation: `_validate_messages` enforces the required structure and raises `ValueError` on bad data.
```python
return _validate_messages(messages)
```

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
