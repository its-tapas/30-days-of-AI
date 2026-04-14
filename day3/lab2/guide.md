# Day 3 — Lab 2 Guide (beginner, step-by-step)

## Repo constraints (must follow)

- **OS:** Windows
- **Shell:** PowerShell
- **Runtime:** Free + local only (no API keys)
- **Independence:** This lab is independent; do **not** import code from other days.
- **Tests:** `day3/lab2/tests`
- **Reference solution:** `day3/solution/solution_lab2`

## Mini-theory (2–5 minutes, then hands-on)

### Why save/load?
In Lab 1, your messages live in RAM. When the program exits, the conversation is gone.

Saving the session:
- makes the chat resumable
- makes debugging easier (you can inspect the JSON)
- forces you to think about data shape and validation (a real-world skill)

### Why validate?
Files can be corrupted, edited manually, or written by older versions. Validation gives you predictable behavior:
- good input → normal behavior
- bad input → clear `ValueError` instead of random crashes later

## 0) Setup (PowerShell)

From the repo root:

1) Activate your venv (if not already):
```powershell
.\venv\Scripts\Activate.ps1
```

2) Install deps (only if you haven’t):
```powershell
pip install -r .\requirements.txt
```

## 1) Open the starter file

Open `day3/lab2/session_store.py`.

You will implement:
- `save_session(path, messages)`
- `load_session(path)`

Important: The file already contains `_validate_messages(value)` — you should use it.

## 2) Implement `save_session(path, messages)`

Find:
```python
def save_session(path: str | Path, messages: list[Message]) -> None:
```

### Step-by-step approach

1) Convert `path` to a `Path`:
- `path = Path(path)`

2) Ensure the parent directory exists:
- `path.parent.mkdir(parents=True, exist_ok=True)`

3) Build the object to write:
```python
data = {
    "version": 1,
    "messages": messages,
}
```

4) Convert to JSON and write UTF-8:
- Use `json.dumps(...)` then `path.write_text(..., encoding="utf-8")`

Recommended (easy to read while debugging):
- `ensure_ascii=False`
- `indent=2`

## 3) Implement `load_session(path)`

Find:
```python
def load_session(path: str | Path) -> list[Message]:
```

### Step-by-step approach

1) Convert to `Path`:
- `path = Path(path)`

2) If missing, return empty list:
- `if not path.exists(): return []`

3) Read text + parse JSON:
- `text = path.read_text(encoding="utf-8")`
- `data = json.loads(text)`

4) Extract the stored messages:
- `messages_value = data.get("messages")` (after confirming `data` is a dict)

5) Validate using the provided helper:
- `return _validate_messages(messages_value)`

### What should raise `ValueError`?
Anything that violates the expected shape, for example:
- root JSON is not an object/dict
- `messages` key missing or not a list
- any message is not a dict
- `role` missing/not a non-empty string
- `content` missing/not a string

(You don’t need to invent new rules — `_validate_messages` already defines them.)

## 4) Run tests

From repo root:
```powershell
python -m pytest -q day3/lab2/tests
```

If a test fails, open `day3/lab2/tests/test_session_store.py` and read what it expects.

## Acceptance criteria (checklist)

- `python -m pytest -q day3/lab2/tests` passes
- `load_session(...)` returns `[]` for missing file
- Invalid shapes raise `ValueError` (not `KeyError`, not silent failure)
- Saved JSON includes `version: 1` and `messages: [...]`
