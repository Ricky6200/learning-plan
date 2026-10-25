# 🤖 AI Engineering · Week 19 — LLMOps: Observability, Prompts, CI Eval Gates, Public Demo

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** Models, prompts and data change weekly in production AI. Traces, versioned prompts, eval gates and cost control are what make AI features safe to ship continuously, and a public demo link makes your work visible to recruiters before you start applying next week.

## 🗓️ Sessions

### Monday 01 Mar · 45 min — Observability with OpenTelemetry and Langfuse
- 📚 **Learn:** OpenTelemetry basics: a trace is a tree of spans with attributes, sent by an exporter; auto-instrumentation creates spans for FastAPI requests; the GenAI semantic conventions name LLM attributes (`gen_ai.request.model`, `gen_ai.usage.input_tokens`) so any backend understands them; Langfuse ingests these traces. Log inputs only after PII masking (W18). Read: [OpenTelemetry Python getting started](https://opentelemetry.io/docs/languages/python/getting-started/). Optional: [OTel GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/).
- 🛠️ **Do:** Add FastAPI auto-instrumentation to DocuMind with a console exporter, plus a manual span around each LLM call carrying model and token attributes. Send traces with session/user IDs and masked inputs to Langfuse and build a dashboard for p95 latency, cost per day and error rate. Done when: the console shows request and LLM spans with `gen_ai` attributes and the dashboard charts 30+ traces.

### Tuesday 02 Mar · 45 min — Prompt management, versioning and rollback
- 📚 **Learn:** Prompts as versioned artifacts with labels (production, staging), templating, linking prompt versions to traces and eval results, instant rollback; Git-only prompts vs a prompt registry. Read: [Langfuse prompt management](https://langfuse.com/docs/prompt-management/overview).
- 🛠️ **Do:** Move DocuMind's answer prompt and CareerPilot's planner prompt into Langfuse prompt management (or a local `prompts/` registry with semver if offline). Fetch by label at runtime with a cached fallback and tag traces with the prompt version. Create v2 of one prompt. Done when: moving the `production` label from v1 to v2 changes behaviour without a redeploy and traces show the version.

### Thursday 04 Mar · 45 min — Evals in CI: a regression gate on pull requests
- 📚 **Learn:** Offline evals as tests: a small, fast smoke set on every PR and a bigger nightly set, with a threshold per metric; reduce judge flakiness (temperature 0, deterministic checks first, cached calls). In GitHub Actions (your first `ci.yml` was Java W14 Sat) a `services:` block can start a pgvector container for the job, and API keys come from repository secrets. Read: [Building and testing Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python). Optional: [PostgreSQL service containers](https://docs.github.com/en/actions/tutorials/use-containerized-services/create-postgresql-service-containers).
- 🛠️ **Do:** Create `.github/workflows/eval.yml`: on PR start a pgvector service, ingest a small fixture corpus, then run unit tests, a 10-question DocuMind smoke eval (recall@5) and 10 attack cases; fail if recall@5 drops more than 0.05 below the committed baseline or the block rate falls under 90%. Store keys as GitHub secrets. Done when: a PR with a deliberately worse retriever or prompt is blocked.

### Friday 05 Mar · 45 min — Cost and latency optimization; feedback loops
- 📚 **Learn:** Levers: shorter prompts and context, `max_tokens`, prompt/context caching (stable prefix first), model routing and cascades, batching, streaming for time-to-first-token, semantic cache; A/B tests and user feedback (thumbs, edits) close the loop. Read: [Building a GenAI platform (Chip Huyen)](https://huyenchip.com/2024/07/25/genai-platform.html) (router, gateway and cache sections). Optional: [Gemini context caching notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Caching.ipynb).
- 🛠️ **Do:** Implement a 2-tier cascade in DocuMind: a small fast model answers first and escalates to a stronger model when the retrieval score is low. Add a thumbs up/down endpoint stored with the trace ID. Compare cost and quality vs a single model on 10 questions. Done when: a table shows savings and quality delta, and feedback appears on traces.

### Saturday 06 Mar · 45 min — BUILD: public DocuMind demo on a Hugging Face Space
- 📚 **Learn:** A Docker Space runs your container on free CPU hardware (it sleeps when idle): the Dockerfile must listen on the port in the README front matter (`app_port`, default 7860) and secrets are set in the Space settings. A Space has no Postgres, so swap in an in-memory retriever over pre-computed embeddings (your retriever interface makes this a small change). Read: [Docker Spaces](https://huggingface.co/docs/hub/spaces-sdks-docker).
- 🛠️ **Do:** Create a public Docker Space for a DocuMind demo over 2-3 public PDFs: `DemoRetriever` loading a NumPy `.npy` embedding matrix, `GEMINI_API_KEY` as a Space secret, a per-IP rate limit and a minimal HTML page that streams answers through a GET SSE endpoint. Link it from the README. Done when: the public URL answers a question with citations and the README shows the link and a screenshot.

## 📦 Deliverable (by Saturday night)
OpenTelemetry + Langfuse dashboards, labelled prompt versions, an `eval.yml` PR gate with a pgvector service, cascade routing with measured savings, feedback capture and a public DocuMind demo Space.

## ✅ Self-check (Sunday test preview)
- What would you log for every LLM call, and what must you never log?
- What are traces, spans and the OpenTelemetry GenAI semantic conventions, and why use them?
- How do you version prompts and roll back safely?
- Design an eval gate for a RAG app: what runs per PR vs nightly?
- Explain model cascades/routing and how you would prove they help.
- How does prompt caching work, and how should prompts be structured to benefit?

## 🚀 Stretch (optional)
Add a nightly workflow that runs the full golden set and the 10 CareerPilot scenarios and uploads reports, documenting the policy in `LLMOPS.md`; or A/B test prompt v2 for a week using feedback scores.
