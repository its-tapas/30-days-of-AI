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

### What to type (line-by-line)

In `prompt_playground.py`, go into `normalize_base_url(...)` and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (strip + default if empty):
Explanation: This handles inputs like `"  http://localhost:11434/  "` and normalizes them.
Explanation: If the result is blank, we use `DEFAULT_OLLAMA_BASE_URL` so later code can rely on it.
```python
base_url = (base_url or "").strip() or DEFAULT_OLLAMA_BASE_URL
```

Step 2 (remove trailing slash and return):
Explanation: We return a “base” URL without the trailing `/` so joining paths is predictable.
```python
return base_url.rstrip("/")
```

## 3) Implement TODO #2 — `validate_controls(temperature, max_output_tokens)`

Goal: reject invalid input **before** building the payload.

Exact rules:

- `temperature` must be between `0.0` and `1.0` inclusive
- `max_output_tokens` must be `> 0`

### What to type (line-by-line)

In `prompt_playground.py`, go into `validate_controls(...)` and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (reject bad temperature range):
Explanation: Temperature controls randomness. Values outside `[0.0, 1.0]` are invalid for this lab.
```python
if temperature < 0.0 or temperature > 1.0:
```

Step 2 (raise ValueError for temperature):
Explanation: Raise early so you fail fast before building/sending a payload.
```python
    raise ValueError("temperature must be between 0.0 and 1.0")
```

Step 3 (reject non-positive max tokens):
Explanation: `max_output_tokens` is your hard cap; `0` or negative doesn’t make sense.
```python
if max_output_tokens <= 0:
```

Step 4 (raise ValueError for max tokens):
Explanation: This enforces the lab rule that max output tokens must be positive.
```python
    raise ValueError("max_output_tokens must be > 0")
```

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

### What to type (line-by-line)

In `prompt_playground.py`, go into `build_generate_payload(...)` and **delete** the line:

```python
raise NotImplementedError
```

Then type these lines **in order**.

Step 1 (build the required payload shape in one dict):
Explanation: This matches the Ollama `/api/generate` JSON shape the tests expect.
Explanation: `stream` must be `False` here, and the control values go under `options`.
```python
payload = {"model": model, "prompt": prompt, "stream": False, "options": {"temperature": temperature, "num_predict": max_output_tokens}}
```

Step 2 (strip system text):
Explanation: We treat whitespace-only system prompts as “not provided”.
```python
system_clean = (system or "").strip()
```

Step 3 (only include system when non-empty):
Explanation: Omitting `system` entirely is different from sending an empty string, and the tests want omission.
```python
if system_clean:
```

Step 4 (set the system field):
Explanation: This adds the system prompt only when it is meaningful.
```python
    payload["system"] = system_clean
```

Step 5 (return the payload):
Explanation: Return the dict you built.
```python
return payload
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
