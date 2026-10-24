# 🏗️ System Design · Week 09 — Splitwise, library, message queues (Boss week)

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Splitwise is a favourite Indian LLD question that tests clean modelling plus an algorithm, and asynchronous messaging is the backbone of the Kafka-based TicketVerse saga you build later in the Java track.

## 🗓️ Sessions

### Monday 21 Dec · 45 min — Message queues & streaming: Kafka vs RabbitMQ vs Service Bus
- 📚 **Learn:** Point-to-point vs pub/sub; log-based streaming (Kafka partitions, offsets, consumer groups, retention) vs broker queues (RabbitMQ exchanges, acks) vs Azure Service Bus (queues, topics, sessions, DLQ); delivery guarantees, per-key ordering, DLQ, backpressure, idempotent consumers. Watch [Message queues (Hello Interview)](https://www.youtube.com/watch?v=1ISRd0bS714) and [Kafka vs RabbitMQ (ByteByteGo)](https://www.youtube.com/watch?v=x4k1XEjNzYQ); read [Azure messaging services compared](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services).
- 🛠️ **Do:** Write `notes/11-messaging.md`: a comparison table (8 rows) and a design for TicketVerse `BookingConfirmed` -> email, analytics, loyalty: broker choice, topic/queue layout, message key for ordering, retry + DLQ policy, consumer idempotency key. Done when: you can explain why 'at-least-once + idempotent consumer' is the default and when ordering per booking matters.

### Wednesday 23 Dec · 45 min — Splitwise LLD: expenses, split types, balances
- 📚 **Learn:** Entities: `User`, `Group`, `Expense`, `Split` (EQUAL/EXACT/PERCENT), `BalanceSheet`; split validation; money as `long` paise or `BigDecimal`; one Strategy per split type. Watch [Splitwise LLD (Concept && Coding)](https://www.youtube.com/watch?v=I4xf4STXgmU); reference: [Splitwise problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/splitwise.md).
- 🛠️ **Do:** Requirements + class diagram, then implement a `SplitStrategy` for EQUAL, EXACT and PERCENT with validation, and a `BalanceSheet` that updates net balances per pair. Done when: tests pass for each split type, rounding (Rs 100 split 3 ways sums to exactly 100), percentages that do not total 100, and exact amounts that do not match the total.

### Thursday 24 Dec · 45 min — Simplify debts + Library management core
- 📚 **Learn:** Simplify debts: compute each user's net balance, then greedily settle the largest creditor with the largest debtor using two heaps (at most N-1 transfers; good, not always minimal). Library core: issue/return, max-books rule, fine strategy, reservation queue + Observer. Watch [Splitwise simplify debt (Concept && Coding)](https://www.youtube.com/watch?v=6UeDb7ORVPI); reference: [Library management problem](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/library-management-system.md).
- 🛠️ **Do:** 15 min: implement `simplifyDebts()` with two `PriorityQueue`s and test that a 3-friend cycle collapses. 30 min: on your W1 library skeleton implement `issue`, `returnCopy` (fine Rs 10/day via `FineStrategy` + `Clock`) and `reserve` (notify the first waiting member on return). Done when: both test sets pass.

### Saturday 26 Dec · 45 min — BOSS BATTLE: Timed Splitwise core + 5 rapid HLD questions
- 📚 **Learn:** Boss rules: 35 min coding from a blank package (no peeking at Wednesday's code), then 10 min rapid-fire HLD. Ask your AI mentor to pick 5 questions from the W5-W9 self-checks (databases, indexing, replication, sharding, CAP, queues). Problem statement: [Splitwise (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/splitwise.md).
- 🛠️ **Do:** 0-35 min: `ExpenseService` with users, `addExpense` (EQUAL/EXACT/PERCENT), net balances, `showBalances(user)` and `simplifyDebts()`, plus >= 5 tests. 35-45 min: answer 5 HLD questions aloud (2 min each) while recording. Score: tests 10 + answers 5 x 2. Done when: the score is logged in `boss/W09.md`; >= 14/20 clears the boss.

## 📦 Deliverable (by Saturday night)
`notes/11-messaging.md`, `lld/splitwise` (with simplify debts), `lld/library` core, and the Boss attempt with score + recording link in `boss/W09.md`.

## ✅ Self-check (Sunday test preview)
- Kafka vs RabbitMQ vs Azure Service Bus: when would you pick each?
- At-most-once, at-least-once, exactly-once: what does each cost?
- How does Kafka guarantee ordering, and what breaks it?
- What is a dead-letter queue, and when should a message go there?
- Explain the greedy simplify-debts algorithm and its complexity.
- How do you represent money in Java to avoid rounding bugs?
- What is backpressure, and how can a consumer apply it?

## 🚀 Stretch (optional)
Find a 4-5 person example where greedy debt simplification needs more transfers than the optimum (the minimum-transfers problem is NP-hard).
