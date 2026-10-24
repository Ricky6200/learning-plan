# ☕ Java Backend · Week 07 — Modern Java 9 to 25, Maven, Git

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** Interviewers now ask about records, sealed types, pattern matching and virtual threads; modern syntax makes code shorter and safer, and Maven/Git fluency is daily work.

## 🗓️ Sessions

### Monday 07 Dec · 60 min — var, records, text blocks, switch expressions
- 📚 **Learn:** `var` rules (locals only, needs an initializer); records: canonical and compact constructors, generated accessors/equals/hashCode/toString, implementing interfaces, static factories; text blocks; switch expressions with arrows and `yield`. [Oracle: Record classes](https://docs.oracle.com/en/java/javase/25/language/records.html), [Oracle: Switch expressions](https://docs.oracle.com/en/java/javase/25/language/switch-expressions-statements.html), [Java channel: Features since 21 (video)](https://www.youtube.com/watch?v=X0-TGhktFnE).
- 🛠️ **Do:** Convert `Money`, `Employee` and `Loan` from earlier weeks into records with compact-constructor validation; write a text-block JSON template; rewrite a 6-branch if/else chain as a switch expression that uses `yield` once. Done when: the old tests pass again after switching getters to record accessors.

### Tuesday 08 Dec · 60 min — Sealed types, pattern matching, record patterns, unnamed _
- 📚 **Learn:** Sealed classes/interfaces with `permits`; exhaustive switch without `default`; type patterns and `when` guards; nested record deconstruction patterns; unnamed variables and patterns `_` (JDK 22); data-oriented programming style. [Oracle: Sealed classes](https://docs.oracle.com/en/java/javase/25/language/sealed-classes-interfaces.html), [Oracle: Pattern matching for switch](https://docs.oracle.com/en/java/javase/25/language/pattern-matching-switch.html), [Oracle: Record patterns](https://docs.oracle.com/en/java/javase/25/language/record-patterns.html).
- 🛠️ **Do:** Model `sealed interface Shape permits Circle, Rect, Triangle` and `sealed interface PaymentResult` (Success, Declined, Failed) as records. Write `area(Shape)` and `describe(PaymentResult)` with exhaustive switches, a `when` guard (amount > 10000), a nested record pattern and `_` for unused parts. Add a 4th shape and read the compiler error. Done when: no `default` branch exists and the new type forces an update.

### Wednesday 09 Dec · 60 min — JDK 21-25: virtual threads intro, gatherers, JDK 25 finals
- 📚 **Learn:** Virtual threads (`Thread.ofVirtual()`, `Executors.newVirtualThreadPerTaskExecutor()`), stream gatherers (JDK 24), JDK 25 final features: compact source files + instance `main`, flexible constructor bodies, module import declarations, scoped values. [JDK 25 feature list](https://openjdk.org/projects/jdk/25/), [JEP 512: Compact source files](https://openjdk.org/jeps/512), [JEP 513: Flexible constructor bodies](https://openjdk.org/jeps/513).
- 🛠️ **Do:** Write `Hello25.java` as a compact source file with `void main()` and run it with `java Hello25.java`; use `import module java.base;`; validate arguments before `super(...)` in a subclass constructor; start 10,000 virtual threads that sleep 100 ms and time it vs a 100-thread fixed pool; use `Gatherers.windowFixed(3)`. Done when: all 5 snippets run on JDK 25 and timings are noted.

### Thursday 10 Dec · 60 min — java.time and the java.net.http HttpClient
- 📚 **Learn:** `LocalDate`, `LocalDateTime`, `ZonedDateTime`, `Instant`; `Duration` vs `Period`; `DateTimeFormatter`; IST vs UTC; inject a `Clock` for testable time; `HttpClient`: builder, timeouts, `send` vs `sendAsync`, body handlers. [dev.java: Date-Time API overview](https://dev.java/learn/api/date-time-regex/date-time/intro/), [Baeldung: Java HttpClient](https://www.baeldung.com/java-9-http-client).
- 🛠️ **Do:** Write `ShowTimeUtil`: convert a 19:30 IST show to UTC and New York time, minutes until the show, next 7 show dates skipping Mondays; test it with a fixed `Clock`. Then call `https://jsonplaceholder.typicode.com/todos/1` with HttpClient (5 s timeout) synchronously, and fetch todos 2-5 in parallel with `sendAsync` + `allOf`; print each title. Done when: time tests pass and all 5 titles print.

### Friday 11 Dec · 60 min — Maven deeper: lifecycle, scopes, BOM, multi-module, wrapper
- 📚 **Learn:** Lifecycle phases (validate -> compile -> test -> package -> verify -> install -> deploy), plugins and goals, dependency scopes (compile/provided/runtime/test), transitive dependencies and `dependency:tree`, `dependencyManagement` with BOM import, parent/aggregator POMs, Maven Wrapper. [Maven: Build lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html), [Maven: Dependency mechanism](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html), [Baeldung: Multi-module project](https://www.baeldung.com/maven-multi-module).
- 🛠️ **Do:** Turn `java-mastery` into a parent POM with modules `core-basics` (W1-W6) and `modern-java` (W7); import the JUnit BOM in the parent `dependencyManagement`; add the Maven Wrapper; run `./mvnw -q verify` and `./mvnw dependency:tree`. Done when: `mvnw verify` at the root builds both modules and all earlier tests still pass.

### Saturday 12 Dec · 60 min — BUILD: Modernize old code via branch, rebase and PR
- 📚 **Learn:** Feature branches, small commits, `rebase -i` to squash, resolving conflicts, PR descriptions and self-review; modernization checklist: records, sealed results, switch patterns, `var` where it helps readability, `List.copyOf`. [Git Book: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing), [GitHub Docs: Pull requests](https://docs.github.com/en/pull-requests/reference/pull-requests), [Learn Git Branching](https://learngitbranching.js.org/).
- 🛠️ **Do:** On branch `modernize`, refactor the W2 bank and W4 library to records, a sealed `TransferResult`, switch patterns and immutable collections. Create a deliberate conflict on `main` and resolve it with a rebase; squash to 3 meaningful commits; open a PR with a before/after table and merge it. Done when: the PR is merged, `mvnw verify` is green, and you can explain merge vs rebase.

## 📦 Deliverable (by Saturday night)
`java-mastery` as a multi-module Maven build with wrapper; `modern-java` module with records/sealed/patterns/JDK 25 demos, ShowTimeUtil + HttpClient; merged modernization PR.

## ✅ Self-check (Sunday test preview)
- What does a record generate? Can a record declare instance fields or extend a class?
- What problem do sealed types solve, and how do they make switch exhaustive?
- Explain record patterns and `when` guards with a short example.
- What problem do virtual threads solve, and when do they not help?
- Duration vs Period; Instant vs LocalDateTime vs ZonedDateTime: when do you use each?
- Explain Maven dependency scopes. What is a BOM and why import it?
- Merge vs rebase: when should you avoid rebasing?

## 🚀 Stretch (optional)
Skim [Java language changes by release](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-release.html) and make a one-page Java 9-to-25 cheat sheet.
