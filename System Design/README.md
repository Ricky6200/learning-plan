# 🏗️ System Design Track — LLD + HLD (26 weeks)

> **Mission:** go from "I can read Java code" to **designing and coding** clean, thread-safe machine-coding solutions *and* defending distributed-system designs with numbers and trade-offs, at **SDE-2 level for Indian product companies**.

Stance: **learn → implement → explain.** Videos are inputs, not outputs. Every session leaves something in your repo `system-design-lab`: code with tests, a diagram, or a write-up.

---

## 1. By Week 26 you will…

| # | Outcome (measurable) | Evidence |
|---|---|---|
| 1 | Explain and apply **SOLID + 20 GoF patterns** with your own Java examples | `patterns/` package + `notes/06-behavioral.md` |
| 2 | Solve **19 LLD / machine-coding problems** in Java with JUnit tests (table below) | `lld/*` folders, green `mvn test` |
| 3 | Finish a familiar machine-coding core in **≤ 35 min** and an unseen problem in **≤ 90 min** | Boss W14 score ≥ 10/15, LLD mock in W25 |
| 4 | Build **13 implementation labs** of building blocks (LRU+TTL, consistent hashing, rate limiters, Snowflake, Bloom filter, pub-sub, KV store, …) | `labs/*` with concurrency tests |
| 5 | Design **19 HLD case studies** using one 7-step framework, each with a 1-page write-up + Excalidraw diagram | `hld/01…19` |
| 6 | Do back-of-the-envelope estimates (QPS, storage, bandwidth) **aloud in < 2 min** | `notes/13-estimation.md`, mocks |
| 7 | Pass **3 recorded solo HLD mocks** (W19 ≥ 16/24, W23 ≥ 17/24, W26 ≥ 18/24) and the final LLD + HLD boss | `boss/` scorecards |
| 8 | Tell the **TicketVerse architecture story** (trade-offs, 10×/100× plan, failure modes) in 5 minutes | `hld/19-ticketverse/` + recording |

---

## 2. Your weekly slots (fixed)

| Day | Minutes | Typical content |
|---|---|---|
| **Mon** | 45 | HLD concept (networking, caching, databases, consistency…) or case study part 1 |
| **Wed** | 45 | LLD concept / pattern / machine-coding problem (design + core code) |
| **Thu** | 45 | Continuation: second LLD problem, HLD topic, or case study part 2 |
| **Sat** | 45 | **PRACTICE** (machine coding, implementation lab, write-up polish) — or **BOSS BATTLE** in W4, W9, W14, W19, W23, W26 |
| Sun | 30 (inside the weekly test) | 5 concept questions + 1 mini design |

Total ≈ **3 h/week** of System Design + 30 min of testing. Day-by-day tasks live in [`Weeks/`](Weeks/) and the overview in [`ROADMAP_26_WEEKS.md`](ROADMAP_26_WEEKS.md).

---

## 3. How to run one 45-minute session (built for "I understand code but struggle to write it")

