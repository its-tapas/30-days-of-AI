# Day 2 — Lab 1: Prompt Controls Payload (system/temperature/max tokens)

## Goal
Build and validate the request payload for an Ollama `/api/generate` call that supports:
- system prompt
- temperature
- max output tokens

## What you’ll practice
- Input validation (raise errors for invalid controls)
- Building a JSON payload with an `options` object

## Acceptance criteria
- `python -m pytest -q day2/lab1/tests` passes

## Constraints
- Keep this lab self-contained in this folder.
- Do not import code from other days.
