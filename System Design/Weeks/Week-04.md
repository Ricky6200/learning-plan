# 🏗️ System Design · Week 04 — Structural patterns and caching (Boss week)

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Caching is the first scaling lever in HLD answers and an LRU cache is a classic machine-coding question; Decorator, Proxy and Adapter are everywhere in Spring and Java I/O.

## 🗓️ Sessions

### Monday 16 Nov · 45 min — Caching deep dive: strategies, eviction, invalidation, stampede
- 📚 **Learn:** Cache layers (browser, CDN, gateway, in-process, Redis, DB buffer pool); cache-aside, read-through, write-through, write-back, write-around; LRU/LFU eviction; TTL; invalidation; stampede (locks, request coalescing, jittered TTL); hot keys. Watch [Cache systems](https://www.youtube.com/watch?v=dGAgxozNWFE) and [Caching pitfalls](https://www.youtube.com/watch?v=wh98s0XhMmQ) (ByteByteGo); read [Caching (Hello Interview)](https://www.hellointerview.com/learn/system-design/core-concepts/caching).
- 🛠️ **Do:** Write `notes/04-caching.md`: a table (strategy -> read path -> write path -> consistency -> failure mode) and decisions for 3 scenarios: movie catalog, seat availability during a big sale, user profile. For each give strategy, TTL, invalidation trigger and stampede protection. Done when: each decision fits in 2 lines and names what can go stale and for how long.

### Wednesday 18 Nov · 45 min — Structural patterns I: Adapter, Decorator, Proxy, Facade
- 📚 **Learn:** Adapter (wrap an incompatible API), Decorator (add behaviour by wrapping: `BufferedInputStream`), Proxy (control access: caching, lazy loading, security; Spring AOP proxies), Facade (simple front door to a subsystem). Read [Decorator](https://refactoring.guru/design-patterns/decorator) and [Proxy](https://refactoring.guru/design-patterns/proxy) (refactoring.guru); Hindi: [All structural patterns (Concept && Coding)](https://www.youtube.com/watch?v=WxGtmIBZszk).
- 🛠️ **Do:** In `patterns.structural`: (1) `LegacyPayAdapter` fitting `LegacyPaySdk.makePayment(String, double)` into your `PaymentProcessor`; (2) `CachingPriceProxy` around a slow `PriceService` that counts calls; (3) `DataSource` decorators `CompressionDecorator` + `EncryptionDecorator` (fake transforms); (4) `CheckoutFacade`. Done when: tests prove the proxy calls the real service once per key and the decorators work in either order.

### Thursday 19 Nov · 45 min — Composite, Bridge, Flyweight + LRU cache warm-up
- 📚 **Learn:** Composite (uniform tree: files/folders), Bridge (split two dimensions: shape x renderer), Flyweight (share intrinsic state: `Integer.valueOf` cache). LRU in O(1): `HashMap` + doubly linked list. Read [Composite (refactoring.guru)](https://refactoring.guru/design-patterns/composite); Hindi: [File system with Composite (Concept && Coding)](https://www.youtube.com/watch?v=FLkCkUY7Wu0); problem: [LRU Cache (LeetCode 146)](https://leetcode.com/problems/lru-cache/).
- 🛠️ **Do:** 15 min: Composite `FileNode`/`DirectoryNode.size()` with a test. 30 min: write JUnit tests FIRST for `LruCache<K,V>` (evicts least-recent at capacity, `get` refreshes recency, `put` updates value, capacity-1 edge case), then implement it with `HashMap` + your own doubly linked list (no `LinkedHashMap`). Done when: tests pass and you can draw the pointer changes of `get` on paper.

### Saturday 21 Nov · 45 min — BOSS BATTLE: Thread-safe LRU cache with TTL + caching pitch
- 📚 **Learn:** Boss rules: blank package, 40-min coding timer, then a 5-min spoken pitch. Just-in-time concurrency: one `ReentrantLock` guards every operation (map + list updates are compound, so `ConcurrentHashMap` alone is not enough); inject `java.time.Clock` for testable expiry. Docs: [ReentrantLock](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReentrantLock.html), [Clock](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/time/Clock.html).
- 🛠️ **Do:** 0-5 min: interface `Cache<K,V>` (`get`, `put(k, v, ttl)`, `size`). 5-35: implement `LruTtlCache` (HashMap + DLL, per-entry expiry, lazy expiry on `get`). 35-40: run Thursday's tests + TTL tests with a fake clock + a 50-thread test (`ExecutorService`, `CountDownLatch`). 40-45: record a pitch on cache-aside vs write-through, stampede, hot keys. Done when: all tests pass inside 40 minutes and the recording exists; otherwise log what blocked you.

## 📦 Deliverable (by Saturday night)
`notes/04-caching.md`, structural pattern code + tests, and the Boss `LruTtlCache` with green tests + 5-min recording, self-scored in `boss/W04.md` (correctness, thread safety, clarity, explanation).

## ✅ Self-check (Sunday test preview)
- Cache-aside vs write-through vs write-back: what are the consistency and failure trade-offs?
- What is a cache stampede? Give three ways to prevent it.
- How do you handle a hot key in a distributed cache?
- Why is `ConcurrentHashMap` alone not enough to make an LRU cache thread-safe?
- Decorator vs Proxy: same structure, different intent. Explain.
- LRU vs LFU: when does LFU win?
- How do you invalidate cached data when the underlying DB row changes?

## 🚀 Stretch (optional)
Add a background sweeper (`ScheduledExecutorService`) that evicts expired entries, and compare throughput with 8 vs 64 threads.
