# 🏗️ System Design Track — LLD + HLD (30 weeks)

> **Mission:** go from "I can read Java code" to **designing and coding** clean, thread-safe machine-coding solutions *and* defending distributed-system designs with numbers and trade-offs, at **SDE-2 level for Indian product companies**.

Stance: **learn → implement → explain.** Videos are inputs, not outputs. Every session leaves something in your repo `system-design-lab`: code with tests, a diagram, or a write-up.

**Calendar:** 30 weeks, **Mon 26 Oct 2026 → Sun 23 May 2027** · sessions Mon, Wed, Thu, Sat (45 min) · **boss battles** on the Saturdays of **W4, W9, W15, W20, W25, W30**.

---

## 1. By Week 30 you will…

| # | Outcome (measurable) | Evidence |
|---|---|---|
| 1 | Explain **SOLID + 22 GoF patterns** and code the **16** you will use most, with your own Java examples | `patterns/` package + `notes/03-solid.md`, `notes/06-behavioral.md` |
| 2 | Solve **22 LLD / machine-coding problems** in Java with JUnit tests, including **4 unseen timed mocks** (table in §6) | `lld/*` folders, green `mvn test` |
| 3 | Finish a familiar machine-coding core in **≤ 35 min** and an unseen problem in **≤ 90 min** | Boss W9 ≥ 14/20 and W15 ≥ 10/15; 90-min mocks in W10 and W28 |
| 4 | Build **11 implementation labs** of building blocks (thread-safe LRU+TTL, consistent hashing, rate limiter, Snowflake IDs, pub-sub, fencing tokens, …) | `labs/*` with concurrency tests |
| 5 | Design **21 HLD case studies** with one 7-step framework, each with a 1-page write-up, Excalidraw diagram and an ADR for its key decision | `hld/01…22`, `adr/` |
| 6 | Do back-of-the-envelope estimates (QPS, storage, bandwidth) **aloud in < 2 min** | `notes/13-estimation.md`, mocks |
| 7 | Pass **3 recorded solo HLD boss mocks** (W20 ≥ 16/24, W25 ≥ 17/24, W30 ≥ 18/24) plus **5 more HLD mocks** scored with the same rubric | `boss/` and `mocks/` scorecards |
| 8 | Tell the **TicketVerse architecture story** (trade-offs, 10×/100× plan, failure modes) in 5 minutes | `hld/19-ticketverse/` + recording |

---

## 2. Your weekly slots (fixed)

| Day | Minutes | Typical content |
|---|---|---|
| **Mon** | 45 | HLD concept (networking, caching, databases, consistency…) or case study part 1 (25-min solo sprint) |
| **Wed** | 45 | LLD concept / pattern / machine-coding problem (core path) or case-study deep dives |
| **Thu** | 45 | Continuation: second LLD problem, HLD topic, or a case-study sprint |
| **Sat** | 45 | **PRACTICE** (machine coding, implementation lab, write-up polish, unseen mock) — or **BOSS BATTLE** in W4, W9, W15, W20, W25, W30 |
| Sun | 30 (inside the weekly test) | 5 concept questions + 1 mini design (W13–W17: a 20-min full-template HLD sketch saved in `hld/mini/`) |

Total ≈ **3 h/week** of System Design + 30 min of testing. Day-by-day tasks live in [`Weeks/`](Weeks/) and the overview in [`ROADMAP.md`](ROADMAP.md).
Exam weeks keep Saturday light: **W16** (AZ-104) and **W26** (AI-200). Holidays: Holi (Mon 22 Mar, W22) is a lite day — move that Monday's sprint to Sunday if needed; Diwali (Sun 8 Nov) is a weekly-test day, so a lighter test is fine; Christmas (Fri 25 Dec), New Year (Fri 1 Jan) and Republic Day (Tue 26 Jan) fall on days without SD sessions.

---

## 3. How to run one 45-minute session (built for "I understand code but struggle to write it")

