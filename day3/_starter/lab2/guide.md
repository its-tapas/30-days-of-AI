# Day 3 — Lab 2 Guide (step-by-step)

## Mini-theory (2–5 minutes)

- Memory in a chat is a list of messages.
- If memory is only in RAM, it disappears when the script exits.
- Saving to disk lets you resume later ("session persistence").
- Basic validation is a real-world habit: it prevents weird crashes later.

## 0) Open the starter code

File: `day3/lab2/session_store.py`

You’ll implement:
- `save_session(path, messages)`
- `load_session(path)`

## 1) Implement TODO #1 — `save_session`

Find:
- `def save_session(path: str | Path, messages: list[Message]) -> None:`

Do this in order:

1) Convert `path` to a `Path` object.
2) Ensure the parent folder exists:
   - `path.parent.mkdir(parents=True, exist_ok=True)`
3) Build the JSON object:

```python
{
  "version": 1,
  "messages": messages,
}
```

4) Write it with UTF-8:
   - `path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")`

## 2) Implement TODO #2 — `load_session`

Find:
- `def load_session(path: str | Path) -> list[Message]:`

Do this in order:

1) Convert `path` to a `Path`.
2) If it doesn’t exist:
   - return `[]`
3) Otherwise:
   - read text
   - parse JSON
   - pull out the `messages`
4) Validate:
   - `messages` must be a list
   - each item must be a dict with `role` and `content` strings

If anything is invalid, raise `ValueError`.

## 3) Run tests

From repo root:

```powershell
python -m pytest -q day3/lab2/tests
```

## Acceptance criteria

- All tests pass
- Missing file returns `[]`
- Bad shape raises `ValueError`
