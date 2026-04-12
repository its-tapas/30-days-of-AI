# Day 1 — Lab 1 Guide (step-by-step)

## Mini-theory (2–5 minutes)
- Ollama runs a local HTTP server (default: `http://localhost:11434`).
- Calling a model is just an HTTP `POST` to `/api/generate` with a JSON body.
- Small helper functions make your code easier to test and easier to debug.

## 0) Pre-req
- Install Ollama and pull a model (example):
  - `ollama pull gemma2:2b`

## 1) Open the starter code
File: `day1/lab1/ollama_one_shot.py`

You’ll see 3 TODO functions:
- `normalize_base_url(base_url)`
- `build_generate_url(base_url)`
- `build_stream_payload(model, prompt)`

## 2) Implement TODO #1 — normalize_base_url
Requirements:
- Strip whitespace
- If empty after strip, use `DEFAULT_OLLAMA_BASE_URL`
- Remove trailing `/`

Tip: do it in 2 lines:
1) `base_url = base_url.strip()`
2) pick default if empty
3) `rstrip('/')`

## 3) Implement TODO #2 — build_generate_url
Requirement:
- Use `normalize_base_url()`
- Return: `<base>/api/generate`

## 4) Implement TODO #3 — build_stream_payload
Requirements:
- Return a `dict` with keys: `model`, `prompt`, `stream`
- `stream` must be `True`

## 5) Run tests (does NOT require Ollama)
From repo root:

```powershell
python -m pytest -q day1/lab1/tests
```

## 6) Run the demo script (requires Ollama running)
Start Ollama (if needed):
- `ollama serve`

Then run:

```powershell
python day1/lab1/ollama_one_shot.py "Explain what an API is in 3 bullets"
```

## If you get stuck
- Check the reference solution in `day1/solution/solution_lab1/`.
