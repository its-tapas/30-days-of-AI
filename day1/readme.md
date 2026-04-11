## Day 1 — What is an LLM (Really) + Run One Locally + First “API Call”

### 1. Pre-requisites

#### a) Self Explanation (MANDATORY)

You’re starting from zero AI/ML — that’s fine. Here’s the only theory you need **today** to build something.

- **AI** (in practice): software that can produce “smart” outputs.
- **ML**: a way to create models from data.
- **LLM (Large Language Model)**: a model that predicts the next token (word-ish chunk) well enough that it can **follow instructions** and **generate useful text**.
- **Training vs Inference**:
  - **Training** = making a model (we are NOT doing this)
  - **Inference** = using an existing model (this is what we do all month)

What you will do today:
- Run an LLM **locally** (free) using **Ollama**.
- Treat it like a backend service and call it via **HTTP + JSON** from Python.

Backend analogy:
- Today is exactly like integrating a 3rd-party API… except the “service” runs on your laptop at `http://localhost:11434`.

#### b) External Learning (ONLY if needed)

Only if you get stuck installing Ollama, spend **max 15 minutes** searching:
- “Ollama Windows install winget”
- “Ollama API generate endpoint example”

---

### 2. Practical Demo(s)

#### Demo 1 — Run a local LLM (no API keys)

**Mini-theory (2–5 min, say it out loud)**
- A “model” is like an engine. Ollama lets you download an engine and run it.
- Once it’s running, it exposes an HTTP server you can call.

Simple flow:

`You → (prompt) → Ollama server → (response) → you`

**What we are building**
- A working local LLM runtime on your machine.

**Why we are building it**
- You said you have **no API key**. Local models are the fastest free way to start building.

**Step-by-step instructions (Windows PowerShell)**

1) Install Ollama (pick one)
- Option A (preferred if you have winget):
  - `winget install Ollama.Ollama`
- Option B:
  - Search “Ollama Windows download”, install the MSI.

2) Verify Ollama works
- `ollama --version`

3) Pull a small model (pick one)
- **Small+fast (recommended for Day 1)**:
  - `ollama pull llama3.2:3b`
- **Gemma (aligns with your lead’s suggestion)**:
  - `ollama pull gemma2:2b`

4) Quick interactive test
- `ollama run llama3.2:3b`
- Ask: `Explain what an API is in 3 bullets.`
- Type `/bye` to exit.

**Expected output**
- It answers locally (no browser, no API key).

---

#### Demo 2 — Your first “LLM API call” from Python (interactive)

**Mini-theory (2–5 min)**
- An “LLM call” is a normal HTTP POST request:
  - URL (endpoint)
  - JSON body (prompt + options)
  - JSON response

Pseudo-request:

```
POST http://localhost:11434/api/generate
{
  "model": "llama3.2:3b",
  "prompt": "Hello",
  "stream": false
}
```

**What we are building**
- A Python script that sends user input to Ollama and prints the model output.

**Why we are building it**
- This becomes your reusable foundation for chat memory, structured output, tools, RAG, and agents.

**Step-by-step instructions**

1) Create a repo-wide virtual environment
- From repo root:
  - `python -m venv .venv`
  - `./.venv/Scripts/Activate.ps1`

2) Install dependencies from `requirements.txt`
- `python -m pip install -r requirements.txt`

3) Create `.env` (DO NOT COMMIT)
- Create a file named `.env` in repo root with:
  - `OLLAMA_BASE_URL=http://localhost:11434`
  - `OLLAMA_MODEL=llama3.2:3b`

4) Create the evolving app files (in root `app/`)

- `app/llm_client.py`
  - loads env
  - function `generate_text(user_prompt: str, system_prompt: str | None = None) -> str`
  - calls `POST {OLLAMA_BASE_URL}/api/generate` with `stream=false`
  - returns the response text
  - handles errors clearly:
    - Ollama not running
    - model not pulled

- `app/cli_prompt.py`
  - interactive loop
  - user types a prompt
  - prints model output
  - `exit` quits

5) Run the CLI
- `python app/cli_prompt.py`

**Expected output**
- You type: `Summarize HTTP vs HTTPS in 4 bullets`
- It prints 4 bullets.

---

### 3. Implementation Task

Build two things:

- **Track A (evolving system)** in `app/` (this will grow every day)
- **Track B (independent day demo)** in `day1/app1/` (separate mini-project)

**Tasks (do in this order)**
1) **Track A:** Implement `app/llm_client.py` + `app/cli_prompt.py`.
2) **Track B:** Implement an independent one-shot demo in `day1/app1/`.
  - Create `day1/app1/ollama_one_shot.py`
  - It should NOT import from `app/` (keep it independent)
  - It should accept a prompt (CLI arg or input), call Ollama, and print the response
3) Keep config in `.env` (repo root) and keep `.env.example` updated.

**Acceptance criteria**
- `python app/cli_prompt.py` works end-to-end.
- `python day1/app1/ollama_one_shot.py "Hello"` prints a model response.
- If Ollama is not running, you get a friendly error (not a scary traceback).
- `day1/app1/` remains a separate demo project (not a copy/mirror of `app/`).

---

### 4. Validation / Test Cases

1) **Happy path**
- Prompt: `Give me 3 bullet points about REST API versioning`
- Output: 3 bullets

2) **Ollama not running**
- Stop Ollama (or just don’t start it), then run CLI
- Expected: clear message like “Ollama server not reachable at …”

3) **Wrong model name**
- Set `OLLAMA_MODEL=does-not-exist`
- Expected: clear message telling you to `ollama pull <model>`

---

### 5. Mistakes to Avoid

- Thinking you must learn neural nets to build AI apps (you don’t).
- Confusing **Gemini Chat UI** with **API access** (today we’re building with a local API).
- Forgetting `stream=false` (streaming is great later, but Day 1 should stay simple).
- Committing `.env`.

---

### 6. Reflection Prompt

Copy/paste into another AI:

"Act as a senior engineer. Review my Day 1 implementation (Ollama client + CLI). Check: clean separation (client vs CLI), good error handling, config via env, and whether this is a solid base for adding prompt modes and chat memory." 

---

### 7. Continuity Tracker (VERY IMPORTANT)

**What I have built so far**
- A local LLM runtime (Ollama + a model).
- An HTTP-based Python client that calls the model.
- An interactive CLI prompt runner.
- An independent Day 1 demo under `day1/app1/`.

**My current capability level**
- Can run an LLM locally and call it like any other API.
- Can build a minimal AI app loop (input → LLM → output) with config + error handling.

**What I am now ready to learn next**
- Prompt control: system prompts + temperature + output limits to make responses predictable.

---

### 8. Next Day Preparation

- Keep 5 real prompts you’d use at work (cloud troubleshooting, API design, summarization).
- Decide your default model (`llama3.2:3b` vs `gemma2:2b`).
- Tomorrow you’ll add:
  - “mode” presets (system prompts)
  - temperature
  - max output tokens
