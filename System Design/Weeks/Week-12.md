# 🏗️ System Design · Week 12 — Pub-sub, job scheduler, microservice patterns

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** Building a mini Kafka and a job scheduler forces you to write real concurrent Java, and microservice patterns prepare you for splitting TicketVerse into services in Java W15.

## 🗓️ Sessions

### Monday 11 Jan · 45 min — Microservice patterns: gateway, discovery, resilience, saga, outbox, CQRS
- 📚 **Learn:** API gateway, BFF, service discovery, circuit breaker + retry + timeout, saga (choreography vs orchestration), transactional outbox, CQRS, event sourcing, strangler fig, sidecar/service mesh, database per service. Read the [microservices.io pattern map](https://microservices.io/patterns/index.html); watch [Top 7 distributed system patterns (ByteByteGo)](https://www.youtube.com/watch?v=nH4qjmP2KEE); Hindi: [SAGA, Strangler, CQRS (Concept && Coding)](https://www.youtube.com/watch?v=qGlUKtjqaEQ).
- 🛠️ **Do:** In `notes/14-microservice-patterns.md` make a table of 10 patterns (problem solved, how, cost, TicketVerse use). Then sketch the TicketVerse booking saga (booking -> payment -> notification) as an orchestration with compensations and an outbox table. Done when: you can explain the dual-write problem the outbox solves and what each compensation undoes.

### Wednesday 13 Jan · 45 min — LLD: in-memory pub-sub (topics, partitions, offsets)
- 📚 **Learn:** Model: a `Topic` has N partitions (append-only lists); key -> partition by hash; producers append; consumer groups track committed offsets per partition; one consumer per partition within a group. References: [Pub-sub system problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/pub-sub-system.md) and [Kafka introduction](https://kafka.apache.org/intro).
- 🛠️ **Do:** Design + core code: `Broker.createTopic(name, partitions)`, `publish(topic, key, msg)` (same key -> same partition), `poll(group, consumerId, max)` and `commit(group, partition, offset)`, guarding each partition with a lock. Done when: tests prove per-key ordering, independent offsets for two consumer groups, and replay from a committed offset.

### Thursday 14 Jan · 45 min — LLD: job scheduler with thread pools
- 📚 **Learn:** Requirements: one-off and fixed-rate jobs, priorities, retries with exponential backoff, cancellation, graceful shutdown. Building blocks: `DelayQueue`/`PriorityBlockingQueue`, a dispatcher thread, a worker pool via `ExecutorService`. Read the [DelayQueue docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/DelayQueue.html) and [Slack's job queue redesign (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/slack-job-queue).
- 🛠️ **Do:** Implement `JobScheduler.schedule(job, delay)`, `scheduleAtFixedRate(job, period)` and `cancel(jobId)` with a dispatcher thread taking from a `DelayQueue` and a 4-thread worker pool; failed jobs retry up to 3 times with exponential backoff. Done when: tests (fake jobs + `CountDownLatch`) prove jobs run in due-time order, a cancelled job never runs, and a failing job runs exactly 3 times.

### Saturday 16 Jan · 45 min — PRACTICE: Pub-sub with consumer groups and DLQ
- 📚 **Learn:** Consumer-group rebalancing (assign partitions round-robin when members join/leave), at-least-once delivery (commit after processing), poison messages -> dead-letter topic after N attempts. Concept refresh: [What is the publisher-subscriber model? (Gaurav Sen)](https://www.youtube.com/watch?v=FMhbR_kQeHw).
- 🛠️ **Do:** Extend Wednesday's broker: `join(group, consumerId)`/`leave(...)` trigger rebalancing; processing failures retry and move to `<topic>.DLQ` after 3 attempts; offsets commit only after success. Done when: tests prove 2 consumers split 4 partitions 2/2, the survivor owns all 4 after one leaves, no message is lost across a rebalance, and a poison message lands in the DLQ.

## 📦 Deliverable (by Saturday night)
`notes/14-microservice-patterns.md` with the saga sketch, `labs/pubsub` (partitions, offsets, groups, DLQ) and `lld/jobscheduler`, all with passing tests.

## ✅ Self-check (Sunday test preview)
- Saga choreography vs orchestration: pros and cons of each?
- What is the dual-write problem, and how does the transactional outbox fix it?
- Explain the circuit breaker states and when it trips.
- CQRS vs event sourcing: are they the same thing? When would you use each?
- In your pub-sub, how is per-key ordering guaranteed, and what breaks it?
- How does a consumer group rebalance, and what can be duplicated during it?
- How does your job scheduler avoid busy-waiting?

## 🚀 Stretch (optional)
Add retention (drop messages older than T) and log compaction (keep the latest value per key) to your broker.
