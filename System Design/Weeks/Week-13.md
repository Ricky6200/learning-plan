# 🏗️ System Design · Week 13 — ATM, meeting rooms, distributed coordination

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** Distributed transactions, idempotency and locks are where senior-sounding HLD answers are made, and ATM/meeting-room problems test state machines and interval logic in machine coding.

## 🗓️ Sessions

### Monday 18 Jan · 45 min — Distributed transactions, idempotency, exactly-once
- 📚 **Learn:** 2PC (prepare/commit; blocks if the coordinator dies), 3PC (why rarely used), saga with compensations; idempotency keys; 'exactly-once' = at-least-once delivery + idempotent processing (dedupe table, outbox/inbox). Watch [2PC vs saga (Hello Interview)](https://www.youtube.com/watch?v=DOFflggE_0Q); read [Making retries safe with idempotent APIs (AWS Builders' Library)](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/); Hindi: [Idempotent POST API (Concept && Coding)](https://www.youtube.com/watch?v=mI73eTlSqeU).
- 🛠️ **Do:** In `notes/15-distributed-tx.md`: sequence diagrams for 2PC (happy path + coordinator crash after prepare) and the TicketVerse booking saga with compensations; then design an idempotency-key table for `POST /payments` (columns, unique key, stored response, TTL). Done when: you can explain why 2PC blocks and how the key prevents a double charge when the client retries.

### Wednesday 20 Jan · 45 min — ATM LLD with the State pattern
- 📚 **Learn:** States: Idle -> CardInserted -> Authenticated -> transaction -> Idle, with card eject on errors; PIN retry limit; cash dispensing as a Chain of Responsibility over Rs 2000/500/100 notes; a `BankService` interface for account checks. Hindi: [ATM LLD (Concept && Coding)](https://www.youtube.com/watch?v=JH7gcXeR3ds); reference: [ATM problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/atm.md).
- 🛠️ **Do:** State diagram + `AtmMachine` with state classes, a `CashDispenser` chain and a fake `BankService`. Done when: tests pass for wrong PIN x3 -> card retained, withdrawing Rs 3,800 -> 1x2000 + 3x500 + 3x100, not enough cash in the ATM -> nothing dispensed and account untouched, and illegal actions in each state throw.

### Thursday 21 Jan · 45 min — Distributed locks, leader election, Raft, gossip
- 📚 **Learn:** Redis lock (`SET NX PX` + unique token, release via Lua), why locks need fencing tokens (GC pauses, expired leases), ZooKeeper/etcd leases; leader election; Raft (terms, elections, log replication, commit index); heartbeats vs gossip membership. Read [How to do distributed locking (Martin Kleppmann)](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html); play with the [Raft visualization](https://thesecretlivesofdata.com/raft/); watch [Raft lecture (Martin Kleppmann)](https://www.youtube.com/watch?v=uXEYuDwm7e4).
- 🛠️ **Do:** In `notes/16-coordination.md`: (1) a timeline showing how a paused client corrupts data with a plain lock and how a fencing token stops it; (2) a Raft cheat-sheet: election steps, what 'committed' means, why a majority; (3) a heartbeat vs gossip table. Done when: you can explain in 3 minutes why Redlock is debated and when a DB row lock is simpler.

### Saturday 23 Jan · 45 min — PRACTICE: Meeting-room scheduler machine coding
- 📚 **Learn:** Interval overlap rule (`start < otherEnd && otherStart < end`), a per-room `TreeMap<start, booking>` with `floorEntry`/`ceilingEntry` for O(log n) conflict checks, a room-selection strategy, per-room locking. Practise: [My Calendar I (LeetCode 729)](https://leetcode.com/problems/my-calendar-i/); watch [Meeting scheduler mock LLD (Concept && Coding)](https://www.youtube.com/watch?v=MRx40JVmmF4).
- 🛠️ **Do:** Implement `MeetingRoomScheduler`: rooms with capacity, `book(start, end, attendees)` picks the smallest free room that fits (Strategy), `cancel(bookingId)`, conflict checks via `TreeMap`. Done when: tests pass for back-to-back meetings (allowed), overlap rejection, capacity filtering, cancel freeing the slot, and 20 threads booking one room produce no overlaps.

## 📦 Deliverable (by Saturday night)
`notes/15-distributed-tx.md`, `notes/16-coordination.md`, `lld/atm` and `lld/meetingrooms` with passing tests.

## ✅ Self-check (Sunday test preview)
- Why does 2PC block when the coordinator fails after prepare?
- How does an idempotency key prevent a double charge? Where is it stored and for how long?
- Is exactly-once delivery possible? What do real systems do instead?
- Why does a distributed lock need a fencing token?
- In Raft, when is a log entry committed, and why does a leader need a majority?
- Heartbeats vs gossip: when would you use each for failure detection?
- How do you detect overlapping bookings in O(log n)?

## 🚀 Stretch (optional)
Extend the scheduler into hotel booking (room types, date ranges, cancellation policy) using the awesome-low-level-design hotel management problem.
