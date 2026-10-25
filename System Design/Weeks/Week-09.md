# 🏗️ System Design · Week 09 — Splitwise, thread-safe LRU, queues (Boss week)

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Splitwise is a favourite Indian LLD question (clean modelling plus an algorithm), a thread-safe LRU with TTL is a classic concurrency machine-coding task, and asynchronous messaging is the backbone of the Kafka saga TicketVerse uses later in the Java track.

## 🗓️ Sessions

### Monday 21 Dec · 45 min — Message queues & streaming: Kafka vs RabbitMQ vs Service Bus
- 📚 **Learn:** Point-to-point vs pub/sub; log-based streaming (Kafka partitions, offsets, consumer groups, retention) vs broker queues (RabbitMQ exchanges, acks) vs Azure Service Bus (queues, topics, sessions, DLQ); delivery guarantees, per-key ordering, DLQ, backpressure, idempotent consumers. Watch the first 15 minutes of [Message queues (Hello Interview)](https://www.youtube.com/watch?v=1ISRd0bS714). Optional: [Kafka vs RabbitMQ (ByteByteGo, 5 min)](https://www.youtube.com/watch?v=x4k1XEjNzYQ).
- 🛠️ **Do:** Write `notes/11-messaging.md`: a comparison table (8 rows) and a design for TicketVerse `BookingConfirmed` -> email, analytics, loyalty: broker choice, topic/queue layout, message key for ordering, retry + DLQ policy, consumer idempotency key. Done when: you can explain why 'at-least-once + idempotent consumer' is the default and when ordering per booking matters.

### Wednesday 23 Dec · 45 min — Splitwise LLD: split types, balances, simplify debts
- 📚 **Learn:** Entities: `User`, `Group`, `Expense`, `Split` (EQUAL/EXACT/PERCENT), `BalanceSheet`; split validation; money as `long` paise. Simplify debts: compute each user's net balance, then repeatedly settle the largest creditor with the largest debtor using two `PriorityQueue`s (Java W5) - at most N-1 transfers, good but not always minimal. Read [Splitwise problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/splitwise.md). Optional: [Splitwise simplify debt (Concept && Coding, Hindi, 32 min)](https://www.youtube.com/watch?v=6UeDb7ORVPI).
- 🛠️ **Do:** Implement one `SplitStrategy` per split type (EQUAL, EXACT, PERCENT) with validation, and a `BalanceSheet` that updates net balances per pair. Then hand-trace simplify-debts for a 3-friend cycle in `lld/splitwise/DESIGN.md`. Done when: tests pass for each split type, rounding (Rs 100 split 3 ways sums to exactly 10,000 paise), percentages that do not total 100 and exact amounts that do not match the total, and your trace collapses the cycle.

### Thursday 24 Dec · 45 min — Thread-safe LRU cache with TTL (LinkedHashMap wrapper)
- 📚 **Learn:** `new LinkedHashMap<>(16, 0.75f, true)` keeps access order and an overridden `removeEldestEntry` evicts the least-recently used entry (Java W5 Tue). It is not thread-safe, and in access order even `get` reorders entries, so one `ReentrantLock` (Java W9 Mon) guards every operation, unlocked in `finally`. TTL: store `expiresAt` per entry from an injected clock and expire lazily on `get`. Read [LinkedHashMap docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/LinkedHashMap.html). Optional: [CountDownLatch docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CountDownLatch.html).
- 🛠️ **Do:** Write `LruTtlCache<K,V>` (`get`, `put(k, v, ttlMillis)`, `size`) wrapping an access-ordered `LinkedHashMap` + one `ReentrantLock`, with your `TimeSource` (or `java.time.Clock`, Java W7 Thu) injected; no hand-written linked list (DSA W10 Sat does that). Tests: eviction order at capacity 3, `get` refreshes recency, expiry with a fake clock, and 50 threads released together by a `CountDownLatch` doing 1,000 mixed `put`/`get` each. Done when: no exceptions, `size()` never exceeds capacity, and all tests pass 10 runs in a row.

### Saturday 26 Dec · 45 min — BOSS BATTLE: Timed Splitwise core + 5 rapid HLD questions
- 📚 **Learn:** Boss rules: 35 min coding from a blank package (no peeking at Wednesday's code), then 10 min rapid-fire HLD. Ask your AI mentor to pick 5 questions from the W5-W9 self-checks (databases, indexing, replication, sharding, CAP, queues). Problem statement: [Splitwise (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/splitwise.md).
- 🛠️ **Do:** 0-35 min: `ExpenseService` with users, `addExpense` (EQUAL/EXACT/PERCENT), net balances, `showBalances(user)` and `simplifyDebts()`, plus >= 5 tests. 35-45 min: answer 5 HLD questions aloud (2 min each) while recording. Score: tests 10 + answers 5 x 2. Done when: the score is logged in `boss/W09.md`; >= 14/20 clears the boss.

## 📦 Deliverable (by Saturday night)
`notes/11-messaging.md`, `lld/splitwise` (strategies, balances, simplify-debts trace), `labs/lrucache` (thread-safe LRU + TTL with the 50-thread test), and the Boss attempt with score + recording link in `boss/W09.md`.

## ✅ Self-check (Sunday test preview)
- Kafka vs RabbitMQ vs Azure Service Bus: when would you pick each?
- At-most-once, at-least-once, exactly-once: what does each cost?
- How does Kafka guarantee ordering, and what breaks it?
- What is a dead-letter queue, and what is backpressure?
- Explain the greedy simplify-debts algorithm and its complexity.
- How do you represent money in Java to avoid rounding bugs?
- Why must even `get` take the lock in an access-ordered `LinkedHashMap` LRU?

## 🚀 Stretch (optional)
Library core (optional; Java already built a library in W3-W4): on your W1 library model implement `issue`, `returnCopy` with a `FineStrategy` (Rs 10/day via your clock) and `reserve` that notifies the first waiting member (Observer) - see [Library management problem](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/library-management-system.md). Find a 4-5 person example where greedy debt simplification needs more transfers than the optimum (minimum transfers is NP-hard). Extra: [ReentrantLock docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReentrantLock.html); [Azure messaging services compared](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services); [Splitwise LLD (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=I4xf4STXgmU).
