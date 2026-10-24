# ☕ Java Backend · Week 26 — Interview mode: revise, tell stories, mock

> 📅 **Mon 19 Apr 2027 → Sun 25 Apr 2027** · Season 6 — Final Boss: The Offer · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 25](Week-25.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-26.md)

**Why this week:** Offers go to candidates who can explain clearly under pressure; this week converts 25 weeks of work into crisp answers, confident live coding and compelling project stories.

## 🗓️ Sessions

### Monday 19 Apr · 60 min — Core Java, OOP, collections and streams: rapid-fire plus live code
- 📚 **Learn:** Revise the Core Java, OOP, Strings, Exceptions, Generics, Collections and Java 8 streams sections of `INTERVIEW_QUESTION_BANK.md`, starred questions first; answer aloud in 60-90 seconds with one example each. [Baeldung: HashMap under the hood](https://www.baeldung.com/java-hashmap-advanced), [Baeldung: equals and hashCode contracts](https://www.baeldung.com/java-equals-hashcode-contracts), [roadmap.sh: Java](https://roadmap.sh/java).
- 🛠️ **Do:** Set a timer and answer 30 starred questions aloud while recording audio; mark any answer that took over 90 s or missed a key point. From a blank file, live-code an O(1) LRU cache (HashMap + doubly linked list) with tests in 25 minutes, then 5 classic stream questions in 10 minutes. Done when: 24+ of 30 answers are confident and the LRU tests pass inside 25 minutes.

### Tuesday 20 Apr · 60 min — Concurrency and JVM: explain, then code under time pressure
- 📚 **Learn:** Revise the Concurrency and JVM/GC sections of the bank: thread states, synchronized vs volatile vs atomics, JMM, executors and rejection, CHM, CompletableFuture, virtual threads, GC choice, leaks and dumps. [Jenkov: Java concurrency tutorial](https://jenkov.com/tutorials/java-concurrency/index.html), [Baeldung: Guide to CompletableFuture](https://www.baeldung.com/java-completablefuture), [Baeldung: JVM garbage collectors](https://www.baeldung.com/jvm-garbage-collectors).
- 🛠️ **Do:** Answer 20 starred questions aloud. Live-code in 20 minutes a bounded blocking queue with ReentrantLock and two Conditions plus a test, then in 15 minutes a CompletableFuture aggregator with per-call timeout and fallback. Explain your W8 deadlock thread dump and W10 GC log as if to an interviewer. Done when: both programs pass tests inside their time boxes.

### Wednesday 21 Apr · 60 min — Spring, JPA, transactions, security: whiteboard the request lifecycle
- 📚 **Learn:** Revise Spring Core/Boot, REST, JPA/Hibernate, Transactions, Security and Testing sections; be ready to trace one request through filters, DispatcherServlet, proxies, persistence context and the database, naming what can fail at each hop. [Spring: DispatcherServlet](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-servlet.html), [Marco Behler: @Transactional in depth](https://www.marcobehler.com/guides/spring-transaction-management-transactional-in-depth), [Vlad Mihalcea: N+1 problem](https://vladmihalcea.com/n-plus-1-query-problem/).
- 🛠️ **Do:** On paper, draw `POST /api/bookings` from the security filter chain to the database commit and the outbox event, explaining 6 failure points (expired JWT, validation, self-invocation, lost update, lazy loading, rollback rules). Then live-code a validated endpoint + ProblemDetail handler + `@WebMvcTest` in 25 minutes. Done when: the drawing is explained aloud in under 8 minutes and the tests pass in time.

### Thursday 22 Apr · 60 min — Microservices, Kafka, Docker, Kubernetes: architecture and failure drills
- 📚 **Learn:** Revise the Microservices, Kafka, Docker and Kubernetes sections; practise explaining trade-offs (sync vs async, outbox vs CDC, choreography vs orchestration, AKS vs Container Apps) and failure handling with your own numbers. [microservices.io: Pattern language](https://microservices.io/patterns/index.html), [Kafka 4.3: Design](https://kafka.apache.org/43/design/design/), [Kubernetes: Components](https://kubernetes.io/docs/concepts/overview/components/).
- 🛠️ **Do:** Whiteboard the TicketVerse container diagram and the booking saga, then walk through 5 failures (payment timeout, Kafka down, duplicate event, Redis down, booking pod killed mid-request) and how each is handled. Then do a 20-minute LLD drill: classes and interfaces for a thread-safe `SeatLockService`. Done when: each failure has a clear answer under 2 minutes and the LLD compiles with one passing test.

### Friday 23 Apr · 60 min — Project deep dive: STAR stories, trade-offs, two-minute pitch
- 📚 **Learn:** STAR (Situation, Task, Action, Result) with numbers; prepare stories for conflict, failure, ownership and learning; how to present trade-offs and what you would do differently; keep a 2-minute and a 10-minute project pitch ready. [Tech Interview Handbook: Behavioral interviews](https://www.techinterviewhandbook.org/behavioral-interview/), [MIT CAPD: The STAR method](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/), [Martin Fowler: Microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html).
- 🛠️ **Do:** Write 5 STAR stories from TicketVerse: zero double booking under 100 threads, circuit-breaker chaos test, outbox fixing lost events, Azure deploy with cost guardrails, AI assistant safety. Record the 2-minute pitch and one 10-minute deep dive; watch them back and cut filler. Done when: every story has a measurable result and fits in 2 minutes.

### Saturday 24 Apr · 60 min — BOSS BATTLE: Full mock technical interview, 60 minutes
- 📚 **Learn:** Format: 5 min intro, 10 min project deep dive, 20 min Core Java + concurrency, 15 min Spring/microservices/Kafka/Kubernetes, 10 min live coding (streams + small concurrency task). Interviewer: a friend, a peer on Pramp, or an AI prompted with random starred questions from the bank. Rubric: communication, correctness, depth, trade-offs, coding (20 each). [Pramp: Mock interviews](https://www.pramp.com/), [Tech Interview Handbook: Coding interview prep](https://www.techinterviewhandbook.org/coding-interview-prep/).
- 🛠️ **Do:** Run the full 60-minute mock with a timer and screen recording; score yourself with the rubric right after (the interviewer scores too); log every miss in `WEAKNESS_TRACKER.md` with a fix date; write a 2-week maintenance plan (daily 20 questions + 1 live-code). Done when: the score is 75/100 or higher and the recording and scored rubric are saved.

## 📦 Deliverable (by Saturday night)
Recorded answers, timed live-coding solutions (LRU, blocking queue, async aggregator, REST endpoint, SeatLockService), lifecycle and saga drawings, 5 STAR stories, 2/10-minute pitches, mock interview recording with a 75+ rubric score.

## ✅ Self-check (Sunday test preview)
- Explain HashMap internals and the equals/hashCode contract in under 90 seconds.
- How would you make seat booking safe across 3 instances of booking-service?
- Walk through a request from the Spring Security filter chain to a database commit.
- Your Kafka consumer processed an event twice: why, and how is TicketVerse protected?
- A pod is in CrashLoopBackOff after a deploy: what are your first three commands?
- Tell me about a time you found and fixed a performance problem (STAR, with numbers).
- What would you change if TicketVerse had to handle 100x traffic on a blockbuster release?

## 🚀 Stretch (optional)
Do a second mock with a different interviewer, focusing only on your three weakest sections from Saturday.
