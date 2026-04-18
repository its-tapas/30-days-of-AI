# Day 1 — Lab 1 Guide (fully step-by-step)

## What you are building

You will implement 3 tiny helper functions that make an Ollama HTTP call reliable:

- `normalize_base_url(base_url)`
- `build_generate_url(base_url)`
- `build_stream_payload(model, prompt)`

These are **pure helpers** (string/dict building). The tests do **not** require Ollama to be running.

## 0) Prerequisites (do this once)

From the repo root (`git-practice/`) in PowerShell:

1) (Optional) If PowerShell blocks activation scripts:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

2) Activate the virtual environment:

```powershell
& .\.venv\Scripts\Activate.ps1
```

3) Install dependencies (only the first time):

```powershell
python -m pip install -r .\requirements.txt
```

4) (Optional, only for the demo run) Install Ollama and pull a model:

```powershell
ollama pull gemma2:2b
```

## 1) Open the file you must edit

Open: `day1/lab1/ollama_one_shot.py`

Scroll until you see these TODO functions raising `NotImplementedError`:

- `normalize_base_url(base_url: str) -> str`
- `build_generate_url(base_url: str) -> str`
- `build_stream_payload(model: str, prompt: str) -> dict[str, Any]`

Do not change the tests.

## 2) Implement TODO #1 — `normalize_base_url(base_url)`

Goal: return a base URL that is safe to join with an endpoint path.

Exact requirements (in order):

1) Remove whitespace:
- Use `base_url.strip()`

2) If the result is empty:
- Return `DEFAULT_OLLAMA_BASE_URL`

3) Remove trailing slashes:
- Use `rstrip("/")`

What to type (example implementation shape):

```python
base_url = base_url.strip()
if not base_url:
    base_url = DEFAULT_OLLAMA_BASE_URL
return base_url.rstrip("/")
```

## 3) Implement TODO #2 — `build_generate_url(base_url)`

Goal: return the full URL for Ollama’s generate endpoint.

Exact steps:

1) Call your helper:
- `base = normalize_base_url(base_url)`

2) Return the endpoint URL:
- `f"{base}/api/generate"`

## 4) Implement TODO #3 — `build_stream_payload(model, prompt)`

Goal: build the request body for a streaming `/api/generate` call.

Exact requirements:

- Return a dictionary with keys exactly: `model`, `prompt`, `stream`
- `stream` must be `True`

What to type:

```python
return {"model": model, "prompt": prompt, "stream": True}
```

## 5) Run the unit tests (no Ollama required)

From repo root:

```powershell
python -m pytest -q day1/lab1/tests
```

Expected result:
- You should see `...` and then `1 passed` (or similar) with exit code 0.

## 6) Optional: run the demo script (requires Ollama)

1) In a separate PowerShell window, start Ollama:

```powershell
ollama serve
```

2) From repo root, run the demo:

```powershell
python day1/lab1/ollama_one_shot.py "Explain what an API is in 3 bullets"
```

Expected result:
- You should see streaming text printed to the console.

## 7) Reset the lab back to starter (when you want a clean slate)

From repo root:

```powershell
python day1/submit_day.py --labs lab1
```

## Troubleshooting (common issues)

- If tests fail: open `day1/lab1/tests/test_builders.py` and compare expected strings to what your helper returns.
- If the demo says Ollama not reachable: make sure `ollama serve` is running.
- If you get a “model not found” error: run `ollama pull gemma2:2b`.

## If you get stuck

- Reference solution: `day1/solution/solution_lab1/`
