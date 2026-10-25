# 🏗️ System Design · Week 17 — KV store, security, DNS and edge

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** A thread-safe KV store with TTL is a favourite concurrency machine-coding problem, and authorization placement plus edge design (DNS, CDN, WAF) come up in every senior-leaning HLD discussion.

## 🗓️ Sessions

### Monday 15 Feb · 45 min — Security in system design: authZ placement, OWASP, secrets, WAF
- 📚 **Learn:** You built login with Spring Security, JWT and OAuth2 in Java W16 - now the system view: where authorization sits across services (gateway checks the token, each service checks roles/ownership, the DB enforces row ownership), service-to-service identity, OWASP API Top 10 risks, encryption in transit and at rest, secrets in a vault, WAF and DDoS protection at the edge. Read [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/). Optional: [Session vs JWT (ByteByteGo, 7 min)](https://www.youtube.com/watch?v=fyTxwIa-1U0).
- 🛠️ **Do:** In `notes/19-security.md`: reuse your Java W16 login diagram, then add an authorization-placement table (gateway, service, database: what each checks), 5 OWASP API risks with your TicketVerse mitigation, and one line each on secrets, encryption and WAF. Done when: you can explain how to limit damage from a stolen JWT (short TTL, refresh-token rotation, denylist) and where BOLA (broken object-level authorization) is prevented.

### Wednesday 17 Feb · 45 min — LLD: thread-safe in-memory KV store with TTL (design)
- 📚 **Learn:** API: `put(k, v, ttl)`, `get`, `delete`, `incrBy`; storage in a `ConcurrentHashMap`; expiry = lazy check on read + periodic sampling sweep (as Redis does); locking options (per-key atomic ops vs `ReentrantReadWriteLock` vs lock striping); optional LRU eviction at a size limit. Read [How Redis expires keys (EXPIRE docs)](https://redis.io/docs/latest/commands/expire/). Optional: [ReentrantReadWriteLock docs](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/locks/ReentrantReadWriteLock.html).
- 🛠️ **Do:** Write `lld/kvstore/DESIGN.md`: requirements, class diagram (`KvStore`, `Entry`, `ExpiryPolicy`, `EvictionPolicy`, `Clock`), a concurrency plan (which lock or atomic op guards what) and a list of >= 8 tests for Saturday. Then code `Entry` + `put`/`get` with lazy expiry. Done when: the design is committed and the first 3 tests pass.

### Thursday 18 Feb · 45 min — DNS, GeoDNS, anycast, CDN edge, DDoS and WAF
- 📚 **Learn:** Resolution chain (recursive resolver -> root -> TLD -> authoritative), record types (A, AAAA, CNAME, NS, TXT), TTL trade-offs; GeoDNS/latency routing; anycast (one IP served from many PoPs); L3/L4 vs L7 DDoS; WAF rules; edge rate limiting. Watch [Everything you need to know about DNS (ByteByteGo, 6 min)](https://www.youtube.com/watch?v=27r4Bzuj5NQ). Optional: [What is anycast? (Cloudflare)](https://www.cloudflare.com/learning/cdn/glossary/anycast-network/).
- 🛠️ **Do:** Run `Resolve-DnsName` (or `nslookup`) for 3 public domains and record A/CNAME/NS answers and TTLs. Then design the global entry for TicketVerse users in India + Singapore: DNS or anycast, CDN, WAF, regional gateways; describe what happens when the Mumbai region fails. Done when: diagram + failover narrative are in `notes/20-edge.md`.

### Saturday 20 Feb · 45 min — PRACTICE: KV store machine coding
- 📚 **Learn:** Finish the store you designed on Wednesday. Useful APIs: `ConcurrentHashMap.compute/merge` for atomic updates, a `ScheduledExecutorService` for the sweeper, an injected `Clock` for deterministic expiry tests. Docs: [ConcurrentHashMap (Java 25)](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html).
- 🛠️ **Do:** Implement `delete`, atomic `incrBy`, TTL refresh on `put` and an active-expiry sweeper (sample 20 keys every 100 ms). Done when: >= 6 tests pass, including 32 threads x 1,000 `incrBy(1)` = 32,000, expired keys invisible to `get`, the sweeper removing expired keys, and `delete` racing `put` without exceptions; max-size LRU eviction goes to the stretch.

## 📦 Deliverable (by Saturday night)
`notes/19-security.md`, `notes/20-edge.md`, and `lld/kvstore` (design + >= 6 green tests including the concurrency test). Sunday mini-design (20 min, full template): a distributed job scheduler in `hld/mini/W17-job-scheduler.md`.

## ✅ Self-check (Sunday test preview)
- Sessions vs JWT: how do you revoke access in each?
- AuthN vs authZ: where does each happen in a microservices system, and what does the database enforce?
- Pick two OWASP API Top 10 risks and explain how TicketVerse prevents them.
- How does anycast help against DDoS and reduce latency?
- What is the trade-off of a low DNS TTL?
- How does Redis expire keys, and why both lazy and active expiry?
- Sunday mini-design: a distributed job scheduler (one-off + cron jobs, at-least-once) - requirements, API, data model, how workers claim jobs.

## 🚀 Stretch (optional)
Add max-size LRU eviction and an append-only log to the KV store so it survives restarts (replay on startup); measure throughput with and without fsync. Extra: [OAuth 2 explained (ByteByteGo)](https://www.youtube.com/watch?v=ZV5yTm4pT8g); [Traffic Manager routing methods (Azure)](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-routing-methods); [LLD of a cache, mock interview (Gaurav Sen)](https://www.youtube.com/watch?v=tzbX4ix2RjI).
