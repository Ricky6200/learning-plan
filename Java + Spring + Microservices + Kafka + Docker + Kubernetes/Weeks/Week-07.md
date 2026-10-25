# ☕ Java Backend · Week 07 — Modern Java 9 to 25, Maven, Git

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** Interviewers now ask about records, sealed types, pattern matching and modules; modern syntax makes code shorter and safer, and Maven/Git fluency is daily work.

## 🗓️ Sessions

### Monday 07 Dec · 60 min — var, records, switch expressions; record vs Python dataclass
- 📚 **Learn:** `var` rules (locals only, needs an initializer); records: canonical and compact constructors, generated accessors/equals/hashCode/toString, implementing interfaces, static factories; switch expressions with arrows and `yield`. Bridge: a record is close to the Python `@dataclass(frozen=True)` from your AI W2 Mon. Read: [Oracle: Record classes](https://docs.oracle.com/en/java/javase/25/language/records.html). Optional: [Oracle: Switch expressions](https://docs.oracle.com/en/java/javase/25/language/switch-expressions-statements.html).
- 🛠️ **Do:** Convert `Money`, `Employee` and `Loan` from earlier weeks into records with compact-constructor validation; rewrite a 6-branch if/else chain as a switch expression that uses `yield` once. Bridge: write `Money` as a Python `@dataclass(frozen=True)` with validation in `__post_init__` and note 3 differences (validation hook, what happens on assignment, what `==` compares). Done when: the old tests pass again after switching getters to record accessors and the 3 differences are in a comment.

### Tuesday 08 Dec · 60 min — Sealed types, pattern matching, record patterns, unnamed _
- 📚 **Learn:** Sealed classes/interfaces with `permits`; exhaustive switch without `default`; type patterns and `when` guards; nested record deconstruction patterns; unnamed variables and patterns `_` (JDK 22); data-oriented programming style. Read: [Oracle: Pattern matching for switch](https://docs.oracle.com/en/java/javase/25/language/pattern-matching-switch.html). Optional: [Oracle: Sealed classes](https://docs.oracle.com/en/java/javase/25/language/sealed-classes-interfaces.html).
- 🛠️ **Do:** Model `sealed interface Shape permits Circle, Rect, Triangle` and `sealed interface PaymentResult` (Success, Declined, Failed) as records. Write `area(Shape)` and `describe(PaymentResult)` with exhaustive switches, a `when` guard (amount > 10000), a nested record pattern and `_` for unused parts. Add a 4th shape and read the compiler error. Done when: no `default` branch exists and the new type forces an update.

### Wednesday 09 Dec · 60 min — JPMS modules and Java 11-25 API additions
- 📚 **Learn:** JPMS: `module-info.java` with `requires` and `exports`; unexported packages are invisible (strong encapsulation); module path vs classpath (most Spring apps still use the classpath). Daily API additions: String `isBlank/strip/lines/repeat` and `Files.readString/writeString` (11), `Stream.toList()` (16), `HexFormat` (17), `Math.clamp` (21); JDK 25 compact source files with an instance `void main()`. Read: [dev.java: Modules](https://dev.java/learn/modules/) (intro, about 15 min). Optional: [Java Version Almanac](https://javaalmanac.io/).
- 🛠️ **Do:** With plain `javac`/`java` (no Maven): module `inventory.api` exports `com.inv.api` but not `com.inv.internal`; module `inventory.app` requires it; use a class from the internal package and save the compile error. Then `Java11to25Tour`: 6 one-liners (`isBlank`, `strip`, `lines().count()`, `repeat`, `Files.writeString/readString`, `Stream.toList()`), plus a compact `Hello25.java` with `void main()` run as `java Hello25.java`. Done when: the encapsulation error is captured and every one-liner prints the value you predicted.

### Thursday 10 Dec · 60 min — java.time and a synchronous HttpClient call
- 📚 **Learn:** `LocalDate`, `LocalDateTime`, `ZonedDateTime`, `Instant`; `Duration` vs `Period`; `DateTimeFormatter`; IST vs UTC; inject a `Clock` for testable time; `HttpClient`: builder, connect timeout, `send` with `BodyHandlers.ofString()`. On the company laptop a `PKIX path building failed` error means Java does not trust the corporate proxy's certificate: add the VM option `-Djavax.net.ssl.trustStoreType=Windows-ROOT` (setup guide Section 5). Read: [dev.java: Date-Time API overview](https://dev.java/learn/api/date-time-regex/date-time/intro/). Optional: [Baeldung: Java HttpClient](https://www.baeldung.com/java-9-http-client).
- 🛠️ **Do:** Write `ShowTimeUtil`: convert a 19:30 IST show to UTC and New York time, minutes until the show, the next 7 show dates skipping Mondays; test it with a fixed `Clock`. Then call `https://jsonplaceholder.typicode.com/todos/1` synchronously with `HttpClient` (5 s timeout) and print the title. Done when: the time tests pass and the title prints (parallel `sendAsync` calls come in W9).

### Friday 11 Dec · 60 min — Maven deeper: lifecycle, scopes, BOM, multi-module, wrapper
- 📚 **Learn:** Lifecycle phases (validate -> compile -> test -> package -> verify -> install -> deploy), plugins and goals, dependency scopes (compile/provided/runtime/test), transitive dependencies and `dependency:tree`, `dependencyManagement` with BOM import, parent/aggregator POMs, Maven Wrapper. Gradle is the other big build tool (Kotlin or Groovy DSL, same ideas). Read: [Maven: Build lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html). Optional: [Baeldung: Multi-module project](https://www.baeldung.com/maven-multi-module).
- 🛠️ **Do:** Turn `java-mastery` into a parent POM with modules `core-basics` (W1-W6) and `modern-java` (W7); import the JUnit BOM in the parent `dependencyManagement`; add the Maven Wrapper; run `./mvnw -q verify` and `./mvnw dependency:tree`. Done when: `mvnw verify` at the root builds both modules and all earlier tests still pass.

### Saturday 12 Dec · 60 min — BUILD: Git workflow: branch, conflict, rebase, PR, recovery
- 📚 **Learn:** Feature branches, small commits, `rebase -i` to squash, resolving conflicts, PR descriptions and self-review; recovery tools: `git restore`, `git revert`, and `git reflog` to find 'lost' commits. Read: [Learn Git Branching](https://learngitbranching.js.org/) (Main levels 1-4, about 15 min). Optional: [Git Book: Rebasing](https://git-scm.com/book/en/v2/Git-Branching-Rebasing).
- 🛠️ **Do:** On branch `modernize`, make two small refactors (the W2 bank's `Transaction` becomes a record; `transfer` returns a sealed `TransferResult`). Create a deliberate conflict on `main` and resolve it with a rebase; squash to 2 meaningful commits; open a PR with a before/after table and merge it. Then 'lose' a commit with `git reset --hard` and recover it via `git reflog`. Done when: the PR is merged, `mvnw verify` is green, and you can explain merge vs rebase.

## 📦 Deliverable (by Saturday night)
`java-mastery` as a multi-module Maven build with wrapper; `modern-java` module with records/sealed/patterns, a JPMS demo, the Java 11-25 API tour and ShowTimeUtil + a sync HttpClient call; a merged modernization PR and a recovered commit.

## ✅ Self-check (Sunday test preview)
- What does a record generate? Can a record declare instance fields or extend a class?
- How is a Java record similar to and different from a Python `@dataclass(frozen=True)`?
- What problem do sealed types solve, and how do they make switch exhaustive?
- Explain record patterns and `when` guards with a short example.
- What does `module-info.java` declare, and why do most Spring apps still run on the classpath?
- Duration vs Period; Instant vs LocalDateTime vs ZonedDateTime: when do you use each?
- Explain Maven dependency scopes. What is a BOM and why import it?
- Merge vs rebase: when should you avoid rebasing? How do you recover a commit after `reset --hard`?

## 🚀 Stretch (optional)
Skim [Java language changes by release](https://docs.oracle.com/en/java/javase/25/language/java-language-changes-release.html) and make a one-page Java 9-to-25 cheat sheet. Extras: a text-block JSON template; flexible constructor bodies ([JEP 513](https://openjdk.org/jeps/513)) to validate arguments before `super(...)`; `import module java.base;`; modernize the W4 library (records, immutable collections) on the same branch.
