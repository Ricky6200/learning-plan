# 🏗️ System Design · Week 16 — Notifications, food delivery, reliability

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** Notification and food-delivery systems are everyday Indian-product problems (Swiggy, Zomato, Paytm), and reliability vocabulary (SLOs, RPO/RTO, bulkheads, load shedding) separates SDE-2 answers from SDE-1 answers. AZ-104 exam week: Saturday is deliberately light.

## 🗓️ Sessions

### Monday 08 Feb · 45 min — Reliability: SLOs, availability math, DR, bulkheads, load shedding
- 📚 **Learn:** SLI vs SLO vs SLA and error budgets; availability math (serial = multiply, parallel = 1 - (1 - a)^n; 99.9% is about 8.8 h/year down); active-active vs active-passive, multi-region; DR with RPO/RTO; bulkheads (isolate resource pools so one slow dependency cannot exhaust all threads); load shedding (reject low-priority work early when overloaded). Read 'Service Level Terminology' in [Service level objectives (Google SRE book)](https://sre.google/sre-book/service-level-objectives/). Optional: [Bulkhead pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead).
- 🛠️ **Do:** In `notes/18-reliability.md`: compute availability of LB (99.99%) -> 3 parallel app servers (99.9% each) -> single DB primary (99.95%); define 3 SLIs + SLOs for the TicketVerse booking API with the monthly error budget in minutes; pick RPO/RTO and a DR strategy (backup-restore, pilot light, warm standby, active-active); name one bulkhead and one load-shedding rule. Done when: the math is shown and each SLO has an alert rule.

### Wednesday 10 Feb · 45 min — Notification system LLD: design + core path
- 📚 **Learn:** Requirements: channels (email/SMS/push/WhatsApp), templates, user preferences and quiet hours, priorities, retries with exponential backoff + jitter, idempotent sends, per-user rate limits. Patterns: Factory/Strategy (channels), Template Method (rendering), Decorator (retry and rate-limit wrappers), Observer (domain events). Read [Timeouts, retries and backoff with jitter (AWS Builders' Library)](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/). Optional: [Designing notifications for Instagram (Arpit Bhayani, 37 min)](https://www.youtube.com/watch?v=kIP8L-CSl2Y).
- 🛠️ **Do:** Evolve your W3 kata into `lld/notification`: class diagram + `NotificationService.notify(event)` -> preference filter -> template render -> channel sender; dedupe by `eventId`. Done when: tests prove opted-out channels are skipped, templates render variables, and the same `eventId` sent twice is delivered once.

### Thursday 11 Feb · 45 min — Food delivery LLD (Zomato/Swiggy)
- 📚 **Learn:** Entities: `Customer`, `Restaurant`, `MenuItem`, `Cart`, `Order` (PLACED -> ACCEPTED -> PREPARING -> PICKED_UP -> DELIVERED, or CANCELLED), `DeliveryPartner`, assignment strategy (nearest available), payment, Observer for status updates. Read [Food delivery problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/food-delivery-service.md). Optional: [Design Gopuff (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/gopuff).
- 🛠️ **Do:** Core path: `OrderService.placeOrder(cart)`, an order state machine with allowed transitions, `DeliveryAssignmentStrategy` (nearest free partner) and observers notifying the customer on every state change. Extension question for Sunday: what changes for ride sharing, where drivers accept or decline offers? Done when: tests pass for valid/invalid transitions, nearest-partner assignment, a partner never getting two orders at once, and no cancellation after PICKED_UP.

### Saturday 13 Feb · 45 min — PRACTICE (light, exam week): retrying sender + DLQ
- 📚 **Learn:** Hardening in one step: a `RetryingSender` decorator (3 attempts, exponential backoff + jitter, injectable sleeper so tests do not wait) and a dead-letter list for permanent failures; the queue in front of senders smooths bursts. Pattern reference: [Queue-based load leveling (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling).
- 🛠️ **Do:** Add `RetryingSender` and a DLQ to `lld/notification`. Done when: >= 3 tests pass: retries stop after the first success, the 3rd failure goes to the DLQ, and the recorded sleeps grow exponentially; async dispatch, rate-limited sender and quiet hours go to the stretch.

## 📦 Deliverable (by Saturday night)
`notes/18-reliability.md`, `lld/notification` (sync core + retry/DLQ) and `lld/fooddelivery`, all with passing tests. Sunday mini-design (20 min, full template): hotel booking in `hld/mini/W16-hotel-booking.md`.

## ✅ Self-check (Sunday test preview)
- SLI vs SLO vs SLA: define each with a TicketVerse example.
- Three 99.9% services in series: what is the total availability? And in parallel?
- RPO vs RTO: which DR strategy gives near-zero values of both, and at what cost?
- What is a bulkhead, and when would you shed load instead of queueing it?
- Why add jitter to exponential backoff?
- How do you guarantee a notification is not sent twice when the sender retries?
- Sunday mini-design: a hotel booking system (search by dates, book, cancel) - requirements, API, data model, how you avoid double booking.

## 🚀 Stretch (optional)
Async dispatch through a bounded `BlockingQueue` + worker pool (a full queue rejects clearly), a `RateLimitedSender` reusing your W11 limiter, quiet hours that delay LOW but not HIGH priority, and per-channel circuit breakers with a fallback SMS provider. Ride-sharing extension: [Ride sharing problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/ride-sharing-service.md). Extra: [Using load shedding to avoid overload (AWS)](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/); [Principles of Chaos Engineering](https://principlesofchaos.org/); [Active-active vs active-passive (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=iL7_8TmrePM).
