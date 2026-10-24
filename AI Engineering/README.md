# 🤖 AI Engineering Track — from AI consumer to AI backend engineer

> **Mission:** in 26 weeks, become the engineer who can *build, evaluate, secure and ship* LLM features — Python-first for the AI ecosystem, Spring AI to bring it into Java backends.

---

## 1. By Week 26 you will…

| # | Outcome (measurable) | Evidence |
|---|---|---|
| 1 | Write idiomatic, typed, tested Python (pydantic, asyncio, pytest, uv) | `ai-engineering-lab/` folders with green `uv run pytest` |
| 2 | Explain LLM internals (tokens, attention, pre/post-training, sampling, hallucinations) in ≤ 2 min each | Sunday tests + ⭐ questions in [`AI_INTERVIEW_QUESTION_BANK.md`](AI_INTERVIEW_QUESTION_BANK.md) |
| 3 | Ship **7 portfolio projects** with READMEs, tags and numbers | [`PROJECTS.md`](PROJECTS.md) acceptance criteria met |
| 4 | Build RAG with *measured* quality: DocuMind recall@5 ≥ 0.80 and faithfulness ≥ 0.85 on a 30-item golden set | `EVAL_REPORT.md` |
| 5 | Build agents (from scratch → LangGraph → multi-agent) with human approval and agent evals (task success ≥ 85% in the capstone) | CareerPilot + TicketVerse AI eval reports |
| 6 | Build and secure **MCP servers** in Python (SDK v2) and Spring AI | `careerpilot-mcp` tests, `ticketverse-ai` MCP tools |
| 7 | Run AI like production software: OWASP threat model, ≥ 25-case attack suite (≥ 90% blocked), CI eval gate, traces, cost dashboards | `SECURITY.md`, `eval.yml`, `LLMOPS.md` |
| 8 | Decide *prompt vs RAG vs fine-tune* with data (LoRA experiment) and run open-weight models locally | FineTune Lab `REPORT.md`, `BENCHMARK.md` |
| 9 | Add AI to a Java microservice with **Spring AI 2.0** (tools, RAG, memory, MCP, evals) and design for Azure (Microsoft Foundry, AI Search, keyless auth) | `ticketverse-ai` service, DocuMind on Azure (or reviewed architecture doc) |
| 10 | Pass two timed mocks (AI system design W23, full AI-engineer interview W26) at ≥ 80/100 | Recordings + scorecards |

> ### 💡 Why Python **and** Spring AI?
> - **Python** is where the AI ecosystem ships first — model SDKs, LangChain/LangGraph, MCP SDK, evals (RAGAS, DeepEval), fine-tuning (TRL, Unsloth). Most AI-engineer JDs ask for it, and **AI-200** (your Azure exam in W26) expects Python + vector databases.
> - **Spring AI** turns your existing Java/Spring strength into a differentiator: most Indian enterprises run Java backends, and engineers who can add AI *inside* those systems are rare.
> - **Strategy:** learn and prove each concept in Python (fast iteration), then port the proven pattern to Spring AI (W20–W24) inside the TicketVerse capstone.

---

## 2. Your weekly slots (AI track)

| Day | Slot | Type |
|---|---|---|
| Mon | 45 min | Learn + do |
| Tue | 45 min | Learn + do |
| Thu | 45 min | Learn + do |
| Fri | 45 min | Learn + do (often prepares Saturday) |
| Sat | 45 min | **BUILD** (ship something runnable) or **BOSS BATTLE** in W4, W9, W14, W19, W23, W26 |
| Sun | 25 min | AI part of the weekly test (see Section 8) |

Total ≈ 3 h 45 min/week + test. No AI slot on Wednesday (DSA/Java/SD/Azure day).

---

## 3. How to run one 45-minute session

You *understand* code but find *writing* complex code hard — so every session is built around **you typing working code**.

