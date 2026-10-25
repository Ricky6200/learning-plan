# ☕ Java Backend · Week 09 — Concurrency II: locks, async, virtual threads, Season 2 boss

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** Modern services lean on concurrent collections, CompletableFuture and virtual threads; SDE-2 interviews expect you to pick the right tool and explain CAS and ConcurrentHashMap internals.

## 🗓️ Sessions

### Monday 21 Dec · 60 min — ReentrantLock, tryLock, fairness, Condition, ReadWriteLock
- 📚 **Learn:** Lock vs synchronized: `tryLock` with timeout, interruptible locking, fairness, multiple `Condition`s; always unlock in `finally`; `ReentrantReadWriteLock` (many readers, one writer, no upgrade). Read: [Jenkov: Java Lock](https://jenkov.com/tutorials/java-util-concurrent/lock.html). Optional: [Baeldung: java.util.concurrent locks](https://www.baeldung.com/java-concurrent-locks).
- 🛠️ **Do:** Rewrite the W8 deadlocking transfer with `tryLock(100, MILLISECONDS)` plus retry with random backoff; build a `PriceCache` on `ReentrantReadWriteLock` (10 readers, 1 writer) and compare reads/sec with a synchronized version. Done when: 1,000 random opposite-direction transfers finish without deadlock and the total money is conserved.

### Tuesday 22 Dec · 60 min — Atomics, CAS, LongAdder and ConcurrentHashMap internals
- 📚 **Learn:** CAS loops and `compareAndSet`; the ABA problem and `AtomicStampedReference`; `LongAdder` striping under contention; ConcurrentHashMap in Java 8+: CAS for empty bins, synchronized on the bin head, atomic `compute/merge`, no null keys/values, weakly consistent iterators. Read: [Jenkov: Compare and swap](https://jenkov.com/tutorials/java-concurrency/compare-and-swap.html). Optional: [ConcurrentHashMap Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html).
- 🛠️ **Do:** Implement `CasCounter` with a hand-written `compareAndSet` loop; benchmark AtomicLong vs LongAdder with 8 threads x 1M increments. Count word frequencies over 8 text chunks in parallel: a buggy `get` then `put` version vs `merge(word, 1, Integer::sum)`. Done when: the buggy version shows wrong counts and the fixed one matches a single-threaded count.

### Wednesday 23 Dec · 60 min — Concurrent collections and synchronizers: latch, barrier, semaphore
- 📚 **Learn:** CopyOnWriteArrayList (read-heavy, snapshot iterators); the BlockingQueue family (Array, Linked, Priority, Delay, Synchronous); CountDownLatch (one-shot), CyclicBarrier (reusable, barrier action), Semaphore (permits that limit concurrency), Phaser awareness. Read: [Jenkov: CountDownLatch](https://jenkov.com/tutorials/java-util-concurrent/countdownlatch.html). Optional: [Defog Tech: Phaser vs Latch vs Barrier (video)](https://www.youtube.com/watch?v=J3QZ5gfCtAg).
- 🛠️ **Do:** (1) App startup waits on `CountDownLatch(3)` for DB, cache and config threads. (2) 4 players meet at a `CyclicBarrier` for 3 rounds. (3) `ConnectionPool` guarded by `Semaphore(3)` serving 10 threads and tracking peak concurrent use. Done when: a test asserts the pool's peak usage never exceeds 3 and the latch demo prints 'ready' only after all 3 threads finish.

### Thursday 24 Dec · 60 min — CompletableFuture, async HttpClient, and asyncio.gather compared
- 📚 **Learn:** `supplyAsync` on the common pool vs a custom executor; `thenApply` vs `thenCompose`; `thenCombine`; `allOf/anyOf`; `exceptionally`, `handle`; `orTimeout`, `completeOnTimeout`; never block inside async stages. `HttpClient.sendAsync` returns a CompletableFuture. Bridge: like `asyncio.gather` (your AI W2 Thu), `allOf` waits for many calls, but here the work runs on threads, not an event loop. Read: [Baeldung: Guide to CompletableFuture](https://www.baeldung.com/java-completablefuture). Optional: [Python docs: Coroutines and tasks](https://docs.python.org/3/library/asyncio-task.html).
- 🛠️ **Do:** Build `TripPlanner`: fetch flight price, hotel price and weather (simulated 300-800 ms calls) in parallel on a custom executor and combine them into a `TripQuote` record; one service fails 30% of the time -> fallback via `exceptionally`; the whole call has `orTimeout(1, SECONDS)`. Then fetch jsonplaceholder todos 2-5 with `sendAsync` + `allOf` (your W7 client). Write 3 differences from `asyncio.gather` in a comment. Done when: parallel time is about the slowest call and a test covers the timeout path.

### Friday 25 Dec · 60 min — Virtual threads deep dive and ThreadLocal pitfalls
- 📚 **Learn:** Virtual threads (`Thread.ofVirtual()`, `Executors.newVirtualThreadPerTaskExecutor()`) run on a few carrier threads and block cheaply, so they suit I/O-bound work; never pool them, limit concurrency with a Semaphore; since JDK 24 `synchronized` no longer pins the carrier (JEP 491); ThreadLocal values leak across pooled tasks; `ScopedValue` is final in JDK 25. Read: [Oracle: Virtual threads (JDK 25)](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html) (about 15 min). Optional: [JEP 491: No pinning in synchronized](https://openjdk.org/jeps/491).
- 🛠️ **Do:** Simulate 10,000 blocking calls (sleep 200 ms) on `newVirtualThreadPerTaskExecutor()` vs `newFixedThreadPool(200)` and time both; cap in-flight calls at 50 with a Semaphore and time again. Then show a ThreadLocal value leaking between pooled tasks and fix it with `remove()`. Christmas lite day: the first timing alone (about 20 min) is enough. Done when: a timings table and the leak demo are committed.

### Saturday 26 Dec · 60 min — BOSS BATTLE: Concurrency gauntlet, 60 min timed
- 📚 **Learn:** Rules: 60 minutes, package `w09.boss`, docs allowed, no AI-generated code. Part A (30 min): `BoundedBlockingQueue<T>` using ReentrantLock + `notFull`/`notEmpty` Conditions with `put`, `take`, `offer(timeout)`. Part B (30 min): `ParallelFetcher` for 50 simulated calls using virtual threads + CompletableFuture, per-call timeout, max 10 in flight. Reference: [Jenkov: Blocking queues](https://jenkov.com/tutorials/java-concurrency/blocking-queues.html). Optional: [Jenkov: Semaphore](https://jenkov.com/tutorials/java-util-concurrent/semaphore.html).
- 🛠️ **Do:** Tests to pass: the queue never exceeds capacity with 4 producers/4 consumers moving 10k items, nothing lost or duplicated; `offer` times out when full; the fetcher finishes 50 x 200 ms calls in under 2 s, never exceeds 10 in flight, and collects failures instead of throwing. Done when: all tests are green 3 runs in a row within 60 min, tagged `boss-s2`, plus a 5-line retro.

## 📦 Deliverable (by Saturday night)
`w09` package: tryLock transfer, RW price cache, CAS counter, CHM word count, synchronizer demos, TripPlanner + async HttpClient, virtual-thread benchmarks and the ThreadLocal leak fix; Boss S2 tagged `boss-s2`.

## ✅ Self-check (Sunday test preview)
- Give four differences between ReentrantLock and synchronized. When is fairness worth its cost?
- How does CAS work, and what is the ABA problem?
- How does ConcurrentHashMap stay thread-safe in Java 8+, and why are null keys forbidden?
- CountDownLatch vs CyclicBarrier vs Semaphore: one real use case each.
- thenApply vs thenCompose vs thenCombine; how do you handle exceptions in a chain?
- CompletableFuture.allOf vs Python's asyncio.gather: what is the same and what differs?
- What problem do virtual threads solve, why must you never pool them, and when do they not help?
- Why can ThreadLocal leak memory in a thread pool?

## 🚀 Stretch (optional)
Read [JEP 505: Structured Concurrency](https://openjdk.org/jeps/505) (preview in JDK 25) and rewrite TripPlanner with `StructuredTaskScope` using `--enable-preview`. Extras: a StampedLock optimistic read in `PriceCache`; sum a 50M-element array with a ForkJoin `RecursiveTask` (thresholds 1k vs 100k) vs a parallel stream; the odd-even printer rebuilt with two Semaphores.
