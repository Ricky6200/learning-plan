# 🏗️ System Design · Week 26 — Monitoring, collaborative editing, design follow-ups

> 📅 **Mon 19 Apr 2027 → Sun 25 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 25](Week-25.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-26.md) · [Week 27 →](Week-27.md)

**Why this week:** Observability platforms and real-time collaboration are increasingly asked at product companies; Thursday turns this week's two designs into interview-ready answers. AI-200 exam week: Saturday is deliberately light.

## 🗓️ Sessions

### Monday 19 Apr · 45 min — Metrics monitoring & alerting (time-series DB)
- 📚 **Learn:** Collection (pull like Prometheus vs push agents), ingestion buffer (Kafka), TSDB storage (append-only, delta compression, time partitions, downsampling, retention tiers), labels and the high-cardinality trap, dashboards, alert evaluation + dedupe + routing, golden signals. Read 'The Building Blocks' in [Time-series databases (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/time-series-databases). Optional: [Prometheus overview](https://prometheus.io/docs/introduction/overview/).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-5 in `hld/16-metrics-monitoring/README.md`, estimating ingestion for 10k hosts x 500 metrics every 10 s (points/s and storage/day). Done when: the estimate is shown and the alert path from a breached threshold to an on-call page is drawn.

### Wednesday 21 Apr · 45 min — Google Docs: collaborative editing with OT and CRDTs
- 📚 **Learn:** Operational Transformation (a server orders operations and transforms concurrent ones) vs CRDTs (operations commute; merge anywhere), one WebSocket session per document, document servers sharded by doc ID, snapshots + operation log, cursors/presence, offline edits. Watch [Real-time collaboration explained (Hello Interview, 16 min)](https://www.youtube.com/watch?v=EX5uZV3Tzss). Optional: [crdt.tech](https://crdt.tech/).
- 🛠️ **Do:** In `hld/17-collab-editor/README.md` do steps 1-5 in a 20-minute sprint; then 5 minutes by hand: two users insert at position 5 concurrently ('X' and 'Y') - show the OT transform so both replicas converge. Done when: the write-up exists and the worked example converges.

### Thursday 22 Apr · 45 min — Follow-up: compare, deep-dive and diagram both designs
- 📚 **Learn:** Follow-up method: compare each design with a reference, keep what you got right, then write the deep dives you missed (cardinality explosion, alert latency, scaling WebSocket servers, storage growth). Read 'Potential Deep Dives' in [Metrics monitoring (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/metrics-monitoring). Optional: [Design Google Docs (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/google-docs).
- 🛠️ **Do:** For each of Monday's and Wednesday's designs: list 3 gaps versus the reference, add 2 deep dives, and draw the Excalidraw diagram (PNG + `.excalidraw`). Done when: both folders have a one-page write-up + PNG and a 'What I changed after review' section.

### Saturday 24 Apr · 45 min — PRACTICE (light, exam week): 2 verbal reps
- 📚 **Learn:** Interview delivery: lead with requirements, show numbers early, say trade-offs out loud ('I chose X over Y because...'). Self-review against [System design interview - biggest mistakes (ByteByteGo, 7 min)](https://www.youtube.com/watch?v=OvufRkoD-D0).
- 🛠️ **Do:** Record two 8-minute verbal walkthroughs (metrics monitoring, collaborative editor) and note one weakness per recording. Done when: both recordings are linked from the W26 folders and the weaknesses are logged for W27 remediation.

## 📦 Deliverable (by Saturday night)
`hld/16-metrics-monitoring/` and `hld/17-collab-editor/` (write-up + PNG + review notes each) and 2 recorded walkthroughs.

## ✅ Self-check (Sunday test preview)
- Pull vs push metrics collection: trade-offs?
- What is high cardinality in metrics, and why is it dangerous?
- How does a time-series database compress and downsample data?
- OT vs CRDT: how does each make replicas converge?
- How do you scale WebSocket servers for collaborative documents?
- What did comparing your designs with a reference change in your answers?

## 🚀 Stretch (optional)
LLM chat / RAG platform design (also a W27 mock option): gateway with token-based rate limits -> orchestrator -> hybrid retrieval -> LLM inference -> streaming via SSE, semantic cache, guardrails, evals and cost tracking; link it to your AI-track design docs. References: [RAG solution design guide (Azure Architecture Center)](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide); [Vector databases (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/vector-databases); [Figma multiplayer (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/figma-multiplayer); [Monitoring distributed systems (Google SRE)](https://sre.google/sre-book/monitoring-distributed-systems/).
