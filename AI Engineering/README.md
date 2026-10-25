# 🤖 AI Engineering Track — from AI consumer to AI backend engineer

> **Mission:** in 30 weeks (Mon 26 Oct 2026 → Sun 23 May 2027), become the engineer who can *build, evaluate, secure and ship* LLM features — Python-first for the AI ecosystem, Spring AI to bring it into Java backends.

---

## 1. By Week 30 you will…

| # | Outcome (measurable) | Evidence |
|---|---|---|
| 1 | Write idiomatic, typed, tested Python (pydantic, asyncio, generators, decorators, typing, pytest, uv) and handle data with NumPy/pandas | `ai-engineering-lab/` folders with green `uv run pytest` |
| 2 | Explain ML fundamentals (splits, precision/recall/F1, overfitting) and LLM internals (tokens, attention, pre/post-training, sampling, hallucinations) in ≤ 2 min each | Sunday tests + ⭐ questions in [`AI_INTERVIEW_QUESTION_BANK.md`](AI_INTERVIEW_QUESTION_BANK.md) |
| 3 | Ship **7 portfolio projects** with READMEs, tags and numbers (plus timed boss builds and a public demo) | [`PROJECTS.md`](PROJECTS.md) acceptance criteria met |
| 4 | Build RAG with *measured* quality: DocuMind recall@5 ≥ 0.80 and faithfulness ≥ 0.85 on a 30-item golden set | `EVAL_REPORT.md` |
| 5 | Build agents (from scratch → LangGraph → multi-agent → agentic RAG) with human approval and agent evals (task success ≥ 85% in the capstone) | CareerPilot + TicketVerse AI eval reports |
| 6 | Build and secure **MCP servers** in Python (SDK v2, bearer-token auth) and Spring AI | `careerpilot-mcp` tests, `ticketverse-ai` MCP tools |
| 7 | Run AI like production software: OWASP threat model, ≥ 15-case attack suite (≥ 90% blocked), CI eval gate, OpenTelemetry traces, cost dashboards | `SECURITY.md`, `eval.yml`, Langfuse dashboards |
| 8 | Decide *prompt vs RAG vs fine-tune* with data (LoRA experiment) and compare local open-weight models with API models | FineTune Lab `REPORT.md`, `BENCHMARK.md` |
| 9 | Add AI to a Java microservice with **Spring AI 2.0** (tools, RAG, memory, MCP, evals) and deploy on Azure (Microsoft Foundry, AI Search, keyless auth) | `ticketverse-ai` service, DocuMind on Azure Container Apps |
| 10 | Pass the timed bosses (W4, W9, W15, W20, W25) and the final mock interview (W30) at ≥ 80/100 | Recordings + scorecards |

> ### 💡 Why Python **and** Spring AI?
> - **Python** is where the AI ecosystem ships first — model SDKs, LangChain/LangGraph, MCP SDK, evals (RAGAS, DeepEval), fine-tuning (TRL, Unsloth). Most AI-engineer JDs ask for it, and **AI-200** (your Azure exam in W26) expects Python + vector databases.
> - **Spring AI** turns your existing Java/Spring strength into a differentiator: most Indian enterprises run Java backends, and engineers who can add AI *inside* those systems are rare.
> - **Strategy:** learn and prove each concept in Python (fast iteration), then port the proven pattern to Spring AI (W23–W24) and the TicketVerse capstone (W27–W28). The `ticketverse-ai` service is owned by this track; the Java track adds the platform hooks around it.

---

## 2. Your weekly slots (AI track)

| Day | Slot | Type |
|---|---|---|
| Mon | 45 min | Learn + do |
| Tue | 45 min | Learn + do |
| Thu | 45 min | Learn + do |
| Fri | 45 min | Learn + do (often prepares Saturday) |
| Sat | 45 min | **BUILD** (ship something runnable) or **BOSS BATTLE** in W4, W9, W15, W20, W25, W30 |
| Sun | 25 min | AI part of the weekly test (see Section 8) |

