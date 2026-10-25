# 🏗️ System Design · Week 18 — Case studies: rate limiter, notifications

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** Full case studies are the HLD interview itself: this week you run the framework end to end twice, in short timed sprints plus follow-ups, and produce interview-ready write-ups and diagrams.

## 🗓️ Sessions

### Monday 22 Feb · 45 min — Case study: distributed rate limiter (steps 1-4)
- 📚 **Learn:** Requirements (limit by user/IP/API key, multiple rules, < 5 ms overhead), estimation (QPS, Redis memory per key), API (`isAllowed(clientId, rule)` + `X-RateLimit-*` headers), data model (Redis keys + TTL). Watch the first 15 minutes of [Design a distributed rate limiter (Hello Interview)](https://www.youtube.com/watch?v=MIJFyUPG4Z4). Optional: [Design rate limiter (Concept && Coding, Hindi, 34 min)](https://www.youtube.com/watch?v=X5daFTDfy2g).
- 🛠️ **Do:** In `hld/02-rate-limiter/README.md` do framework steps 1-4 solo in a 25-minute sprint. Done when: a Redis memory estimate for 10M active keys is shown and the API includes the rate-limit headers and the 429 response.

### Wednesday 24 Feb · 45 min — Rate limiter deep dives: Redis, Lua, failure modes
- 📚 **Learn:** Placement (gateway vs sidecar vs library), Redis Cluster sharding by client key, atomic check-and-update with a Lua script, local + global hybrid limits, fail-open vs fail-closed, hot clients, multi-region limits. Read [Redis Lua scripting intro](https://redis.io/docs/latest/develop/programmability/eval-intro/). Optional: [Rate limiting pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern).
- 🛠️ **Do:** Finish steps 5-7 in 20 minutes: high-level diagram (Excalidraw), 3 deep dives (atomicity with Lua; Redis outage -> fail-open with local fallback; hot-key mitigation) and trade-offs. Then 5 minutes comparing with [the Hello Interview breakdown](https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter). Done when: the write-up fits one page, the PNG is committed and 2 gaps are listed.

### Thursday 25 Feb · 45 min — Case study: notification system at scale (steps 1-5)
- 📚 **Learn:** Requirements: multi-channel, 10M+/day, priorities, templates, preferences, dedupe, delivery tracking. Architecture: API -> validation -> preference service -> queues per priority/channel -> channel workers -> providers (email/SMS/FCM/APNs/WhatsApp) with retries, DLQ, per-provider rate limits; analytics. Read [Priority Queue pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/priority-queue). Optional: [Design a notification system (Nikhil Lohia, 21 min)](https://www.youtube.com/watch?v=1E3oeYkJ1P8).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-5 in `hld/03-notification-system/README.md`, with an estimate for 10M notifications/day at 10x peak and a box diagram. Done when: requirements, estimate, API, data model and diagram are filled and you have written down the two deep dives you will do on Saturday.

### Saturday 27 Feb · 45 min — PRACTICE: Notification deep dives + polish both write-ups
- 📚 **Learn:** Diagram conventions: clients left, data stores as cylinders, solid arrows = sync calls, dashed = async/events, number the main flow. Deep-dive targets: avoiding double sends (idempotency key) and surviving a provider outage (circuit breaker + fallback provider). Compare afterwards with [Design a notification system (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/notification-system).
- 🛠️ **Do:** 15 min: write the two notification deep dives + trade-offs and clean both diagrams (export PNG + `.excalidraw`). 10 min: record a 3-minute summary of each design. Done when: both folders have README + `.excalidraw` + PNG, each case has one ADR in `adr/`, and your AI mentor's review comments are addressed or logged.

## 📦 Deliverable (by Saturday night)
`hld/02-rate-limiter/` and `hld/03-notification-system/` each with a one-page write-up, `.excalidraw` source, PNG export, an ADR for its key decision and a 3-minute recorded summary.

## ✅ Self-check (Sunday test preview)
- Where would you place a rate limiter in a microservices system, and why?
- How do you make check-and-increment atomic in Redis?
- Fail-open or fail-closed when the rate-limit store is down? Defend your answer.
- Notification system: how do you prioritise OTPs over marketing messages?
- How do you handle a third-party SMS provider outage?
- How do you track delivery status end to end?

## 🚀 Stretch (optional)
Add a 'notification digest' feature (batch low-priority messages hourly per user) to your design and explain the data model change. Test your W11 Redis Lua token bucket with Testcontainers (Java W12 Sat), pulling `redis:8` through the company's Docker mirror in JFrog via the [image name prefix setting](https://java.testcontainers.org/features/image_name_substitution/).
