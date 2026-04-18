# Day 1 Notes — Local LLM (Ollama) + First HTTP Call

## Contents List

1. [Local-first LLM (No API keys)](#1--local-first-llm-no-api-keys)
2. [Base URL Hygiene (The “URL Cleaner”)](#2--base-url-hygiene-the-url-cleaner)
3. [HTTP Endpoint Call (The “Request/Response Loop”)](#3--http-endpoint-call-the-requestresponse-loop)
4. [Request Payload (The “Instruction Packet”)](#4--request-payload-the-instruction-packet)
5. [Streaming vs Non-streaming (The “Live Feed”)](#5--streaming-vs-non-streaming-the-live-feed)
6. [Timeouts (The “Hang Preventer”)](#6--timeouts-the-hang-preventer)
7. [Error Detail Extraction (The “Translator”)](#7--error-detail-extraction-the-translator)
8. [Functions and meanings (Conceptual helpers)](#8--functions-and-meanings-conceptual-helpers)

## 1 — Local-first LLM (No API keys)

Definition: Running an LLM on your own computer and calling it like a local service (usually over HTTP).

Example:
- You start a local model server.
- Your Python script sends an HTTP request to `http://localhost:11434/...`.
- You get back generated text.

Why do we need this?
1. Privacy: prompts and documents can stay on your machine.
2. Cost control: no paid API usage for basic practice.
3. Reliability: works offline or with limited internet.

## 2 — Base URL Hygiene (The “URL Cleaner”)

Definition: Cleaning and normalizing the server base address so every request builds a valid URL.

Example:
- User types ` http://localhost:11434/ ` (with spaces and a trailing slash).
- Your program normalizes it to `http://localhost:11434`.

Why do we need this?
1. Prevents broken URLs like `http://localhost:11434//api/generate`.
2. Makes config flexible (env vars, CLI flags) without fragile string bugs.
3. Avoids “it works on my machine” issues due to formatting differences.

## 3 — HTTP Endpoint Call (The “Request/Response Loop”)

Definition: Sending an HTTP request (usually `POST`) with JSON, then reading the JSON response.

Example:
- Request: `POST /api/generate` with a JSON body containing `model` and `prompt`.
- Response: JSON containing generated text.

Why do we need this?
1. Every local LLM workflow boils down to “send request → parse response”.
2. The same pattern applies to chat, embeddings, tools, etc.
3. It gives you a stable interface regardless of model internals.

## 4 — Request Payload (The “Instruction Packet”)

Definition: The JSON object you send that specifies what you want the model to do.

Example payload (conceptual):

```json
{
  "model": "gemma2:2b",
  "prompt": "Explain HTTP in 3 bullets",
  "stream": false
}
```

Why do we need this?
1. It standardizes inputs (model name, prompt, options).
2. It’s easy to log/debug (copy/paste JSON).
3. It’s easy to validate (missing/empty fields are common bugs).

## 5 — Streaming vs Non-streaming (The “Live Feed”)

Definition:
- Non-streaming: the server returns one JSON response after finishing.
- Streaming: the server sends many small JSON “events” as the model generates (often NDJSON).

Example:
- Streaming response events (simplified):

```json
{ "response": "Hello", "done": false }
{ "response": " world", "done": false }
{ "response": "", "done": true }
```

Why do we need this?
1. Better UX: users see text appear immediately.
2. Lower perceived latency on longer answers.
3. Enables progress indicators and early stopping.

## 6 — Timeouts (The “Hang Preventer”)

Definition: A limit on how long your HTTP client will wait for a response.

Example:
- You set a 60-second timeout.
- If the server is stuck, your code fails fast with a clear error.

Why do we need this?
1. Prevents infinite hangs.
2. Makes failure mode predictable.
3. Helps you implement retries or fallback behavior safely.

## 7 — Error Detail Extraction (The “Translator”)

Definition: Converting “something went wrong” into a useful, human-readable message.

Example:
- Sometimes errors are JSON: `{ "error": "model not found" }`.
- Sometimes errors are plain text.
- You attempt JSON parsing first, then fall back to raw text.

Why do we need this?
1. You can’t fix what you can’t understand.
2. Good error messages reduce debugging time massively.
3. Makes CLI tools feel professional and reliable.

## 8 — Functions and meanings (Conceptual helpers)

These are generic “building block” helpers that make local-LLM code stable and testable.

### `normalize_base_url(base_url: str, default: str) -> str`

Meaning: Returns a clean base URL (trim whitespace, apply default if empty, remove trailing `/`).

### `build_url(base_url: str, path: str) -> str`

Meaning: Joins base URL + endpoint path safely (guarantees exactly one `/` between them).

### `build_generate_payload(*, model: str, prompt: str, stream: bool = False, options: dict | None = None) -> dict`

Meaning: Builds the JSON body for a generation request and omits empty fields.

### `iter_ndjson_events(response) -> "Iterator[dict]"`

Meaning: Reads a streaming (NDJSON) response line-by-line and yields parsed event dicts.

### `extract_error_detail(response_text: str, response_json: dict | None) -> str`

Meaning: Produces one clean error string, preferring JSON fields like `error`/`message` when present.

### `build_generate_payload(*, model: str, prompt: str, stream: bool, system: str | None = None, options: dict | None = None) -> dict`

Meaning:
- Builds the JSON you will send to `/api/generate`.

Key behaviors:
- Validate `model` is non-empty
- Validate `prompt` is non-empty (or decide an explicit policy)
- Include `system` only if non-empty
- Put sampling controls under `options` (if using them)

### `iter_ndjson_events(response) -> "Iterator[dict]"`

Meaning:
- Reads a streaming HTTP response and yields parsed JSON events line-by-line.

Rules:
- Skip blank lines
- If a line is not valid JSON, either skip or raise (pick one consistent policy)

### `extract_generated_text(event: dict) -> str | None`

Meaning:
- Pulls the text chunk from a streaming event.

Rules:
- Return `event.get("response")` when it’s a string
- Return `None` when missing

### `extract_error_detail(response_text: str, response_json: dict | None) -> str`

Meaning:
- Returns one human-readable error message.

Priority:
1) non-empty `response_json["error"]`
2) non-empty `response_json["message"]`
3) `response_text.strip()`

## Practical commands (generic)

Start Ollama:

```powershell
ollama serve
```

Pull a model:

```powershell
ollama pull gemma2:2b
```

Quick “is server alive?” check:

```powershell
curl http://localhost:11434
```

Example `/api/generate` call:

```powershell
curl http://localhost:11434/api/generate -H "Content-Type: application/json" -d '{"model":"gemma2:2b","prompt":"Say hi","stream":false}'
```

## Common pitfalls (and fixes)

- Double slashes in URLs (`//api/generate`): normalize and strip trailing `/`.
- No timeout: always set one.
- Streaming but calling `resp.json()`: streaming returns NDJSON, parse line-by-line.
- Printing raw exceptions only: convert to a clear, actionable message (what to do next).
