# 30-day topic map (with labs)

This repo is **day-wise**:

- Each day has **2–5 labs** (min 2, max 5).
- You work in `dayX/lab1/`, `dayX/lab2/`, ... (starter code with TODOs).
- You run lab tests from repo root (example): `python -m pytest -q dayX/lab1/tests`.
- When done, you reset labs back to starter code with:
  - `python dayX/submit_day.py`
  - Mode: `python dayX/submit_day.py --verify`

Planned total labs across 30 days: **79**.

| Day | Title | Labs | Lab titles |
|---:|---|---:|---|
| 1 | Local LLM + first HTTP call (Ollama) | 2 | Lab 1: URL + payload builders (streaming `/api/generate`)<br>Lab 2: Error detail extraction helper |
| 2 | Prompt control: system + temperature + max output tokens | 2 | Lab 1: Validate controls + build `/api/generate` payload<br>Lab 2: System prompt modes (presets) |
| 3 | Chat memory: multi-turn + session save/load | 3 | Lab 1: `/api/chat` payload + turn-based trimming<br>Lab 2: Session save/load (JSON persistence)<br>Lab 3: Character-budget trimming |
| 4 | Structured output: strict JSON schema | 3 | Lab 1: Parse JSON safely (strip fences, reject non-JSON)<br>Lab 2: Validate JSON shape (required keys + types)<br>Lab 3: Prompting for strict JSON (schema-first prompting) |
| 5 | Tool calling basics: route intents to Python functions | 3 | Lab 1: Intent router (string → tool name)<br>Lab 2: Tool registry + dispatch (validated args)<br>Lab 3: End-to-end mini-agent loop (plan → call tool → respond) |
| 6 | Tool reliability: validation + retries + safe fallbacks | 3 | Lab 1: Retry + backoff wrapper with timeout<br>Lab 2: Error classification (retryable vs fatal)<br>Lab 3: Safe fallback responses + structured error reporting |
| 7 | RAG basics: chunking + embeddings (local-first) + retrieval | 4 | Lab 1: Chunk documents + attach metadata<br>Lab 2: Create embeddings (local-first) + store vectors<br>Lab 3: Retrieval (top-k) with cosine similarity<br>Lab 4: Answer with citations (show which chunks were used) |
| 8 | RAG quality: hybrid search + evaluation prompts | 3 | Lab 1: Hybrid retrieval (keyword + vector)<br>Lab 2: Re-rank results (simple scoring or LLM re-rank)<br>Lab 3: Retrieval evaluation (queries + expected sources) |
| 9 | RAG app integration: chat + citations + source tracking | 3 | Lab 1: Chat + retrieval integration (ask → retrieve → answer)<br>Lab 2: Citation formatting + source IDs<br>Lab 3: Debug mode (show retrieved chunks + scores) |
| 10 | Observability: logs + traces + prompt/version tracking | 3 | Lab 1: Structured logging (JSON logs + request IDs)<br>Lab 2: Timing/tracing helper (durations per step)<br>Lab 3: Prompt/version tracking (log prompt + settings) |
| 11 | LangChain basics (minimal) applied to your app | 2 | Lab 1: Minimal LangChain pipeline with local model<br>Lab 2: Add memory or retrieval using LangChain primitives |
| 12 | LangChain tools + structured output integration | 2 | Lab 1: Structured output with Pydantic (validated results)<br>Lab 2: Tools integration with guardrails (allowed tools only) |
| 13 | LangGraph basics: state + nodes + edges | 2 | Lab 1: Build a small graph (state → steps → result)<br>Lab 2: Add conditional routing and debug output |
| 14 | LangGraph memory + checkpoints | 2 | Lab 1: Checkpoint state to disk<br>Lab 2: Resume from checkpoint (continue where you left off) |
| 15 | Agentic architecture: plan → act → reflect (single agent) | 3 | Lab 1: Planner step (produce a short plan)<br>Lab 2: Act step (tool calls + results)<br>Lab 3: Reflect step (stop/continue + summary) |
| 16 | AutoGen-style multi-agent roles: planner/executor/reviewer | 2 | Lab 1: AutoGen-style role prompts + handoff contract<br>Lab 2: Shared memory/state between roles |
| 17 | CrewAI-style coordination: shared state + handoffs | 3 | Lab 1: Shared state schema (what gets shared)<br>Lab 2: Handoff rules + conflict resolution<br>Lab 3: Router (send tasks to the right agent) |
| 18 | Constraints + safety: tool allowlists + sandboxing mindset | 2 | Lab 1: Tool allowlist + argument validation<br>Lab 2: Safe-mode behaviors (refuse unsafe actions) |
| 19 | Local model selection: speed vs quality + quantization basics | 2 | Lab 1: Benchmark harness (latency + output sanity checks)<br>Lab 2: Model selection checklist + configuration presets |
| 20 | Performance: caching + streaming UX + context window control | 3 | Lab 1: Simple caching (prompt/settings → cached answer)<br>Lab 2: Streaming UX for chat in CLI<br>Lab 3: Context control (trim + summarize strategy) |
| 21 | Document ingestion pipeline: loaders + cleaning + metadata | 3 | Lab 1: Load documents (txt/md) + normalize<br>Lab 2: Cleaning + chunking pipeline<br>Lab 3: Metadata extraction (title, section, source) |
| 22 | Retrieval tuning: chunk sizes + re-ranking | 3 | Lab 1: Chunk size experiments (quality vs speed)<br>Lab 2: Re-ranking experiments<br>Lab 3: Result filtering + score thresholds |
| 23 | Evaluation harness: golden set + regression checks | 3 | Lab 1: Golden set format + runner<br>Lab 2: Regression thresholds (fail the build if worse)<br>Lab 3: Report output (summary table) |
| 24 | Deployment shape: run as CLI + simple API service | 3 | Lab 1: Package a CLI entrypoint<br>Lab 2: Add a minimal API service (local-only)<br>Lab 3: Health checks + config |
| 25 | Cloud-friendly architecture: config, secrets, portability | 2 | Lab 1: Config layering (defaults + env + flags)<br>Lab 2: Secrets handling patterns (no secrets in git) |
| 26 | Agent workflows for dev tools: code search + summaries | 2 | Lab 1: Repo summarizer (files → overview)<br>Lab 2: Change reviewer (diff → feedback) |
| 27 | Agent workflows for cloud ops: runbooks + incident triage | 2 | Lab 1: Incident triage helper (inputs → next actions)<br>Lab 2: Runbook retrieval + draft response |
| 28 | Hardening: failure modes + timeouts + rate limits | 3 | Lab 1: Circuit breaker + timeouts<br>Lab 2: Rate limiting + queue<br>Lab 3: Failure-mode tests (simulate outages) |
| 29 | Final integration day: end-to-end demo script | 2 | Lab 1: End-to-end demo scenario runner<br>Lab 2: Regression checks + "known good" baselines |
| 30 | Final project: polished assistant + README + demo scenarios | 4 | Lab 1: Define the spec + architecture (inputs/outputs/tools)<br>Lab 2: Implement core assistant loop (memory + tools + retrieval)<br>Lab 3: Add evaluation + tests (golden set)<br>Lab 4: Polish docs + demo scripts |

Note: Each day’s folder (`dayX/`) defines the exact deliverables, acceptance criteria, and how to run the demo/tests.