| Minute | Step | What you actually do |
|---|---|---|
| 0–3 | **Recall** | Without notes, write 3 bullets about the previous SD session. (Spaced recall beats re-watching.) |
| 3–15 | **Learn** | One resource from the session's `learn` field at 1.25–1.5× speed. Write notes as *questions*, not transcripts. |
| 15–40 | **Do** | Produce the artifact. **Code:** write the test first, then type every line yourself — no copy-paste. **HLD:** fill the template from [`HLD_INTERVIEW_FRAMEWORK.md`](HLD_INTERVIEW_FRAMEWORK.md) *before* reading any solution. |
| 40–45 | **Verify & log** | Check the `Done when:` line, `git commit -m "W07-Wed parking lot core"`, tick the checkbox, write one "mistake I made" line. |

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
| **S1 Foundation Forge** | W1–W4 | URL journey, UML, OOP → SOLID; creational + structural patterns; networking, APIs, scaling, caching | **W4:** thread-safe LRU cache with TTL in 40 min + 5-min caching pitch |
| **S2 Concurrency Crucible** | W5–W9 | Behavioral patterns, machine-coding method; Tic-Tac-Toe → Splitwise; databases, indexing, replication, sharding, CAP, message queues | **W9:** Splitwise core in 35 min + 5 rapid HLD questions (≥ 14/20) |
| **S3 Spring Citadel** | W10–W14 | BookMyShow seat locking, rate limiters, Snowflake IDs, URL shortener, pub-sub, scheduler, ATM, meeting rooms, chess, inventory; microservice patterns, distributed transactions, locks/Raft, storage & search | **W14:** random machine-coding core in 35 min + verbal Pastebin (≥ 10/15) |
| **S4 Distributed Kingdom** | W15–W19 | Notification, food delivery, KV store; reliability, security, DNS/edge; case studies: rate limiter, notifications, news feed, typeahead, chat, crawler | **W19:** 45-min solo HLD mock — WhatsApp, recorded (≥ 16/24) |
| **S5 Cloud Ascension** | W20–W23 | YouTube, Dropbox, Uber, Ticketmaster, payments, Dynamo-style KV, Kafka internals, ad clicks, top-K | **W23:** 45-min HLD mock on a random case (≥ 17/24) |
| **S6 Final Boss: The Offer** | W24–W26 | Metrics monitoring, Google Docs, LLM/RAG platform; mock week; TicketVerse interview story | **W26:** final LLD + HLD mock (≥ 7/9 LLD and ≥ 18/24 HLD) |

---

## 5. LLD problems you will code

| Week | Problem | Key patterns / skills | Folder |
|---|---|---|---|
| W1 | Bank or Library (class diagram + skeleton) | UML, OOP pillars | `lld/bank` |
| W2 | God-class refactor (`OrderManager`) | SRP, DIP, characterization tests | `patterns/solid` |
| W3 | Notification factory kata | Factory registry, Builder | `patterns/creational` |
| W4 | **LRU cache with TTL, thread-safe** (Boss) | HashMap + DLL, `ReentrantLock`, `Clock` | `labs/lrucache` |
| W5 | Pricing + notifications kata | Strategy, Observer | `patterns/behavioral` |
| W6 | Tic-Tac-Toe · Snake & Ladder | O(1) win check, Strategy (dice) | `lld/tictactoe`, `lld/snakeladder` |
| W7 | Parking Lot · Vending Machine | Strategy, Factory · State | `lld/parkinglot`, `lld/vendingmachine` |
| W8 | Elevator · Logging framework | State + LOOK scheduling · Chain of Responsibility, Singleton | `lld/elevator`, `lld/logger` |
| W9 | Splitwise (+ simplify debts) · Library management | Strategy, heaps · Observer | `lld/splitwise`, `lld/library` |
| W10 | **BookMyShow** seat holds (feeds TicketVerse W13) | Locks, TTL holds, race tests | `lld/bookmyshow` |
| W12 | Kafka-like pub-sub · Job scheduler | Partitions/offsets/groups · `DelayQueue`, thread pools | `labs/pubsub`, `lld/jobscheduler` |
| W13 | ATM · Meeting-room scheduler | State + Chain · `TreeMap` intervals | `lld/atm`, `lld/meetingrooms` |
| W14 | Chess (or Cricbuzz) · Inventory/order management | Polymorphism, Command · no-oversell concurrency | `lld/chess`, `lld/inventory` |
| W15 | Notification system · Food delivery | Decorator (retry/rate-limit), queues · State, Observer | `lld/notification`, `lld/fooddelivery` |
| W16 | Thread-safe KV store with TTL | Atomic ops, expiry sweeper | `lld/kvstore` |
| W25 | Unseen problem (e.g., Amazon Locker) — LLD mock | Everything | `lld/mock-w25` |

