# ☕ Java Backend · Week 12 — Spring Core: DI, lifecycle, AOP, async, logging

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** Spring IoC questions appear in every SDE-2 loop; knowing what happens under `@Autowired`, `@Async` and proxies (built from the reflection and annotations you used in W10) makes Spring Boot debuggable instead of magic.

## 🗓️ Sessions

### Monday 11 Jan · 60 min — Spring Core: IoC, ApplicationContext, bean definitions, DI
- 📚 **Learn:** IoC vs DI; BeanFactory vs ApplicationContext; bean definitions (class, scope, dependencies); component scanning vs `@Configuration` + `@Bean`; constructor vs setter vs field injection and why constructor injection wins (immutability, required deps, easy tests); circular dependencies. Spring does with reflection what your W10 MiniContainer did. Read: [Spring: IoC container introduction](https://docs.spring.io/spring-framework/reference/core/beans/introduction.html). Optional: [Martin Fowler: IoC and DI](https://martinfowler.com/articles/injection.html).
- 🛠️ **Do:** New module `spring-core-lab` (spring-context 7.x, no Boot): wire `NotificationService` -> `MessageFormatter` + `Sender` (Email, Sms) first by hand with `new`, then via `AnnotationConfigApplicationContext` + `@ComponentScan` using constructor injection; print `getBeanDefinitionNames()`. Create a constructor circular dependency and read the error. Done when: both wirings print identical output and the error is explained in a comment.

### Tuesday 12 Jan · 60 min — Bean scopes, lifecycle, BeanPostProcessor, @Qualifier/@Primary, profiles
- 📚 **Learn:** Singleton vs prototype (and web scopes); the prototype-into-singleton fix with `ObjectProvider`; lifecycle: instantiate -> populate -> Aware -> BPP before -> `@PostConstruct` -> BPP after (where proxies are made) -> ready -> `@PreDestroy`; `@Primary`, `@Qualifier`; profiles. Read: [Spring: Lifecycle callbacks](https://docs.spring.io/spring-framework/reference/core/beans/factory-nature.html). Optional: [Baeldung: BeanPostProcessor](https://www.baeldung.com/spring-beanpostprocessor).
- 🛠️ **Do:** Add `LifecycleLoggerBean` (BeanNameAware, InitializingBean, DisposableBean, `@PostConstruct`, `@PreDestroy`) and a `TimingBeanPostProcessor` logging before/after init for every bean; show prototype vs singleton identity; resolve two `Sender` beans with `@Primary` and `@Qualifier("sms")`; switch senders with `dev`/`prod` profiles. Done when: the console shows the full lifecycle order for one bean.

### Wednesday 13 Jan · 60 min — AOP and proxies: JDK vs CGLIB, self-invocation pitfall
- 📚 **Learn:** Aspect, advice, pointcut, join point; Spring AOP uses runtime proxies: JDK dynamic proxies when a bean has an interface, CGLIB subclasses otherwise (Spring Boot defaults to CGLIB); calling `this.method()` bypasses the proxy, so `@Transactional`, `@Async` and `@Cacheable` silently do nothing there; final/private methods are not advised. Read: [Spring: Proxying mechanisms](https://docs.spring.io/spring-framework/reference/core/aop/proxying.html). Optional: [Baeldung: Dynamic proxies](https://www.baeldung.com/java-dynamic-proxies).
- 🛠️ **Do:** Write a plain `java.lang.reflect.Proxy` that times any interface call (reflection from W10). In `spring-core-lab` add `spring-aspects`, `@EnableAspectJAutoProxy`, a custom `@Timed` annotation (RUNTIME, METHOD) and an `@Around` aspect; print a bean's `getClass()` with and without an interface to spot the proxy type; call a `@Timed` method via `this` from the same bean and observe no timing, then fix it by moving the method to another bean. Done when: both behaviours are visible in the console.

### Thursday 14 Jan · 60 min — @Async, @Scheduled, ThreadPoolTaskExecutor and Spring events
- 📚 **Learn:** `@EnableAsync` + `@Async` runs a method on a `TaskExecutor` (a `ThreadPoolTaskExecutor` bean: core, max, queue, thread-name prefix, as in W8 Fri) and may return a `CompletableFuture` (W9); `@EnableScheduling` + `@Scheduled(fixedDelay = 5000)` or `cron`; events: `ApplicationEventPublisher.publishEvent(...)` + `@EventListener`, synchronous by default, add `@Async` to decouple; `@Async` works only through the proxy (Wednesday). Read: [Spring: Task execution and scheduling](https://docs.spring.io/spring-framework/reference/integration/scheduling.html) (annotation support). Optional: [Baeldung: Spring events](https://www.baeldung.com/spring-events).
- 🛠️ **Do:** In `spring-core-lab`: `OrderService.place()` publishes `OrderPlaced`; an `@Async @EventListener` 'email' listener runs on a `ThreadPoolTaskExecutor` named `mail-` (core 2, max 4, queue 10); a `@Scheduled(fixedDelay = 5000)` job logs pending orders. Print thread names everywhere. Done when: the listener runs on `mail-` threads, `place()` returns before the email finishes, and the scheduled job fires every 5 s.

### Friday 15 Jan · 60 min — Logging with SLF4J and Logback; MDC correlation ids
- 📚 **Learn:** SLF4J is the logging API and Logback the implementation (Spring Boot's default); levels TRACE to ERROR; parameterized messages `log.info("order {} placed", id)` instead of string concatenation; MDC stores per-thread key-values printed with `%X{orderId}`; MDC is a ThreadLocal, so it is lost on `@Async` threads unless a `TaskDecorator` copies it. Read: [SLF4J manual](https://www.slf4j.org/manual.html) (about 10 min). Optional: [Baeldung: MDC with Logback](https://www.baeldung.com/mdc-in-log4j-2-logback).
- 🛠️ **Do:** Add `slf4j-api` + `logback-classic` and a `logback.xml` pattern with `%thread` and `%X{orderId}`; replace every `System.out` in `spring-core-lab`; put `orderId` into MDC inside `place()` and clear it in `finally`; show it is missing in the async email log, then fix it with a `TaskDecorator` on the executor. Done when: every log line for one order, sync and async, shows the same orderId.

### Saturday 16 Jan · 60 min — BUILD: Spring Core app without Boot + Postgres + Testcontainers
- 📚 **Learn:** `@Configuration` + `@Bean` (full vs lite mode), `@PropertySource` + `Environment`, `@Profile`, graceful `context.close()`; a `DataSource` bean (`DriverManagerDataSource`) and Spring's `JdbcClient` for one insert (primer: `jdbcClient.sql("insert into audit(order_id) values (?)").param(id).update()`; data access in depth in W14). Read: [Spring: @Bean and @Configuration](https://docs.spring.io/spring-framework/reference/core/beans/java/basic-concepts.html). Optional: [Testcontainers: Getting started for Java](https://testcontainers.com/guides/getting-started-with-testcontainers-for-java/).
- 🛠️ **Do:** Finish `OrderPipeline` in `spring-core-lab`: `OrderService` -> `PricingService` (strategy chosen by profile), `InventoryService`, `AuditLogger` writing one row per order to Postgres (your W11 Compose) via `JdbcClient`; the `@Timed` aspect, async email and MDC logs stay on; config from `app.properties`. Add a JUnit test that starts a `PostgreSQLContainer`, builds the context against it and asserts the audit row. Done when: the app runs under both profiles and the Testcontainers test is green.

## 📦 Deliverable (by Saturday night)
`spring-core-lab` module: DI by hand vs container, lifecycle + BPP logs, scopes/qualifiers/profiles, JDK proxy + `@Timed` aspect with the self-invocation demo, async events + scheduled job on a named pool, MDC logging with a TaskDecorator, OrderPipeline on Postgres with a Testcontainers test.

## ✅ Self-check (Sunday test preview)
- BeanFactory vs ApplicationContext; why is constructor injection preferred?
- List the Spring bean lifecycle steps in order. Where are AOP proxies created?
- How do you correctly inject a prototype bean into a singleton?
- JDK dynamic proxy vs CGLIB proxy: when is each used, and why does `this.method()` skip the aspect?
- What must be true for `@Async` to really run asynchronously, and which executor does it use?
- Spring events are synchronous by default: what does that mean for a slow listener?
- Why is MDC lost on async threads, and how does a TaskDecorator fix it?

## 🚀 Stretch (optional)
Read `AbstractAutowireCapableBeanFactory.initializeBean` in IntelliJ and map each line to the lifecycle steps. Extras: your own `@RetryOnce` annotation + aspect; read about `@TransactionalEventListener` (you will use it after transactions in W15).