| Minute | Step | What you do |
|---|---|---|
| 0–5 | **Recall** | Without notes, write 3 bullets from the last session. |
| 5–15 | **Learn** | Read/watch **only** the linked sections in `learn`. Write a 5-line note: *what · why · how · gotcha · example*. Videos at 1.25×. |
| 15–40 | **Do: Predict → Try → Verify → Explain** | Predict the output/behaviour, write the code **yourself**, run it, then explain the result in one sentence in your notes. Commit small and often. |
| 40–45 | **Close** | Check the `Done when:` line honestly, commit with a clear message, tick the box in `01_Daily_Planner`, write 1 question for Sunday. |

**AI-assistant rules (important for your growth):**
1. First attempt is always yours (≥ 15 min). Then use AI as a **reviewer** ("what's wrong / what's unidiomatic?"), not an author.
2. **20-minute stuck rule:** docs → example → ask AI for a *hint*, never the full solution.
3. Never commit code you cannot explain line by line. In Boss Battles: **no AI code generation**.

**Saturday BUILD / BOSS:** timebox to 45 min, ship the smallest working version, then README + tag. Unfinished polish goes into the next week's *stretch*, not into Sunday's test time.

---

## 4. Phase map (Seasons)

| Season | Weeks (dates) | Focus | Milestone |
|---|---|---|---|
| **S1 Foundation Forge** | W1–W4 (26 Oct – 22 Nov 2026) | Python for Java devs, how LLMs work, LLM APIs | 🐉 **W4 Boss:** TerminalGPT v1.0 + reusable `llmkit` |
| **S2 Concurrency Crucible** | W5–W9 (23 Nov – 27 Dec 2026) | Prompting & structured output, embeddings & pgvector, RAG I/II, evals | JD Parser, SemanticSearch API, DocuMind v1 · 🐉 **W9 Boss:** eval report |
| **S3 Spring Citadel** | W10–W14 (28 Dec 2026 – 31 Jan 2027) | Production FastAPI, agents from scratch, LangGraph, MCP, multi-agent | DocuMind v2 (Docker), CareerPilot + MCP server · 🐉 **W14 Boss:** multi-agent demo + eval |
| **S4 Distributed Kingdom** | W15–W19 (1 Feb – 7 Mar 2027) | AI security, LLMOps, open-source inference, fine-tuning, multimodal | Attack suite + CI eval gate, FineTune Lab · 🐉 **W19 Boss:** Resume/JD extractor |
| **S5 Cloud Ascension** | W20–W23 (8 Mar – 4 Apr 2027) | Spring AI I/II, Azure AI (Microsoft Foundry, AI Search), AI system design | `ticketverse-ai` v0.2, DocuMind on Azure · 🐉 **W23 Boss:** system-design mock |
| **S6 Final Boss: The Offer** | W24–W26 (5 – 25 Apr 2027) | TicketVerse AI capstone, observability, demo, interview prep | `ticketverse-v2.0-ai`, demo video · 🐉 **W26 Boss:** full mock interview |

Cross-track anchors: AZ-900 exam W5 · AZ-104 exam W16 · **AI-200 exam W26** (your Python + vector DB work here directly serves it) · TicketVerse AI work runs alongside the Java track in W24.

---

## 5. Navigation

| File / folder | What it is |
|---|---|
| [`ROADMAP_26_WEEKS.md`](ROADMAP_26_WEEKS.md) | One-page view of all 26 weeks (generated) |
| [`Weeks/`](Weeks/) | `Week-01.md` … `Week-26.md`: the 5 sessions of each week with `learn` / `do` / `Done when` |
| [`RESOURCES.md`](RESOURCES.md) | Verified courses, docs, videos (English + Hindi), labs, tools with versions |
| [`PROJECTS.md`](PROJECTS.md) | Specs, architecture, acceptance criteria and eval thresholds for the 7 projects |
| [`AI_INTERVIEW_QUESTION_BANK.md`](AI_INTERVIEW_QUESTION_BANK.md) | 132 interview questions by topic, ⭐ = most frequent, with covering week + W26 practice prompts |
| `../00_Progress_Tracker/AI_MEMORY.md` | Paste-in context for your AI mentor (progress, decisions, catch-up rules) |
| `../01_Daily_Planner/` | Daily checklists across all five tracks |