**Implementation labs (building blocks):** consistent hashing (W7) · token-bucket & sliding-window limiters (W10) · Snowflake IDs + Base62 shortener (W11) · pub-sub with consumer groups + DLQ (W12) · Bloom filter (W14) · typeahead trie (W18) · chunk store with dedupe (W20) · virtual waiting room (W21) · vector clocks + quorum store (W22) · count-min sketch + top-K (W23).

## 6. HLD case studies you will design

Each lives in `hld/NN-name/` with `README.md` (1-page write-up from the template), `diagram.excalidraw` and `diagram.png`.

| # | Week | Case study | Signature trade-off |
|---|---|---|---|
| 01 | W11 | URL shortener | Key generation, 301 vs 302, cache hot links |
| 02 | W17 | Distributed rate limiter | Redis + Lua atomicity, fail-open vs fail-closed |
| 03 | W17 | Notification system | Priority queues, retries, provider outage |
| 04 | W18 | News feed | Fan-out on write vs read, celebrities |
| 05 | W18 | Typeahead | Precomputed top-K trie, rebuild pipeline |
| 06 | W19 | Chat (WhatsApp) | WebSocket routing, ordering, offline delivery |
| 07 | W19 | Web crawler | Frontier + politeness, dedupe |
| 08 | W20 | YouTube / Netflix | Transcoding pipeline, ABR, CDN cost |
| 09 | W20 | Google Drive / Dropbox | Chunking, dedupe, sync conflicts |
| 10 | W21 | Uber / Ola | Geo index, matching without double assignment |
| 11 | W21 | Ticketmaster / BookMyShow (TicketVerse) | Seat holds under contention, waiting room |
| 12 | W22 | Payment system | Idempotency, double-entry ledger, reconciliation |
| 13 | W22 | Distributed KV store (Dynamo-style) | Quorums, vector clocks, hinted handoff |
| 14 | W23 | Distributed message queue (Kafka internals) | ISR, acks, ordering vs throughput |
| 15 | W23 | Ad-click aggregation (+ top-K/leaderboard notes) | Windows, late events, exactly-once |
| 16 | W24 | Metrics monitoring & alerting | TSDB storage, cardinality |
| 17 | W24 | Google Docs | OT vs CRDT |
| 18 | W24 | LLM chat / RAG platform | Token rate limits, streaming, cost |
| 19 | W26 | **TicketVerse end-to-end** | Your own system at 10× / 100× |

Plus: Pastebin (verbal, W14 Boss) and unseen cases in the W23/W25 mocks.

---

## 7. Navigation

| File / folder | Use it for |
|---|---|
| [`ROADMAP_26_WEEKS.md`](ROADMAP_26_WEEKS.md) | One-page view of all 26 weeks (generated) |
| [`Weeks/`](Weeks/) | Day-by-day sessions with `learn`, `do`, `Done when`, self-checks |
| [`RESOURCES.md`](RESOURCES.md) | Verified links: free first, Hindi + English, tools with versions |
| [`HLD_INTERVIEW_FRAMEWORK.md`](HLD_INTERVIEW_FRAMEWORK.md) | 45-min HLD framework, estimation cheat sheet, deep-dive menu, write-up template, scoring rubric |
| [`LLD_MACHINE_CODING_FRAMEWORK.md`](LLD_MACHINE_CODING_FRAMEWORK.md) | 90-min machine-coding playbook, pattern table, Java skeleton, concurrency & testing checklists |
| [`../00_Progress_Tracker/AI_MEMORY.md`](../00_Progress_Tracker/AI_MEMORY.md) | How your AI mentor tracks progress, tests and remediation |

### Your repo: `system-design-lab`

```text
system-design-lab/
├─ pom.xml                      # JDK 25, JUnit 6 (Jupiter), AssertJ
├─ src/main/java/com/sdlab/
│   ├─ patterns/                # solid, creational, structural, behavioral
│   ├─ lld/                     # one package per machine-coding problem
│   └─ labs/                    # building blocks: lrucache, ratelimiter, idgen, bloom, pubsub, ...
├─ src/test/java/com/sdlab/     # mirrors main; every problem has tests
├─ hld/NN-case-name/            # README.md (write-up) + diagram.excalidraw + diagram.png
├─ notes/                       # concept notes 01..21 (protocols, caching, databases, ...)
├─ boss/                        # boss-battle scorecards + recording links
└─ mocks/                       # mock interview scorecards (W25+)
```