| Minute | Step | What you actually do |
|---|---|---|
| 0–3 | **Recall** | Without notes, write 3 bullets about the previous SD session. (Spaced recall beats re-watching.) |
| 3–17 | **Learn** | The session's **one main resource** (≤ 15 min, or the named section) at 1.25–1.5× speed; the `Optional:` link only if time remains. Write notes as *questions*, not transcripts. |
| 17–42 | **Do** | **≤ 25 minutes** of hands-on. **Code:** write the test first, then type every line yourself — no copy-paste. **HLD:** fill the template from [`HLD_INTERVIEW_FRAMEWORK.md`](HLD_INTERVIEW_FRAMEWORK.md) *before* reading any solution. |
| 42–45 | **Verify & log** | Check the `Done when:` line, `git commit -m "W07-Wed parking lot core"`, tick the checkbox, write one "mistake I made" line. |

**Exceptions:** boss battles and unseen mocks use the whole 45 minutes. The three 90-minute machine-coding mocks run across two sessions: **W10** Wed + Thu (car rental, command-line input), **W28** Mon + Wed (hotel booking) and Thu + Sat (digital wallet, command-line input).

**Stuck rules**

- **10 min stuck** → ask your AI mentor for a *hint* (not code).
- **20 min stuck** → read the reference solution, close it, then re-type from memory in a fresh file.
- **Didn't finish?** Write the leftover as a TODO in the file and do it as the week's stretch — never steal time from the next session.
- **Long videos (40–90 min walkthroughs):** watch only the part named in the session, or *after* your solo attempt.

**Predict → try → verify → explain** is the loop. If you can't explain your design aloud in 2 minutes, you don't own it yet.

---

## 4. Phase map

| Season | Weeks | Focus | Milestone (Boss) |
|---|---|---|---|
| **S1 Foundation Forge** | W1–W4 | URL journey, UML, OOP → SOLID; creational + structural patterns; networking, API conventions, scaling, caching | **W4:** pattern-stacked `PriceService` (Adapter + caching Proxy with TTL + logging Decorator) in 35 min + caching pitch |
| **S2 Concurrency Crucible** | W5–W9 | Behavioral patterns, machine-coding method; Tic-Tac-Toe → Splitwise; databases, indexing, replication, sharding, CAP, message queues; thread-safe LRU + TTL | **W9:** Splitwise core in 35 min + 5 rapid HLD questions (≥ 14/20) |
| **S3 Spring Citadel** | W10–W15 | LLD under time pressure (concurrency for LLD, 90-min car-rental mock, file system); BookMyShow, rate limiters, HLD method + estimation, Snowflake IDs, URL shortener, pub-sub, job scheduler, microservice patterns, distributed transactions, locks + fencing, ATM, meeting rooms, chess, inventory, blobs + CDN | **W15:** random Season 3 machine-coding core in 35 min + verbal Pastebin (≥ 10/15) |
| **S4 Distributed Kingdom** | W16–W20 | Notification, food delivery, KV store; reliability (SLOs, bulkheads, load shedding), security, DNS/edge; case studies: rate limiter, notifications, news feed, typeahead + search, chat, crawler | **W20:** 45-min **unseen** solo HLD mock — FB Live comments, recorded (≥ 16/24); job applications start this week |
| **S5 Cloud Ascension** | W21–W25 | HLD gaps (batch vs stream + OLAP, distributed job scheduler, unseen Yelp mock); YouTube, Dropbox, Uber, Ticketmaster, payments, Dynamo-style KV, Kafka internals + Raft, ad clicks, top-K | **W25:** 45-min HLD mock on a random unseen case (≥ 17/24) |
| **S6 Final Boss: The Offer** | W26–W30 | Metrics monitoring, Google Docs + design follow-ups; mock week + portfolio polish; two 90-min machine-coding mocks; HLD finish (hotel/Airbnb, leaderboard, stock-exchange and flash-sale mocks); TicketVerse interview story | **W30:** final LLD + HLD mock (≥ 7/9 LLD and ≥ 18/24 HLD) |

---

## 5. Week-by-week curriculum

