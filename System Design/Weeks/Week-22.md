# 🏗️ System Design · Week 22 — Payment system and Dynamo-style KV store

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Payments test correctness under failure (idempotency, ledgers, reconciliation), and a Dynamo-style KV store ties together consistent hashing, replication, quorums and conflict resolution.

## 🗓️ Sessions

### Monday 22 Mar · 45 min — Payment system: idempotency, ledger, PSP integration
- 📚 **Learn:** Flow: checkout -> payment service -> PSP (Razorpay/Stripe) -> webhook; states (CREATED -> AUTHORIZED -> CAPTURED, or FAILED/REFUNDED); idempotency keys; double-entry ledger (immutable entries, debits = credits); reconciliation with PSP settlement reports. Read [Designing robust APIs with idempotency (Stripe)](https://stripe.com/blog/idempotency) and [Accounting for developers (Modern Treasury)](https://www.moderntreasury.com/journal/accounting-for-developers-part-i); watch [Payments with idempotency keys (Arpit Bhayani)](https://www.youtube.com/watch?v=m6DtqSb1BDM).
- 🛠️ **Do:** In `hld/12-payments/README.md` do steps 1-5, including a ledger table with sample double-entry rows for a Rs 500 ticket purchase (customer -> merchant, platform fee) and its refund. Done when: every transaction's rows sum to zero and the payment state machine is drawn.

### Wednesday 24 Mar · 45 min — Payment deep dives: webhooks, reconciliation, failures
- 📚 **Learn:** Webhook signature verification + dedupe, timeouts with unknown outcome (query the PSP before retrying), reconciliation jobs, outbox for payment events, PCI scope reduction via tokenization, retry with backoff. Read [Transactional outbox (microservices.io)](https://microservices.io/patterns/data/transactional-outbox.html) and [Compensating Transaction pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction).
- 🛠️ **Do:** Finish the deep dives + diagram and write 3 failure stories with your design's response: (1) PSP times out after actually charging; (2) the same webhook arrives twice; (3) the settlement report disagrees with the ledger. Done when: the write-up + PNG are committed and each story ends in a consistent state.

### Thursday 25 Mar · 45 min — Distributed KV store (Dynamo-style)
- 📚 **Learn:** Consistent hashing + replication factor N, preference lists, tunable R/W quorums, sloppy quorum + hinted handoff, vector clocks for conflicts, read repair, Merkle-tree anti-entropy, gossip membership. Read section 4 of the [Dynamo paper](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf); watch [How key-value stores work (ByteByteGo)](https://www.youtube.com/watch?v=Dwt8R0KPu7k); Hindi: [Design a key-value store (Concept && Coding)](https://www.youtube.com/watch?v=VKNIhztQnbY).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/13-kv-store/README.md`. Done when: you can explain a write with N = 3, W = 2 while one replica is down (hinted handoff) and how the replicas converge later (anti-entropy).

### Saturday 27 Mar · 45 min — PRACTICE: Vector clocks + quorum store lab
- 📚 **Learn:** Vector clock = map nodeId -> counter; compare gives BEFORE, AFTER, EQUAL or CONCURRENT; concurrent versions become siblings that the client (or a merge rule) resolves. Visual intuition: [Distributed systems lecture series (Martin Kleppmann)](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB).
- 🛠️ **Do:** Implement `VectorClock` (`increment`, `merge`, `compare`) and an in-memory `QuorumStore` with 3 replicas: `put(key, value, context, W)` and `get(key, R)` returning all concurrent siblings. Done when: tests prove two concurrent writes yield 2 siblings, a write that saw both resolves them, and with R + W > N a read always sees the latest write.

## 📦 Deliverable (by Saturday night)
`hld/12-payments/` and `hld/13-kv-store/` (write-up + PNG each) and `labs/quorumstore` with passing tests.

## ✅ Self-check (Sunday test preview)
- How do idempotency keys prevent double charges? Where are they stored and for how long?
- What is a double-entry ledger, and why must entries be immutable?
- The PSP call timed out: was the user charged? How do you find out safely?
- Explain sloppy quorum and hinted handoff.
- How do vector clocks detect concurrent writes?
- What do Merkle trees speed up in anti-entropy?

## 🚀 Stretch (optional)
Add a nightly reconciliation job design that matches ledger rows with a PSP settlement CSV and raises alerts on mismatches.
