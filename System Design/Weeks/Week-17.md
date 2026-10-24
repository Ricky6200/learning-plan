# 🏗️ System Design · Week 17 — Case studies: rate limiter, notifications

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Full case studies are the HLD interview itself: this week you run the framework end to end twice and produce interview-ready write-ups and diagrams.

## 🗓️ Sessions

### Monday 15 Feb · 45 min — Case study: distributed rate limiter (steps 1-4)
- 📚 **Learn:** Requirements (limit by user/IP/API key, multiple rules, < 5 ms overhead), estimation (QPS, Redis memory per key), API (`isAllowed(clientId, rule)` + `X-RateLimit-*` headers), data model (Redis keys + TTL). Read [Design a distributed rate limiter (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter); watch its [walkthrough](https://www.youtube.com/watch?v=MIJFyUPG4Z4) (first 25 min); Hindi: [Design rate limiter (Concept && Coding)](https://www.youtube.com/watch?v=X5daFTDfy2g).
- 🛠️ **Do:** In `hld/02-rate-limiter/README.md` do framework steps 1-4 solo in 25 minutes, then spend 15 minutes comparing with the Hello Interview breakdown and fixing gaps. Done when: a Redis memory estimate for 10M active keys is shown and the API includes headers and the 429 response.

### Wednesday 17 Feb · 45 min — Rate limiter deep dives: Redis, Lua, failure modes
- 📚 **Learn:** Placement (gateway vs sidecar vs library), Redis Cluster sharding by client key, atomic check-and-update with Lua, local + global hybrid limits, fail-open vs fail-closed, hot clients, multi-region limits. Read [Redis Lua scripting intro](https://redis.io/docs/latest/develop/programmability/eval-intro/) and [Rate limiting pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern).
- 🛠️ **Do:** Finish steps 5-7: high-level diagram (Excalidraw), 3 deep dives (atomicity with Lua; Redis outage -> fail-open with local fallback; hot-key mitigation) and a trade-offs section. Done when: the write-up fits one page and the diagram PNG is committed.

### Thursday 18 Feb · 45 min — Case study: notification system at scale
- 📚 **Learn:** Requirements: multi-channel, 10M+/day, priorities, templates, preferences, dedupe, delivery tracking. Architecture: API -> validation -> preference service -> queues per priority/channel -> channel workers -> providers (email/SMS/FCM/APNs/WhatsApp) with retries, DLQ, per-provider rate limits; analytics. Watch [Design a notification system (Nikhil Lohia)](https://www.youtube.com/watch?v=1E3oeYkJ1P8); read [Priority Queue pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/priority-queue).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/03-notification-system/README.md`, with an estimate for 10M notifications/day at 10x peak. Include how you avoid double sends (idempotency key) and survive a provider outage (circuit breaker + fallback provider). Done when: all 7 sections are filled and you note your two weakest sections.

### Saturday 20 Feb · 45 min — PRACTICE: Polish both write-ups + Excalidraw diagrams
- 📚 **Learn:** Diagram conventions: clients left, data stores as cylinders, solid arrows = sync calls, dashed = async/events, number the main flow. Reuse the write-up template from `HLD_INTERVIEW_FRAMEWORK.md`; draw in [Excalidraw](https://excalidraw.com/).
- 🛠️ **Do:** 20 min per case: clean diagram, export PNG + `.excalidraw`, add 'Trade-offs I made' and 'What changes at 10x' sections. Last 5 min: record a 3-minute summary of each design. Done when: both folders have README + `.excalidraw` + PNG and your AI mentor's review comments are addressed or logged.

## 📦 Deliverable (by Saturday night)
`hld/02-rate-limiter/` and `hld/03-notification-system/` each with a one-page write-up, `.excalidraw` source, PNG export and a 3-minute recorded summary.

## ✅ Self-check (Sunday test preview)
- Where would you place a rate limiter in a microservices system, and why?
- How do you make check-and-increment atomic in Redis?
- Fail-open or fail-closed when the rate-limit store is down? Defend your answer.
- Notification system: how do you prioritise OTPs over marketing messages?
- How do you handle a third-party SMS provider outage?
- How do you track delivery status end to end?

## 🚀 Stretch (optional)
Add a 'notification digest' feature (batch low-priority messages hourly per user) to your design and explain the data model change.