| Week | Starts (Mon) | Theme | Saturday |
|---|---|---|---|
| W1 | 26 Oct 2026 | SD interviews, the web, and UML | PRACTICE: Hotel-booking class diagram + Java skeleton |
| W2 | 2 Nov | SOLID design and API protocols | PRACTICE: Refactor a God class with SOLID |
| W3 | 9 Nov | Creational patterns and scaling basics | PRACTICE: Notification factory kata |
| W4 | 16 Nov | Structural patterns and caching (Boss week) | **BOSS BATTLE:** Pattern-stacked PriceService + caching pitch |
| W5 | 23 Nov | Behavioral patterns and choosing databases | PRACTICE: Strategy + Observer kata (pricing + notifications) |
| W6 | 30 Nov | Machine-coding method, indexing, replication | PRACTICE: Snake & Ladder machine coding |
| W7 | 7 Dec | Parking Lot, Vending Machine, sharding | PRACTICE: Consistent-hash ring with virtual nodes |
| W8 | 14 Dec | Elevator, logger, CAP and consistency | PRACTICE: Elevator machine coding (core simulation) |
| W9 | 21 Dec | Splitwise, thread-safe LRU, queues (Boss week) | **BOSS BATTLE:** Timed Splitwise core + 5 rapid HLD questions |
| W10 | 28 Dec | LLD under time pressure: mock + file system | PRACTICE: In-memory file system (Composite + path parsing) |
| W11 | 4 Jan 2027 | BookMyShow LLD and rate limiting | PRACTICE: Token-bucket rate limiter in Java |
| W12 | 11 Jan | HLD method, estimation, IDs, URL shortener | PRACTICE: URL shortener review + Base62 implementation |
| W13 | 18 Jan | Pub-sub, job scheduler, microservice patterns | PRACTICE: Pub-sub with consumer groups and DLQ |
| W14 | 25 Jan | ATM, meeting rooms, distributed locks | PRACTICE: Meeting-room scheduler machine coding |
| W15 | 1 Feb | Chess, inventory, blobs and CDN (Boss week) | **BOSS BATTLE:** 35-min machine coding + verbal Pastebin HLD |
| W16 | 8 Feb | Notifications, food delivery, reliability | PRACTICE (light, exam week): retrying sender + DLQ |
| W17 | 15 Feb | KV store, security, DNS and edge | PRACTICE: KV store machine coding |
| W18 | 22 Feb | Case studies: rate limiter, notifications | PRACTICE: Notification deep dives + polish both write-ups |
| W19 | 1 Mar | Case studies: news feed, typeahead, search | PRACTICE: Typeahead trie with cached top-K |
| W20 | 8 Mar | Chat, web crawler, unseen HLD mock (Boss week) | **BOSS BATTLE:** 45-min unseen HLD mock - FB Live comments |
| W21 | 15 Mar | HLD gaps: streams, job scheduler, Yelp mock | PRACTICE: Unseen 45-min HLD mock - Design Yelp |
| W22 | 22 Mar | Video streaming and file sync | PRACTICE: Chunked upload + dedupe lab |
| W23 | 29 Mar | Uber and Ticketmaster at scale | PRACTICE: Virtual waiting room + Ticketmaster review |
| W24 | 5 Apr | Payment system and Dynamo-style KV store | PRACTICE: Dynamo-style KV store write-up (timed) |
| W25 | 12 Apr | Kafka internals, ad clicks, top-K (Boss week) | **BOSS BATTLE:** Timed 45-min HLD mock (random unseen case) |
| W26 | 19 Apr | Monitoring, collaborative editing, design follow-ups | PRACTICE (light, exam week): 2 verbal reps |
| W27 | 26 Apr | Mock week: HLD, LLD, revision sheets | PRACTICE: One-page summary sheet + portfolio polish |
| W28 | 3 May | Machine-coding mocks: hotel booking, digital wallet | PRACTICE: Unseen mock B part 2 (minutes 45-90) + review |
| W29 | 10 May | HLD finish: hotels, leaderboards, unseen mocks | PRACTICE: Unseen flash-sale mock (35 min) + SUMMARY refresh |
| W30 | 17 May | TicketVerse story and final mocks (Final Boss) | **BOSS BATTLE:** Final LLD + HLD mock (TicketVerse) |