**Repo layout you will build (`ai-engineering-lab`):**

```text
ai-engineering-lab/
├─ llmkit/                    # W4: shared provider layer (settings, clients, cost meter, retries)
├─ 00-python-katas/           # W1
├─ 01-python-async-cli/       # W2
├─ 02-llm-playground/         # W3 notebooks
├─ 03-terminalgpt/            # W4  BOSS
├─ 04-jd-parser/              # W5  (CareerPilot seed)
├─ 05-semantic-search-api/    # W6
├─ 06-documind/               # W7–W10, W16–W17, W22 (+ evals/, azure/)
├─ 07-careerpilot/            # W11–W16 (+ mcp_server/, security/)
├─ 08-oss-inference/          # W17
├─ 09-finetune-lab/           # W18
├─ 10-resume-jd-extractor/    # W19 BOSS
└─ 11-ai-system-design/       # W23 BOSS
ticketverse/ticketverse-ai/   # W20–W25 Spring AI service inside the capstone repo
```

---

## 6. 🔑 Free API keys setup checklist (do this in W4 Mon)

> 🏠 **Do this on your personal laptop** (GitHub Codespaces). Gemini, AI Studio, Groq, OpenRouter and Ollama model downloads are
> **blocked on the company network** (tested 24 Oct 2026). Details: Section 8 of [03_SETUP_YOUR_LAPTOP.md](../03_SETUP_YOUR_LAPTOP.md).
>
> ⚠️ **GitHub Models was retired on 30 Jul 2026** (playground, catalog and inference API are gone). Older tutorials that use it will not work — use the providers below.

