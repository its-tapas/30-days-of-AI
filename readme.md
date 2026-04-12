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

- `dayX/dayX.txt` → **copy/paste generator prompt** (run in another AI to regenerate `dayX/readme.md` + each `dayX/labN/problem_statement.md` + `dayX/labN/guide.md`)
- `dayX/readme.md` → **the day plan + outcomes** (what to build, how to validate, continuity)
- `dayX/lab1/`, `dayX/lab2/`, ... → **labs** (HackerRank-style: "write your code here")
   - `problem_statement.md`
   - `guide.md`
   - lab files (starter code with TODOs)
   - `tests/`
- `dayX/solution/solution_labN/` → complete reference solution (for when you’re stuck)

Root files:

- `readme.md` → this file
- `LICENSE` → actual license text
- `tracker.csv` → daily progress tracker (VS Code friendly)

High-level day/topic map: see `CURRICULUM.md`.
End-of-day checklist: see `END_OF_DAY_CHECKLIST.md`.

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

Suggested daily routine:

1) Open `dayX/readme.md` and complete the demos/tasks
2) Use `dayX/dayX.txt` in Gemini/ChatGPT for step-by-step help
3) Implement in `dayX/lab1/` (starter files with TODOs)
   - Some days have multiple labs: `dayX/lab1`, `dayX/lab2`, ...
4) Run tests for the day from repo root:

```powershell
python -m pytest -q dayX/lab1/tests
```

5) When the day is complete:
   - Save + reset your workspace code using:

```powershell
python dayX/submit_day.py

# Mode: verify tests before reset
python dayX/submit_day.py --verify

# Mode: reset only specific labs
python dayX/submit_day.py --labs lab1 lab2
```

Note: reset uses `dayX/_starter/` snapshots, so it works even outside git.

   - This verifies each lab’s tests and then resets your lab folders back to the starter code.
6) Update `tracker.csv`:
   - `Done` when you pass the day’s validation cases
   - `Blocked` if you hit a hard issue

One-day-at-a-time rule:

- Only the **current day** is generated/maintained.
- When you mark a day as `Done` in `tracker.csv`, generate the next day.

Before you mark a day as `Done`, run the checklist in `END_OF_DAY_CHECKLIST.md`.

## Continuity rule

Every day **extends what you learned previously**.

- Code is day-scoped (you work in `dayX/labN/`, then reset back to starter).
- Continuity comes from the concepts, the habits (tests/validation), and the prompts you refine over time.
