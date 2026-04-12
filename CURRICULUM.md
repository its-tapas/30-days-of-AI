# 30-day topic map (high-level)

This repo is **day-wise**:

- You work in `dayX/lab1/`, `dayX/lab2/`, ... (starter code with TODOs).
- You run lab tests from repo root (example): `python -m pytest -q dayX/lab1/tests`.
- When done, you can reset your labs with:
  - `./scripts/submit_day.ps1 -Day dayX -Name <your_name>`

## Days 1–30 (titles + focus)

1) Local LLM + first HTTP call (Ollama)
2) Prompt control: system prompt + temperature + max tokens
3) Chat memory: multi-turn + session save/load
4) Structured output: strict JSON schema
5) Tool calling basics: route intents to Python functions
6) Tool reliability: validation + retries + safe fallbacks
7) RAG basics: chunking + embeddings (local-first) + retrieval
8) RAG quality: hybrid search + evaluation prompts
9) RAG app integration: chat + citations + source tracking
10) Observability: logs + traces + prompt/version tracking
11) LangChain basics (minimal) applied to your app
12) LangChain tools + structured output integration
13) LangGraph basics: state + nodes + edges
14) LangGraph memory + checkpoints
15) Multi-step agent loop: plan → act → reflect (single agent)
16) Multi-agent intro: roles (planner/executor/reviewer)
17) Multi-agent coordination: shared state + handoffs
18) Constraints + safety: tool allowlists + sandboxing mindset
19) Local model selection: speed vs quality + quantization basics
20) Performance: caching + streaming UX + context window control
21) Document ingestion pipeline: loaders + cleaning + metadata
22) Retrieval tuning: chunk sizes + re-ranking
23) Evaluation harness: golden set + regression checks
24) Deployment shape: run as CLI + simple API service
25) Cloud-friendly architecture: config, secrets, portability
26) Agent workflows for dev tools: code search + summaries
27) Agent workflows for cloud ops: runbooks + incident triage
28) Hardening: failure modes + timeouts + rate limits
29) Final integration day: end-to-end demo script
30) Final project: polished assistant + README + demo scenarios

Note: Each day’s folder (`dayX/`) defines the exact deliverables, acceptance criteria, and how to run the demo/tests.
