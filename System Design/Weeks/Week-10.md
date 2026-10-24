# 🏗️ System Design · Week 10 — BookMyShow LLD and rate limiting

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** Seat booking under concurrency is the heart of TicketVerse (Java W13 builds it for real on Postgres/Redis), and rate limiters are a top HLD and machine-coding question.

## 🗓️ Sessions

### Monday 28 Dec · 45 min — Rate limiting algorithms and distributed rate limiting
- 📚 **Learn:** Why and where (client, gateway, service); token bucket (allows bursts), leaky bucket (smooth outflow), fixed window (boundary spikes), sliding-window log (exact, memory-heavy), sliding-window counter (approximate); HTTP 429 + `Retry-After`; Redis counters + Lua for atomicity; per-user vs per-IP keys. Watch [Rate limiter system design (ByteByteGo)](https://www.youtube.com/watch?v=YXkOdWBwqaA); read [Scaling your API with rate limiters (Stripe)](https://stripe.com/blog/rate-limiters).
- 🛠️ **Do:** In `notes/12-rate-limiting.md` build a 5-algorithm table (burst behaviour, memory per key, accuracy, typical use) and choose an algorithm for: OTP login, public API free/pro tiers, payment webhooks, seat-hold endpoint during a blockbuster release. Hand-trace a token bucket (capacity 10, refill 5/s, bursts at t = 0, 0.5, 1.0 s). Done when: the hand trace is written as expected values you will assert on Saturday.

### Wednesday 30 Dec · 45 min — BookMyShow LLD: entities, seat-hold flow, locking choices
- 📚 **Learn:** Entities: `City`, `Cinema`, `Screen`, `Seat`, `Show`, `ShowSeat` (AVAILABLE/HELD/BOOKED), `Booking`, `Payment`. Flow: search -> select -> hold with TTL -> pay -> confirm or release. Locking options: per-show lock, optimistic version check, DB `SELECT ... FOR UPDATE`, Redis `SET NX PX`. Hindi: [BookMyShow LLD](https://www.youtube.com/watch?v=wCyzvDn3Pp8) and [Optimistic vs pessimistic locking](https://www.youtube.com/watch?v=D3XhDu--uoI) (Concept && Coding); reference: [Movie ticket booking problem](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/movie-ticket-booking-system.md).
- 🛠️ **Do:** Write `lld/bookmyshow/DESIGN.md`: requirements, class diagram, a sequence diagram for hold -> pay -> confirm/expire, and a 5-line ADR choosing your in-memory locking approach plus what TicketVerse will use in Postgres/Redis (Java W13). Done when: the ADR names the race you prevent and explains how expiry releases seats.

### Thursday 31 Dec · 45 min — BookMyShow core: thread-safe seat holds with TTL
- 📚 **Learn:** `ConcurrentHashMap.compute` vs an explicit `ReentrantLock` per show; all-or-nothing multi-seat holds (lock in a fixed order to avoid deadlock); lazy expiry with an injected `Clock`; testing races with `ExecutorService` + `CountDownLatch`. Read [Concurrency in LLD (Hello Interview)](https://www.hellointerview.com/learn/low-level-design/concurrency/intro) and the [ConcurrentHashMap docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html).
- 🛠️ **Do:** Implement `SeatHoldService`: `hold(showId, seatIds, userId)` (all-or-nothing, returns `holdId`), `confirm(holdId)`, `release(holdId)`, expiry after 5 minutes via `Clock`. Tests: 100 threads race for the same 2 seats -> exactly 1 wins; an expired hold frees its seats; confirm after expiry fails. Done when: the race test passes 20 runs in a row (`@RepeatedTest(20)`).

### Saturday 02 Jan · 45 min — PRACTICE: Token-bucket and sliding-window limiters in Java
- 📚 **Learn:** Lazy refill math (`tokens = min(capacity, tokens + elapsed x rate)`), per-key buckets in a `ConcurrentHashMap`, a fake clock for deterministic tests. Compare afterwards with [rate limiting code (awesome-system-design-resources)](https://github.com/ashishps1/awesome-system-design-resources/tree/main/implementations/java/rate_limiting); LLD angle: [Rate limiter LLD (Gaurav Sen)](https://www.youtube.com/watch?v=Eg5uH5sU3zw).
- 🛠️ **Do:** Create `labs/ratelimiter`: interface `RateLimiter.tryAcquire(key)`, `TokenBucketLimiter` (capacity, refill per second) and `SlidingWindowLogLimiter` (limit per window, `Deque<Long>` per key). Done when: >= 6 tests pass: burst up to capacity, refill after time, window boundary, per-key isolation, Monday's hand trace, and 50 threads never over-admit.

## 📦 Deliverable (by Saturday night)
`notes/12-rate-limiting.md`, `lld/bookmyshow` (design + thread-safe seat holds) and `labs/ratelimiter` with >= 6 green tests.

## ✅ Self-check (Sunday test preview)
- Token bucket vs leaky bucket: how does each treat bursts?
- Why is a fixed-window counter unfair at window boundaries?
- How would you rate-limit across 20 API servers? What does Redis + Lua solve?
- BookMyShow: how do you stop two users from booking the same seat?
- Optimistic vs pessimistic locking for seat booking: when would you use each?
- How are expired seat holds released, and what if the releasing process crashes?

## 🚀 Stretch (optional)
Redis version: token bucket as a Lua script called via Jedis or Lettuce against Docker `redis:8`, tested with Testcontainers.
