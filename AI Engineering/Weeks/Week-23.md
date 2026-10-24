# 🤖 AI Engineering · Week 23 — AI System Design at Scale

> 📅 **Mon 29 Mar 2027 → Sun 04 Apr 2027** · Season 5 — Cloud Ascension · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 22](Week-22.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-23.md) · [Week 24 →](Week-24.md)

**Why this week:** Senior-leaning AI interviews include a design round (LLM gateway, RAG at scale, production agents) where trade-offs on cost, latency, safety and evals matter more than code.

## 🗓️ Sessions

### Monday 29 Mar · 45 min — LLM gateway: routing, fallbacks, quotas, cost attribution
- 📚 **Learn:** Gateway duties: one API for many providers, auth, per-tenant token quotas and rate limits, routing and fallbacks across providers/regions, caching, PII redaction, logging and cost attribution; build vs buy (LiteLLM, Azure API Management AI gateway). Read: [AI gateway in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities), [LiteLLM routing](https://docs.litellm.ai/docs/routing), [Building a GenAI platform](https://huyenchip.com/2024/07/25/genai-platform.html).
- 🛠️ **Do:** Design an LLM gateway for a 2,000-employee company: components, request flow, token-bucket quotas per team, fallback policy, cost-attribution schema and failure modes. Done when: `11-ai-system-design/llm_gateway.md` has a diagram, an API sketch, a data model and 5 trade-offs.

### Tuesday 30 Mar · 45 min — Multi-tenant RAG and vector database scaling
- 📚 **Learn:** Tenant isolation (index per tenant vs shared index + tenant filter vs separate database), document-level ACL security trimming, ingestion at scale (queues, idempotency, re-embedding on model change), vector scaling: HNSW RAM, quantization (halfvec, binary), shards and replicas. Read: [Secure multitenant RAG](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/secure-multitenant-rag) and [Qdrant distributed deployment](https://qdrant.tech/documentation/guides/distributed_deployment/).
- 🛠️ **Do:** Size 10M chunks x 768 dimensions: raw float32 size (about 30 GB), rough HNSW overhead, halfvec savings, and shards/replicas for 200 QPS at p95 under 300 ms. Choose an isolation model for 50 tenants with ACLs. Done when: `rag_at_scale.md` contains formulas, numbers and a decision record.

### Thursday 01 Apr · 45 min — Caching layers, feedback pipelines, guardrail placement, cost models
- 📚 **Learn:** Cache layers (exact, semantic, provider prompt caching, retrieval cache) and invalidation; online feedback -> labelled data -> eval sets -> regression gates; guardrails at the gateway, retrieval (ACLs), tool layer and output; cost = requests x tokens x price + infrastructure. Read: [RAG design and evaluation guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) (skim) and [What we learned from a year of building with LLMs](https://applied-llms.org/).
- 🛠️ **Do:** Build a cost model (spreadsheet or script) for a customer-support agent: 50k conversations/day, 6 turns, tokens per step, cache hit rates and a 2-model cascade. Compute INR per month and cost per resolved ticket, with sensitivity to cache hit rate. Done when: low/expected/high scenarios are committed and the biggest cost driver is named.

### Friday 02 Apr · 45 min — Timed practice: ChatGPT-like chat and a support agent
- 📚 **Learn:** Design framework: requirements (functional, scale, latency, safety, compliance) -> APIs -> high-level architecture -> data and ingestion -> retrieval/generation -> evals and observability -> safety -> scaling and cost -> trade-offs. Reference: [Patterns for building LLM-based systems](https://eugeneyan.com/writing/llm-patterns/).
- 🛠️ **Do:** Do two 20-minute timed designs on paper: (1) ChatGPT-like chat at 1M daily users (streaming, conversation storage, rate limits, model routing, abuse prevention); (2) customer-support agent with tools and human handoff. Scan or photograph them and write 10 takeaway bullets each. Done when: both are in `11-ai-system-design/` with an improvement list.

### Saturday 03 Apr · 45 min — BOSS BATTLE: 45-minute AI system-design mock plus design doc
- 📚 **Learn:** Prompt: 'Enterprise RAG over 10M documents for a bank (Hindi + English, ACLs, audit trail)'. 35 minutes designing aloud (recorded), 10 minutes writing a 1-page doc. Rubric /100: requirements 15, architecture 25, retrieval and evals 20, safety and compliance 15, scale and cost 15, communication 10. Reference: [Baseline Foundry chat architecture](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-microsoft-foundry-chat).
- 🛠️ **Do:** Run the mock with a friend, or record yourself and use an AI interviewer only for follow-up questions after you finish. Write `DESIGN_enterprise_rag.md` (diagram, key decisions, numbers, risks), self-score with the rubric and list 3 gaps for W26. Done when: recording and doc are committed and the score is 80+.

## 📦 Deliverable (by Saturday night)
`11-ai-system-design/`: LLM gateway design, RAG-at-scale sizing sheet, support-agent cost model, two timed practice designs, recorded mock and a 1-page enterprise RAG design doc.

## ✅ Self-check (Sunday test preview)
- Design an LLM gateway: what are its responsibilities and failure modes?
- How do you isolate tenants and enforce document ACLs in RAG?
- Estimate memory for 10M 768-dimension vectors and explain how to reduce it.
- Where would you place guardrails in an agentic system?
- How do you build a feedback loop that improves an AI product over time?
- How would you cut LLM cost by 50% without hurting quality much?
- How do you roll out a new model version safely?

## 🚀 Stretch (optional)
Redesign the support agent as an explicit workflow (per [Building effective agents](https://www.anthropic.com/research/building-effective-agents)) instead of an open-ended agent and compare risks and cost.
