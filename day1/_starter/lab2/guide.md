# Day 1 — Lab 2 Guide (step-by-step)

## Mini-theory (2–5 minutes)
- In real systems, failures come back in different shapes.
- Sometimes it’s JSON with an `error` key, sometimes `message`, sometimes plain text.
- A small helper makes your logs and CLI errors much more readable.

## 1) Open the starter code
File: `day1/lab2/error_detail.py`

You’ll implement:
- `extract_error_detail(response_text, response_json)`

## 2) Implement the TODO
Rules (in order):
1) If `response_json` has a non-empty string at key `error`, return it.
2) Else if it has a non-empty string at key `message`, return it.
3) Else return stripped `response_text`.

Implementation hint:
- Treat `response_json` as optional (`None`).
- Use `isinstance(value, str)` and `.strip()`.

## 3) Run tests
From repo root:

```powershell
python -m pytest -q day1/lab2/tests
```

## If you get stuck
- Check the reference solution in `day1/solution/solution_lab2/`.
