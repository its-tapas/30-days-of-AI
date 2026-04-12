# Day 1 — Lab 1: First Ollama HTTP Call (Streaming)

## Goal
Build the *request pieces* needed to call a local Ollama model via HTTP.

You will implement a few small helper functions in `ollama_one_shot.py` and then run a one-shot prompt.

## What you’ll practice
- Basic HTTP endpoint composition
- Building JSON payloads
- Defensive string handling (strip, defaults)

## Acceptance criteria
- `python -m pytest -q day1/lab1/tests` passes
- Running the script prints model output when Ollama is running

## Constraints
- Keep this lab self-contained in this folder.
- Do not import code from other days.
