# Day 1 Notes — Local LLM + HTTP + Prompt Controls

These notes are meant to be **readable in 10–15 minutes** and used as a quick reference while coding.

## Contents

- [Cheat Sheet](#cheat-sheet)
- [Key Terms](#key-terms)
- [Ollama Mental Model](#ollama-mental-model)
- [`/api/generate` Endpoint](#apigenerate-endpoint)
- [Streaming vs Non-streaming](#streaming-vs-non-streaming)
- [Prompt Controls](#prompt-controls)
- [Code Snippets](#code-snippets)
- [Common Errors](#common-errors)

## Cheat Sheet

- Ollama default server: `http://localhost:11434`
- Endpoint we use: `POST /api/generate`
- Minimal request JSON:

```json
{ "model": "gemma2:2b", "prompt": "Hello", "stream": false }
```

## Key Terms

- **LLM (Large Language Model)**: a model that predicts the next token well enough to follow instructions.
- **Token**: a chunk of text (not exactly a word). Output “length” is measured in tokens.
- **Training**: creating a model from data (we are NOT doing this).
- **Inference**: using an existing model to generate output (this is what we do all month).

## Ollama Mental Model

Think of Ollama like a local backend service:

`Your Python code → HTTP POST → Ollama server → JSON response → your code`

Ollama also provides a CLI (`ollama run ...`) which internally calls the same runtime.

## `/api/generate` Endpoint

### Non-streaming request/response

Request:

```json
{
  "model": "gemma2:2b",
  "prompt": "Explain what an API is in 3 bullets",
  "stream": false
}
```

Response shape (simplified):

```json
{
  "response": "...the generated text...",
  "done": true
}
```

### Streaming response (NDJSON)

When `stream: true`, Ollama sends **multiple JSON lines** (NDJSON). Each line is a small partial update.

Example lines (simplified):

```json
{ "response": "APIs are ", "done": false }
{ "response": "interfaces...", "done": false }
{ "response": "", "done": true }
```

Your client prints each `response` chunk as it arrives.

## Streaming vs Non-streaming

- **Non-streaming (`stream=false`)**
  - Pro: easiest to use (one response JSON)
  - Con: you see *nothing* until the full answer is finished (feels slow)

- **Streaming (`stream=true`)**
  - Pro: “fast first token” (feels like `ollama run`)
  - Con: slightly more code (read line-by-line)

In this repo:
- `generate_text()` uses **non-streaming** and returns a full string.
- The CLI uses **streaming** so you see output immediately.

## Prompt Controls

### 1) System prompt

A **system prompt** is high-priority instruction that sets rules and style.

Good system prompts are:
- short
- specific
- constraint-based

Example:

> “You are a concise tutor. Answer in exactly 3 bullets. No emojis.”

Ollama JSON field: `system`

### 2) Temperature

**Temperature** controls randomness.

- `0.0–0.3`: more consistent/deterministic (good for coding + step-by-step)
- `0.7+`: more varied/creative (good for brainstorming)

Ollama JSON field: `options.temperature`

### 3) Max tokens

**Max tokens** caps how long the output can be.

- If too low, the answer gets cut off.
- Good starting range: `60–200`.

Ollama JSON field: `options.num_predict`

### Quick mapping table

| Concept | Ollama JSON | Example |
|---|---|---|
| System prompt | `system` | `"system": "Answer in 3 bullets"` |
| Temperature | `options.temperature` | `"options": {"temperature": 0.2}` |
| Max tokens | `options.num_predict` | `"options": {"num_predict": 120}` |

## Code Snippets

### 1) Minimal Python call (non-streaming)

```python
import requests

base_url = "http://localhost:11434"
url = f"{base_url}/api/generate"

payload = {
    "model": "gemma2:2b",
    "prompt": "Explain what an API is in 3 bullets",
    "stream": False,
}

resp = requests.post(url, json=payload, timeout=60)
resp.raise_for_status()
print(resp.json()["response"])
```

### 2) Python streaming (prints tokens immediately)

```python
import json
import requests

base_url = "http://localhost:11434"
url = f"{base_url}/api/generate"

payload = {
    "model": "gemma2:2b",
    "prompt": "Explain what an API is in 3 bullets",
    "stream": True,
}

with requests.post(url, json=payload, stream=True, timeout=60) as resp:
    resp.raise_for_status()
    for line in resp.iter_lines(decode_unicode=True):
        if not line:
            continue
        event = json.loads(line)
        print(event.get("response", ""), end="", flush=True)
        if event.get("done") is True:
            break

print()
```

### 3) Use the repo client

From repo root:

```python
import sys
sys.path.append("app")

from llm_client import generate_text

print(generate_text(
    "Explain HTTP vs HTTPS",
    system_prompt="Answer in exactly 4 bullets. Be concise."
))
```

## Common Errors

- **Ollama not running / connection refused**
  - Fix: start Ollama (or run `ollama serve`), then retry.

- **Model not found**
  - Fix: `ollama pull <model>`.

- **500: requires more system memory**
  - Fix: pick a smaller model (e.g., `gemma2:2b`, `llama3.2:1b`).

- **First call is slow**
  - Reason: cold start (loading weights).
  - Fix: run one warm-up prompt.
