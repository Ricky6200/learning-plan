# ☕ Java Backend · Week 10 — JVM internals and GC, then Spring Core

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** GC, memory-leak and Spring IoC questions appear in every SDE-2 loop; knowing what happens under `@Autowired` makes Spring Boot debuggable instead of magic.

## 🗓️ Sessions

### Monday 28 Dec · 60 min — Class loading, delegation, runtime data areas, JIT
- 📚 **Learn:** Loading, linking (verify, prepare, resolve) and initialization; bootstrap/platform/application loaders and parent delegation; heap, metaspace, thread stacks/frames, PC register, code cache; interpreter + C1/C2 tiered JIT, inlining, escape analysis. [Baeldung: Class loaders](https://www.baeldung.com/java-classloaders), [Baeldung: JVM run-time data areas](https://www.baeldung.com/java-jvm-run-time-data-areas), [JVMS ch. 5: Loading, linking, initializing](https://docs.oracle.com/javase/specs/jvms/se25/html/jvms-5.html).
- 🛠️ **Do:** Print the loader chain for your class, `String` and `java.sql.Connection`; write a custom `ClassLoader` that loads a `.class` from a folder and show two loaders produce two different `Class` objects. Trigger `StackOverflowError` and compare recursion depth with `-Xss256k` vs `-Xss2m`; count classes with `-Xlog:class+load`. Done when: notes explain every output.

### Tuesday 29 Dec · 60 min — GC: roots, generations, G1, generational ZGC, stop-the-world
- 📚 **Learn:** Reachability and GC roots; mark-sweep-compact; generational hypothesis (eden, survivor, old); minor vs full GC; stop-the-world pauses; Serial, Parallel, G1 (default, region-based, pause goal), ZGC (generational by default since JDK 23); GC logging with `-Xlog:gc*`. [dev.java: GC in Java](https://dev.java/learn/jvm/tool/garbage-collection/java-specifics/), [Oracle: G1 collector (JDK 25)](https://docs.oracle.com/en/java/javase/25/gctuning/garbage-first-g1-garbage-collector1.html), [Concept && Coding: Memory and GC (Hindi video)](https://www.youtube.com/watch?v=vz6vSZRuS2M).
- 🛠️ **Do:** Write `Allocator` creating short-lived and long-lived objects; run it with `-Xmx256m -Xlog:gc` under G1, then `-XX:+UseZGC`, then `-XX:+UseParallelGC`; compare pause times and GC counts in a table. Explain one G1 log line field by field. Done when: the table and annotated log are in `notes/gc.md`.

### Wednesday 30 Dec · 60 min — Memory leaks, OOM types, heap-dump and JFR lab
- 📚 **Learn:** Leak patterns (static collections, unbounded caches, listeners, ThreadLocal in pools, inner-class references); OOM types (Java heap space, GC overhead limit, Metaspace, unable to create native thread, direct buffer); tools: `jcmd`, `jmap`, `jstack`, `-XX:+HeapDumpOnOutOfMemoryError`, VisualVM/Eclipse MAT, JFR + JMC. [Baeldung: Memory leaks](https://www.baeldung.com/java-memory-leaks), [Oracle: Troubleshoot memory leaks](https://docs.oracle.com/en/java/javase/25/troubleshoot/troubleshooting-memory-leaks.html), [dev.java: jcmd](https://dev.java/learn/jvm/monitoring-troubleshooting/troubleshooting/jcmd/).
- 🛠️ **Do:** Write `LeakyCache` (static HashMap growing per simulated request); run with `-Xmx128m -XX:+HeapDumpOnOutOfMemoryError`; open the `.hprof` in VisualVM or Eclipse MAT and find the dominator; record a JFR (`jcmd <pid> JFR.start duration=60s filename=leak.jfr`) and inspect allocations. Fix with your W5 LRU cache. Done when: a dominator screenshot is saved and the fixed app runs 5 minutes without OOM.

### Thursday 31 Dec · 60 min — Spring Core: IoC, ApplicationContext, bean definitions, DI
- 📚 **Learn:** IoC vs DI; BeanFactory vs ApplicationContext; bean definitions (class, scope, dependencies); component scanning vs `@Configuration` + `@Bean`; constructor vs setter vs field injection and why constructor injection wins (immutability, required deps, easy tests); circular dependencies. [Spring: IoC container introduction](https://docs.spring.io/spring-framework/reference/core/beans/introduction.html), [Spring: Dependency injection](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html), [Martin Fowler: IoC and DI](https://martinfowler.com/articles/injection.html).
- 🛠️ **Do:** New module `spring-core-lab` (spring-context 7.x, no Boot): wire `NotificationService` -> `MessageFormatter` + `Sender` (Email, Sms) first by hand with `new`, then via `AnnotationConfigApplicationContext` + `@ComponentScan` using constructor injection; print `getBeanDefinitionNames()`. Create a constructor circular dependency and read the error. Done when: both wirings print identical output and the error is explained in a comment.

### Friday 01 Jan · 60 min — Bean scopes, lifecycle, BeanPostProcessor, @Qualifier/@Primary, profiles
- 📚 **Learn:** Singleton vs prototype (and web scopes); prototype-into-singleton fix with `ObjectProvider`; lifecycle: instantiate -> populate -> Aware -> BPP before -> `@PostConstruct` -> BPP after (where proxies are made) -> ready -> `@PreDestroy`; `@Primary`, `@Qualifier`; profiles. [Spring: Bean scopes](https://docs.spring.io/spring-framework/reference/core/beans/factory-scopes.html), [Spring: Lifecycle callbacks](https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html), [Baeldung: BeanPostProcessor](https://www.baeldung.com/spring-beanpostprocessor).
- 🛠️ **Do:** Add `LifecycleLoggerBean` (BeanNameAware, InitializingBean, DisposableBean, `@PostConstruct`, `@PreDestroy`) and a `TimingBeanPostProcessor` logging before/after init for every bean; show prototype vs singleton identity; resolve two `Sender` beans with `@Primary` and `@Qualifier("sms")`; switch senders with `dev`/`prod` profiles. Done when: the console shows the full lifecycle order for one bean.

### Saturday 02 Jan · 60 min — BUILD: Spring Core app without Boot; Postgres in Docker
- 📚 **Learn:** `@Configuration` + `@Bean` (full vs lite mode), `@PropertySource` + `Environment`, `@Profile`, graceful `context.close()`. Then install a container runtime: Docker Desktop is free only for small companies/personal use, so on a corporate laptop use a licensed seat or Rancher/Podman Desktop. [Spring: @Bean and @Configuration](https://docs.spring.io/spring-framework/reference/core/beans/java/basic-concepts.html), [Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/), [Rancher Desktop](https://rancherdesktop.io/).
- 🛠️ **Do:** Build `OrderPipeline` in `spring-core-lab`: `OrderService` -> `PricingService` (strategy chosen by profile), `InventoryService`, `AuditLogger`; timing via your BPP; config from `app.properties`; print lifecycle on start and close. Install Docker/Rancher and run `docker run --name pg -e POSTGRES_PASSWORD=pg -p 5432:5432 -d postgres:18`. Done when: the app runs under both profiles and `select version();` works against the container.

## 📦 Deliverable (by Saturday night)
`w10` JVM notes (class loading, GC table, heap-dump screenshot, JFR) + `spring-core-lab` module (DI, scopes, lifecycle, BPP, profiles, OrderPipeline); Docker/Rancher + Postgres container working.

## ✅ Self-check (Sunday test preview)
- Explain parent-delegation in class loading. Why does it matter for security?
- What lives on the stack vs the heap vs metaspace?
- What are GC roots? Minor vs full GC? Why is G1 the default and when would you pick ZGC?
- Name four OutOfMemoryError types with a likely cause for each. How do you analyse a heap dump?
- BeanFactory vs ApplicationContext; why is constructor injection preferred?
- List the Spring bean lifecycle steps in order. Where are AOP proxies created?
- How do you correctly inject a prototype bean into a singleton?

## 🚀 Stretch (optional)
Run TripPlanner (W9) with JFR and explore the threads and CPU views in [JDK Mission Control](https://adoptium.net/jmc/).
