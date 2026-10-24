# 🏗️ System Design · Week 24 — Monitoring, collaborative editing, LLM platforms

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** Observability platforms, real-time collaboration and LLM/RAG platforms are increasingly asked at product companies, and the last one connects your system design skills to your AI-engineering track.

## 🗓️ Sessions

### Monday 05 Apr · 45 min — Metrics monitoring & alerting (time-series DB)
- 📚 **Learn:** Collection (pull like Prometheus vs push agents), ingestion buffer (Kafka), TSDB storage (compression, downsampling, retention tiers), labels and the high-cardinality trap, queries/dashboards, alert evaluation + dedupe + routing, golden signals. Read [Time-series databases (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/time-series-databases), [Prometheus overview](https://prometheus.io/docs/introduction/overview/) and [Monitoring distributed systems (Google SRE)](https://sre.google/sre-book/monitoring-distributed-systems/).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/16-metrics-monitoring/README.md`, estimating ingestion for 10k hosts x 500 metrics every 10 s (points/s and storage/day). Done when: all 7 sections are filled and the alert path from a breached threshold to an on-call page is drawn.

### Wednesday 07 Apr · 45 min — Google Docs: collaborative editing with OT and CRDTs
- 📚 **Learn:** Operational Transformation (server orders operations and transforms concurrent ones) vs CRDTs (operations commute; merge anywhere), one WebSocket session per document, document servers sharded by doc ID, snapshots + operation log, cursors/presence, offline edits. Watch [Real-time collaboration explained (Hello Interview)](https://www.youtube.com/watch?v=EX5uZV3Tzss); read [Figma multiplayer (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/figma-multiplayer) and [crdt.tech](https://crdt.tech/).
- 🛠️ **Do:** In `hld/17-collab-editor/README.md` do the framework in 35 minutes; then 10 minutes by hand: two users insert at position 5 concurrently ('X' and 'Y') - show the OT transform so both replicas converge. Done when: the write-up exists and the worked example converges.

### Thursday 08 Apr · 45 min — LLM chat / RAG platform at scale
- 📚 **Learn:** Gateway (auth, quotas, token-based rate limits) -> orchestrator -> retrieval (hybrid keyword + vector search) -> LLM inference (managed API or self-hosted GPU pool with batching) -> streaming via SSE; conversation store, semantic cache, guardrails, evals and cost/latency observability. Read the [RAG solution design guide (Azure Architecture Center)](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) and [Vector databases (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/vector-databases).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/18-llm-chat-platform/README.md` for 1M DAU x 10 messages x ~1.5k tokens: tokens/s, monthly token cost at an assumed price, cache hit-rate savings. Link it to 'Ask TicketVerse' and your AI-track RAG project. Done when: all 7 sections are filled and streaming + rate limiting by tokens are explained.

### Saturday 10 Apr · 45 min — PRACTICE: Diagram polish + 3 verbal reps
- 📚 **Learn:** Interview delivery: lead with requirements, show numbers early, say trade-offs out loud ('I chose X over Y because...'). Self-review against [System design interview - biggest mistakes (ByteByteGo)](https://www.youtube.com/watch?v=OvufRkoD-D0).
- 🛠️ **Do:** 15 min: finish the three W24 diagrams (PNG + `.excalidraw`). 30 min: record three 10-minute verbal walkthroughs (metrics, docs, LLM platform) and note one weakness per recording. Done when: diagrams and recordings are committed and weaknesses are logged for W25 remediation.

## 📦 Deliverable (by Saturday night)
`hld/16-metrics-monitoring/`, `hld/17-collab-editor/`, `hld/18-llm-chat-platform/` (write-up + PNG each) and 3 recorded walkthroughs.

## ✅ Self-check (Sunday test preview)
- Pull vs push metrics collection: trade-offs?
- What is high cardinality in metrics, and why is it dangerous?
- OT vs CRDT: how does each make replicas converge?
- How do you scale WebSocket servers for collaborative documents?
- How do you rate-limit and bill an LLM API by tokens?
- Where do caching and streaming help in an LLM chat platform?

## 🚀 Stretch (optional)
Add evaluation and observability to the LLM platform design: which metrics (latency, tokens, groundedness) you log and where.
