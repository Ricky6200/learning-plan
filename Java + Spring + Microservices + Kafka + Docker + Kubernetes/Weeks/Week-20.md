# ☕ Java Backend · Week 20 — Kafka fundamentals and delivery semantics: Season 4 boss

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Kafka is the default event backbone in Indian product companies; interviews probe partitions and ordering, consumer groups and rebalancing, acks/ISR and exactly-once, and Saturday's boss checks that you can prove it under time pressure.

## 🗓️ Sessions

### Monday 08 Mar · 60 min — Kafka architecture: brokers, topics, partitions, replication, ISR, KRaft
- 📚 **Learn:** Append-only log, topics and partitions, offsets, segments; brokers, leaders and followers, replication factor, ISR and `min.insync.replicas`; KRaft controllers (ZooKeeper removed in 4.0); retention by time/size. Kafka 4.4 is the newest release (Oct 2026); the linked 4.3 docs cover the same concepts. Read: [Confluent: Kafka 101 partitions](https://developer.confluent.io/courses/apache-kafka/partitions/). Optional: [Kafka 4.3: Introduction](https://kafka.apache.org/43/getting-started/introduction/).
- 🛠️ **Do:** Run Kafka 4.4 in Docker (`apache/kafka:4.4.0` through your mirror, single-node KRaft); create `bookings` with 3 partitions; produce and consume with the CLI scripts (with and without keys); run `--describe` on the topic and on a consumer group; sketch broker/partition/leader/ISR on paper. Done when: you can explain every column of the describe output.

### Tuesday 09 Mar · 60 min — Producers: acks, idempotence, retries, batching, keys and ordering
- 📚 **Learn:** `acks=0/1/all`; idempotent producer (default on) and `max.in.flight.requests.per.connection`; retries and `delivery.timeout.ms`; batching with `linger.ms`/`batch.size`; compression; key -> partition (murmur2) gives per-key ordering; async send callbacks. Read: [Confluent: Kafka producers](https://developer.confluent.io/courses/apache-kafka/producers/). Optional: [Kafka 4.3: Producer configs](https://kafka.apache.org/43/configuration/producer-configs/).
- 🛠️ **Do:** Write a plain-Java producer (kafka-clients 4.x) that sends 10,000 `BookingEvent` JSON strings keyed by showId, logging partition/offset in the callback for a few; compare throughput for `linger.ms=0` vs `20` and `compression.type=none` vs `lz4`. Done when: a results table is committed and all events for one key landed in one partition, in order.

### Wednesday 10 Mar · 60 min — Consumers: groups, offsets, commits, rebalancing, new group protocol
- 📚 **Learn:** Consumer groups and partition assignment; the poll loop and `max.poll.interval.ms`; `auto.offset.reset`; auto vs manual commits (sync/async) and their duplicate/loss trade-offs; rebalancing (eager vs cooperative); Kafka 4.x next-generation protocol KIP-848 (`group.protocol=consumer`). Read: [Confluent: Kafka consumers](https://developer.confluent.io/courses/apache-kafka/consumers/). Optional: [Kafka 4.3: Consumer rebalance protocol](https://kafka.apache.org/43/operations/consumer-rebalance-protocol/).
- 🛠️ **Do:** Write a plain-Java consumer with manual commit after processing; run 3 instances in one group, observe assignments, kill one and time the rebalance; repeat with `group.protocol=consumer`; add a 4th instance and see it idle. Done when: notes record assignments before/after each change and which messages were reprocessed.

### Thursday 11 Mar · 60 min — Delivery semantics, transactions, retention vs compaction, share groups
- 📚 **Learn:** At-most/at-least/exactly-once; transactional producer + `read_committed` (EOS covers Kafka-to-Kafka; database side effects need idempotency or an outbox); delete vs compact cleanup, tombstones; share groups (queues for Kafka) became production-ready in Kafka 4.2. Read: [Confluent: Kafka transactions](https://developer.confluent.io/courses/architecture/transactions/). Optional: [Kafka 4.2 release notes blog](https://kafka.apache.org/blog/2026/02/17/apache-kafka-4.2.0-release-announcement/).
- 🛠️ **Do:** Write a transactional producer that writes `booking-confirmed` and `seat-status` atomically, abort every 3rd transaction, and compare `read_committed` vs `read_uncommitted` consumers. Create a compacted `seat-status` topic with small `segment.ms`, write 5 updates per key plus one tombstone, and observe what remains. Done when: the aborted records are invisible to `read_committed` and compaction keeps the latest value per key.

### Friday 12 Mar · 60 min — Event design, schemas and evolution, consumer lag, partition sizing
- 📚 **Learn:** Event naming and envelopes (eventId, type, version, occurredAt, key); JSON vs Avro/Protobuf; Schema Registry compatibility modes (backward/forward/full); consumer lag monitoring; choosing partition counts (throughput, ordering key, consumer parallelism); retention planning. Kafka Streams is the library for stateful stream processing (joins, windows) when plain consumers are not enough. Read: [Confluent: Schema Registry concepts](https://developer.confluent.io/courses/schema-registry/key-concepts/). Optional: [Engineering Digest: Kafka playlist (Hindi)](https://www.youtube.com/playlist?list=PLA3GkZPtsafbAjKYkhWnD6GdhRtm6JrD1).
- 🛠️ **Do:** Write `docs/events.md` defining 6 TicketVerse events (BookingRequested, SeatsHeld, PaymentSucceeded, PaymentFailed, BookingConfirmed, BookingCancelled) with key, envelope fields and versioning rules; evolve one event backward-compatibly. Slow your consumer and watch lag grow with `kafka-consumer-groups.sh --describe`. Done when: the doc justifies each key and partition count, and lag numbers are recorded.

### Saturday 13 Mar · 60 min — BOSS BATTLE: Kafka + microservices gauntlet, 60 min timed
- 📚 **Learn:** Rules: 60 minutes, docs allowed, no AI-generated code, evidence in `kafka-lab/BOSS_S4.md`. Part A (40 min, Kafka): prove 4 claims with your plain-Java clients: keyed records keep per-partition order; unkeyed records spread; a consumer killed before committing causes duplicates; committing before processing loses messages on a crash. Part B (20 min, microservices): from a clean `docker compose up`, run the smoke script through the gateway, stop payment-service and show the circuit breaker open and recover. Reference: [Kafka 4.3: Design](https://kafka.apache.org/43/design/design/).
- 🛠️ **Do:** For each Kafka claim write a hypothesis, the command or code you ran, an output snippet and a one-line lesson; for Part B paste the actuator circuit-breaker states and the smoke output. Done when: all 5 pieces of evidence are committed within 60 minutes, tagged `boss-s4`, plus a 5-line retro.

## 📦 Deliverable (by Saturday night)
`kafka-lab` module: plain-Java producer/consumer clients, throughput table, rebalance notes (classic vs KIP-848), transactions + compaction demos, event catalog doc; Boss S4 evidence in `kafka-lab/BOSS_S4.md` tagged `boss-s4`.

## ✅ Self-check (Sunday test preview)
- How does Kafka guarantee ordering, and what breaks it?
- Explain acks=all together with min.insync.replicas=2 and replication factor 3.
- What does the idempotent producer prevent?
- Auto vs manual offset commits: where can you lose or duplicate messages?
- What triggers a rebalance, and what does the new KIP-848 protocol improve?
- Is exactly-once possible when a consumer writes to PostgreSQL? How do you get effectively-once?
- Retention vs log compaction: when do you use each? What is a tombstone?

## 🚀 Stretch (optional)
Try a share group with the Kafka 4.x console share consumer and compare it with a classic consumer group on one partition. Extras: write up a 5th experiment (scale consumers 1 -> 3 -> 4 and explain the idle one) in the boss format; skim the [Kafka Streams introduction](https://kafka.apache.org/43/streams/introduction/).
