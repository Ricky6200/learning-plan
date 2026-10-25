# 📚 System Design Resources (verified Oct 2026)

Every link below was checked (HTTP 200; YouTube IDs verified through oEmbed titles). **Free first.** Items marked **(paid)** are optional.
Hello Interview mixes free and premium content — every page linked here has a free part, and the weekly sessions name the section to read (some pages end with a premium section).
Week numbers refer to the **30-week plan** (W1 = 26 Oct 2026, W30 = 17 May 2027).

---

## 1. Primary (daily use)

| Resource | What it's for | Weeks |
|---|---|---|
| [Hello Interview — System Design in a Hurry](https://www.hellointerview.com/learn/system-design/in-a-hurry/introduction) | Interview framework, [core concepts](https://www.hellointerview.com/learn/system-design/in-a-hurry/core-concepts), [key technologies](https://www.hellointerview.com/learn/system-design/in-a-hurry/key-technologies), [patterns](https://www.hellointerview.com/learn/system-design/in-a-hurry/patterns) (contention, multi-step processes, long-running tasks, realtime updates, large blobs), problem breakdowns (Bitly, Ticketmaster, Uber, WhatsApp, Dropbox, YouTube, news feed, top-K, crawler, ad clicks, job scheduler, Yelp, flash sale…) | W2–W30 |
| [Hello Interview — Low Level Design in a Hurry](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/introduction) | LLD delivery, [OOP](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/oop-concepts), [design principles](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/design-principles), [patterns](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/patterns), [concurrency intro](https://www.hellointerview.com/learn/low-level-design/concurrency/intro), LLD breakdowns (parking lot, elevator, logging service, file system, BookMyShow, rate limiter, inventory) | W1–W30 |
| [refactoring.guru — Design patterns catalog](https://refactoring.guru/design-patterns/catalog) | Best visual explanation of all GoF patterns; [Java examples](https://refactoring.guru/design-patterns/java); [code smells](https://refactoring.guru/refactoring/smells) (site free; ebook paid) | W2–W5 |
| [ashishps1/awesome-low-level-design](https://github.com/ashishps1/awesome-low-level-design) | Problem statements for 30+ LLD problems (incl. the unseen-mock problems: car rental W10, hotel management and digital wallet W28) + [Java solutions](https://github.com/ashishps1/awesome-low-level-design/tree/main/solutions/java/src) to compare *after* your attempt | W3–W28 |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Free HLD textbook: scalability, caching, databases, async, plus solved designs (OOD solutions W1, Pastebin W15, Twitter timeline W19) | W1–W19 |
| [Excalidraw](https://excalidraw.com/) | All HLD diagrams (save `.excalidraw` + export PNG); extra shapes at [Excalidraw libraries](https://libraries.excalidraw.com/) | W3–W30 |

## 2. Secondary / reference

| Resource | Use |
|---|---|
| [ashishps1/awesome-system-design-resources](https://github.com/ashishps1/awesome-system-design-resources) + [Java implementations](https://github.com/ashishps1/awesome-system-design-resources/tree/main/implementations/java) | Curated HLD reading list; compare your rate limiter / consistent-hashing labs |
| [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) | Free open-source system design "book" |
| [Hello Interview deep dives](https://www.hellointerview.com/learn/system-design/in-a-hurry/key-technologies) | [Flink](https://www.hellointerview.com/learn/system-design/deep-dives/flink) (batch vs stream, W21) · [Cassandra](https://www.hellointerview.com/learn/system-design/deep-dives/cassandra) (data modelling, W20) · [Change data capture](https://www.hellointerview.com/learn/system-design/deep-dives/change-data-capture) (W15) · [Kafka](https://www.hellointerview.com/learn/system-design/deep-dives/kafka) (W25) · [Proximity search](https://www.hellointerview.com/learn/system-design/deep-dives/proximity-search) (W23) · [Time-series databases](https://www.hellointerview.com/learn/system-design/deep-dives/time-series-databases) (W26) |
| [microservices.io patterns](https://microservices.io/patterns/index.html) | Saga, [transactional outbox](https://microservices.io/patterns/data/transactional-outbox.html), API gateway, CQRS… (W13, W24) |
| [Azure Architecture Center — cloud design patterns](https://learn.microsoft.com/en-us/azure/architecture/patterns/) | Same patterns in Azure terms (helps the Azure track): [circuit breaker](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker), [bulkhead](https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead), [valet key](https://learn.microsoft.com/en-us/azure/architecture/patterns/valet-key), [rate limiting](https://learn.microsoft.com/en-us/azure/architecture/patterns/rate-limiting-pattern), [priority queue](https://learn.microsoft.com/en-us/azure/architecture/patterns/priority-queue), [choose a data store](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-store-overview), [big data architectures](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/big-data-architectures) (Lambda/Kappa, W21) |
| [Patterns of Distributed Systems (martinfowler.com)](https://martinfowler.com/articles/patterns-of-distributed-systems/) | Leader-follower, quorum, heartbeat, gossip, Raft-style log (W6, W8, W25) |
| [Amazon Builders' Library](https://aws.amazon.com/builders-library/) | Production wisdom: [retries + jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), [idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/), [load shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/), [caching](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/), [leader election](https://aws.amazon.com/builders-library/leader-election-in-distributed-systems/), [static stability](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) |
| [Google SRE book](https://sre.google/sre-book/table-of-contents/) | [SLOs](https://sre.google/sre-book/service-level-objectives/), [monitoring](https://sre.google/sre-book/monitoring-distributed-systems/), [availability table](https://sre.google/sre-book/availability-table/) (W16, W26) |
| [Raft site](https://raft.github.io/) + [The Secret Lives of Data — Raft](https://thesecretlivesofdata.com/raft/) | Consensus, visually (W25, next to Kafka's KRaft) |
| [How to do distributed locking — Martin Kleppmann](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html) | Fencing tokens; why Redlock is debated (W14) |
| [Stripe: idempotency](https://stripe.com/blog/idempotency) · [Stripe: rate limiters](https://stripe.com/blog/rate-limiters) | Real-world API design (W11, W24) |
| [Dynamo paper (2007)](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) | The classic leaderless KV design (W24) |
| [Kafka docs — design](https://kafka.apache.org/documentation/#design) · [Confluent Kafka internals course](https://developer.confluent.io/courses/architecture/get-started/) | W9, W13, W25 |
| [Redis docs](https://redis.io/docs/latest/) | Expiry, Lua scripts, sorted sets, geo (W11, W17, W18, W23, W29) |
| [Leaderboard system design (systemdesign.one)](https://systemdesign.one/leaderboard-system-design/) · [Design a hotel booking system (System Design Handbook)](https://www.systemdesignhandbook.com/guides/design-hotel-booking-system/) · [PostgreSQL range types](https://www.postgresql.org/docs/current/rangetypes.html) | HLD finish week (W29) |
| [What is OLAP? (ClickHouse)](https://clickhouse.com/docs/concepts/olap) | Columnar analytics stores (W21) |
| [MADR — Markdown Architectural Decision Records](https://adr.github.io/madr/) | Template for `adr/` — one decision record per case study (from W11) |
| [sirupsen/napkin-math](https://github.com/sirupsen/napkin-math) · [Latency numbers gist](https://gist.github.com/jboner/2841832) · [Interactive latency by year](https://colin-scott.github.io/personal_website/research/interactive_latency.html) | Estimation (W12+) |
| [ByteByteGo blog](https://blog.bytebytego.com/) · [Arpit Bhayani](https://arpitbhayani.me/) | Weekly deep dives (some posts paid) |
| [Mermaid class diagrams](https://mermaid.js.org/syntax/classDiagram.html) · [sequence diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html) · [state diagrams](https://mermaid.js.org/syntax/stateDiagram.html) | UML that renders inside GitHub Markdown |

## 3. Books (optional)

| Book | Status / how to use | Cost |
|---|---|---|
| Alex Xu — *System Design Interview*, Vol 1 & Vol 2 | Most-used HLD prep books in India; also available online as the [ByteByteGo course](https://bytebytego.com/) | **(paid)** |
| Martin Kleppmann & Chris Riccomini — *Designing Data-Intensive Applications*, **2nd edition** ([O'Reilly, March 2026](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html); [book site](https://dataintensive.net/)) | The depth book. Read the replication, sharding/partitioning, transactions and consistency/consensus chapters alongside W6–W8, W14 and W24–W25. Prefer the 2nd edition over the 2017 1st edition. | **(paid)** |
| Eric Freeman & Elisabeth Robson — [*Head First Design Patterns*, 2nd ed.](https://wickedlysmart.com/head-first-design-patterns/) | Friendly, Java-based patterns book for W3–W5 | **(paid)** |

## 4. YouTube

### English

| Channel / playlist | Best for |
|---|---|
| [ByteByteGo](https://www.youtube.com/@ByteByteGo) — [System Design Fundamentals](https://www.youtube.com/playlist?list=PLCRMIe5FDPsd0gVs500xeOewfySTsmEjf) · [System Design Interview](https://www.youtube.com/playlist?list=PLCRMIe5FDPseVvwzRiCQBmNOVUIZSSkP8) | 5–10 min visual explainers (caching, CAP, Kafka, CDN, OAuth…) |
| [Hello Interview](https://www.youtube.com/@hello_interview) — [System Design Walkthroughs](https://www.youtube.com/playlist?list=PL5q3E8eRUieWtYLmRU3z94-vGRcwKr9tM) · [Deep Dives](https://www.youtube.com/playlist?list=PL5q3E8eRUieUHnsz0rh0W6AzwdVJBwEK6) | Full mock-style case studies (Bitly, Ticketmaster, Uber, WhatsApp…) + LLD walkthroughs — watch the named first 15 minutes, or after your solo attempt |
| [Gaurav Sen](https://www.youtube.com/@gkcs) — [System Design playlist](https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX) · [Low Level Design playlist](https://www.youtube.com/playlist?list=PLMCXHnjXnTnvQVh7WsgZ8SurU1O2v_UM7) | Fundamentals + LLD (Tic-Tac-Toe, logger, chess, rate limiter) |
| [Arpit Bhayani](https://www.youtube.com/@AsliEngineering) — [System Design playlist](https://www.youtube.com/playlist?list=PLsdq-3Z1EPT27BuTnJ_trF7BsaTpYLqst) · [Redis internals](https://www.youtube.com/playlist?list=PLsdq-3Z1EPT0eElcdOON9fdaeaQjlyXDt) | Indian engineer, first-principles depth |
| [Hussein Nasser](https://www.youtube.com/@hnasr) — [Backend Engineering (Beginner)](https://www.youtube.com/playlist?list=PLQnljOFTspQUNnO4p00ua_C5mKTfldiYT) | Protocols, databases, proxies |
| [Martin Kleppmann — Distributed Systems lectures](https://www.youtube.com/playlist?list=PLeKd45zvjcDFUEv_ohr_HdUFe97RItdiB) | University-grade replication, consensus, 2PC (W24, W25) |
| [Jordan has no life](https://www.youtube.com/@jordanhasnolife5163) | Advanced/rapid case studies for W21+ revision |

### Hindi

| Channel / playlist | Best for |
|---|---|
| [Concept && Coding (Shrayansh Jain)](https://www.youtube.com/@ConceptAndCodingByShrayansh) — [Low Level Design from Basics to Advanced](https://www.youtube.com/playlist?list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW) · [High Level Design from Basics to Advanced](https://www.youtube.com/playlist?list=PL6W8uoQQ2c63W58rpNFDwdrBnq5G3EfT7) · [LLD English-dubbed](https://www.youtube.com/playlist?list=PL6W8uoQQ2c611H_IeIcNGnUATVcd2FOav) | **The** Hindi LLD/HLD series with Java code: SOLID, all patterns, Parking Lot, Elevator, BookMyShow, Splitwise, ATM… |
| [Coder Army — System Design Full Course](https://www.youtube.com/playlist?list=PLQEaRBV9gAFvzp6XhcNFpk1WdOcyVo9qT) | Hindi LLD course: OOP, UML, SOLID, patterns, project-style designs |
| [Engineering Digest](https://www.youtube.com/@engineeringdigest) | Short Hindi explainers (CAP, Bloom filter, URL shortener, Dropbox) |

## 5. Practice / labs

| What | Where |
|---|---|
| Your 11 building-block labs (consistent hashing, thread-safe LRU + TTL, token-bucket limiter, Snowflake IDs, pub-sub, lease lock + fencing tokens, typeahead trie, chunk store, waiting room, vector clocks + quorum store, count-min sketch) + Bloom filter as a stretch | `system-design-lab/labs/` — see the README tables |
| LeetCode design problems (free) | [LRU Cache 146](https://leetcode.com/problems/lru-cache/) (DSA W10 Sat) · [LFU Cache 460](https://leetcode.com/problems/lfu-cache/) · [My Calendar I 729](https://leetcode.com/problems/my-calendar-i/) · [Implement Trie 208](https://leetcode.com/problems/implement-trie-prefix-tree/) (DSA W16 Sat; reused in SD W19) · [Design Twitter 355](https://leetcode.com/problems/design-twitter/) · [Time Based Key-Value Store 981](https://leetcode.com/problems/time-based-key-value-store/) · [Design Underground System 1396](https://leetcode.com/problems/design-underground-system/) |
| Free LLD walkthroughs to compare against | Hello Interview: [Parking Lot](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/parking-lot), [Elevator](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/elevator), [Logging service](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/logging-service), [File system](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/file-system), [BookMyShow](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/bookmyshow), [Rate limiter](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/rate-limiter), [Inventory management](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/inventory-management), [Connect Four](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/connect-four), [Amazon Locker](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/amazon-locker) |
| Unseen mocks (read the reference only afterwards) | Machine coding: car rental (W10), Amazon Locker (W27), hotel booking + digital wallet (W28). HLD: FB Live comments (W20), Yelp (W21), random case (W25), two in W27, stock exchange + flash sale (W29) |
| Mock interviews | **AI mentor** (ask it to run timed LLD/HLD mocks and score with the rubrics in the framework docs) + **peer mocks** with colleagues/friends (swap interviewer/candidate roles weekly from W20, when job applications start) |

## 6. Tools to install

| Tool | Version (Oct 2026) | Notes |
|---|---|---|
| [Amazon Corretto 25](https://docs.aws.amazon.com/corretto/latest/corretto-25-ug/what-is-corretto-25.html) | **JDK 25 (LTS)** | Same JDK as the Java track (company software catalogue) |
| [Apache Maven](https://maven.apache.org/download.cgi) | **3.9.x / 3.10.x** (Maven 4 is still a release candidate) | Through the company JFrog settings used by `java-mastery`; `mvn -q test` after every session |
| JUnit + AssertJ (Maven dependencies) | **JUnit 6.1.x (Jupiter API)**, **AssertJ 3.27.x** | [JUnit user guide](https://docs.junit.org/current/user-guide/) · [AssertJ docs](https://assertj.github.io/doc/) — a one-assert `SmokeTest` in W1, real tests from W2 |
| [IntelliJ IDEA](https://www.jetbrains.com/idea/download/) | Latest | Free (Community-level) features are enough for this track |
| Git + GitHub | Latest | Repo `system-design-lab`, commit every session |
| GitHub Actions | — | `mvn -B test` workflow + status badge in W27 ([Java with Maven](https://docs.github.com/en/actions/tutorials/build-and-test-code/java-with-maven), [status badge](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge)); Java writes its first `ci.yml` in W14 |
| [Docker Desktop](https://docs.docker.com/desktop/) + [`redis` image](https://hub.docker.com/_/redis) | `redis:8` | Only for stretches: NGINX (W3) and Postgres `EXPLAIN` (W6) run in GitHub Codespaces; Redis (W11, W18) runs from Java W11 (~4 Jan) on Podman in the company's WSL Ubuntu image (same commands as Docker) or in Codespaces. Pull images through the company's mirror in JFrog |
| [Testcontainers](https://testcontainers.com/) | 2.0.x | Optional after Java W12 Sat: real Redis in JUnit tests (W18 stretch); set the [image name prefix](https://java.testcontainers.org/features/image_name_substitution/) to the company's Docker mirror |
| [Excalidraw](https://excalidraw.com/) | Web | Primary diagram tool |
| [Mermaid Live Editor](https://mermaid.live/) | Web | Draft UML before pasting into Markdown |
| [draw.io / diagrams.net](https://app.diagrams.net/) | Web | Optional alternative to Excalidraw |
| [OBS Studio](https://obsproject.com/) (or Windows Snipping Tool screen recording) | Latest | Record boss battles and mocks |
