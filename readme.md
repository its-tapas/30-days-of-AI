# 30-Day AI Systems (Hands-on)

This repo is a **30-day, 2-hours/day** execution track to transition from backend/cloud development into **building real AI/LLM systems**:

- Chatbot foundations
- Prompt control and memory
- Structured outputs + tool use
- RAG systems
- LangChain + LangGraph
- Multi-agent workflows
- Local model options
- Final end-to-end AI system

## Repo structure (fixed)

Each day lives in its own folder:

- `dayX/dayX.txt` → **copy/paste prompt** to run in another AI (Gemini/ChatGPT/etc.)
- `dayX/readme.md` → **the day plan + outcomes** (what to build, how to validate, continuity)
- `dayX/app1/` → **independent day demo mini-project** (separate from `app/`; does NOT evolve)

Root files:

- `readme.md` → this file
- `LICENSE` → actual license text
- `tracker.csv` → daily progress tracker (VS Code friendly)

Root codebase:

- `app/` → the **single evolving project** that grows across all days (chatbot → RAG → agents)

## Getting started (clone + setup)

These steps are written for **Windows + PowerShell**.

### 1) Clone the repo

1) Install Git (if needed)
- Search: “Git for Windows download”

2) Clone and enter the folder

```powershell
git clone https://github.com/its-tapas/30-days-of-AI
cd 30-days-of-AI
```

### 2) Install prerequisites

1) Install Python
- Recommended: Python 3.11+ (newer versions are fine)

2) Verify

```powershell
python --version
```

### 3) Create + activate a virtual environment

```powershell
python -m venv .venv
.venv/Scripts/activate
```

### 4) Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5) Install a free local LLM runtime (Day 1 uses this)

This series starts with **local models** so you don’t need paid API keys.

1) Install Ollama
- If you have winget:

```powershell
winget install Ollama.Ollama
```

- Otherwise: search “Ollama Windows download” and install it.

2) Pull a starter model

```powershell
ollama pull llama3.2:3b
```

(Optional) If you want Gemma early too:

```powershell
ollama pull gemma2:2b
```

### 6) Configure environment variables

1) Create `.env` in the repo root
- Copy the keys from `.env.example`

2) Set your default model (example)
- `OLLAMA_MODEL=llama3.2:3b`

### 7) Start Day 1

1) Open `tracker.csv` and set Day 1 `Status` to `In Progress`
2) Follow `day1/readme.md`

---

## Day-by-day workflow

Each day has **two tracks** (both are useful):

- **Track A (evolving system)**: you implement the “real” assistant in `app/`.
- **Track B (independent day demo)**: you implement a separate mini-project in `dayX/app1/`.

Suggested daily routine:

1) Open `dayX/readme.md` and complete the demos/tasks
2) Use `dayX/dayX.txt` in Gemini/ChatGPT for step-by-step help
3) Update `tracker.csv`:
   - `In Progress` while you work
   - `Done` when you pass the day’s validation cases
   - `Blocked` if you hit a hard issue

One-day-at-a-time rule:

- Only the **current day** is generated/maintained.
- When you mark a day as `Done` in `tracker.csv`, generate the next day.

## Continuity rule

Every day **extends what you built previously**. Do not start fresh projects daily—evolve a single codebase into chatbot → RAG → agents.
