# 📚 Java Backend Track — Resources (all links verified Oct 2026)

Free first. **(paid)** marks paid items. Each week's exact pages/videos are linked inside `Weeks/Week-XX.md`; this page is the map.
Rule of thumb: **docs + one tutorial + code** beats three videos.

---

## 1. Primary — daily use

| Resource | Use it for | Weeks |
|---|---|---|
| [dev.java — Learn](https://dev.java/learn/) | Official modern Java tutorials (language, OOP, generics, lambdas, collections, streams, modules, I/O, reflection, regex, JVM tools, GC) | W1–W11 |
| [University of Helsinki — Java Programming MOOC](https://java-programming.mooc.fi/) | Beginner-friendly explanations + exercises (methods, objects, references, testing, hash tables) | W1–W6 |
| [Oracle Java Tutorials — Concurrency](https://docs.oracle.com/javase/tutorial/essential/concurrency/index.html) | Threads, synchronization, guarded blocks, executors, fork/join (classic, still accurate) | W8–W9 |
| [Jenkov — Java Concurrency and Multithreading](https://jenkov.com/tutorials/java-concurrency/index.html) · [java.util.concurrent](https://jenkov.com/tutorials/java-util-concurrent/index.html) | Short, precise pages on JMM, happens-before, locks, CAS, queues, synchronizers | W8–W9 |
| [Baeldung — Java Collections series](https://www.baeldung.com/java-collections) | Focused how-to articles (HashMap internals, streams, CompletableFuture, Spring, JPA, Kafka) | All |
| [Spring Boot reference](https://docs.spring.io/spring-boot/index.html) · [Spring Framework reference](https://docs.spring.io/spring-framework/reference/index.html) | Source of truth for Boot 4.1 / Framework 7 behaviour (Spring Core without Boot in W12) | W12–W30 |
| [Spring Data JPA](https://docs.spring.io/spring-data/jpa/reference/index.html) · [Spring Security](https://docs.spring.io/spring-security/reference/index.html) · [Spring for Apache Kafka](https://docs.spring.io/spring-kafka/reference/index.html) | Module references used in TicketVerse | W14–W25 |
| [Spring Guides](https://spring.io/guides/) · [start.spring.io](https://start.spring.io/) | Step-by-step getting-started guides; project generator | W11+ |
| [Spring Boot 4.0 migration guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide) | Why older tutorials differ (modular starters, Jackson 3, `@MockitoBean`, Flyway starter) | W13+ |
| [Testcontainers guides](https://testcontainers.com/guides/) | Real Postgres/Redis/Kafka in tests (first test in W11, everywhere from W14) | W11–W26 |
| [Kafka 4.3 documentation](https://kafka.apache.org/43/getting-started/introduction/) · [Confluent Developer courses](https://developer.confluent.io/courses/) | Kafka concepts (Kafka 101, architecture, transactions); 4.4 is the newest release, the 4.3 docs cover the same concepts | W20–W21 |
| [Docker Docs — Get started](https://docs.docker.com/get-started/) · [Kubernetes — Learn Kubernetes basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) | Containers and orchestration fundamentals (Docker basics first come in AI W8) | W11, W22–W24 |
| [Microsoft Learn — Azure for Java developers](https://learn.microsoft.com/en-us/azure/developer/java/) | Java on Container Apps / AKS, Spring Cloud Azure | W28 |

---

## 2. Secondary / reference (by topic)

**Core Java & OOP**
- [Oracle tutorial: Classes and Objects](https://docs.oracle.com/javase/tutorial/java/javaOO/index.html) · [Interfaces and Inheritance](https://docs.oracle.com/javase/tutorial/java/IandI/index.html) · [Generics](https://docs.oracle.com/javase/tutorial/java/generics/index.html) · [Exceptions](https://docs.oracle.com/javase/tutorial/essential/exceptions/index.html) · [Collections trail](https://docs.oracle.com/javase/tutorial/collections/index.html)
- [JLS SE 25 — Ch. 12 Execution (class initialization)](https://docs.oracle.com/javase/specs/jls/se25/html/jls-12.html) · [Ch. 17 Threads and Locks (JMM)](https://docs.oracle.com/javase/specs/jls/se25/html/jls-17.html)
- [Java SE 25 API: HashMap](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/HashMap.html) · [ConcurrentHashMap](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ConcurrentHashMap.html) · [ThreadPoolExecutor](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ThreadPoolExecutor.html) · [CompletableFuture](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/CompletableFuture.html)
- [Refactoring.Guru — Design patterns in Java](https://refactoring.guru/design-patterns/java)

**Core Java gaps (W10)**
- [dev.java: Java I/O API](https://dev.java/learn/java-io/) · [Reflection](https://dev.java/learn/reflection/) · [Annotations](https://dev.java/learn/annotations/) · [Regular expressions](https://dev.java/learn/regex/) · [regex101](https://regex101.com/) (pick the Java flavor)
- [Baeldung: Java serialization](https://www.baeldung.com/java-serialization) · [Deep copy](https://www.baeldung.com/java-deep-copy) · [Mockito](https://site.mockito.org/) · [AssertJ](https://assertj.github.io/doc/) · [Martin Fowler: Test double](https://martinfowler.com/bliki/TestDouble.html)

**Modern Java (9 → 25)**
- [Java Language Updates (JDK 25)](https://docs.oracle.com/en/java/javase/25/language/index.html) · [Language changes by release](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-release.html)
- [JDK 25 feature list](https://openjdk.org/projects/jdk/25/) · [JEP 444 Virtual Threads](https://openjdk.org/jeps/444) · [JEP 491 No pinning in synchronized](https://openjdk.org/jeps/491) · [JEP 485 Stream Gatherers](https://openjdk.org/jeps/485) · [JEP 512 Compact source files](https://openjdk.org/jeps/512) · [JEP 513 Flexible constructor bodies](https://openjdk.org/jeps/513) · [JEP 506 Scoped Values](https://openjdk.org/jeps/506)
- [Oracle: Virtual threads guide (JDK 25)](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html) · [dev.java: Modules (JPMS)](https://dev.java/learn/modules/) · [Java Version Almanac (API changes per release)](https://javaalmanac.io/)

**JVM, GC & troubleshooting**
- [HotSpot GC Tuning Guide (JDK 25)](https://docs.oracle.com/en/java/javase/25/gctuning/index.html) · [G1](https://docs.oracle.com/en/java/javase/25/gctuning/garbage-first-g1-garbage-collector1.html) · [ZGC](https://docs.oracle.com/en/java/javase/25/gctuning/z-garbage-collector1.html)
- [Troubleshooting Guide (JDK 25)](https://docs.oracle.com/en/java/javase/25/troubleshoot/index.html) · [jcmd](https://docs.oracle.com/en/java/javase/25/docs/specs/man/jcmd.html) · [jstack](https://docs.oracle.com/en/java/javase/25/docs/specs/man/jstack.html)
- [dev.java: JDK Flight Recorder](https://dev.java/learn/jvm/monitoring-troubleshooting/jfr/) · [Inside Java: the `jfr view` command](https://inside.java/2023/09/26/sip082/) · [JVMS ch. 2: JVM structure](https://docs.oracle.com/javase/specs/jvms/se25/html/jvms-2.html) — on the company laptop `jcmd` and `jfr` (they ship with the JDK) replace VisualVM/MAT/JMC until IT approves those
- JVM in containers: [Microsoft Learn: Containerize your Java applications](https://learn.microsoft.com/en-us/azure/developer/java/containers/overview) · [Spring Boot: Efficient container images](https://docs.spring.io/spring-boot/reference/packaging/container-images/efficient-images.html) · [Testcontainers: Image name substitution](https://java.testcontainers.org/features/image_name_substitution/) (company Docker mirror)

**Spring, data & transactions**
- [Marco Behler — Spring Framework guide](https://www.marcobehler.com/guides/spring-framework) · [@Transactional in depth](https://www.marcobehler.com/guides/spring-transaction-management-transactional-in-depth) · [Spring Security in depth](https://www.marcobehler.com/guides/spring-security)
- [Vlad Mihalcea — Hibernate tutorials](https://vladmihalcea.com/tutorials/hibernate/) (N+1, dirty checking, locking, isolation levels)
- [PostgreSQL docs: EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) · [Transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) · [Explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) · [Use The Index, Luke](https://use-the-index-luke.com/)
- [HikariCP — About pool sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) · [Spring Data Redis](https://docs.spring.io/spring-data/redis/reference/) · [Kleppmann — How to do distributed locking](https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html)
- [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457.html) · [springdoc-openapi](https://springdoc.org/)
- Spring Core extras (W12): [Task execution and scheduling (`@Async`, `@Scheduled`)](https://docs.spring.io/spring-framework/reference/integration/scheduling.html) · [Baeldung: Spring events](https://www.baeldung.com/spring-events) · [SLF4J manual](https://www.slf4j.org/manual.html) · [Baeldung: MDC](https://www.baeldung.com/mdc-in-log4j-2-logback)
- JPA extras (W14, W25): [Spring Data JPA: Specifications](https://docs.spring.io/spring-data/jpa/reference/jpa/specifications.html) · [Auditing](https://docs.spring.io/spring-data/jpa/reference/auditing.html) · [Use The Index, Luke: keyset pagination](https://use-the-index-luke.com/no-offset) · [Vlad Mihalcea: @ManyToMany](https://vladmihalcea.com/the-best-way-to-use-the-manytomany-annotation-with-jpa-and-hibernate/)

**Security**
- [OAuth 2.0](https://oauth.net/2/) · [PKCE](https://oauth.net/2/pkce/) · [How OpenID Connect works](https://openid.net/developers/how-connect-works/) · [JWT introduction](https://jwt.io/introduction)
- [Keycloak guides](https://www.keycloak.org/guides) · [OWASP API Security Top 10 (2023)](https://api-security.owasp.org/editions/2023/en/0x11-t10) · [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- Service-to-service (W18): [OAuth 2.0 client credentials](https://oauth.net/2/grant-types/client-credentials/) · [Spring Security: Authorized clients (RestClient integration)](https://docs.spring.io/spring-security/reference/servlet/oauth2/client/authorized-clients.html)

**Microservices, resilience & observability**
- [microservices.io — pattern language](https://microservices.io/patterns/index.html) (saga, outbox, database per service, API gateway, idempotent consumer)
- [Martin Fowler — Microservices](https://martinfowler.com/articles/microservices.html) · [Microservice trade-offs](https://martinfowler.com/articles/microservice-trade-offs.html) · [Bounded context](https://martinfowler.com/bliki/BoundedContext.html)
- [Spring Cloud Gateway](https://docs.spring.io/spring-cloud-gateway/reference/index.html) ([Server Web MVC](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc.html), [RateLimiter filter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc/filters/ratelimiter.html), [CircuitBreaker filter](https://docs.spring.io/spring-cloud-gateway/reference/spring-cloud-gateway-server-webmvc/filters/circuitbreaker-filter.html)) · [Resilience4j docs](https://resilience4j.readme.io/docs/getting-started) · [Spring Framework resilience features](https://docs.spring.io/spring-framework/reference/core/resilience.html) (`@Retryable` needs `@EnableResilientMethods`)
- The split (W17–W18): [Martin Fowler: Strangler fig](https://martinfowler.com/bliki/StranglerFigApplication.html) · [Spring Cloud Contract](https://docs.spring.io/spring-cloud-contract/reference/getting-started/introducing-spring-cloud-contract.html) · [ArchUnit user guide](https://www.archunit.org/userguide/html/000_Index.html) · [Spring Modulith](https://docs.spring.io/spring-modulith/reference/)
- [Micrometer](https://docs.micrometer.io/micrometer/reference/) · [OpenTelemetry Java](https://opentelemetry.io/docs/languages/java/) · [Prometheus](https://prometheus.io/docs/introduction/overview/) · [Jaeger](https://www.jaegertracing.io/docs/latest/getting-started/)

**Kafka**
- [Kafka 4.3: Design](https://kafka.apache.org/43/design/design/) · [Consumer rebalance protocol (KIP-848)](https://kafka.apache.org/43/operations/consumer-rebalance-protocol/) · [Kafka 4.2 release (share groups production-ready)](https://kafka.apache.org/blog/2026/02/17/apache-kafka-4.2.0-release-announcement/)
- [Confluent: Kafka architecture deep dive](https://developer.confluent.io/courses/architecture/get-started/) · [Event streaming patterns](https://developer.confluent.io/patterns/)

**Docker, Kubernetes, CI/CD, Azure**
- [Docker build best practices](https://docs.docker.com/build/building/best-practices/) · [Compose docs](https://docs.docker.com/compose/) · [Jib](https://github.com/GoogleContainerTools/jib) · [Trivy](https://trivy.dev/docs/latest/getting-started/)
- [Kubernetes docs: Gateway API](https://kubernetes.io/docs/concepts/services-networking/gateway/) · [Gateway API project](https://gateway-api.sigs.k8s.io/) · [Envoy Gateway](https://gateway.envoyproxy.io/) · [Ingress NGINX retirement notice](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/)
- [Helm docs](https://helm.sh/docs/) · [kubectl quick reference](https://kubernetes.io/docs/reference/kubectl/quick-reference/) · [Argo CD](https://argo-cd.readthedocs.io/en/stable/)
- [GitHub Actions docs](https://docs.github.com/en/actions) · [OIDC to Azure](https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect)
- [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/) ([Manage secrets / Key Vault references](https://learn.microsoft.com/en-us/azure/container-apps/manage-secrets)) · [AKS](https://learn.microsoft.com/en-us/azure/aks/) · [Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/azure/postgresql/overview) · [Azure Managed Redis](https://learn.microsoft.com/en-us/azure/redis/overview) · [Event Hubs for Kafka](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview) · [Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) · [App Insights + OpenTelemetry](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=java)

**AI integration (W27) — `ticketverse-ai` is built and owned by the AI track (AI W23–W24, W27)**
- To read its code: [Spring AI: ChatClient](https://docs.spring.io/spring-ai/reference/api/chatclient.html) · [Tool calling](https://docs.spring.io/spring-ai/reference/api/tools.html) · [RAG](https://docs.spring.io/spring-ai/reference/api/retrieval-augmented-generation.html) · [MCP](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html) · [Observability](https://docs.spring.io/spring-ai/reference/observability/index.html) · [LangChain4j](https://docs.langchain4j.dev/)
- Awareness (W27 Fri): [Reactor reference](https://projectreactor.io/docs/core/release/reference/) · [Spring WebFlux](https://docs.spring.io/spring-framework/reference/web/webflux.html) · [Spring for GraphQL](https://docs.spring.io/spring-graphql/reference/) · [Spring gRPC](https://docs.spring.io/spring-grpc/reference/)

**Roadmaps**: [roadmap.sh Java](https://roadmap.sh/java) · [roadmap.sh Spring Boot](https://roadmap.sh/spring-boot) · [roadmap.sh Backend](https://roadmap.sh/backend)

---

## 3. Books (optional — all paid)

| Book | Why | When |
|---|---|---|
| *Head First Java, 3rd ed.* — Sierra, Bates, Gee **(paid)** | Friendliest OOP + Java basics refresher | W1–W4 |
| *Effective Java, 3rd ed.* — Joshua Bloch **(paid)** | The interview "why" behind equals/hashCode, immutability, generics, enums, lambdas | W2–W7 (one item per day) |
| *Java Concurrency in Practice* — Brian Goetz et al. **(paid)** | Still the concurrency bible (JMM, safe publication, executors) | W8–W9 |
| *Spring Start Here* — Laurențiu Spilcă **(paid)** | Clear Spring Core/Boot foundations | W12–W13 |
| *Kafka: The Definitive Guide, 2nd ed.* — Shapira, Palino, Sivaram, Petty **(paid)** | Producer/consumer internals, reliability, exactly-once | W20–W21 |
| *High-Performance Java Persistence* — Vlad Mihalcea **(paid, optional)** | JPA/Hibernate performance deep dive | W14–W15 |
| *Microservices Patterns* — Chris Richardson **(paid, optional)** | Saga, outbox, decomposition — same author as microservices.io | W17–W21 |

---

## 4. YouTube (pick ONE per topic; 1.5× speed; max 20 min per session)

| Topic | English | Hindi (or Indian-English creators) |
|---|---|---|
| Core Java from scratch | [Telusko — Java Tutorial for Beginners (playlist)](https://www.youtube.com/playlist?list=PLsyeobzWxl7pe_IiTfNyr55kwJPWbgxB5) · [Coding with John — Java tutorials (playlist)](https://www.youtube.com/playlist?list=PLkeaG1zpPTHhXOfy-mFbdqd1Zz4GnjcpC) | [Concept && Coding — Java Basics to Advanced (playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c63f469AyV78np0rbxRFppkx) · [CodeWithHarry — Java Tutorials in Hindi (playlist)](https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q) |
| Java 8 streams / functional | [Defog Tech — Java 8 (playlist)](https://www.youtube.com/playlist?list=PLhfHPmPYPPRmwlUqOv4eDhMOF6IUXCWDJ) | [Engineering Digest — Java 8 full course in Hindi (playlist)](https://www.youtube.com/playlist?list=PLA3GkZPtsafZR6arC1A3N0i968gk9RvMv) |
| Concurrency | [Defog Tech — Java Concurrency (playlist)](https://www.youtube.com/playlist?list=PLhfHPmPYPPRk6yMrcbfafFGSbE2EPK_A6) · [Java Brains — Java Concurrency (playlist)](https://www.youtube.com/playlist?list=PLqq-6Pq4lTTY8JY-DwAfoMiIZWHt2FKVX) | [Engineering Digest — Java Multithreading Masterclass (playlist)](https://www.youtube.com/playlist?list=PLA3GkZPtsafYhmrZR_1nmQqfFSnkftOud) |
| Modern Java (21 → 25) | [Java — Road to 25 (playlist)](https://www.youtube.com/playlist?list=PLX8CzqL3ArzXJ2_0FIGleUisXuUm4AESE) | — |
| Spring Boot | [Telusko — Spring 6 and Spring Boot (playlist)](https://www.youtube.com/playlist?list=PLsyeobzWxl7qbKoSgR5ub6jolI8-ocxCF) · [Amigoscode — Spring Boot full course](https://www.youtube.com/watch?v=9SGDpanrc8U) · [Dan Vega — Spring Boot 4 (playlist)](https://www.youtube.com/playlist?list=PLZV0a2jwt22v874ngZcWw3umP2yfsV9sK) | [Engineering Digest — Spring Boot Mastery (playlist)](https://www.youtube.com/playlist?list=PLA3GkZPtsafacdBLdd3p1DyRd5FGfr3Ue) · [Concept && Coding — Spring Boot Basics to Advanced (playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c60g6_fcjDCLHSx1LBeVYqyZ) |
| JPA / Hibernate | [Java Brains — JPA and Hibernate Essentials (playlist)](https://www.youtube.com/playlist?list=PLqq-6Pq4lTTb3J4IxKEg80LFTUbzm2p7V) | (Concept && Coding Spring Boot playlist above has JPA parts) |
| Testing | [Coding with John — JUnit tutorial](https://www.youtube.com/watch?v=vZm0lHciFsQ) | [Concept && Coding — JUnit 5 and Mockito (playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c61_unqN5bY0kYp65Dt_Sm3c) |
| Spring Security | [Java Brains — Spring Security Basics (playlist)](https://www.youtube.com/playlist?list=PLqq-6Pq4lTTYTEooakHchTGglSvkZAjnE) | [Engineering Digest — JWT auth in Spring Boot](https://www.youtube.com/watch?v=qvAoUVXgpZg) |
| Microservices | [Telusko — Microservices tutorial (playlist)](https://www.youtube.com/playlist?list=PLsyeobzWxl7rRyGcqgZ3MP5pWGPwUvprI) · [Daily Code Buffer — Microservices with Spring Boot](https://www.youtube.com/watch?v=HFl2dzhVuUo) | [Concept && Coding — Distributed Microservices (playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c60yO3LbjYkpKikwgAZHAT5o) |
| Kafka | [Confluent — Kafka 101 (playlist)](https://www.youtube.com/playlist?list=PLa7VYi0yPIH0KbnJQcMv5N9iW8HkZHztH) · [Confluent — Spring for Apache Kafka 101 (playlist)](https://www.youtube.com/playlist?list=PLa7VYi0yPIH1Su3nVNuRePh2Gdw6_UujU) | [Engineering Digest — Kafka for beginners (playlist)](https://www.youtube.com/playlist?list=PLA3GkZPtsafbAjKYkhWnD6GdhRtm6JrD1) · [Concept && Coding — Event-driven architecture with Kafka (playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c62YCR2kkE-0tg3-y1QwaIWk) |
| Docker | [TechWorld with Nana — Docker full course](https://www.youtube.com/watch?v=3c-iBn73dDE) · [Telusko — Docker for Java developers (playlist)](https://www.youtube.com/playlist?list=PLsyeobzWxl7r566kReuTnjnINHqaRuRFn) | [Abhishek Veeramalla — Docker (playlist)](https://www.youtube.com/playlist?list=PLdpzxOOAlwvLjb0vTD9BXLOwwLD_GWCmC) (Indian-English) |
| Kubernetes & Helm | [TechWorld with Nana — Kubernetes full course](https://www.youtube.com/watch?v=X48VuDVv0do) | [Abhishek Veeramalla — Kubernetes (playlist)](https://www.youtube.com/playlist?list=PLdpzxOOAlwvJdsW6A0jCz_3VaANuFMLpc) · [Gateway API](https://www.youtube.com/watch?v=EG27AzlHolU) · [Helm](https://www.youtube.com/watch?v=7A5cH8iqgHU) |
| CI/CD & DevSecOps | [TechWorld with Nana — GitHub Actions](https://www.youtube.com/watch?v=R8_veQiYBjI) · [DevSecOps pipeline](https://www.youtube.com/watch?v=gLJdrXPn0ns) | [Abhishek Veeramalla — DevOps Zero to Hero (playlist)](https://www.youtube.com/playlist?list=PLdpzxOOAlwvIKMhk8WhzN1pYoJ1YU8Csa) |
| Observability | [Dan Vega — Spring Boot 4 OpenTelemetry](https://www.youtube.com/watch?v=6_Y41z7OIv8) | [Abhishek Veeramalla — Observability Zero to Hero (playlist)](https://www.youtube.com/playlist?list=PLdpzxOOAlwvJUIfwmmVDoPYqXXUNbdBmb) |
| Databases | [Hussein Nasser — Database Engineering (playlist)](https://www.youtube.com/playlist?list=PLQnljOFTspQXjD0HOzN7P2tgzu7scWpl2) · [techTFQ — SQL window functions](https://www.youtube.com/watch?v=Ww71knvhQ-s) | — |
| Spring AI (to read the AI track's `ticketverse-ai`; Java W27 integrates it) | [Dan Vega — Spring AI (playlist)](https://www.youtube.com/playlist?list=PLZV0a2jwt22uoDm3LNDFvN6i2cAVU_HTH) · [Telusko — Spring AI tutorial (playlist)](https://www.youtube.com/playlist?list=PLsyeobzWxl7qJSZcMaN18c5l-k2n1FWHx) | [Concept && Coding — Spring AI Basics to Advanced (playlist)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c602ytEt7f_qVtlV7jNkdabL) |

---

## 5. Practice & labs

| Where | What | When |
|---|---|---|
| [Exercism — Java track](https://exercism.org/tracks/java) | Small graded exercises with mentoring — great for "write from scratch" warm-ups | W1–W7 |
| [CodingBat — Java](https://codingbat.com/java) | 5-minute logic/string/array warm-ups | W1–W3 |
| [Learn Git Branching](https://learngitbranching.js.org/) | Interactive branching/rebase practice | W7 |
| [regex101](https://regex101.com/) | Test regular expressions (Java flavor) before coding them | W10 |
| [LeetCode — SQL 50](https://leetcode.com/studyplan/top-sql-50/) · [PostgreSQL Exercises](https://pgexercises.com/) · [SQLBolt](https://sqlbolt.com/) | SQL interview drills | W14, W30 |
| [Testcontainers — Getting started for Java](https://testcontainers.com/guides/getting-started-with-testcontainers-for-java/) | Integration tests with real services | W11+ |
| [Killercoda — Kubernetes playground](https://killercoda.com/playgrounds/scenario/kubernetes) · [GitHub Codespaces](https://docs.github.com/en/codespaces/quickstart) | Browser Kubernetes for plain manifests; a 4-core Codespace (kind + your GHCR images) if kind is not yet approved on the laptop | W23–W24 |
| [Grafana k6 docs](https://grafana.com/docs/k6/latest/) | Load-testing scripts | W29 |
| [Tech Interview Handbook — Behavioral](https://www.techinterviewhandbook.org/behavioral-interview/) · [Pramp](https://www.pramp.com/) | STAR stories and free peer mock interviews | W30 |

---

## 6. Tools to install (with versions)

| Tool | Version (Oct 2026) | Install / notes | When |
|---|---|---|---|
| JDK | **Amazon Corretto 25 (LTS)** — from your company's software catalogue | [Corretto 25 guide](https://docs.aws.amazon.com/corretto/latest/corretto-25-ug/what-is-corretto-25.html) — use it **per project** (IntelliJ project SDK / per-window `JAVA_HOME`, Section 5 of `03_SETUP_YOUR_LAPTOP.md`) so work stays on JDK 11. Any Java SE 25 build behaves the same (Docker images and CI use Temurin 25). JDK 27 is the latest feature release but stay on LTS | W1 |
| IDE | **IntelliJ IDEA 2026.x** (free unified edition; Community Edition was merged in 2025.3) | [Download](https://www.jetbrains.com/idea/download/) · [why it changed](https://blog.jetbrains.com/idea/2025/12/intellij-idea-unified-release/) | W1 |
| Build | **Maven 3.9.x / 3.10.x** via the Maven Wrapper (`./mvnw`) in each repo; Maven 4 is still a release candidate — not the default | [Maven download](https://maven.apache.org/download.cgi) · [Maven Wrapper](https://maven.apache.org/tools/wrapper/) | W1, W7 |
| VCS | **Git 2.x** + your personal GitHub over HTTPS (personal repos live in `C:\dev\personal`; SSH port 22 is blocked on the corporate network) | [Git downloads](https://git-scm.com/downloads) · Section 6 of `03_SETUP_YOUR_LAPTOP.md` | W1 |
| Containers | **Docker, installed by IT** (whichever desktop runtime they provide); images come through the company's Docker mirror in JFrog — keep the prefix in a git-ignored `.env` and `~/.testcontainers.properties`, never in a repo. Fallback: a GitHub Codespace (Docker preinstalled) | [Docker: Get started](https://docs.docker.com/get-started/) · [GitHub Codespaces quickstart](https://docs.github.com/en/codespaces/quickstart) | W11 |
| Databases & infra images | `eclipse-temurin:25-jre`, `postgres:18`, `redis:8`, `apache/kafka:4.4.0` (KRaft), `keycloak/keycloak` (current), Prometheus, Grafana, Jaeger v2 | via Docker Compose, pulled through the company's Docker mirror | W11–W22 |
| JVM tools | JDK built-ins first: `jcmd`, `jstack`, `jfr` (ship with Corretto 25). JDK Mission Control 9.x, VisualVM 2.x and Eclipse MAT only once IT approves them; async-profiler runs inside the Linux container (no Windows build) | [JMC (Adoptium)](https://adoptium.net/jmc/) · [VisualVM](https://visualvm.github.io/) · [Eclipse MAT](https://eclipse.dev/mat/) · [async-profiler](https://github.com/async-profiler/async-profiler) | W11, W29 |
| HTTP clients | IntelliJ HTTP Client (built-in), Postman or HTTPie | [IntelliJ HTTP Client](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html) · [Postman](https://www.postman.com/downloads/) · [HTTPie](https://httpie.io/cli) | W13 |
| Kubernetes | kubectl (match your cluster), **kind**, **Helm 4.x** — requested from IT for W23 (incl. registry.k8s.io images); fallback: a 4-core Codespace, Azure Cloud Shell or Killercoda | [Install tools](https://kubernetes.io/docs/tasks/tools/) · [kind](https://kind.sigs.k8s.io/docs/user/quick-start/) · [Helm install](https://helm.sh/docs/intro/install/) | W23 |
| Security scan | Trivy (latest) and gitleaks, both run as containers (`aquasec/trivy`, `zricethezav/gitleaks`); if Trivy's database download fails behind the corporate proxy, scan in a Codespace | [Trivy getting started](https://trivy.dev/docs/latest/getting-started/) · [gitleaks](https://github.com/gitleaks/gitleaks) | W22, W26 |
| Load test | Grafana k6 (latest), run as the `grafana/k6` container | [k6 docs](https://grafana.com/docs/k6/latest/) | W29 |
| Cloud | Azure CLI 2.x (+ Bicep); personal-account work on the personal laptop or in a Codespace | [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) · [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview) | W26–W28 |
| AI service | None to install: the AI track's `ticketverse-ai` runs in a 4-core Codespace (free LLM APIs are blocked on the company network) | see the AI track's README | W27–W28 |

**Library versions (let the Spring Boot BOM manage them — don't pin patch versions by hand):**

| Managed by Spring Boot 4.1.x | Added separately |
|---|---|
| Spring Framework 7.0.x · Spring Security 7.1.x · Hibernate ORM 7.4 · **Jackson 3.x** (`tools.jackson` packages; a Jackson 2 BOM is kept for compatibility) · Flyway 12 (`spring-boot-starter-flyway`) · Micrometer 1.17 · Spring for Apache Kafka 4.1.x · kafka-clients 4.2.x · **JUnit 6** (Jupiter — same API as JUnit 5) · Mockito 5.2x · **Testcontainers 2.0.x** · AssertJ | Spring Cloud **2025.1.x** (matches Boot 4.1: Gateway Server Web MVC, Contract, CircuitBreaker — pick it on [start.spring.io](https://start.spring.io/)) · Resilience4j 2.4.x (`resilience4j-spring-boot4`) · springdoc-openapi 3.x · ArchUnit 1.5.x (W18) · Jib Maven plugin 3.5.x (W22) · Spring AI 2.0.x (BOM) only inside the AI track's `ticketverse-ai` · LangChain4j 1.x (awareness) |
