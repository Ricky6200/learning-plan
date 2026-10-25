# 🤖 AI Engineering · Week 26 — AI System Design at Scale

> 📅 **Mon 19 Apr 2027 → Sun 25 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 25](Week-25.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-26.md) · [Week 27 →](Week-27.md)

**Why this week:** Senior-leaning AI interviews include a design round (LLM gateway, RAG at scale, production agents) where trade-offs on cost, latency, safety and evals matter more than code. (AI-200 exam week: Friday and Saturday are deliberately light.)

## 🗓️ Sessions

### Monday 19 Apr · 45 min — LLM gateway: routing, fallbacks, quotas, cost attribution
- 📚 **Learn:** Gateway duties: one API for many providers, auth, per-tenant token quotas and rate limits (token buckets from SD W11), routing and fallbacks across providers and regions, caching, PII redaction, logging and cost attribution; build vs buy (LiteLLM, Azure API Management AI gateway). Read: [AI gateway in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities). Optional: [LiteLLM routing](https://docs.litellm.ai/docs/routing).
- 🛠️ **Do:** Design an LLM gateway for a 2,000-employee company: components, request flow, token-bucket quotas per team, fallback policy, cost-attribution schema and failure modes. Done when: `14-ai-system-design/llm_gateway.md` has a diagram, an API sketch, a data model and 5 trade-offs.

### Tuesday 20 Apr · 45 min — Multi-tenant RAG and vector database scaling
- 📚 **Learn:** Tenant isolation (index per tenant vs shared index + tenant filter vs separate database), document-level ACL security trimming, ingestion at scale (queues, idempotency, re-embedding on model change), vector scaling: HNSW RAM, quantization (halfvec, binary), shards and replicas (SD W7). Read: [Secure multitenant RAG](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag). Optional: [Qdrant distributed deployment](https://qdrant.tech/documentation/guides/distributed_deployment/).
- 🛠️ **Do:** Size 10M chunks x 768 dimensions: raw float32 size (about 30 GB), rough HNSW overhead, halfvec savings, and shards/replicas for 200 QPS at p95 under 300 ms. Choose an isolation model for 50 tenants with ACLs. Done when: `rag_at_scale.md` contains formulas, numbers and a decision record.

### Thursday 22 Apr · 45 min — Caching layers, feedback pipelines, guardrail placement, cost models
- 📚 **Learn:** Cache layers (exact, semantic, provider prompt caching, retrieval cache) and invalidation; online feedback -> labelled data -> eval sets -> regression gates; guardrails at the gateway, retrieval (ACLs), tool layer and output; cost = requests x tokens x price + infrastructure. Read: [What we learned from a year of building with LLMs](https://applied-llms.org/) (tactical section). Optional: [RAG design and evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide).
- 🛠️ **Do:** Build a cost model (spreadsheet or script) for a customer-support agent: 50k conversations/day, 6 turns, tokens per step, cache hit rates and a 2-model cascade. Compute INR per month and cost per resolved ticket, with sensitivity to cache hit rate. Done when: low/expected/high scenarios are committed and the biggest cost driver is named.

### Friday 23 Apr · 45 min — Timed practice: a ChatGPT-like chat service (light)
- 📚 **Learn:** Design framework: requirements (functional, scale, latency, safety, compliance) -> APIs -> high-level architecture -> data and ingestion -> retrieval/generation -> evals and observability -> safety -> scaling and cost -> trade-offs. Read: [Patterns for building LLM-based systems](https://eugeneyan.com/writing/llm-patterns/) (skim the headings).
- 🛠️ **Do:** AI-200 week, so one 20-minute timed design on paper: a ChatGPT-like chat service for 1M daily users (streaming, conversation storage, rate limits, model routing, abuse prevention). Photograph it and write 8 takeaway bullets. Done when: the design and bullets are in `14-ai-system-design/`.

### Saturday 24 Apr · 45 min — PRACTICE: one-page enterprise RAG design (light)
- 📚 **Learn:** Prompt: 'Enterprise RAG over 10M documents for a bank (Hindi + English, ACLs, audit trail)'. Reuse this week's gateway, sizing and cost notes; aim for decisions and numbers, not prose. Reference: [Baseline Foundry chat architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat).
- 🛠️ **Do:** AI-200 exam day, so 25 minutes only: write `DESIGN_enterprise_rag.md` (diagram, 5 key decisions, sizing numbers, 3 risks) from your notes and list 3 gaps to practise in W30. Done when: the one-page design and the gap list are committed.

## 📦 Deliverable (by Saturday night)
`14-ai-system-design/`: LLM gateway design, RAG-at-scale sizing sheet, support-agent cost model, a timed chat-service design and a 1-page enterprise RAG design doc.

## ✅ Self-check (Sunday test preview)
- Design an LLM gateway: what are its responsibilities and failure modes?
- How do you isolate tenants and enforce document ACLs in RAG?
- Estimate memory for 10M 768-dimension vectors and explain how to reduce it.
- Where would you place guardrails in an agentic system?
- How do you build a feedback loop that improves an AI product over time?
- How would you cut LLM cost by 50% without hurting quality much?
- How do you roll out a new model version safely?

## 🚀 Stretch (optional)
After the exam, do a recorded 45-minute design mock of the customer-support agent (tools + human handoff), or redesign it as an explicit workflow (per [Building effective agents](https://www.anthropic.com/research/building-effective-agents)) and compare risks and cost.
