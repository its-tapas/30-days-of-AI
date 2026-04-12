# Day 3 — Lab 3: Trim Memory by Character Budget

## Goal

In real chats, you often need a **budget** so your message history doesn’t grow forever.

In Lab 1 you trimmed by **turn count**.
In this lab you’ll trim by an approximate **character budget** (a simple stand-in for token limits).

This lab is pure Python and fully testable **without Ollama**.

## Starter files

- Starter code: `day3/lab3/budget_trim.py`
- Tests: `day3/lab3/tests/test_budget_trim.py`
- Reference solution: `day3/solution/solution_lab3/`

## What you need to implement (TODOs)

Open `day3/lab3/budget_trim.py`.

### TODO — `trim_messages_by_chars(messages, max_chars)`

Return a **trimmed copy** of `messages`.

Rules:
- Keep **all** `system` messages.
- For non-system messages (`user` and `assistant`), keep as many **from the end** as possible.
- Count budget using `len(message["content"])` (characters in content).
- If `max_chars <= 0`, return only the system messages.
- Always include the **most recent** non-system message (even if it alone exceeds the budget).

## Acceptance criteria

- `python -m pytest -q day3/lab3/tests` passes
