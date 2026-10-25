# 🏗️ System Design · Week 13 — Pub-sub, job scheduler, microservice patterns

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** Building a mini Kafka and a job scheduler forces you to write real concurrent Java, and microservice patterns prepare you for splitting TicketVerse into services in Java W17-W18.

## 🗓️ Sessions

### Monday 18 Jan · 45 min — Microservice patterns: gateway, discovery, resilience, saga, outbox, CQRS
- 📚 **Learn:** API gateway, BFF, service discovery, circuit breaker + retry + timeout, saga (choreography vs orchestration), transactional outbox, CQRS, event sourcing, strangler fig, sidecar/service mesh, database per service. Read the [microservices.io pattern map](https://microservices.io/patterns/index.html) (one paragraph per pattern). Optional: [Multi-step processes (Hello Interview)](https://www.hellointerview.com/learn/system-design/patterns/multi-step-processes).
- 🛠️ **Do:** In `notes/14-microservice-patterns.md` make a table of 8 patterns (problem solved, how, cost, TicketVerse use). Then sketch the TicketVerse booking saga (booking -> payment -> notification) as an orchestration with compensations and an outbox table. Done when: you can explain the dual-write problem the outbox solves and what each compensation undoes.

### Wednesday 20 Jan · 45 min — LLD: in-memory pub-sub (topics, partitions, offsets)
- 📚 **Learn:** Model: a `Topic` has N partitions (append-only lists); key -> partition by hash; producers append; consumer groups track committed offsets per partition; one consumer per partition within a group; one lock per partition keeps appends and reads safe. Read [Pub-sub system problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/pub-sub-system.md). Optional: [Kafka introduction](https://kafka.apache.org/intro).
- 🛠️ **Do:** Code the core: `Broker.createTopic(name, partitions)`, `publish(topic, key, msg)` (same key -> same partition), `poll(group, partition, max)` and `commit(group, partition, offset)`, with each partition guarded by its own lock. Done when: tests prove per-key ordering, independent offsets for two consumer groups, and replay from a committed offset.

### Thursday 21 Jan · 45 min — LLD: job scheduler core (one-off jobs + cancel)
- 📚 **Learn:** Requirements: one-off and fixed-rate jobs, priorities, retries with backoff, cancellation, graceful shutdown. Building blocks: a `DelayQueue` (elements become available when their delay expires), one dispatcher thread that `take()`s due jobs, and a worker pool from an `ExecutorService`; cancellation = a flag checked before running. Read the [DelayQueue docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/DelayQueue.html). Optional: [Managing long-running tasks (Hello Interview)](https://www.hellointerview.com/learn/system-design/patterns/long-running-tasks).
- 🛠️ **Do:** Implement `JobScheduler.schedule(job, delayMillis)` returning a `jobId`, and `cancel(jobId)`, with a dispatcher thread taking from a `DelayQueue` and handing jobs to a 2-thread pool; `shutdown()` stops the dispatcher. Done when: tests (fake jobs + `CountDownLatch`) prove jobs run in due-time order and a cancelled job never runs; fixed-rate jobs and retries stay as extension questions in the stretch.

### Saturday 23 Jan · 45 min — PRACTICE: Pub-sub with consumer groups and DLQ
- 📚 **Learn:** Consumer-group rebalancing (assign partitions round-robin when members join or leave), at-least-once delivery (commit only after processing), poison messages -> dead-letter topic after N attempts. Concept refresh: [What is the publisher-subscriber model? (Gaurav Sen, 11 min)](https://www.youtube.com/watch?v=FMhbR_kQeHw).
- 🛠️ **Do:** Extend Wednesday's broker: `join(group, consumerId)`/`leave(...)` trigger rebalancing; processing failures retry and move to `<topic>.DLQ` after 3 attempts; offsets commit only after success. Done when: tests prove 2 consumers split 4 partitions 2/2, the survivor owns all 4 after one leaves, and a poison message lands in the DLQ without blocking later messages.

## 📦 Deliverable (by Saturday night)
`notes/14-microservice-patterns.md` with the saga sketch, `labs/pubsub` (partitions, offsets, groups, DLQ) and `lld/jobscheduler`, all with passing tests. Sunday mini-design (20 min, full template): a unique-ID generator service in `hld/mini/W13-id-generator.md`.

## ✅ Self-check (Sunday test preview)
- Saga choreography vs orchestration: pros and cons of each?
- What is the dual-write problem, and how does the transactional outbox fix it?
- Explain the circuit breaker states and when it trips.
- CQRS vs event sourcing: are they the same thing? When would you use each?
- In your pub-sub, how is per-key ordering guaranteed, and what breaks it?
- How does your job scheduler avoid busy-waiting?
- Sunday mini-design: design a unique-ID generator service for 50k IDs/s across 3 regions (requirements, API, ID layout, failure modes).

## 🚀 Stretch (optional)
Scheduler extensions: `scheduleAtFixedRate(job, period)` and retries with exponential backoff (a failing job runs exactly 3 times). Broker: retention (drop messages older than T) and log compaction. Read [Slack's job queue redesign (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/slack-job-queue). Extra: [Top 7 distributed system patterns (ByteByteGo)](https://www.youtube.com/watch?v=nH4qjmP2KEE); [SAGA, Strangler, CQRS (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=qGlUKtjqaEQ).