Total ≈ 3 h 45 min/week + test. No AI slot on Wednesday (DSA/Java/SD/Azure day).

**Lighter days are built in:** AZ-900 exam (Fri 27 Nov, W5), AZ-104 week (W16 Fri/Sat), AI-200 week (W26 Fri/Sat), Christmas (Fri 25 Dec, W9), New Year (Fri 1 Jan, W10), Republic Day (Tue 26 Jan, W14) and Holi (Mon 22 Mar, W22). W29 is a buffer week with protected catch-up time.

**Where you work:** W1–W5 on the company laptop (Python 3.12 + uv via the company JFrog; no LLM API calls). From **W6 (Mon 30 Nov)** every session that calls an LLM runs in **GitHub Codespaces on your personal laptop**, because free LLM APIs are blocked on the company network.

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
| **S1 Foundation Forge** | W1–W4 (26 Oct – 22 Nov 2026) | Python I–III for Java devs (incl. generators, decorators, typing, NumPy/pandas), ML fundamentals | Katas, async CLI, data labs · 🐉 **W4 Boss:** spam classifier with honest metrics |
| **S2 Concurrency Crucible** | W5–W9 (23 Nov – 27 Dec 2026) | How LLMs work, LLM APIs in Codespaces, prompting & structured output, Docker/SQL/FastAPI, embeddings & pgvector | TerminalGPT + reusable `llmkit`, JD Parser · 🐉 **W9 Boss:** SemanticSearch API |
| **S3 Spring Citadel** | W10–W15 (28 Dec 2026 – 7 Feb 2027) | RAG I/II, evals, production FastAPI, agents from scratch, LangGraph | DocuMind v0 → v2 (Docker), eval report · 🐉 **W15 Boss:** CareerPilot v0 graph |
| **S4 Distributed Kingdom** | W16–W20 (8 Feb – 14 Mar 2027) | MCP, multi-agent, AI security, LLMOps (OpenTelemetry, CI eval gate, public demo), open-source models | `careerpilot-mcp`, CareerPilot v1.1-secure, public demo Space · 🐉 **W20 Boss:** local vs API model comparison · 💼 start applying (W20) |
| **S5 Cloud Ascension** | W21–W25 (15 Mar – 18 Apr 2027) | Fine-tuning, multimodal, Spring AI I/II, Azure AI (Microsoft Foundry, AI Search) | FineTune Lab, Resume/JD extractor, `ticketverse-ai` v0.2 · 🐉 **W25 Boss:** DocuMind on Azure |
| **S6 Final Boss: The Offer** | W26–W30 (19 Apr – 23 May 2027) | AI system design, TicketVerse AI capstone + Azure launch, demo, agentic RAG + MCP auth, interview prep | `ticketverse-v2.0-ai`, demo video, DocuMind v3.1 · 🐉 **W30 Final Boss:** full mock interview |

Cross-track anchors: AZ-900 exam W5 · AZ-104 exam W16 · **AI-200 exam W26** (your Python + vector DB work here directly serves it; its skills outline has no Foundry objectives, so W25 serves AI-103 and interviews) · Java W25 publishes the catalog/review events your capstone consumes · Java W27 adds platform hooks (gateway route, JWT relay, Kafka topics, Helm values) for your `ticketverse-ai` · Java W28 + Azure W28 launch TicketVerse on Azure with it.

---

## 5. Navigation

