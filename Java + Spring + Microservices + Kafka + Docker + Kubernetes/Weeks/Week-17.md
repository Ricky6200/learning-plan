# ☕ Java Backend · Week 17 — Kafka fundamentals: partitions, groups, delivery semantics

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Kafka is the default event backbone in Indian product companies; interviews probe partitions and ordering, consumer groups and rebalancing, acks/ISR and exactly-once.

## 🗓️ Sessions

### Monday 15 Feb · 60 min — Kafka architecture: brokers, topics, partitions, replication, ISR, KRaft
- 📚 **Learn:** Append-only log, topics and partitions, offsets, segments; brokers, leaders and followers, replication factor, ISR and `min.insync.replicas`; KRaft controllers (ZooKeeper removed in 4.0); retention by time/size. [Confluent: Kafka 101 partitions](https://developer.confluent.io/courses/apache-kafka/partitions/), [Kafka 4.3: Introduction](https://kafka.apache.org/43/getting-started/introduction/), [Confluent: Kafka 101 (video playlist)](https://www.youtube.com/playlist?list=PLa7VYi0yPIH0KbnJQcMv5N9iW8HkZHztH).
- 🛠️ **Do:** Run Kafka 4.3 in Docker (`apache/kafka`, single-node KRaft); create `bookings` with 3 partitions; produce and consume with the CLI scripts (with and without keys); run `--describe` on the topic and on a consumer group; sketch broker/partition/leader/ISR on paper. Done when: you can explain every column of the describe output.

### Tuesday 16 Feb · 60 min — Producers: acks, idempotence, retries, batching, keys and ordering
- 📚 **Learn:** `acks=0/1/all`; idempotent producer (default on) and `max.in.flight.requests.per.connection`; retries and `delivery.timeout.ms`; batching with `linger.ms`/`batch.size`; compression; key -> partition (murmur2) gives per-key ordering; async send callbacks. [Confluent: Kafka producers](https://developer.confluent.io/courses/apache-kafka/producers/), [Kafka 4.3: Producer configs](https://kafka.apache.org/43/configuration/producer-configs/), [Confluent: Kafka and Java getting started](https://developer.confluent.io/get-started/java/).
- 🛠️ **Do:** Write a plain-Java producer (kafka-clients 4.x) that sends 10,000 `BookingEvent` JSON strings keyed by showId, logging partition/offset in the callback for a few; compare throughput for `linger.ms=0` vs `20` and `compression.type=none` vs `lz4`. Done when: a results table is committed and all events for one key landed in one partition, in order.

### Wednesday 17 Feb · 60 min — Consumers: groups, offsets, commits, rebalancing, new group protocol
- 📚 **Learn:** Consumer groups and partition assignment; poll loop and `max.poll.interval.ms`; `auto.offset.reset`; auto vs manual commits (sync/async) and their duplicate/loss trade-offs; rebalancing (eager vs cooperative); Kafka 4.x next-generation protocol KIP-848 (`group.protocol=consumer`). [Confluent: Kafka consumers](https://developer.confluent.io/courses/apache-kafka/consumers/), [Kafka 4.3: Consumer rebalance protocol](https://kafka.apache.org/43/operations/consumer-rebalance-protocol/), [Confluent: Consumer group protocol](https://developer.confluent.io/courses/architecture/consumer-group-protocol/).
- 🛠️ **Do:** Write a plain-Java consumer with manual commit after processing; run 3 instances in one group, observe assignments, kill one and time the rebalance; repeat with `group.protocol=consumer`; add a 4th instance and see it idle. Done when: notes record assignments before/after each change and which messages were reprocessed.

### Thursday 18 Feb · 60 min — Delivery semantics, transactions, retention vs compaction, share groups
- 📚 **Learn:** At-most/at-least/exactly-once; transactional producer + `read_committed` (EOS covers Kafka-to-Kafka; database side effects need idempotency or an outbox); delete vs compact cleanup, tombstones; share groups (queues for Kafka) became production-ready in Kafka 4.2. [Confluent: Kafka transactions](https://developer.confluent.io/courses/architecture/transactions/), [Kafka 4.3: Topic configs](https://kafka.apache.org/43/configuration/topic-configs/), [Kafka 4.2 release notes blog](https://kafka.apache.org/blog/2026/02/17/apache-kafka-4.2.0-release-announcement/).
- 🛠️ **Do:** Write a transactional producer that writes `booking-confirmed` and `seat-status` atomically, abort every 3rd transaction, and compare `read_committed` vs `read_uncommitted` consumers. Create a compacted `seat-status` topic with small `segment.ms`, write 5 updates per key plus one tombstone, and observe what remains. Done when: the aborted records are invisible to `read_committed` and compaction keeps the latest value per key.

### Friday 19 Feb · 60 min — Event design, schemas and evolution, consumer lag, partition sizing
- 📚 **Learn:** Event naming and envelopes (eventId, type, version, occurredAt, key); JSON vs Avro/Protobuf; Schema Registry compatibility modes (backward/forward/full); consumer lag monitoring; choosing partition counts (throughput, ordering key, consumer parallelism); retention planning. [Confluent: Schema Registry concepts](https://developer.confluent.io/courses/schema-registry/key-concepts/), [Kafka 4.3: Basic operations](https://kafka.apache.org/43/operations/basic-kafka-operations/), [Engineering Digest: Kafka playlist (Hindi)](https://www.youtube.com/playlist?list=PLA3GkZPtsafbAjKYkhWnD6GdhRtm6JrD1).
- 🛠️ **Do:** Write `docs/events.md` defining 6 TicketVerse events (BookingRequested, SeatsHeld, PaymentSucceeded, PaymentFailed, BookingConfirmed, BookingCancelled) with key, envelope fields and versioning rules; evolve one event backward-compatibly. Slow your consumer and watch lag grow with `kafka-consumer-groups.sh --describe`. Done when: the doc justifies each key and partition count, and lag numbers are recorded.

### Saturday 20 Feb · 60 min — BUILD: Ordering and consumer-group experiments lab
- 📚 **Learn:** Experiment method: hypothesis -> setup -> run -> observe -> conclusion. Focus: per-key ordering, effect of no key, group scaling, duplicates during rebalancing with late commits, idempotence on/off. [Kafka 4.3: Design](https://kafka.apache.org/43/design/design/), [Baeldung: Exactly-once processing in Kafka](https://www.baeldung.com/kafka-exactly-once).
- 🛠️ **Do:** Run 5 experiments with your plain-Java clients: (1) keyed ordering per partition, (2) unkeyed spread, (3) scale consumers 1 -> 3 -> 4, (4) kill a consumer before commit and count duplicates, (5) consumer that commits before processing loses messages on crash. Write `kafka-lab/LAB_REPORT.md` with evidence. Done when: each experiment has a hypothesis, output snippet and a one-line lesson.

## 📦 Deliverable (by Saturday night)
`kafka-lab` module: plain-Java producer/consumer clients, throughput table, rebalance notes (classic vs KIP-848), transactions + compaction demos, event catalog doc, 5-experiment lab report.

## ✅ Self-check (Sunday test preview)
- How does Kafka guarantee ordering, and what breaks it?
- Explain acks=all together with min.insync.replicas=2 and replication factor 3.
- What does the idempotent producer prevent?
- Auto vs manual offset commits: where can you lose or duplicate messages?
- What triggers a rebalance, and what does the new KIP-848 protocol improve?
- Is exactly-once possible when a consumer writes to PostgreSQL? How do you get effectively-once?
- Retention vs log compaction: when do you use each? What is a tombstone?

## 🚀 Stretch (optional)
Try a share group with the Kafka 4.x console share consumer and compare it with a classic consumer group on one partition.