Timed-practice weeks to know about: **W10** (concurrency for LLD + your first unseen 90-min mock), **W21** (HLD gaps: batch vs stream, job scheduler, unseen Yelp mock), **W28** (two unseen 90-min machine-coding mocks), **W29** (HLD finish + two unseen HLD mocks + `hld/SUMMARY.md` refresh), **W30** (final boss).

---

## 6. LLD problems you will code (22)

| Week | Problem | Key patterns / skills | Folder |
|---|---|---|---|
| W1 | Hotel booking (class diagram + skeleton) | UML, OOP pillars, 2-line enum/interface primer | `lld/hotel` |
| W6 | Tic-Tac-Toe · Snake & Ladder | O(1) win check · Strategy (dice), `ArrayDeque` turn queue | `lld/tictactoe`, `lld/snakeladder` |
| W7 | Parking Lot · Vending Machine | Strategy, Factory, injected `TimeSource` · State | `lld/parkinglot`, `lld/vendingmachine` |
| W8 | Elevator · Logging framework | State + LOOK scheduling · Chain of Responsibility, Singleton (single-threaded; thread safety is the stretch after Java W8) | `lld/elevator`, `lld/logger` |
| W9 | Splitwise (+ simplify debts) | Strategy, two heaps, money in paise | `lld/splitwise` |
| W10 | **Car rental CLI — unseen 90-min mock** · In-memory file system (+ multi-gate Parking Lot concurrency) | Command parser, overlap checks · Composite + path parsing · lock per aggregate, lock ordering | `lld/mock-w10`, `lld/filesystem`, `lld/parkinglot` |
| W11 | **BookMyShow** seat holds (feeds TicketVerse in Java W15) | Locks taken in sorted order, TTL holds, race tests, first ADR | `lld/bookmyshow` |
| W13 | Job scheduler | `DelayQueue`, dispatcher thread, worker pool, cancel | `lld/jobscheduler` |
| W14 | ATM · Meeting-room scheduler | State + Chain (₹500/200/100 notes) · `TreeMap` intervals | `lld/atm`, `lld/meetingrooms` |
| W15 | Chess · Inventory/order management | Polymorphism (King/Rook/Knight core), Command · no-oversell concurrency | `lld/chess`, `lld/inventory` |
| W16 | Notification system · Food delivery | Factory, Template Method, Decorator (retry + DLQ) · State, Observer | `lld/notification`, `lld/fooddelivery` |
| W17 | Thread-safe KV store with TTL | Atomic ops, lazy + active expiry | `lld/kvstore` |
| W27 | Unseen LLD mock, 45 min (e.g., Amazon Locker) | Everything | `lld/mock-w27` |
| W28 | **Hotel booking — unseen 90-min mock (API-style)** · **Digital wallet CLI — unseen 90-min mock** | Date ranges, all-or-nothing booking, race test · two-wallet lock ordering, money conservation | `lld/mock-w28-hotel`, `lld/mock-w28-wallet` |

**Pattern katas (not counted above):** God-class refactor (W2) · notification factory (W3) · pattern-stacked `PriceService` boss (W4) · pricing + notifications (W5).

**Implementation labs (11):** consistent hashing (W7) · thread-safe LRU + TTL (W9) · token-bucket limiter (W11) · Snowflake IDs (W12; Base62 + range allocator live in `hld/01-url-shortener`) · pub-sub with consumer groups + DLQ (W13) · lease lock + fencing tokens (W14) · typeahead trie with cached top-K (W19) · chunk store with dedupe (W22) · virtual waiting room (W23) · vector clocks + quorum store (W24) · count-min sketch + top-K (W25). Stretch lab: Bloom filter (W15).

**LRU progression (one idea, three tracks):** Java W5 Tue builds an access-order `LinkedHashMap` LRU → SD W4 Thu draws LRU/LFU pointer changes only → SD W9 Thu makes it thread-safe with TTL (`LinkedHashMap(accessOrder=true)` wrapper + one `ReentrantLock` + injected clock + 50-thread `CountDownLatch` test) → DSA W10 Sat hand-rolls the HashMap + doubly-linked-list version (LeetCode 146).