| File / folder | What it is |
|---|---|
| [`ROADMAP.md`](ROADMAP.md) | One-page view of all 30 weeks (generated) |
| [`Weeks/`](Weeks/) | `Week-01.md` … `Week-30.md`: the 5 sessions of each week with `learn` / `do` / `Done when` |
| [`RESOURCES.md`](RESOURCES.md) | Verified courses, docs, videos (English + Hindi), labs, tools with versions |
| [`PROJECTS.md`](PROJECTS.md) | Specs, architecture, acceptance criteria and eval thresholds for the 7 projects |
| [`AI_INTERVIEW_QUESTION_BANK.md`](AI_INTERVIEW_QUESTION_BANK.md) | 150 interview questions by topic, ⭐ = most frequent, with covering week + W30 practice prompts |
| `../00_Progress_Tracker/AI_MEMORY.md` | Paste-in context for your AI mentor (progress, decisions, catch-up rules) |
| `../01_Daily_Planner/` | Daily checklists across all five tracks; all weeks in one PDF: `Daily_Planner_All_30_Weeks.pdf` |

**Repo layout you will build (`ai-engineering-lab`):**

```text
ai-engineering-lab/
├─ .devcontainer/             # W6: Codespaces setup (Python 3.13, Docker-in-Docker, Node)
├─ llmkit/                    # W6: shared provider layer (settings, clients, cost meter, retries, fallback)
├─ 00-python-katas/           # W1
├─ 01-python-async-cli/       # W2
├─ 02-python-data/            # W3  generators, decorators, typing, NumPy, pandas
├─ 03-ml-basics/              # W4  BOSS (spam classifier) + W7 LLM-vs-classifier note
├─ 04-llm-playground/         # W5  notebooks
├─ 05-terminalgpt/            # W6
├─ 06-jd-parser/              # W7  (CareerPilot seed)
├─ 07-backend-foundations/    # W8  Docker, SQL, FastAPI
├─ 08-semantic-search-api/    # W9  BOSS
├─ 09-documind/               # W10–W13, W19, W25 BOSS, W29 (+ evals/, azure/)
├─ 10-careerpilot/            # W14–W18, W25, W29 (+ mcp_server/ as its own uv project, security/)
├─ 11-oss-inference/          # W20 BOSS
├─ 12-finetune-lab/           # W21
├─ 13-resume-jd-extractor/    # W22
└─ 14-ai-system-design/       # W26
ticketverse/ticketverse-ai/   # W23–W24, W27–W28: Spring AI service (owned by this track) inside the capstone repo
```

---

## 6. 🔑 Free API keys + Codespaces checklist (do this in W6 Mon)

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
- [ ] A `.devcontainer/devcontainer.json` in `ai-engineering-lab` (Python 3.13 image, Docker-in-Docker and Node features, `postCreateCommand: pip install uv`) so every codespace rebuild is identical.
- [ ] Keys saved as **Codespaces secrets** (they arrive as environment variables) and read via `pydantic-settings` (Python) or `${GROQ_API_KEY}` (Spring) — never hard-coded, never printed in logs, notebooks or screenshots. If you ever use a local `.env`, add it to `.gitignore` *before* the first commit and commit only a `.env.example` with variable *names*.
- [ ] Idle timeout set to 10 minutes; one codespace only; stop it after each session and check usage on the billing page weekly — the free plan gives about **120 core-hours and 15 GB-month storage** per month (2-core by default; 4-core only for the TicketVerse full-stack weeks, W27–W28).
- [ ] Ollama installed in the codespace (Linux install script, then `ollama serve &`) with a small model (`ollama pull llama3.2:1b`) plus an embedding model (`ollama pull nomic-embed-text`).
- [ ] PyTorch installed only from the **CPU-only index** when you first need it (W9) — the default CUDA wheels add several GB.
- [ ] One script calls Gemini, Groq and Ollama by switching only `base_url` + `model` (this becomes `llmkit`).
- [ ] Retries with backoff for HTTP 429 (free tiers *will* rate-limit you) and a provider fallback.

Safety notes:
- **Free tiers are not private.** Google states free-tier prompts/responses may be used to improve its products, and some free OpenRouter endpoints may log or train on prompts. Never send personal data (Aadhaar, PAN, phone numbers, salary slips), your employer's code/data, or real customer documents — use public or synthetic data.
- **If a key leaks** (pushed to GitHub, pasted in chat): revoke/rotate it immediately, then rewrite history or delete the repo copy. Keep GitHub secret scanning / push protection on.
- **Paid accounts:** set budgets and alerts before the first call; your Azure labs (W25) use pay-per-token deployments and end with a teardown script.
- Prefer **keyless auth** (managed identity) once you reach Azure in W25.

