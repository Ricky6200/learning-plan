# 🧭 HLD Interview Framework (45 minutes)

One framework for **every** case study in this plan — requirements → estimation → API → data model → high-level design → deep dives → bottlenecks & trade-offs. Practise it until the order is automatic; then your brain is free for the actual design.

> Target level: **SDE-2 (3–4 YOE) at Indian product companies.** You are expected to drive the discussion, reach a working end-to-end design in ~25 minutes, go deep on 2–3 areas with justified choices, use numbers, and name failure modes. You are *not* expected to invent new algorithms.

---

## 1. The 45-minute timeline

| Step | Clock | Output on the board | Ask yourself |
|---|---|---|---|
| **1. Requirements** | 0–5 | 3–5 functional requirements (FR), 4–6 non-functional (NFR) **with numbers**, explicit out-of-scope | "What are the 3 things a user must be able to do?" |
| **2. Estimation** | 5–9 | DAU, avg/peak QPS (read vs write), storage/year, bandwidth, read:write ratio — **and the "so what"** | "Which number changes my design?" |
| **3. API** | 9–13 | 3–6 endpoints or events (method, path, key params, response) | "Does every FR have an API?" |
| **4. Data model** | 13–17 | Core entities, keys (PK / partition / sort), store choice per entity | "What are the access patterns?" |
| **5. High-level design** | 17–27 | Boxes + arrows that satisfy every FR; numbered request flows | "Can I walk each FR through the diagram?" |
| **6. Deep dives** | 27–40 | 2–3 deep dives driven by the NFRs (scale, latency, consistency, failure) | "What would break first at 10×?" |
| **7. Bottlenecks & wrap-up** | 40–45 | SPOFs, failure modes, monitoring, what you'd do with more time | "What did I trade away?" |

**60-minute round?** Multiply each step by ~1.3 and add a 4th deep dive. **Interviewer jumps ahead?** Follow them — the framework is a guide, not a script.

**2-minute opener (say it aloud):** *"Let me start by clarifying requirements and scale, then I'll sketch the APIs and data model, draw a high-level design that works end to end, and spend most of our time on the deep dives that matter for these requirements. I'll call out trade-offs as I go."*

---

## 2. Requirement checklists

**Functional (pick the top 3–5, confirm with the interviewer)**

- [ ] Who are the actors (user, admin, driver, merchant, internal service)?
- [ ] Core write actions (create/post/book/pay/upload) and core read actions (view/search/feed/download)
- [ ] Real-time needs (live updates, notifications, presence)?
- [ ] Search, ranking, recommendations — in or out of scope?
- [ ] Explicit **out of scope** list (auth, billing, analytics, admin UI…)

**Non-functional (always attach a number)**

| NFR | Typical question | Example answer |
|---|---|---|
| Scale | DAU/MAU? Items per day? Peak events? | 50M DAU, 10× spikes at ticket drops |
| Latency | p99 for the hot path? | Redirect < 100 ms p99; feed < 300 ms |
| Availability | Can reads/writes go down? | 99.99% reads, 99.9% writes |
| Consistency | Can users see stale data? Is double-spend possible? | Bookings strongly consistent; likes eventually consistent |
| Durability | Can we ever lose data? | Payments: never; analytics: small loss OK |
| Security / privacy | PII? Payments (PCI)? Abuse? | Rate limits, encryption at rest |
| Geography | One region or global? | India-first, SEA later |
| Cost | Any constraint? | CDN egress dominates — optimise it |

---

## 3. Estimation cheat sheet

### Powers of 2 and units

| Power | Exact | Approx | Unit |
|---|---|---|---|
| 2^10 | 1,024 | 1 thousand | 1 KB |
| 2^20 | 1,048,576 | 1 million | 1 MB |
| 2^30 | 1,073,741,824 | 1 billion | 1 GB |
| 2^40 | ≈ 1.1 × 10^12 | 1 trillion | 1 TB |
| 2^50 | ≈ 1.1 × 10^15 | 1 quadrillion | 1 PB |

Handy sizes: char/byte = 1 B · int = 4 B · long/timestamp = 8 B · UUID = 16 B · short text post ≈ 300 B–1 KB · DB row with metadata ≈ 0.5–1 KB · image ≈ 200 KB–2 MB · 1 min of 720p video ≈ 20–40 MB at 2.5–5 Mbps (state assumptions!).

### Latency numbers (classic orders of magnitude — learn the ratios)

