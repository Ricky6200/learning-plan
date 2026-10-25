# 🏗️ System Design · Week 11 — BookMyShow LLD and rate limiting

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** Seat booking under concurrency is the heart of TicketVerse (Java W15 builds it for real on Postgres/Redis), and rate limiters are a top HLD and machine-coding question.

## 🗓️ Sessions

### Monday 04 Jan · 45 min — Rate limiting algorithms and distributed rate limiting
- 📚 **Learn:** Why and where (client, gateway, service); token bucket (allows bursts), leaky bucket (smooth outflow), fixed window (boundary spikes), sliding-window log (exact, memory-heavy), sliding-window counter (approximate); HTTP 429 + `Retry-After`; Redis counters + Lua for atomicity; per-user vs per-IP keys. Watch [Rate limiter system design (ByteByteGo, 8 min)](https://www.youtube.com/watch?v=YXkOdWBwqaA). Optional: [Scaling your API with rate limiters (Stripe)](https://stripe.com/blog/rate-limiters).
- 🛠️ **Do:** In `notes/12-rate-limiting.md` build a 5-algorithm table (burst behaviour, memory per key, accuracy, typical use) and choose an algorithm for: OTP login, public API free/pro tiers, payment webhooks, seat-hold endpoint during a blockbuster release. Hand-trace a token bucket (capacity 10, refill 5/s, bursts at t = 0, 0.5, 1.0 s). Done when: the hand trace is written as expected values you will assert on Saturday.

### Wednesday 06 Jan · 45 min — BookMyShow LLD: entities, seat-hold flow, locking choices
- 📚 **Learn:** Entities: `City`, `Cinema`, `Screen`, `Seat`, `Show`, `ShowSeat` (AVAILABLE/HELD/BOOKED), `Booking`, `Payment`. Flow: search -> select -> hold with TTL -> pay -> confirm or release. Locking options: per-show lock, optimistic version check, DB `SELECT ... FOR UPDATE`, Redis `SET NX PX`. Read [Dealing with contention (Hello Interview)](https://www.hellointerview.com/learn/system-design/patterns/dealing-with-contention). Optional: [BookMyShow LLD (Concept && Coding, Hindi, 36 min)](https://www.youtube.com/watch?v=wCyzvDn3Pp8).
- 🛠️ **Do:** Write `lld/bookmyshow/DESIGN.md`: requirements, class diagram and a sequence diagram for hold -> pay -> confirm/expire. Then start an `adr/` folder: write `adr/0001-seat-hold-locking.md` from the [MADR template](https://adr.github.io/madr/) - your in-memory locking choice, the options you rejected, and what TicketVerse will use in Postgres/Redis (Java W15). Done when: the ADR names the race it prevents and explains how expiry releases seats.

### Thursday 07 Jan · 45 min — BookMyShow core: thread-safe seat holds with TTL
- 📚 **Learn:** `ConcurrentHashMap.compute` vs an explicit `ReentrantLock` per show; all-or-nothing multi-seat holds (lock seats in sorted order to avoid deadlock, as in W10 Mon); lazy expiry with an injected `Clock` (Java W7 Thu); race tests with an `ExecutorService` + `CountDownLatch`. Read the `compute`/`merge` docs in [ConcurrentHashMap (Java 25)](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html). Optional: [BookMyShow (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/bookmyshow).
- 🛠️ **Do:** Implement `SeatHoldService`: `hold(showId, seatIds, userId)` (all-or-nothing, returns `holdId`) and `confirm(holdId)`, with holds expiring after 5 minutes via the `Clock`. Tests: 100 threads race for the same 2 seats -> exactly 1 wins; an expired hold frees its seats; confirm after expiry fails. Done when: the race test passes 20 runs in a row (`@RepeatedTest(20)`); `release(holdId)` goes to the stretch.

### Saturday 09 Jan · 45 min — PRACTICE: Token-bucket rate limiter in Java
- 📚 **Learn:** Lazy refill math (`tokens = min(capacity, tokens + elapsed x rate)`), per-key buckets in a `ConcurrentHashMap`, refill + take done atomically per bucket (`synchronized` or a lock), a fake clock for deterministic tests. Read 'Class Design' and 'Implementation' in [Rate limiter (Hello Interview LLD)](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/rate-limiter). Optional: [rate limiting code (awesome-system-design-resources)](https://github.com/ashishps1/awesome-system-design-resources/tree/main/implementations/java/rate_limiting).
- 🛠️ **Do:** Create `labs/ratelimiter`: interface `RateLimiter.tryAcquire(key)` and `TokenBucketLimiter` (capacity, refill per second, injected clock). Done when: >= 5 tests pass: burst up to capacity, refill after time, per-key isolation, Monday's hand trace, and 50 threads never over-admitting; a `SlidingWindowLogLimiter` goes to the stretch.

## 📦 Deliverable (by Saturday night)
`notes/12-rate-limiting.md`, `lld/bookmyshow` (design + thread-safe seat holds), `adr/0001-seat-hold-locking.md`, and `labs/ratelimiter` with >= 5 green tests.

## ✅ Self-check (Sunday test preview)
- Token bucket vs leaky bucket: how does each treat bursts?
- Why is a fixed-window counter unfair at window boundaries?
- How would you rate-limit across 20 API servers? What does Redis + Lua solve?
- BookMyShow: how do you stop two users from booking the same seat?
- Optimistic vs pessimistic locking for seat booking: when would you use each?
- How are expired seat holds released, and what if the releasing process crashes?

## 🚀 Stretch (optional)
Add `release(holdId)` and a `SlidingWindowLogLimiter` (`ArrayDeque<Long>` per key). Redis version (Docker from Java W11 Mon): pull `redis:8` through the company's Docker mirror in JFrog, start it with `docker run`, and implement the token bucket as a Lua script called via Jedis or Lettuce. Extra: [Movie ticket booking problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/movie-ticket-booking-system.md); [Optimistic vs pessimistic locking (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=D3XhDu--uoI); [Rate limiter LLD (Gaurav Sen)](https://www.youtube.com/watch?v=Eg5uH5sU3zw).