---

## 7. Rules, pitfalls & tips

**Rules**
1. **Measure every "improvement".** No number → it didn't happen (hits@5, faithfulness, latency, ₹ cost).
2. **Ship on Saturday.** A tagged, runnable v0 beats a perfect plan. Every BUILD ends with README + tag.
3. **Concepts over frameworks.** Build it raw first (RAG W10, agents W14), then use the framework. Pin versions with `uv.lock`.
4. **Security by default:** treat documents, tool outputs and user reviews as untrusted input; least-privilege tools; human approval for irreversible actions.

**Pitfalls to avoid**
- Version drift: this plan targets **LangChain 1.x, LangGraph 1.x, MCP Python SDK v2** (`FastMCP` was renamed `MCPServer`; MCP spec **2026-07-28** is stateless; `langchain-mcp-adapters` 0.3.x still requires `mcp<2`, so the MCP server lives in its own uv project), **Spring AI 2.0** (Azure OpenAI models are accessed through the OpenAI module; `QuestionAnswerAdvisor` lives in `spring-ai-vector-store-advisor`). Check the version banner of any tutorial.
- Python version: **3.12 on the company laptop** (W1–W5: the Company Portal's Python, started with `py`, plus uv already pointed at the company JFrog) and **3.13 in Codespaces** (W6 onward, via the devcontainer image). Several AI libraries (e.g., CrewAI, NeMo Guardrails) still cap below 3.14. If uv ever fails on the company laptop, use the pip + venv equivalents in Section 4 of [03_SETUP_YOUR_LAPTOP.md](../03_SETUP_YOUR_LAPTOP.md).
- Corporate proxy: Python programs that call internet HTTPS from the company laptop fail with `CERTIFICATE_VERIFY_FAILED` unless you add `pip-system-certs` (or call `truststore.inject_into_ssl()`) — set up in W2 Thu. Installing packages through the company JFrog already works.
- Embedding dimensions: pgvector indexes `vector` up to 2,000 dimensions (`halfvec` up to 4,000) — choose models/dimensions accordingly and never mix embedding models in one index.
- Trusting LLM-as-judge blindly — always calibrate on 10–15 hand-labelled items.
- Building an agent where a workflow (or a single call) is enough.
- Compute limits: Docker runs inside your codespace (W8); a 2-core codespace handles 1–3B local models only, so heavier inference and fine-tuning run on free Colab/Kaggle GPUs (W20–W21).

**Tips**
- Keep `llmkit` as your one provider layer — every later project reuses it.
- Keep a `learning-log.md` in the repo: date, what broke, how you fixed it. These become interview stories.
- Behind schedule? Follow the catch-up rules in Section 7 of `../00_Progress_Tracker/AI_MEMORY.md`: skip *stretch* first, never skip the Saturday ship or the Sunday test, and use the W29 buffer week for red items.

---

## 8. How you're tested on Sundays (AI: 25 minutes)

| Part | Format | Source |
|---|---|---|
| 6 questions | Concepts + **code reading** (e.g., "what does this LangGraph edge do?", "find the bug in this retry loop", "which metric is this computing?") | The week's `self_check`, your own repo code, ⭐ questions from the bank |
| 1 scenario | Short design/trade-off question (e.g., "RAG answers cite the wrong page — how do you debug it?") | The week's topic + earlier weeks (spaced repetition) |

**Scoring /100:** ≥ 80 🟢 green · 60–79 🟡 amber · < 60 🔴 red → weak topics are logged in `WEAKNESS_TRACKER.md` and become remediation tasks in next week's *Fix-it* section. Boss weeks (W4, W9, W15, W20, W25, W30) add the Boss Battle rubric score (target ≥ 80).