| Provider | Cost | Get a key | OpenAI-compatible base URL (prefix `https://`) | Use it for |
|---|---|---|---|---|
| **Google Gemini API** | Free tier (rate-limited per project; limits shown in AI Studio) | Google AI Studio → *Get API key* | `generativelanguage.googleapis.com/v1beta/openai/` | Default cloud model, embeddings, vision/PDF, audio |
| **Groq** | Free tier (per-org RPM/RPD/TPM limits) | GroqCloud console → *API Keys* | `api.groq.com/openai/v1` | Very fast open-weight models, fallback provider, Whisper |
| **Ollama** (local) | Free, offline | [Download Ollama](https://ollama.com/download) | `localhost:11434/v1` (key: any string) | Private/offline dev, embeddings, vision, benchmarks |
| **OpenRouter** | `:free` models with a small daily cap | openrouter.ai → *Keys* | `openrouter.ai/api/v1` | Backup provider, trying many models |
| *Paid (optional)* | Pay-as-you-go | OpenAI / Anthropic / Azure OpenAI in Microsoft Foundry | provider-specific | Only if you want frontier models; set a budget first |

Checklist:
- [ ] `uv` project created; **`.env` added to `.gitignore` *before* the first commit**; commit a `.env.example` with variable *names* only (`GEMINI_API_KEY=`, `GROQ_API_KEY=`, `OPENROUTER_API_KEY=`).
- [ ] Keys loaded via `python-dotenv` / `pydantic-settings` (Python) or environment variables (Spring `${GROQ_API_KEY}`), never hard-coded, never printed in logs, notebooks or screenshots.
- [ ] Ollama installed; a 3–4B model pulled (e.g., `ollama pull llama3.2:3b`) plus an embedding model (`ollama pull nomic-embed-text`).
- [ ] One script calls Gemini, Groq and Ollama by switching only `base_url` + `model` (this becomes `llmkit`).
- [ ] Retries with backoff for HTTP 429 (free tiers *will* rate-limit you) and a provider fallback.

Safety notes:
- **Free tiers are not private.** Google states free-tier prompts/responses may be used to improve its products, and some free OpenRouter endpoints may log or train on prompts. Never send personal data (Aadhaar, PAN, phone numbers, salary slips), your employer's code/data, or real customer documents — use public or synthetic data.
- **If a key leaks** (pushed to GitHub, pasted in chat): revoke/rotate it immediately, then rewrite history or delete the repo copy. Keep GitHub secret scanning / push protection on.
- **Paid accounts:** set budgets and alerts before the first call; delete Azure resources after each lab.
- Prefer **keyless auth** (managed identity) once you reach Azure in W22.

---

## 7. Rules, pitfalls & tips

**Rules**
1. **Measure every "improvement".** No number → it didn't happen (hits@5, faithfulness, latency, ₹ cost).
2. **Ship on Saturday.** A tagged, runnable v0 beats a perfect plan. Every BUILD ends with README + tag.
3. **Concepts over frameworks.** Build it raw first (RAG W7, agents W11), then use the framework. Pin versions with `uv.lock`.
4. **Security by default:** treat documents, tool outputs and user reviews as untrusted input; least-privilege tools; human approval for irreversible actions.

**Pitfalls to avoid**
- Version drift: this plan targets **LangChain 1.x, LangGraph 1.x, MCP Python SDK v2** (`FastMCP` was renamed `MCPServer`; MCP spec **2026-07-28** is stateless), **Spring AI 2.0** (Azure OpenAI models are accessed through the OpenAI module; `QuestionAnswerAdvisor` lives in `spring-ai-vector-store-advisor`). Check the version banner of any tutorial.
- Python version: use **3.13** where you can (personal laptop / Codespaces) — several AI libraries (e.g., CrewAI, NeMo Guardrails) still cap below 3.14, and many below 3.15. **3.12 also works** for everything in this plan: on the company laptop use the Company Portal's Python 3.12 (start it with `py`) with `venv` + pip via JFrog Artifactory. No uv there? Use the command equivalents in Section 4 of [03_SETUP_YOUR_LAPTOP.md](../03_SETUP_YOUR_LAPTOP.md).
- Embedding dimensions: pgvector indexes `vector` up to 2,000 dimensions (`halfvec` up to 4,000) — choose models/dimensions accordingly and never mix embedding models in one index.
- Trusting LLM-as-judge blindly — always calibrate on 10–15 hand-labelled items.
- Building an agent where a workflow (or a single call) is enough.
- Laptop limits: local models need RAM (≈ 3–4 GB for a 3–4B 4-bit model); fine-tune on free Colab/Kaggle GPUs, not your laptop. Docker Desktop needs WSL2 and ~10 GB free disk.

**Tips**
- Keep `llmkit` as your one provider layer — every later project reuses it.
- Keep a `learning-log.md` in the repo: date, what broke, how you fixed it. These become interview stories.
- Behind schedule? Follow the catch-up rules in Section 7 of `../00_Progress_Tracker/AI_MEMORY.md`: skip *stretch* first, never skip the Saturday ship or the Sunday test.

---

## 8. How you're tested on Sundays (AI: 25 minutes)

| Part | Format | Source |
|---|---|---|
| 6 questions | Concepts + **code reading** (e.g., "what does this LangGraph edge do?", "find the bug in this retry loop", "which metric is this computing?") | The week's `self_check`, your own repo code, ⭐ questions from the bank |
| 1 scenario | Short design/trade-off question (e.g., "RAG answers cite the wrong page — how do you debug it?") | The week's topic + earlier weeks (spaced repetition) |

**Scoring /100:** ≥ 80 🟢 green · 60–79 🟡 amber · < 60 🔴 red → weak topics are logged in `WEAKNESS_TRACKER.md` and become remediation tasks in next week's *Fix-it* section. Boss weeks add the Boss Battle rubric score (target ≥ 80).
