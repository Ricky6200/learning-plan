# 🏗️ System Design · Week 15 — Notifications, food delivery, reliability

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** Notification and food-delivery systems are everyday Indian-product problems (Swiggy, Zomato, Paytm), and reliability vocabulary (SLOs, RPO/RTO, failover) separates SDE-2 answers from SDE-1 answers.

## 🗓️ Sessions

### Monday 01 Feb · 45 min — Reliability: SLI/SLO/SLA, availability math, failover, DR
- 📚 **Learn:** SLI vs SLO vs SLA and error budgets; availability math (serial = multiply, parallel = 1 - (1 - a)^n; 99.9% is about 8.8 h/year down); redundancy, active-active vs active-passive, multi-region; DR with RPO/RTO; golden-signal monitoring and SLO-burn alerts; chaos engineering. Read [Service level objectives (Google SRE book)](https://sre.google/sre-book/service-level-objectives/) and [Principles of Chaos Engineering](https://principlesofchaos.org/); Hindi: [High availability: active-active vs active-passive (Concept && Coding)](https://www.youtube.com/watch?v=iL7_8TmrePM).
- 🛠️ **Do:** In `notes/18-reliability.md`: compute availability of LB (99.99%) -> 3 parallel app servers (99.9% each) -> single DB primary (99.95%); define 3 SLIs + SLOs for the TicketVerse booking API with the monthly error budget in minutes; pick RPO/RTO and a DR strategy (backup-restore, pilot light, warm standby, active-active) with its cost. Done when: the math is shown and each SLO has an alert rule.

### Wednesday 03 Feb · 45 min — Notification system LLD: design + core path
- 📚 **Learn:** Requirements: channels (email/SMS/push/WhatsApp), templates, user preferences and quiet hours, priorities, retries with exponential backoff + jitter, idempotent sends, per-user rate limits. Patterns: Factory/Strategy (channels), Template Method (rendering), Decorator (retry and rate-limit wrappers), Observer (domain events). Read [Timeouts, retries and backoff with jitter (AWS Builders' Library)](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/); watch [Designing notifications for Instagram (Arpit Bhayani)](https://www.youtube.com/watch?v=kIP8L-CSl2Y).
- 🛠️ **Do:** Evolve your W3 kata into `lld/notification`: class diagram + `NotificationService.notify(event)` -> preference filter -> template render -> channel sender; dedupe by `eventId`. Done when: tests prove opted-out channels are skipped, templates render variables, and the same `eventId` sent twice is delivered once.

### Thursday 04 Feb · 45 min — Food delivery LLD (Zomato/Swiggy)
- 📚 **Learn:** Entities: `Customer`, `Restaurant`, `MenuItem`, `Cart`, `Order` (PLACED -> ACCEPTED -> PREPARING -> PICKED_UP -> DELIVERED, or CANCELLED), `DeliveryPartner`, assignment strategy (nearest available), payment, Observer for status updates. Reference: [Food delivery problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/food-delivery-service.md); HLD context: [Design Gopuff (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/gopuff).
- 🛠️ **Do:** Design + core: `OrderService.placeOrder(cart)`, an order state machine with allowed transitions, `DeliveryAssignmentStrategy` (nearest free partner by distance) and observers that notify the customer on every state change. Done when: tests pass for valid/invalid transitions, nearest-partner assignment, a partner never getting two orders at once, and no cancellation after PICKED_UP.

### Saturday 06 Feb · 45 min — PRACTICE: Notification system - async, retries, DLQ
- 📚 **Learn:** Hardening: async dispatch through a bounded `BlockingQueue` + worker pool (backpressure), `RetryingSender` decorator with injectable sleeper, permanent failures to a dead-letter list, quiet hours with an OTP/HIGH-priority bypass. Pattern reference: [Queue-based load leveling (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling).
- 🛠️ **Do:** Add async dispatch, `RetryingSender` (3 attempts, exponential backoff + jitter), `RateLimitedSender` (reuse your W10 limiter), a DLQ, and quiet hours. Done when: >= 6 tests pass: retries stop after success, the 4th failure goes to the DLQ, a full queue rejects with a clear exception, quiet hours delay LOW but not HIGH priority, and per-user limits hold.

## 📦 Deliverable (by Saturday night)
`notes/18-reliability.md`, `lld/notification` (sync core + async/retry/DLQ hardening) and `lld/fooddelivery`, all with passing tests.

## ✅ Self-check (Sunday test preview)
- SLI vs SLO vs SLA: define each with a TicketVerse example.
- Three 99.9% services in series: what is the total availability? And in parallel?
- RPO vs RTO: which DR strategy gives near-zero values of both, and at what cost?
- Why add jitter to exponential backoff?
- How do you guarantee a notification is not sent twice when the sender retries?
- Food delivery: how do you stop one partner from being assigned two orders at the same moment?

## 🚀 Stretch (optional)
Add per-channel circuit breakers and a fallback provider (e.g., a second SMS gateway) to the notification system.
