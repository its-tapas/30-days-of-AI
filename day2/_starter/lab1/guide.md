# Day 2 — Lab 1 Guide (step-by-step)

## Mini-theory (2–5 minutes)
- The *model* stays the same, but request parameters change behavior.
- `system` sets rules/style.
- `options.temperature` controls randomness.
- `options.num_predict` caps output length.

## 1) Open the starter code
File: `day2/lab1/prompt_playground.py`

TODO functions:
- `normalize_base_url(base_url)`
- `validate_controls(temperature, max_output_tokens)`
- `build_generate_payload(model, prompt, system, temperature, max_output_tokens)`

## 2) Implement normalize_base_url
Same idea as Day 1:
- strip
- default if empty
- remove trailing slash

## 3) Implement validate_controls
Rules:
- temperature must be between 0.0 and 1.0 inclusive
- max_output_tokens must be > 0

Raise `ValueError` with a helpful message.

## 4) Implement build_generate_payload
Rules:
- Must include: `model`, `prompt`, `stream: false`
- Must include:
  - `options.temperature`
  - `options.num_predict`
- Include `system` only if non-empty after strip

## 5) Run tests (does NOT require Ollama)
From repo root:

```powershell
python -m pytest -q day2/lab1/tests
```

## 6) Run the script (requires Ollama running)

```powershell
python day2/lab1/prompt_playground.py --help
```

Example:

```powershell
python day2/lab1/prompt_playground.py --prompt "Explain retries" --system "Answer in 3 bullets" --temperature 0.2 --max-output-tokens 120
```

## If you get stuck
- Check the reference solution in `day2/solution/solution_lab1/`.
