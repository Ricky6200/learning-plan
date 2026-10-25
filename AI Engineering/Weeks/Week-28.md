# 🤖 AI Engineering · Week 28 — Capstone II: Azure Launch, Observability, Tuning, Demo

> 📅 **Mon 03 May 2027 → Sun 09 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 27](Week-27.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-28.md) · [Week 29 →](Week-29.md)

**Why this week:** One polished, measured, well-explained project beats five half-finished demos. This week `ticketverse-ai` joins the TicketVerse launch on Azure (Java W28 deploys, Azure W28 provisions), and you turn the work into interview stories and public proof.

## 🗓️ Sessions

### Monday 03 May · 45 min — Ship ticketverse-ai for the Azure launch
- 📚 **Learn:** Production readiness for one service: an `azure` profile whose model key comes from Key Vault (Azure W22) through a platform secret reference, readiness and liveness probes on Actuator health groups, resource requests, graceful degradation when the provider is down, and an image tagged by commit SHA in the registry the Java W28 deployment pulls from. Read: [Manage secrets in Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets). Optional: [Spring AI OpenAI chat](https://docs.spring.io/spring-ai/reference/api/chat/openai-chat.html) (base URL and key properties).
- 🛠️ **Do:** Add the `azure` profile (key via environment variable backed by Key Vault, no secret in Git), probes and a degraded-mode response, build and push the image, and open a pull request with the environment values the Java W28 deployment needs. Done when: the image is in the registry, the PR is reviewed against the Java W28 checklist, and a local run with the `azure` profile answers.

### Tuesday 04 May · 45 min — AI observability: traces, token and cost dashboards, SLOs
- 📚 **Learn:** One view across services: OpenTelemetry traces from gateway -> ticketverse-ai -> LLM and tools, `gen_ai` metrics in Prometheus/Grafana (Java W19), prompt and cost views; SLOs for AI endpoints (p95 latency, error rate, cost per request) with alert rules. Read: [Spring AI observability](https://docs.spring.io/spring-ai/reference/observability/index.html). Optional: [OTel GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/).
- 🛠️ **Do:** Build a Grafana (or Langfuse) dashboard for AI endpoints: requests, p50/p95 latency, tokens, cost per day, tool-call errors and cache hit rate. Define 3 SLOs with alert rules. Done when: a dashboard screenshot and the SLO definitions are in `docs/ai-observability.md`.

### Thursday 06 May · 45 min — Latency and cost tuning with load tests
- 📚 **Learn:** Profile before optimising (retrieval, time-to-first-token, tools?), then apply: parallel tool calls, smaller models for routing and summaries, prompt trimming, caching, streaming, `max_tokens`, batched backfills; re-run evals to confirm quality holds. Read: [Locust quickstart](https://docs.locust.io/en/stable/quickstart.html).
- 🛠️ **Do:** Load-test `/ai/assistant` and `/ai/search` with Locust (20 users, 5 minutes), find the top 2 bottlenecks in traces, apply 2 optimisations, then rerun the load test and evals. Done when: a before/after table shows better p95 latency and cost per request with eval scores within 2%.

### Friday 07 May · 45 min — READMEs and a demo script that sell
- 📚 **Learn:** Recruiter-friendly README: problem, demo GIF, architecture diagram, key decisions (ADR style), metrics (evals, latency, cost), 'run in 3 commands', what's next; keep one format across projects. Demo storytelling: problem -> live flow -> one diagram under the hood -> metrics -> next steps, in 3-5 minutes with recorded fallback clips. Read: README styles in [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) (browse 3).
- 🛠️ **Do:** Rewrite the READMEs of TicketVerse AI, DocuMind and CareerPilot (30-second summary, architecture, eval table, security notes, trade-offs) and write `DEMO_SCRIPT.md` with timed sections and fallback clips. Done when: someone can run each project from its README alone and the demo script fits in 5 minutes when rehearsed.

### Saturday 08 May · 45 min — BUILD: live end-to-end check and the demo video
- 📚 **Learn:** Recording tips: 1080p, large fonts, clean terminal and browser, mic check, one take per section, captions; publish unlisted first, then share. Free recorder: [OBS Studio](https://obsproject.com/).
- 🛠️ **Do:** Run the end-to-end script against the live Azure URL from today's Java deployment (fallback: your 4-core codespace stack), record the 4-5 minute TicketVerse AI demo plus a 2-minute DocuMind/CareerPilot montage, upload them (YouTube unlisted or LinkedIn) and link them from the READMEs. You are the last block using the stack: run Java's `infra/teardown`. Done when: the end-to-end run is logged, the videos are linked from the READMEs and `az group exists` returns false.

## 📦 Deliverable (by Saturday night)
`ticketverse-ai` shipped for the Azure launch, an AI observability dashboard with SLOs, measured latency/cost tuning, polished READMEs for three flagship projects, a demo script and a recorded demo video.

## ✅ Self-check (Sunday test preview)
- Walk me through your TicketVerse AI architecture in 2 minutes.
- How does `ticketverse-ai` get its model key in Azure without a secret in Git?
- What was your biggest latency bottleneck, and how did you fix it?
- Which SLOs did you define for AI endpoints, and why those?
- How did you verify that optimisations did not hurt quality?
- Tell me about a bug in your AI system and how you debugged it.

## 🚀 Stretch (optional)
Draft a LinkedIn post 'How I built an AI booking assistant with Spring AI + MCP' (250 words, 1 diagram) and schedule it, or write a technical blog post with your own numbers (e.g., hybrid search + re-ranking gains in DocuMind).
