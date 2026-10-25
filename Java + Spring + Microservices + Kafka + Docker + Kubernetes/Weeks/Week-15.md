# ☕ Java Backend · Week 15 — Transactions, locking, Redis seat holds: Season 3 boss

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** "How do you prevent double booking?" is the signature question for a ticketing system; it tests transactions, isolation, locking and distributed caching together, and Saturday's boss proves you can do it under time pressure.

## 🗓️ Sessions

### Monday 01 Feb · 60 min — @Transactional: propagation, rollback rules, readOnly, proxy pitfalls
- 📚 **Learn:** Propagation (REQUIRED, REQUIRES_NEW, NESTED, SUPPORTS, MANDATORY, NOT_SUPPORTED, NEVER); rollback only on unchecked exceptions by default (`rollbackFor` for checked); `readOnly` hints; proxy limits (self-invocation, private methods) from W12; transaction-bound events. Read: [Marco Behler: @Transactional in depth](https://www.marcobehler.com/guides/spring-transaction-management-transactional-in-depth). Optional: [Spring: Transaction propagation](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-propagation.html).
- 🛠️ **Do:** Write integration tests showing: an `AuditService.log` with REQUIRES_NEW survives when the outer booking transaction rolls back; a checked exception commits by default and rolls back with `rollbackFor`; self-invocation silently skips REQUIRES_NEW. Done when: 3 tests pass and each has a one-line comment explaining the behaviour.

### Tuesday 02 Feb · 60 min — Isolation levels and anomalies: dirty read to write skew
- 📚 **Learn:** Dirty read, non-repeatable read, phantom, lost update, write skew; PostgreSQL MVCC, default READ COMMITTED, REPEATABLE READ as snapshot isolation, SERIALIZABLE (SSI) with serialization failures that must be retried. Read: [PostgreSQL: Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html). Optional: [Vlad Mihalcea: Write skew](https://vladmihalcea.com/write-skew-2pl-mvcc/).
- 🛠️ **Do:** With two psql sessions (or two JDBC threads with a latch), reproduce a lost update on a seat price at READ COMMITTED and a write-skew case (two admins each disabling one of the last two screens). Prevent both with SERIALIZABLE and add a retry on serialization failure. Done when: each anomaly has a script in `sql/anomalies/` and a written explanation.

### Wednesday 03 Feb · 60 min — Optimistic @Version vs pessimistic FOR UPDATE; deadlocks; HikariCP sizing
- 📚 **Learn:** Optimistic locking with `@Version` (conflict -> retry); pessimistic `@Lock(PESSIMISTIC_WRITE)` = `SELECT ... FOR UPDATE`, `SKIP LOCKED` for queues; consistent lock ordering to avoid DB deadlocks; Spring Framework 7 `@Retryable` does nothing until you declare `@EnableResilientMethods` on a `@Configuration` class; HikariCP pool sizing. Read: [Vlad Mihalcea: Optimistic vs pessimistic locking](https://vladmihalcea.com/optimistic-vs-pessimistic-locking/). Optional: [Spring Framework: Resilience features](https://docs.spring.io/spring-framework/reference/core/resilience.html).
- 🛠️ **Do:** Implement `reserveSeat` twice: optimistic (`@Version` on ShowSeat + retry with `@Retryable`, enabled by `@EnableResilientMethods`) and pessimistic (FOR UPDATE, seats locked in id order). Hit one seat with 50 threads in a test and record successes, conflicts and duration for each. Done when: exactly one booking wins in both versions and you can justify which you would ship.

### Thursday 04 Feb · 60 min — Redis with Spring: cache-aside, TTL, @Cacheable and eviction
- 📚 **Learn:** Cache-aside pattern; Spring Cache abstraction (`@Cacheable`, `@CacheEvict`, `@CachePut`); Redis cache manager with TTL and JSON serialization; what to cache (catalog) vs never cache (seat availability, the source of truth); invalidation strategies; Redis in Docker. Read: [Spring Boot: Caching](https://docs.spring.io/spring-boot/reference/io/caching.html). Optional: [Engineering Digest: Redis with Spring Boot (Hindi video)](https://www.youtube.com/watch?v=2srQ-RiJHps).
- 🛠️ **Do:** Add Redis to `compose.yaml`; cache `GET /api/events/{id}` and venue lists with a 10-minute TTL; evict on update/delete; log cache hits/misses; inspect keys and TTLs with `redis-cli`. Measure p50 latency of 100 calls cold vs warm. Done when: the second call skips the DB (no SQL in logs) and an update makes the next read fresh.

### Friday 05 Feb · 60 min — Seat holds with SET NX PX; distributed-lock caveats
- 📚 **Learn:** Hold = `SET hold:{show}:{seat} {user} NX PX 600000`; release only if you own it (Lua compare-and-delete); multi-seat holds all-or-nothing; why Redis locks are not correctness guarantees (GC pauses, clock drift, failover) and why the DB constraint stays the source of truth; fencing tokens. Read: [Redis: Distributed locks](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks/). Optional: [Kleppmann: How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html).
- 🛠️ **Do:** Implement `SeatHoldService.hold(showId, seatIds, userId)` (all-or-nothing, roll back partial holds), `release` via Lua, and `heldBy`; expose `POST /api/shows/{id}/holds`. Test with Testcontainers Redis: concurrent holds on one seat (only one wins), TTL expiry frees the seat, a non-owner cannot release. Done when: all 3 tests pass.

### Saturday 06 Feb · 60 min — BOSS BATTLE: Hold-and-book under 100 threads, 60 min timed
- 📚 **Learn:** Rules: 60 minutes, branch `boss-s3`, docs allowed, no AI-generated code. Build `POST /api/bookings` (holdId -> booking) in one DB transaction: verify the hold owner in Redis, flip `show_seat` with the optimistic version check, insert booking + booking_seat under the unique constraint, release the hold; a repeated confirm for the same holdId returns the same booking (idempotent). Reference: [Spring: Using @Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html). Optional: [Vlad Mihalcea: Lost update and locking](https://vladmihalcea.com/a-beginners-guide-to-database-locking-and-the-lost-update-phenomena/).
- 🛠️ **Do:** Tests to pass: 100 threads try to book the same 2 seats (exactly 1 success and 99 clean 409 ProblemDetails); 100 threads book random seats (a SQL check finds no seat booked twice); the same confirm sent twice returns one booking. Done when: all 3 tests pass 3 runs in a row within 60 min, the commit is tagged `boss-s3`, and a 5-line retro is in the README.

## 📦 Deliverable (by Saturday night)
TicketVerse with transaction-propagation tests, anomaly scripts, optimistic + pessimistic reservation benchmarks, Redis cache-aside, Redis seat holds, and the Boss S3 hold-and-book flow with a 100-thread no-double-booking suite tagged `boss-s3`.

## ✅ Self-check (Sunday test preview)
- REQUIRED vs REQUIRES_NEW vs NESTED: give a real use case for REQUIRES_NEW.
- Why does a checked exception not roll back a Spring transaction by default?
- Explain lost update and write skew. Which isolation level prevents each in PostgreSQL?
- Optimistic vs pessimistic locking: trade-offs and when to use each for seat booking.
- How does a Redis SET NX PX seat hold work, and why must release check ownership?
- Why is a Redis lock alone not enough to guarantee no double booking?
- How would you size a HikariCP pool for an 8-core database server?

## 🚀 Stretch (optional)
Replace the per-seat Java loop with a single Lua script that holds N seats atomically and benchmark both. Extra: document the hold-and-book flow as a Mermaid sequence diagram in the README.
