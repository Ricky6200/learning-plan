# 🏗️ System Design · Week 24 — Payment system and Dynamo-style KV store

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** Payments test correctness under failure (idempotency, ledgers, reconciliation), and a Dynamo-style KV store ties together consistent hashing, replication, quorums and conflict resolution.

## 🗓️ Sessions

### Monday 05 Apr · 45 min — Payment system: idempotency, ledger, PSP integration
- 📚 **Learn:** Flow: checkout -> payment service -> PSP (Razorpay/Stripe) -> webhook; states (CREATED -> AUTHORIZED -> CAPTURED, or FAILED/REFUNDED); idempotency keys; double-entry ledger (immutable entries, debits = credits); reconciliation with PSP settlement reports. Read [Designing robust APIs with idempotency (Stripe)](https://stripe.com/blog/idempotency). Optional: [Accounting for developers (Modern Treasury)](https://www.moderntreasury.com/journal/accounting-for-developers-part-i).
- 🛠️ **Do:** In `hld/12-payments/README.md` do steps 1-5 in a 25-minute sprint, including a ledger table with sample double-entry rows for a Rs 500 ticket purchase (customer -> merchant, platform fee) and its refund. Done when: every transaction's rows sum to zero and the payment state machine is drawn.

### Wednesday 07 Apr · 45 min — Payment deep dives: webhooks, reconciliation, failures
- 📚 **Learn:** Webhook signature verification + dedupe, timeouts with unknown outcome (query the PSP before retrying), reconciliation jobs, an outbox for payment events, PCI scope reduction via tokenization, retry with backoff. Read [Transactional outbox (microservices.io)](https://microservices.io/patterns/data/transactional-outbox.html). Optional: [Compensating Transaction pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction).
- 🛠️ **Do:** Finish the deep dives + diagram and write 3 failure stories with your design's response: (1) the PSP times out after actually charging; (2) the same webhook arrives twice; (3) the settlement report disagrees with the ledger. Done when: the write-up + PNG are committed and each story ends in a consistent state.

### Thursday 08 Apr · 45 min — Vector clocks + quorum store lab
- 📚 **Learn:** Vector clock = map nodeId -> counter; comparing two gives BEFORE, AFTER, EQUAL or CONCURRENT; concurrent versions become siblings that the client (or a merge rule) resolves. Quorum reminder (W8): R + W > N makes read and write sets overlap, but a read sees the latest acknowledged write only with strict quorums (no sloppy quorum) and no concurrent writes. Read [Vector clock (Wikipedia)](https://en.wikipedia.org/wiki/Vector_clock). Optional: [Distributed systems lectures (Martin Kleppmann)](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB).
- 🛠️ **Do:** Implement `VectorClock` (`increment`, `merge`, `compare`) and an in-memory `QuorumStore` with 3 replicas: `put(key, value, context, W)` and `get(key, R)` returning all concurrent siblings. Done when: tests prove two concurrent writes yield 2 siblings, a write that saw both resolves them, and with strict R + W > N and no concurrent writes a read returns the latest acknowledged write.

### Saturday 10 Apr · 45 min — PRACTICE: Dynamo-style KV store write-up (timed)
- 📚 **Learn:** Now that vector clocks and quorums are in your hands: consistent hashing + replication factor N, preference lists, tunable R/W quorums, sloppy quorum + hinted handoff, read repair, Merkle-tree anti-entropy, gossip membership. Read section 4 ('System Architecture') of the [Dynamo paper](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf). Optional: [How key-value stores work (ByteByteGo, 6 min)](https://www.youtube.com/watch?v=Dwt8R0KPu7k).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-7 in `hld/13-kv-store/README.md` (bullets), reusing Thursday's lab for the conflict-resolution deep dive. Done when: you can explain a write with N = 3, W = 2 while one replica is down (hinted handoff) and how the replicas converge later (anti-entropy).

## 📦 Deliverable (by Saturday night)
`hld/12-payments/` and `hld/13-kv-store/` (write-up + PNG + ADR each) and `labs/quorumstore` with passing tests.

## ✅ Self-check (Sunday test preview)
- How do idempotency keys prevent double charges? Where are they stored and for how long?
- What is a double-entry ledger, and why must entries be immutable?
- The PSP call timed out: was the user charged? How do you find out safely?
- Explain sloppy quorum and hinted handoff. Why does a sloppy quorum weaken the R + W > N guarantee?
- How do vector clocks detect concurrent writes?
- What do Merkle trees speed up in anti-entropy?

## 🚀 Stretch (optional)
Add a nightly reconciliation job design that matches ledger rows with a PSP settlement CSV and raises alerts on mismatches. Extra: [Payments with idempotency keys (Arpit Bhayani)](https://www.youtube.com/watch?v=m6DtqSb1BDM); [Design a key-value store (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=VKNIhztQnbY).
