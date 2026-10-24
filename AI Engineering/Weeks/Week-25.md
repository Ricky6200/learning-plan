# 🤖 AI Engineering · Week 25 — Capstone II: Observability, Tuning, Demo

> 📅 **Mon 12 Apr 2027 → Sun 18 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 24](Week-24.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-25.md) · [Week 26 →](Week-26.md)

**Why this week:** One polished, measured, well-explained project beats five half-finished demos. This week converts your work into interview stories and public proof.

## 🗓️ Sessions

### Monday 12 Apr · 45 min — AI observability: traces, token and cost dashboards, SLOs
- 📚 **Learn:** One view across services: OpenTelemetry traces from gateway -> ticketverse-ai -> LLM and tools, `gen_ai` metrics in Prometheus/Grafana, prompt and cost views; SLOs for AI endpoints (p95 latency, error rate, cost per request). Read: [Spring AI observability](https://docs.spring.io/spring-ai/reference/observability/index.html) and [OTel GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/).
- 🛠️ **Do:** Build a Grafana (or Langfuse) dashboard for AI endpoints: requests, p50/p95 latency, tokens, cost per day, tool-call errors, cache hit rate. Define 3 SLOs with alert rules. Done when: a dashboard screenshot and the SLO definitions are in `docs/ai-observability.md`.

### Tuesday 13 Apr · 45 min — Latency and cost tuning with load tests
- 📚 **Learn:** Profile before optimising (retrieval, time-to-first-token, tools?), then apply: parallel tool calls, smaller models for routing/summaries, prompt trimming, caching, streaming, `max_tokens`, batched backfills; re-run evals to confirm quality holds. Load-testing tool: [Locust](https://locust.io/) (Python).
- 🛠️ **Do:** Load-test `/ai/assistant` and `/ai/search` (20 users, 5 minutes), find the top 2 bottlenecks in traces, apply 2 optimisations, then rerun load and evals. Done when: a before/after table shows better p95 latency and cost per request with eval scores within 2%.

### Thursday 15 Apr · 45 min — READMEs, decision records and resume bullets that sell
- 📚 **Learn:** Recruiter-friendly README: problem, demo GIF, architecture diagram, key decisions (ADR style), metrics (evals, latency, cost), 'run in 3 commands', what's next; keep the format consistent across projects. Browse README styles in [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps).
- 🛠️ **Do:** Rewrite the READMEs of TicketVerse AI, DocuMind and CareerPilot: 30-second summary, architecture, eval table, security notes, trade-offs and 'what I learned'. Add 3 numbers-backed resume bullets to `Career & Interview Prep`. Done when: someone can run each project from its README alone and understand its value in 60 seconds.

### Friday 16 Apr · 45 min — Demo script and LinkedIn post draft
- 📚 **Learn:** Demo storytelling: problem -> live flow -> one diagram under the hood -> metrics -> next steps, in 3-5 minutes with recorded fallback clips. A 'How I built...' post: hook, problem, approach, numbers, lesson, link. Example of a strong build write-up: [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system).
- 🛠️ **Do:** Write `DEMO_SCRIPT.md` (timed sections, commands, fallback clips) and draft a LinkedIn post 'How I built an AI booking assistant with Spring AI + MCP' (250 words max, 1 diagram). Rehearse once with a timer. Done when: both are committed and the rehearsal fits in 5 minutes.

### Saturday 17 Apr · 45 min — BUILD: record and publish the demo video
- 📚 **Learn:** Recording tips: 1080p, large fonts, clean terminal and browser, mic check, one take per section, captions; publish unlisted first, then share. Free recorder: [OBS Studio](https://obsproject.com/).
- 🛠️ **Do:** Record the 4-5 minute TicketVerse AI demo plus a 2-minute DocuMind/CareerPilot montage, upload (YouTube unlisted or LinkedIn), link them from the READMEs and publish or schedule the LinkedIn post. Done when: all video links work, the post is live or scheduled and the READMEs embed the demo.

## 📦 Deliverable (by Saturday night)
AI observability dashboard with SLOs, measured latency/cost tuning, polished READMEs for three flagship projects, demo script, recorded demo video and a LinkedIn post.

## ✅ Self-check (Sunday test preview)
- Walk me through your TicketVerse AI architecture in 2 minutes.
- What was your biggest latency bottleneck, and how did you fix it?
- Which SLOs did you define for AI endpoints, and why those?
- How did you verify that optimisations did not hurt quality?
- What would you do differently if you rebuilt the project?
- Tell me about a bug in your AI system and how you debugged it.

## 🚀 Stretch (optional)
Write a technical blog post on one deep topic with your own numbers (e.g., hybrid search + re-ranking gains in DocuMind).