From the well-known [latency numbers list](https://gist.github.com/jboner/2841832) (hardware is faster today; see the [interactive version by year](https://colin-scott.github.io/personal_website/research/interactive_latency.html)).

| Operation | Time |
|---|---|
| L1 cache reference | 0.5 ns |
| Branch mispredict | 5 ns |
| L2 cache reference | 7 ns |
| Mutex lock/unlock | 25 ns |
| Main memory reference | 100 ns |
| Compress 1 KB (fast codec) | 3 µs |
| Send 1 KB over 1 Gbps network | 10 µs |
| Read 4 KB randomly from SSD | 150 µs |
| Read 1 MB sequentially from memory | 250 µs |
| Round trip within the same datacenter | 500 µs |
| Read 1 MB sequentially from SSD | 1 ms |
| Disk seek (HDD) | 10 ms |
| Read 1 MB sequentially from HDD | 20 ms |
| Packet round trip California → Netherlands → California | 150 ms |

Takeaways: memory ≫ SSD ≫ network across regions; **avoid cross-region round trips on the hot path**; batch and cache.

### Time and availability conversions

| Quantity | Value |
|---|---|
| Seconds per day | 86,400 ≈ **10^5** (use 10^5 for mental math) |
| Seconds per month | ≈ 2.6 million |
| Seconds per year | ≈ 31.5 million ≈ 3 × 10^7 |
| 1M requests/day | ≈ 12 req/s |
| 99% availability | ≈ 3.65 days down/year |
| 99.9% | ≈ 8.76 hours/year ≈ 43.8 min/month |
| 99.99% | ≈ 52.6 min/year ≈ 4.4 min/month |
| 99.999% | ≈ 5.3 min/year |

Serial dependencies multiply: 99.9% × 99.9% ≈ 99.8%. Redundant copies: 1 − (1 − a)^n (two 99% replicas → 99.99%).

### Formulas

```text
Average QPS   = DAU × actions per user per day ÷ 86,400
Peak QPS      = average × 2–5   (use 3 by default; ticket drops / sales: 10× or more)
Storage/year  = new items per day × bytes per item × 365 × replication factor (× ~1.3 for indexes/metadata)
Bandwidth     = QPS × payload size   (compute ingress and egress separately)
Cache memory  = hot fraction (~20%) × items read per day × item size   ("80/20 rule")
Servers       = peak QPS ÷ per-server capacity ÷ target utilisation (0.6–0.7)
```

### Planning assumptions (order of magnitude — always say "assuming…")

| Component | Assume roughly | Then |
|---|---|---|
| Stateless app instance (simple CRUD) | 1k–2k req/s | Scale horizontally behind an LB |
| Single SQL primary (Postgres/MySQL) | a few thousand writes/s; reads scale with replicas + cache | Shard or move hot writes to an LSM store beyond ~10k writes/s |
| Redis node | ~100k simple ops/s, memory-bound | Shard with Redis Cluster |
| Kafka partition | a few MB/s per consumer; brokers do hundreds of MB/s | Partitions = target throughput ÷ per-consumer throughput |
| WebSocket gateway | tens of thousands of concurrent connections per server (more with tuning) | Connection registry + pub/sub between gateways |

These are interview heuristics, not benchmarks — the point is to show *how* numbers drive design.

### Worked example — URL shortener

Assumptions: 100M new links/month, read:write = 100:1, ~500 B per record, keep 5 years.

| Quantity | Math | Result |
|---|---|---|
| Writes | 100M ÷ 2.6M s | ≈ 40/s avg, ≈ 120/s peak |
| Reads | 40 × 100 | ≈ 4,000/s avg, ≈ 12,000/s peak |
| Records in 5 years | 100M × 12 × 5 | 6 billion |
| Storage | 6B × 500 B = 3 TB; × 3 replicas | ≈ 9 TB |
| Code length | 62^6 ≈ 57B, 62^7 ≈ 3.5 trillion | 7 Base62 chars = ample headroom |
| Cache | 4,000 × 86,400 ≈ 350M reads/day; 20% × 500 B | ≈ 35 GB → small Redis cluster |
| Egress | 12,000/s × ~500 B | ≈ 6 MB/s (tiny) |

**So what:** read-heavy → cache + replicas; low write rate → one primary is fine; pure key → value access → KV store or an indexed SQL table; 7-character codes.

---

## 4. API template

| Method | Path | Request | Response | Notes |
|---|---|---|---|---|
| POST | `/v1/<resources>` | body JSON | `201` + id | `Idempotency-Key` header for retries |
| GET | `/v1/<resources>/{id}` | — | `200` / `404` | Cacheable? ETag? |
| GET | `/v1/<resources>?cursor=…&limit=20` | — | items + `nextCursor` | Cursor pagination, not offset |
| PUT/PATCH | `/v1/<resources>/{id}` | partial JSON | `200` | Optimistic concurrency via `If-Match`/version |
| DELETE | `/v1/<resources>/{id}` | — | `204` | Idempotent |

Also state: **auth** (JWT from gateway; user id from token, never from body), **rate limits** (429 + `Retry-After`), **real-time channel** (WebSocket/SSE endpoint), **async events** (`BookingConfirmed {bookingId, userId, showId, seats, ts}` with the partition key named).

## 5. Data-model template

| Entity | Key fields | Primary / partition key | Sort key / indexes | Store | Why this store |
|---|---|---|---|---|---|
| `User` | id, name, email | `user_id` | unique(email) | Postgres | Relational, low write rate |
| `<HotEntity>` | … | chosen for even spread | for main query | e.g., Cassandra/DynamoDB | Write-heavy, key-based access |
| `<Blob>` | id, url, size, hash | `blob_id` | — | Object storage + CDN | Large, immutable |

Rules: **start from access patterns**, name the partition key and the query it serves, say where strong consistency is needed, and what is derived (caches, search index, feed) vs source of truth.

## 6. High-level design checklist

- [ ] Clients → (CDN for static/media) → load balancer / API gateway (auth, rate limits)
- [ ] Stateless services split by responsibility (not too many — 3–6 boxes is plenty)
- [ ] Cache in front of hot reads; source-of-truth DB; replicas
- [ ] Queue/stream for async work, fan-out, retries; workers
- [ ] Object storage for blobs; search index fed by CDC/events if needed
- [ ] **Number the flows** (1, 2, 3…) and walk each FR through them
- [ ] Mark sync (solid) vs async (dashed) arrows

## 7. Deep-dive menu ("if the requirement says X, reach for Y")

| Requirement / pain | Reach for | Say the trade-off |
|---|---|---|
| Read-heavy, low latency | Cache-aside + TTL, CDN, read replicas | Staleness window; invalidation; stampede protection |
| Write-heavy | Sharding by a high-cardinality key, LSM stores, batching, async queues | Cross-shard queries; rebalancing |
| Hot keys / celebrities | Key replication, local caches, hybrid fan-out, request coalescing | Memory; complexity |
| Contention (tickets, inventory, drivers) | Row locks / optimistic versioning, Redis TTL holds, per-resource queues, virtual waiting room | Throughput vs fairness; lock expiry |
| Duplicate requests / retries | Idempotency keys, dedupe tables, upserts | Storage for keys; TTL choice |
| Multi-step workflows | Saga (orchestrated) + transactional outbox, or a workflow engine | Eventual consistency; compensations |
| Real-time updates | WebSockets or SSE; pub/sub between gateway servers | Connection state; reconnect logic |
| Large files | Presigned/SAS URLs, multipart + resumable uploads, CDN | Security of URLs; CDN cost |
| Search | Inverted index (Elasticsearch) fed by CDC/events | Index lag; ops cost |
| Geo / proximity | Geohash, quadtree, H3, Redis GEO | Cell size vs hotspots |
| Strong consistency | Single leader + sync replicas, consensus (Raft/etcd), quorums R + W > N | Latency; availability during partitions |
| High availability | Redundancy across zones, health checks, failover, graceful degradation | Cost; split-brain risk |
| Abuse / overload | Rate limiting, load shedding, WAF, backpressure | False positives; fail-open vs fail-closed |
| Counting / analytics | Kafka + stream processing windows, count-min sketch, batch reconciliation | Accuracy vs cost; late events |
| Observability | Metrics (golden signals), logs, traces, SLO-burn alerts | Cardinality; cost |
| Failure handling | Timeouts, retries with backoff + jitter, circuit breakers, DLQs, bulkheads | Retry storms; duplicate effects |

## 8. Trade-off phrases that sound senior

- "I'm choosing **X over Y** because **<requirement>**; the cost is **<downside>**, which is acceptable because **<reason>** — if that changes, I'd switch to Y."
- "This path is **eventually consistent**; users may see a like count a few seconds old, which is fine. Bookings are on the **strongly consistent** path."
- "The first bottleneck at 10× is **<component>**; I'd fix it by **<sharding/caching/queueing>** before anything else."
- "To keep this simple for v1, I'll use **one Postgres primary with replicas**; we only need to shard once writes exceed **~N/s**."
- "If **<component>** fails, users see **<impact>**; we detect it with **<metric/alert>** and recover via **<failover/retry/DLQ>**."

## 9. Common mistakes

| Mistake | Instead |
|---|---|
| Drawing boxes before requirements | Spend the first 5 minutes on FR/NFR + numbers |
| No estimation, or estimation with no "so what" | Every number ends in a design consequence |
| Technology name-dropping ("use Kafka") | Say *why*: decoupling, buffering, ordering key, delivery guarantee |
| Vague caching | What is cached, key, TTL, invalidation, hit ratio |
| Skipping the data model | Partition keys and access patterns win interviews |
| Over-engineering for Google scale | Correct and simple first; scale with reasons |
| Monologue | Check in every ~10 minutes: "Shall I go deeper here or move on?" |
| No failure handling | Timeouts, retries, idempotency, DLQ, failover |
| Running out of time | Watch the clock; hit step 5 by minute ~27 |

## 10. Scoring rubric (used in mocks and boss battles)

Score each line **0–3** (0 = missing, 1 = weak, 2 = solid, 3 = strong). Max 24.

| # | Dimension | 3 looks like |
|---|---|---|
| 1 | Requirements | Clear FR/NFR with numbers, scoped out-of-scope |
| 2 | Estimation | Correct order of magnitude, drives decisions |
| 3 | API | Complete for FRs, idempotency/pagination/auth considered |
| 4 | Data model | Access-pattern-driven keys and store choices |
| 5 | High-level design | Works end to end; flows walked through |
| 6 | Deep dives | 2–3 relevant, quantified, alternatives compared |
| 7 | Trade-offs & failures | SPOFs, failure modes, consistency choices explicit |
| 8 | Communication | Structured, checks in, handles hints and pushback |

Pass marks in this plan: W19 ≥ 16, W23 ≥ 17, W26 ≥ 18.

## 11. Fill-in write-up template (`hld/NN-case/README.md`, one page)

```markdown
# <Case study> — HLD write-up (Week NN)

## 1. Requirements
- Functional: 1) … 2) … 3) …
- Non-functional: scale …, latency p99 …, availability …, consistency …
- Out of scope: …

## 2. Estimation
| Quantity | Math | Result |
|---|---|---|
| Avg / peak QPS (reads, writes) | | |
| Storage (per year, with replicas) | | |
| Bandwidth | | |
**So what:** …

## 3. API
| Method | Path | Request | Response | Notes |
|---|---|---|---|---|

## 4. Data model
| Entity | Key / partition | Store | Why |
|---|---|---|---|

## 5. High-level design
![diagram](diagram.png)
Flows: 1) … 2) … 3) …

## 6. Deep dives
### 6.1 <topic> — options, choice, why
### 6.2 <topic>
### 6.3 <topic>

## 7. Bottlenecks, failures, trade-offs
- First bottleneck at 10×: …
- Failure modes (component → impact → detection → mitigation): …
- Trade-offs I made: …

## 8. Compared with reference (after solo attempt)
- Gaps: 1) … 2) … 3) …
- What I did better: …
```

## 12. How case studies are split across 45-minute sessions

| Session | What you do |
|---|---|
| Part 1 (e.g., Mon) | Steps 1–5 solo with a timer (25–30 min) → compare with the reference (15 min) → note gaps |
| Part 2 (e.g., Wed) | Steps 6–7 deep dives + Excalidraw diagram → one-page write-up |
| Single-session cases (Thu) | Full framework in 40 min, 5 min to note weakest sections |
| Sat polish | Clean diagram, add "what changes at 10×", record a 3–5 min verbal summary |

Want a mock? Ask your AI mentor: *"Be my HLD interviewer for <case>. 45 minutes. Make me drive; give hints only if I'm stuck for 2 minutes; ask 3 follow-ups; then score me with the rubric in HLD_INTERVIEW_FRAMEWORK.md."*

Useful references: [Hello Interview delivery framework](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery) · [ByteByteGo: system design interview step by step](https://www.youtube.com/watch?v=i7twT3x5yv8) · [Back-of-the-envelope estimation (ByteByteGo)](https://www.youtube.com/watch?v=UC5xf8FbdJc) · [napkin-math](https://github.com/sirupsen/napkin-math).
