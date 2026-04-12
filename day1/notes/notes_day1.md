# Day 1 Notes — Local LLM (Ollama) + First HTTP Call

## Abbreviations / technical terms

| Term | Meaning |
|---|---|
| LLM | Large Language Model; generates output by predicting tokens. |
| Ollama | Local model runtime that exposes an HTTP API (default: `http://localhost:11434`). |
| Endpoint | A URL path that performs an action (example: `/api/generate`). |
| HTTP | Request/response protocol using methods (GET/POST) + status codes (200/400/500). |
| URL | The full address of a resource (`base_url` + `/path`). |
| JSON | Text format for structured data used in request/response bodies. |
| NDJSON | Newline-delimited JSON: one JSON object per line (common for streaming). |
| Payload | The JSON object you send in the request body. |
| Timeout | A hard limit for how long you wait for a response. |
| env var | Environment variable (config without changing code). |

## Topics (1-liners)

| Topic | One-liner |
|---|---|
| Local-first LLM | Run models on your machine (no API keys). |
| `/api/generate` | One-shot generation endpoint (prompt → text). |
| Base URL hygiene | Strip whitespace, default safely, remove trailing `/`. |
| Streaming vs non-streaming | Streaming returns NDJSON chunks; non-streaming returns one JSON object. |
| Error handling | Always handle connection errors, timeouts, and non-200 HTTP responses. |
| Observability basics | Print actionable errors; keep inputs/outputs easy to inspect. |
| Reusable helpers | Small pure functions make code testable and reliable. |

## Core mental model (how local LLM calls work)

Think of Ollama like a local backend server:

- Your app builds a URL + payload
- Your HTTP client sends `POST` JSON
- Ollama returns JSON
- Your app extracts text (or streams chunks)

This is the same “shape” you’ll reuse all month.

## The `/api/generate` request/response shape

### Minimal non-streaming request

```json
{
  "model": "gemma2:2b",
  "prompt": "Explain HTTP in 3 bullets",
  "stream": false
}
```

### Minimal non-streaming response (typical)

```json
{
  "response": "...text...",
  "done": true
}
```

### Streaming response (NDJSON)

When `"stream": true`, the response body is multiple JSON lines. Each line can include:

- `response`: the next text chunk
- `done`: `false` until the final line
- sometimes `error`

Example lines (simplified):

```json
{ "response": "HTTP is ", "done": false }
{ "response": "a protocol...", "done": false }
{ "response": "", "done": true }
```

## Error handling patterns that actually matter

### 1) Always set timeouts

- Without a timeout, a request can hang forever.
- Use a single “human reasonable” value first (example: 60 seconds) before adding fancy retry logic.

### 2) Separate “network failures” from “HTTP failures”

- Network failures: connection refused, DNS issues, timeouts.
- HTTP failures: you got a response but status is not 200.

### 3) Extract a useful error message

Many services return errors in different shapes:
- JSON `{ "error": "..." }`
- JSON `{ "message": "..." }`
- plain text

So your client should try JSON first, then fall back to text.

## Reusable helper functions (generic, not repo-specific)

Below are common helpers you’ll reuse in any local-LLM client.

### `normalize_base_url(base_url: str, default: str) -> str`

Meaning:
- Returns a usable base URL with no trailing `/`.

Typical rules:
- `strip()` whitespace
- if empty: use `default`
- remove trailing slash with `rstrip("/")`

### `build_url(base_url: str, path: str) -> str`

Meaning:
- Returns a correct URL even if inputs have extra slashes.

Rules:
- Normalize base
- Ensure `path` starts with `/`

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
