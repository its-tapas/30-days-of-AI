# Day 3 — Lab 1: Chat Memory (multi-turn) + Payload Builder

## Goal

You will implement the **core building blocks** for a multi-turn chat:

1) Keep a message history (memory)
2) Trim history so it doesn’t grow forever
3) Build the JSON payload for Ollama `/api/chat`

This lab is designed to be testable **without Ollama**.

## Starter files

- Starter code: `day3/lab1/chat_memory.py`
- Tests: `day3/lab1/tests/test_chat_memory.py`
- Reference solution: `day3/solution/solution_lab1/`

## What you need to implement (TODOs)

Open `day3/lab1/chat_memory.py`.

### TODO 1 — `trim_messages(messages, max_turns)`

Write a function that returns a **trimmed copy** of `messages`.

Rules:
- Each message is a dict: `{ "role": <role>, "content": <text> }`
- Roles you will use: `system`, `user`, `assistant`
- A **turn** is **2 messages**: `user` + `assistant`
- Keep **system** message(s)
- Keep only the **last** `max_turns` turns (so, last `max_turns * 2` non-system messages)
- If `max_turns <= 0`, return only system messages (or `[]` if none)

### TODO 2 — `build_chat_payload(model, messages, stream=False)`

Build the JSON payload for Ollama `/api/chat`.

Rules:
- Return a dict with keys: `model`, `messages`, `stream`
- `model` must be a non-empty string (after strip) or raise `ValueError`
- `messages` must be a list (it can be empty, but usually shouldn’t be)

## Acceptance criteria

- `python -m pytest -q day3/lab1/tests` passes
- (Manual) Running `python day3/lab1/chat_memory.py` lets you chat multiple turns
