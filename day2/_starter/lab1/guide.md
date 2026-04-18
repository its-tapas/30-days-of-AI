# Day 2 — Lab 1 Guide (fully step-by-step)

## What you are building

You will implement helpers that build and validate a `/api/generate` request with controls:

- `system` prompt (rules/style)
- `temperature` (randomness)
- `num_predict` (max output tokens)

You implement 3 TODO functions in one file:

- `normalize_base_url(base_url)`
- `validate_controls(temperature, max_output_tokens)`
- `build_generate_payload(model, prompt, system, temperature, max_output_tokens)`

## 0) Prerequisites (do this once)

From the repo root in PowerShell:

1) (Optional) Allow activation scripts in this terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

2) Activate venv:

```powershell
& .\.venv\Scripts\Activate.ps1
```

3) Install dependencies (first time only):

```powershell
python -m pip install -r .\requirements.txt
```

4) (Optional, only for the manual run) Ensure Ollama + model are available:

```powershell
ollama pull gemma2:2b
```

## 1) Open the file you must edit

Open: `day2/lab1/prompt_playground.py`

Find the 3 functions that raise `NotImplementedError`.

Do not change tests.

## 2) Implement TODO #1 — `normalize_base_url(base_url)`

Exact requirements:

1) `strip()` whitespace
2) If empty after strip, use `DEFAULT_OLLAMA_BASE_URL`
3) Remove trailing `/` using `rstrip("/")`

This is the same concept as Day 1.

## 3) Implement TODO #2 — `validate_controls(temperature, max_output_tokens)`

Goal: reject invalid input **before** building the payload.

Exact rules:

- `temperature` must be between `0.0` and `1.0` inclusive
- `max_output_tokens` must be `> 0`

What to do step-by-step:

1) If `temperature < 0.0` or `temperature > 1.0`:
- raise `ValueError("temperature must be between 0.0 and 1.0")` (message can differ, but keep it clear)

2) If `max_output_tokens <= 0`:
- raise `ValueError("max_output_tokens must be > 0")`

3) Otherwise return `None` (i.e., do nothing).

## 4) Implement TODO #3 — `build_generate_payload(...)`

Goal: return a dict shaped like a non-streaming Ollama request.

Exact payload requirements:

1) The top-level dict must include:
- `model`
- `prompt`
- `stream`: must be `False`

2) Must include an `options` dict with:
- `temperature`: set from the argument
- `num_predict`: set from `max_output_tokens`

3) Only include `system` if it is non-empty after stripping:
- `system_clean = system.strip()`
- If `system_clean` is empty, omit the key entirely (do not send `"system": ""`).

Example shape:

```python
{
  "model": "gemma2:2b",
  "prompt": "Explain retries",
  "stream": False,
  "system": "Answer in 3 bullets.",  # only if non-empty
  "options": {"temperature": 0.2, "num_predict": 160},
}
```

## 5) Run the unit tests (no Ollama required)

From repo root:

```powershell
python -m pytest -q day2/lab1/tests
```

Expected result:
- Tests pass (exit code 0).

## 6) Manual run (requires Ollama running)

1) Start the Ollama server (separate terminal):

```powershell
ollama serve
```

2) See CLI options:

```powershell
python day2/lab1/prompt_playground.py --help
```

3) Run an example prompt:

```powershell
python day2/lab1/prompt_playground.py --prompt "Explain retries" --system "Answer in 3 bullets" --temperature 0.2 --max-output-tokens 120
```

Expected result:
- The script prints a short answer.

## 7) Reset the lab back to starter (optional)

```powershell
python day2/submit_day.py --labs lab1
```

## Troubleshooting

- If you see `[error] temperature must be ...`: fix your range checks.
- If you see “Ollama not reachable”: make sure `ollama serve` is running.

## If you get stuck

- Reference solution: `day2/solution/solution_lab1/`
