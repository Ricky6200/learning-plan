# 🏗️ System Design · Week 14 — ATM, meeting rooms, distributed locks

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Distributed transactions, idempotency and locks with fencing are where senior-sounding HLD answers are made, and ATM/meeting-room problems test state machines and interval logic in machine coding. Republic Day (Tue 26 Jan) does not touch SD's days.

## 🗓️ Sessions

### Monday 25 Jan · 45 min — Distributed transactions, idempotency, exactly-once
- 📚 **Learn:** 2PC (prepare/commit; blocks if the coordinator dies), 3PC (why rarely used), saga with compensations (W13 Mon); idempotency keys; 'exactly-once' = at-least-once delivery + idempotent processing (dedupe table, outbox/inbox). Watch [2PC vs saga (Hello Interview, 15 min)](https://www.youtube.com/watch?v=DOFflggE_0Q). Optional: [Making retries safe with idempotent APIs (AWS Builders' Library)](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).
- 🛠️ **Do:** In `notes/15-distributed-tx.md`: a 2PC sequence diagram for the happy path and for a coordinator crash after prepare; then design an idempotency-key table for `POST /payments` (columns, unique key, stored response, TTL) with the retry flow. Done when: you can explain why 2PC blocks and how the key prevents a double charge when the client retries.

### Wednesday 27 Jan · 45 min — ATM LLD with the State pattern
- 📚 **Learn:** States: Idle -> CardInserted -> Authenticated -> transaction -> Idle, with card eject on errors; PIN retry limit; cash dispensing as a Chain of Responsibility over Rs 500/200/100 notes (Rs 2000 notes were withdrawn from circulation by the RBI in May 2023); a `BankService` interface for account checks. Read [ATM problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/atm.md). Optional: [ATM LLD (Concept && Coding, Hindi, 45 min)](https://www.youtube.com/watch?v=JH7gcXeR3ds).
- 🛠️ **Do:** Core path in 25 min: `AtmMachine` with state classes, a `CashDispenser` chain (500 -> 200 -> 100) and a fake `BankService`. Done when: tests pass for wrong PIN x3 -> card retained, withdrawing Rs 3,800 -> 7x500 + 1x200 + 1x100, not enough cash in the ATM -> nothing dispensed and the account untouched; deposits and mini-statements are extension questions.

### Thursday 28 Jan · 45 min — Distributed locks, leases and fencing tokens
- 📚 **Learn:** Redis lock (`SET NX PX` + unique token, release via Lua), leases that expire, and why a lock alone is unsafe: a client paused by GC can wake up after its lease expired and still write. Fix: a monotonically increasing fencing token checked by the storage. When a DB row lock or a conditional update is simpler. Read 'Protecting a resource with a lock' and 'Making the lock safe with fencing' in [How to do distributed locking (Martin Kleppmann)](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html). Optional: [Redis deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/redis).
- 🛠️ **Do:** Implement an in-memory `LeaseLockService` (`acquire(resource, leaseMillis)` returns a lease with an increasing fencing token; injected clock) and a `FencedStorage.write(token, data)` that rejects tokens older than the last one seen. Test the story: client A acquires, 'pauses' (advance the clock past the lease), B acquires and writes, A's late write is rejected. Done when: the test passes and `notes/16-locks.md` has the timeline plus one case where a DB row lock is simpler.

### Saturday 30 Jan · 45 min — PRACTICE: Meeting-room scheduler machine coding
- 📚 **Learn:** Interval overlap rule (`start < otherEnd && otherStart < end`); a per-room `TreeMap<start, booking>` with `floorEntry`/`ceilingEntry` gives O(log n) conflict checks (Java W5); a room-selection strategy; one lock per room. Read the `floorEntry`/`ceilingEntry` docs in [TreeMap (Java 25)](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/TreeMap.html). Optional: [Meeting scheduler mock LLD (Concept && Coding, 37 min)](https://www.youtube.com/watch?v=MRx40JVmmF4).
- 🛠️ **Do:** Implement `MeetingRoomScheduler`: rooms with capacity, `book(start, end, attendees)` picks the smallest free room that fits (Strategy), `cancel(bookingId)`, conflict checks via `TreeMap`. Done when: tests pass for back-to-back meetings (allowed), overlap rejection, capacity filtering, cancel freeing the slot, and 20 threads booking one room producing no overlaps.

## 📦 Deliverable (by Saturday night)
`notes/15-distributed-tx.md`, `notes/16-locks.md`, `labs/fencing` (lease lock + fenced storage), `lld/atm` and `lld/meetingrooms` with passing tests. Sunday mini-design (20 min, full template): a game leaderboard in `hld/mini/W14-leaderboard.md`.

## ✅ Self-check (Sunday test preview)
- Why does 2PC block when the coordinator fails after prepare?
- How does an idempotency key prevent a double charge? Where is it stored and for how long?
- Is exactly-once delivery possible? What do real systems do instead?
- Why does a distributed lock need a fencing token? Walk through the GC-pause story.
- When is a database row lock or conditional update better than a distributed lock?
- How do you detect overlapping bookings in O(log n)?
- Sunday mini-design: a leaderboard for 10M players (top 10, my rank, score updates) - requirements, API, storage, scaling.

## 🚀 Stretch (optional)
Add recurring meetings (daily/weekly) to the scheduler and deposits + mini-statements to the ATM. Extra: [Idempotent POST API (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=mI73eTlSqeU). (Raft, leader election and gossip now live in W25 Mon next to Kafka's KRaft.)
