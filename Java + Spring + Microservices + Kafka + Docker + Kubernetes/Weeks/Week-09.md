# ☕ Java Backend · Week 09 — Concurrency II: locks, atomics, async, virtual threads

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Modern services lean on concurrent collections, CompletableFuture and virtual threads; SDE-2 interviews expect you to pick the right tool and explain CAS and ConcurrentHashMap internals.

## 🗓️ Sessions

### Monday 21 Dec · 60 min — ReentrantLock, tryLock, fairness, Condition, ReadWriteLock, StampedLock
- 📚 **Learn:** Lock vs synchronized: `tryLock` with timeout, interruptible locking, fairness, multiple `Condition`s; always unlock in `finally`; `ReentrantReadWriteLock` (many readers, one writer, no upgrade); `StampedLock` optimistic reads. [Jenkov: Java Lock](https://jenkov.com/tutorials/java-util-concurrent/lock.html), [Baeldung: java.util.concurrent locks](https://www.baeldung.com/java-concurrent-locks), [StampedLock Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/StampedLock.html).
- 🛠️ **Do:** Rewrite the W8 deadlocking transfer with `tryLock(100, MILLISECONDS)` plus retry with random backoff; build a `PriceCache` on `ReentrantReadWriteLock` (10 readers, 1 writer) and compare reads/sec with a synchronized version; add a StampedLock optimistic read. Done when: 1,000 random opposite-direction transfers finish without deadlock and the total money is conserved.

### Tuesday 22 Dec · 60 min — Atomics, CAS, LongAdder and ConcurrentHashMap internals
- 📚 **Learn:** CAS loops and `compareAndSet`; the ABA problem and `AtomicStampedReference`; `LongAdder` striping under contention; ConcurrentHashMap in Java 8+: CAS for empty bins, synchronized on the bin head, atomic `compute/merge`, no null keys/values, weakly consistent iterators. [Jenkov: Compare and swap](https://jenkov.com/tutorials/java-concurrency/compare-and-swap.html), [Baeldung: LongAdder](https://www.baeldung.com/java-longadder-and-longaccumulator), [ConcurrentHashMap Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html).
- 🛠️ **Do:** Implement `CasCounter` with a hand-written `compareAndSet` loop; benchmark AtomicLong vs LongAdder with 8 threads x 1M increments. Count word frequencies over 8 text chunks in parallel: a buggy `get` then `put` version vs `merge(word, 1, Integer::sum)`. Done when: the buggy version shows wrong counts and the fixed one matches a single-threaded count.

### Wednesday 23 Dec · 60 min — Concurrent collections and synchronizers: latch, barrier, semaphore
- 📚 **Learn:** CopyOnWriteArrayList (read-heavy, snapshot iterators); BlockingQueue family (Array, Linked, Priority, Delay, Synchronous); CountDownLatch (one-shot), CyclicBarrier (reusable, barrier action), Semaphore (permits for limiting concurrency), Phaser awareness. [Jenkov: CountDownLatch](https://jenkov.com/tutorials/java-util-concurrent/countdownlatch.html), [Baeldung: CyclicBarrier](https://www.baeldung.com/java-cyclic-barrier), [Defog Tech: Phaser vs Latch vs Barrier (video)](https://www.youtube.com/watch?v=J3QZ5gfCtAg).
- 🛠️ **Do:** (1) App startup waits on `CountDownLatch(3)` for DB, cache and config threads. (2) 4 players meet at a `CyclicBarrier` for 3 rounds. (3) `ConnectionPool` guarded by `Semaphore(3)` serving 10 threads, tracking peak concurrent use. (4) Odd-even printer rebuilt with two Semaphores. Done when: a test asserts the pool's peak usage never exceeds 3.

### Thursday 24 Dec · 60 min — CompletableFuture: compose, combine, allOf, errors, custom executors
- 📚 **Learn:** `supplyAsync` on the common pool vs a custom executor; `thenApply` vs `thenCompose`; `thenCombine`; `allOf/anyOf`; `exceptionally`, `handle`, `whenComplete`; `orTimeout` and `completeOnTimeout`; never block inside async stages. [Baeldung: Guide to CompletableFuture](https://www.baeldung.com/java-completablefuture), [Defog Tech: CompletableFuture (video)](https://www.youtube.com/watch?v=ImtZgX1nmr8), [CompletableFuture Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CompletableFuture.html).
- 🛠️ **Do:** Build `TripPlanner`: fetch flight price, hotel price and weather (simulated 300-800 ms calls) in parallel on a custom executor and combine into a `TripQuote` record; one service fails 30% of the time -> fallback via `exceptionally`; whole call `orTimeout(1, SECONDS)`. Compare with sequential latency. Done when: parallel time is about the slowest call, and failure and timeout paths have tests.

### Friday 25 Dec · 60 min — ForkJoin work stealing, virtual threads deep dive, ThreadLocal pitfalls
- 📚 **Learn:** ForkJoinPool and RecursiveTask, work-stealing deques; virtual threads run on carrier threads, block cheaply, must not be pooled, limit them with a Semaphore; since JDK 24 `synchronized` no longer pins (native calls still can); ThreadLocal leaks in pools; ScopedValue (JDK 25). [Baeldung: Fork/Join](https://www.baeldung.com/java-fork-join), [Oracle: Virtual threads (JDK 25)](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html), [JEP 491: No pinning in synchronized](https://openjdk.org/jeps/491).
- 🛠️ **Do:** Sum a 50M-element array with a `RecursiveTask` (try thresholds 1k and 100k) vs sequential vs parallel stream. Simulate 10,000 blocking calls (sleep 200 ms) on `newVirtualThreadPerTaskExecutor()` vs `newFixedThreadPool(200)`. Show a ThreadLocal value leaking between pooled tasks, then fix it with `remove()`. Done when: a timings table and the leak demo are committed.

### Saturday 26 Dec · 60 min — BOSS BATTLE: Concurrency gauntlet, 60 min timed
- 📚 **Learn:** Rules: 60 minutes, package `w09.boss`, docs allowed, no AI-generated code. Part A (30 min): `BoundedBlockingQueue<T>` using ReentrantLock + `notFull`/`notEmpty` Conditions with `put`, `take`, `offer(timeout)`. Part B (30 min): `ParallelFetcher` for 50 simulated calls using virtual threads + CompletableFuture, per-call timeout, max 10 in flight. [Jenkov: Blocking queues](https://jenkov.com/tutorials/java-concurrency/blocking-queues.html), [Jenkov: Semaphore](https://jenkov.com/tutorials/java-util-concurrent/semaphore.html).
- 🛠️ **Do:** Tests to pass: the queue never exceeds capacity with 4 producers/4 consumers moving 10k items, nothing lost or duplicated; `offer` times out when full; the fetcher finishes 50 x 200 ms calls in under 2 s, never exceeds 10 in flight, and collects failures instead of throwing. Done when: all tests are green 3 runs in a row within 60 min, tagged `boss-s2`, plus a 5-line retro.

## 📦 Deliverable (by Saturday night)
`w09` package: tryLock transfer, RW/Stamped cache, CAS counter, CHM word count, synchronizer demos, TripPlanner, ForkJoin + virtual-thread benchmarks; Boss S2 tagged `boss-s2`.

## ✅ Self-check (Sunday test preview)
- Give four differences between ReentrantLock and synchronized. When is fairness worth its cost?
- How does CAS work, and what is the ABA problem?
- How does ConcurrentHashMap stay thread-safe in Java 8+, and why are null keys forbidden?
- CountDownLatch vs CyclicBarrier vs Semaphore: one real use case each.
- thenApply vs thenCompose vs thenCombine; how do you handle exceptions in a chain?
- What is virtual-thread pinning, and why should you never pool virtual threads?
- Why can ThreadLocal leak memory in a thread pool?

## 🚀 Stretch (optional)
Read [JEP 505: Structured Concurrency](https://openjdk.org/jeps/505) (preview in JDK 25) and rewrite TripPlanner with `StructuredTaskScope` using `--enable-preview`.
