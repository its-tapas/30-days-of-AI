# Day 3 — Lab 2: Save/Load a Chat Session

## Goal

A chat session is just a list of messages.

In this lab, you’ll implement **persistence**:
- save messages to a JSON file
- load messages back later

This lets you resume a conversation across runs.

## Starter files

- Starter code: `day3/lab2/session_store.py`
- Tests: `day3/lab2/tests/test_session_store.py`
- Reference solution: `day3/solution/solution_lab2/`

## What you need to implement (TODOs)

Open `day3/lab2/session_store.py`.

### TODO 1 — `save_session(path, messages)`

Rules:
- Write JSON to `path` using UTF-8.
- Create parent folders if needed.
- Store a JSON object with at least:
  - `version`: number (use `1`)
  - `messages`: the list of messages

### TODO 2 — `load_session(path)`

Rules:
- If the file does not exist, return `[]`.
- If it exists, read JSON and return the stored messages.
- Validate the loaded messages:
  - must be a list
  - each item must be a dict with string keys `role` and `content`
- If validation fails, raise `ValueError`.

## Acceptance criteria

- `python -m pytest -q day3/lab2/tests` passes
- You can save and load messages without losing content