## 7. HLD case studies you will design (21 + 1 optional)

Each lives in `hld/NN-name/` with `README.md` (1-page write-up from the template), `diagram.excalidraw`, `diagram.png` and a decision record in `adr/` ([MADR template](https://adr.github.io/madr/)). Folder numbers are IDs, not week order.

| # | Week | Case study | Signature trade-off |
|---|---|---|---|
| 01 | W12 | URL shortener | Key generation (range-allocated counters for 7-char Base62), 301 vs 302, cache hot links |
| 02 | W18 | Distributed rate limiter | Redis + Lua atomicity, fail-open vs fail-closed |
| 03 | W18 | Notification system | Priority queues, retries, provider outage |
| 04 | W19 | News feed | Fan-out on write vs read, celebrities |
| 05 | W19 | Typeahead (+ inverted-index search) | Precomputed top-K trie, rebuild pipeline; when Elasticsearch replaces the trie |
| 06 | W20 | Chat (WhatsApp) | WebSocket routing, ordering, offline delivery |
| 07 | W20 | Web crawler | Frontier + politeness, Bloom-filter dedupe |
| 20 | W21 | Distributed job scheduler | Time-bucketed scans, worker leases, idempotent execution |
| 08 | W22 | YouTube / Netflix | Transcoding pipeline, ABR, CDN cost, view counts |
| 09 | W22 | Google Drive / Dropbox | Chunking, dedupe, sync conflicts |
| 10 | W23 | Uber / Ola | Geo index, matching without double assignment |
| 11 | W23 | Ticketmaster / BookMyShow (TicketVerse) | Seat holds under contention, waiting room |
| 12 | W24 | Payment system | Idempotency, double-entry ledger, reconciliation |
| 13 | W24 | Distributed KV store (Dynamo-style) | Quorums, vector clocks, hinted handoff |
| 14 | W25 | Distributed message queue (Kafka internals + Raft/KRaft) | ISR, acks, ordering vs throughput |
| 15 | W25 → W29 | Ad-click aggregation | Windows, late events, exactly-once; batch reconciliation (deep dives in W29) |
| 16 | W26 | Metrics monitoring & alerting | TSDB storage, cardinality |
| 17 | W26 | Google Docs | OT vs CRDT |
| 21 | W29 | Hotel booking / Airbnb | Room-night inventory, capped overbooking |
| 22 | W29 | Leaderboard | Sorted sets, rank across shards |
| 19 | W30 | **TicketVerse end-to-end** | Your own system at 10× / 100× |
| 18 | W26 stretch / W27 mock | LLM chat / RAG platform (optional) | Token rate limits, streaming, cost |

Plus: **Pastebin** (verbal in the W15 boss → `hld/mini/W15-pastebin.md`), five **Sunday mini-designs** in `hld/mini/` (W13 ID generator, W14 leaderboard, W15 Pastebin, W16 hotel booking, W17 job scheduler), and **unseen HLD mocks**: FB Live comments (W20 boss), Yelp (W21), a random case (W25 boss), two mocks in W27, stock exchange + flash sale (W29). `hld/SUMMARY.md` (built W27, refreshed W29) gives one row per case.

---

## 8. Navigation

| File / folder | Use it for |
|---|---|
| [`ROADMAP.md`](ROADMAP.md) | One-page view of all 30 weeks (generated) |
| [`Weeks/`](Weeks/) | Day-by-day sessions with `learn`, `do`, `Done when`, self-checks |
| [`RESOURCES.md`](RESOURCES.md) | Verified links: free first, Hindi + English, tools with versions |
| [`HLD_INTERVIEW_FRAMEWORK.md`](HLD_INTERVIEW_FRAMEWORK.md) | 45-min HLD framework, estimation cheat sheet, deep-dive menu, write-up template, scoring rubric |
| [`LLD_MACHINE_CODING_FRAMEWORK.md`](LLD_MACHINE_CODING_FRAMEWORK.md) | 90-min machine-coding playbook, pattern table, Java skeleton, concurrency & testing checklists |
| [`../00_Progress_Tracker/AI_MEMORY.md`](../00_Progress_Tracker/AI_MEMORY.md) | How your AI mentor tracks progress, tests and remediation |

### Your repo: `system-design-lab`

```text
system-design-lab/
├─ pom.xml                      # JDK 25, JUnit 6 (Jupiter), AssertJ
├─ .github/workflows/ci.yml     # mvn -B test + README badge (W27)
├─ src/main/java/com/sdlab/
│   ├─ patterns/                # solid, creational, structural, behavioral
│   ├─ lld/                     # one package per machine-coding problem (incl. mock-w10, mock-w27, mock-w28-*)
│   └─ labs/                    # building blocks: lrucache, ratelimiter, idgen, pubsub, fencing, ...
├─ src/test/java/com/sdlab/     # mirrors main; every problem has tests
├─ hld/NN-case-name/            # README.md (write-up) + diagram.excalidraw + diagram.png
├─ hld/mini/                    # Sunday mini-designs (W13-W17)
├─ hld/SUMMARY.md               # one row per case study + LLD problem (W27, W29)
├─ notes/                       # concept notes 01..23 (protocols, caching, databases, ...)
├─ adr/                         # decision records, MADR format (from W11)
├─ boss/                        # boss-battle scorecards + recording links (W04 ... W30)
└─ mocks/                       # mock scorecards (W10, W21, W27, W28, W29)
```

### Cross-track sync (why topics land in these weeks)

SD teaches each distributed-systems idea **before** the Java track builds it, and only uses Java features **after** Java teaches them (Season 1 relies on 2-line primers for interfaces/enums; threads and locks wait for Java W8–W9).

| SD week | Topic | Syncs with |
|---|---|---|
| W1–W3 | UML, SOLID, creational patterns, first JUnit tests | Java W2 Mon (first JUnit tests), W2 Wed (interface preview), W3 (inheritance, interfaces, enums, JUnit basics) |
| W4 → W9 | LRU progression: drawings in W4, thread-safe LRU + TTL in W9 | Java W5 Tue `LinkedHashMap` LRU → Java W9 locks/latches → DSA W10 Sat LeetCode 146 |
| W7–W9 | Injected `TimeSource`; single-threaded Parking Lot, Elevator, Logger | Java W7 Thu `java.time` (switch to `Clock` from W11), Java W8 threads → executors |
| W9 | Message queues (Kafka vs RabbitMQ vs Service Bus) | Java W20 Kafka hands-on, W21 Spring Kafka + outbox/saga; Azure W20 Service Bus + Event Hubs |
| W10 | Concurrency for LLD (lock per aggregate, lock ordering, `ConcurrentHashMap`, `BlockingQueue`) | Java W8–W9 concurrency |
| W11 | BookMyShow seat locking + ADR | **Java W15** TicketVerse transactions, locking, Redis seat holds |
| W13 | Microservice patterns (gateway, saga, outbox, circuit breaker, CQRS) | **Java W17–W18** microservices split, W19 Resilience4j, W21 saga + outbox |
| W14 | Idempotency keys, distributed locks, fencing tokens | Java W15 idempotency keys |
| W16 | Reliability incl. bulkheads and load shedding | Java W19 Resilience4j + OpenTelemetry |
| W17 | Security: where authorization sits, OWASP API Top 10, secrets, WAF | Java W16 Spring Security, JWT, OAuth2 (reuse its login diagram) |
| W18–W20 stretches | Testcontainers Redis; Spring `SseEmitter` | Java W12 Sat Testcontainers; Java W13 Spring Boot |
| W19 | Typeahead trie with cached top-K | DSA W16 Sat Trie (LeetCode 208) |
| W21 → W22/W25/W29 | Batch vs stream processing, windows, OLAP | Feeds video view counts (W22), ad clicks (W25) and the W29 follow-up |
| W23 | Ticketmaster HLD | TicketVerse booking design (Java W15 locking choices) |
| W26 stretch / W27 | LLM chat / RAG platform (mock option); `hld/SUMMARY.md` links your AI design docs | AI track (DocuMind RAG, Spring AI W23–W24, Azure AI W25) |
| W27 | CI badge on `system-design-lab` | Java W14 Sat first `ci.yml` |
| W30 | TicketVerse interview story | Java W28 TicketVerse live on Azure, Java W30 final boss |

---

## 9. Rules, pitfalls & tips

**Rules**

1. **No artifact, no XP.** Every session ends with a commit (code, diagram or write-up).
2. **Solo first, solution second.** Read Hello Interview / awesome-low-level-design solutions only *after* your attempt; then list 3 gaps.
3. **Type it, don't paste it.** Your gap is writing code — reference code is for comparison, not for copying.
4. **Tests are the definition of done** for LLD: happy path, edge cases, invalid input, and a race test whenever state is shared.
5. **Numbers in every HLD.** No design without QPS, storage and one latency budget.
6. **Timebox.** 45 minutes means 45, and hands-on means ≤ 25 minutes. Unfinished work becomes the stretch, not overtime.

**Pitfalls to avoid**

| Pitfall | Fix |
|---|---|
| Binge-watching 1-hour walkthroughs | Watch the named segment only; attempt first |
| Pattern-stuffing (5 patterns in a parking lot) | Use a pattern only where something *varies* or must be *decoupled* — say why aloud |
| `String` states and `if/else` ladders | Enums + State/Strategy |
| "Just add a cache / Kafka" | Say what is cached, TTL, invalidation; why async is needed, delivery guarantee, ordering key |
| Ignoring failure modes | Every HLD write-up has a "what fails and what happens" section |
| Over-scaling | SDE-2 interviews reward a correct, simple design first, then scaling with reasons |

**Tips**

- Keep a **mistakes log** at the bottom of each `DESIGN.md`; reread it before boss battles and mocks.
- Diagram conventions (Excalidraw): clients left → data right; cylinders = stores; solid arrows = sync calls; dashed = async/events; number the main flow.
- Hindi helps? Use Concept && Coding or Coder Army for first exposure, then an English resource for interview vocabulary.
- Hello Interview mixes free and premium content — every Hello Interview link in this plan has a free part, and sessions name the section to read (some pages end with a premium section).
- Docker-based stretches (Redis, NGINX, Postgres `EXPLAIN`) start once Docker arrives (Java W11, ~4 Jan) or run in GitHub Codespaces; images come through the company's Docker mirror in JFrog.
- **Mocks:** (a) *Peer mocks* — swap roles with a colleague/friend: you interview them on a case you know well, they interview you on one you don't; (b) *AI mocks* — ask your AI mentor: *"Run a 45-minute HLD mock for &lt;case&gt; as my interviewer. Answer my clarifying questions, push on 3 deep dives, then score me with the rubric in HLD_INTERVIEW_FRAMEWORK.md."* The same works for LLD with the rubric in `LLD_MACHINE_CODING_FRAMEWORK.md`.

---

## 10. How you're tested on Sundays

The Sunday weekly test (150 min across all tracks) includes **System Design — 30 min**:

| Part | Format |
|---|---|
| 5 concept questions | Drawn from the week's `self_check` list plus 1–2 spaced-repetition questions from earlier weeks |
| 1 mini design | Either an **LLD class diagram** (entities, relationships, key interfaces, one pattern justified) or an **HLD sketch** (requirements, rough estimate, boxes-and-arrows, one deep dive). In **W13–W17** it is a 20-min full-template HLD sketch (ID generator, leaderboard, Pastebin, hotel booking, job scheduler) saved in `hld/mini/` |

Scoring per track is **/100**: **≥ 80 green**, **60–79 amber**, **< 60 red** → weak topics become remediation tasks in next week's plan (e.g., "redo Parking Lot core from a blank file", "re-derive the quorum math").

**Boss battles** (Saturday, 45 min, timed — W4, W9, W15, W20, W25, W30) award +300 XP when cleared; pass marks are listed in the phase map above.