### Cross-track sync (why topics land in these weeks)

| SD week | Topic | Syncs with |
|---|---|---|
| W1–W2 | OOP from a design view, SOLID | Java W3 OOP |
| W4 | Thread-safe LRU (one coarse lock, just-in-time) | Deepened by Java W8–W9 concurrency; DSA W24 meets LRU again (LeetCode 146) |
| W8–W9 | Thread-safe logger, Elevator, Splitwise | Java W8–W9 concurrency |
| W9 | Message queues (Kafka vs RabbitMQ vs Service Bus) | Java W17 Kafka; Azure Service Bus |
| W10 | BookMyShow seat locking | **Java W13** TicketVerse seat holds (optimistic/pessimistic, Redis TTL) |
| W12 | Microservice patterns (gateway, saga, outbox, CQRS) | **Java W15** microservices split, W17–W18 saga + outbox |
| W15–W16 | Reliability/observability, OAuth2/JWT security | Java W14 Spring Security + Keycloak, W16 Resilience4j + OpenTelemetry |
| W21 | Ticketmaster HLD | TicketVerse booking design |
| W24 | LLM chat / RAG platform | AI track (DocuMind RAG, "Ask TicketVerse") |
| W26 | TicketVerse interview story | Java W26 interview mode |

---

## 8. Rules, pitfalls & tips

**Rules**

1. **No artifact, no XP.** Every session ends with a commit (code, diagram or write-up).
2. **Solo first, solution second.** Read Hello Interview / awesome-low-level-design solutions only *after* your attempt; then list 3 gaps.
3. **Type it, don't paste it.** Your gap is writing code — reference code is for comparison, not for copying.
4. **Tests are the definition of done** for LLD: happy path, edge cases, invalid input, and a race test whenever state is shared.
5. **Numbers in every HLD.** No design without QPS, storage and one latency budget.
6. **Timebox.** 45 minutes means 45. Unfinished work becomes the stretch, not overtime.

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

- Keep a **mistakes log** at the bottom of each `DESIGN.md`; reread it before boss battles.
- Diagram conventions (Excalidraw): clients left → data right; cylinders = stores; solid arrows = sync calls; dashed = async/events; number the main flow.
- Hindi helps? Use Concept && Coding or Coder Army for first exposure, then an English resource for interview vocabulary.
- Hello Interview has free and premium pages — every link in this plan points to a **free** page (checked Oct 2026).
- **Mocks:** (a) *Peer mocks* — swap roles with a colleague/friend: you interview them on a case you know well, they interview you on one you don't; (b) *AI mocks* — ask your AI mentor: *"Run a 45-minute HLD mock for &lt;case&gt; as my interviewer. Answer my clarifying questions, push on 3 deep dives, then score me with the rubric in HLD_INTERVIEW_FRAMEWORK.md."* The same works for LLD with the rubric in `LLD_MACHINE_CODING_FRAMEWORK.md`.

---

## 9. How you're tested on Sundays

The Sunday weekly test (150 min across all tracks) includes **System Design — 30 min**:

| Part | Format |
|---|---|
| 5 concept questions | Drawn from the week's `self_check` list plus 1–2 spaced-repetition questions from earlier weeks |
| 1 mini design | Either an **LLD class diagram** (entities, relationships, key interfaces, one pattern justified) or an **HLD sketch** (requirements, rough estimate, boxes-and-arrows, one deep dive) |

Scoring per track is **/100**: **≥ 80 green**, **60–79 amber**, **< 60 red** → weak topics become remediation tasks in next week's plan (e.g., "redo Parking Lot core from a blank file", "re-derive the quorum math").

**Boss battles** (Saturday, 45 min, timed) award +300 XP when cleared; pass marks are listed in the phase map above.
