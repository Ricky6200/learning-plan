# ☕ Java Backend · Week 04 — Exceptions, generics, collections: Season 1 boss

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Exception design, PECS and fail-fast iterators are interview staples; together they turn toy code into production-grade Java.

## 🗓️ Sessions

### Monday 16 Nov · 60 min — Exception hierarchy, checked vs unchecked, try/catch/finally
- 📚 **Learn:** Throwable -> Error vs Exception -> RuntimeException; checked vs unchecked; catch order and multi-catch; finally semantics and the `return`-inside-finally pitfall; chaining causes; reading stack traces. Read: [dev.java: Exceptions](https://dev.java/learn/language/annotations-exceptions/exceptions/). Optional: [Coding with John: Exception handling (video)](https://www.youtube.com/watch?v=1XAfapkBQjk).
- 🛠️ **Do:** Write `ExceptionPuzzles` with 6 predict-then-run methods: finally overriding a return, exception in finally hiding the original, wrong catch order (compile error), multi-catch, rethrow with cause, `NumberFormatException`. Then write `parseAge(String)` throwing a custom checked `InvalidAgeException`. Done when: predictions are recorded and `parseAge` tests (valid, negative, non-numeric) pass.

### Tuesday 17 Nov · 60 min — try-with-resources, custom exceptions, best practices
- 📚 **Learn:** `AutoCloseable`; resources close in reverse order; suppressed exceptions; designing custom exceptions (unchecked domain exceptions in Spring apps, meaningful message, keep the cause); anti-patterns: swallowing, catching `Exception`, log-and-rethrow, exceptions as control flow. Read: [Oracle: try-with-resources](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html). Optional: [Baeldung: Custom exceptions](https://www.baeldung.com/java-new-custom-exception).
- 🛠️ **Do:** Write `DemoResource implements AutoCloseable` that logs open/close and can throw on close; use two in one try-with-resources, throw in the body and in `close()`, print `getSuppressed()`. Create `LibraryException` -> `ItemNotAvailableException`, `LoanLimitExceededException` and refactor the W3 library. Done when: the suppressed exception prints and W3 tests assert the new types.

### Wednesday 18 Nov · 60 min — Generics: generic classes, methods and bounded types
- 📚 **Learn:** Why generics (compile-time safety, no casts); generic classes and methods; inference and the diamond; bounded types `<T extends Comparable<T>>`; why raw types are dangerous. Primer: `Optional<T>` is a box that may be empty (`isPresent()`, `orElseThrow()`) and the usual return type of `findById`; full story in W6. Read: [Oracle: Generic methods](https://docs.oracle.com/javase/tutorial/java/generics/methods.html). Optional: [Coding with John: Generics (video)](https://www.youtube.com/watch?v=K1iu1kXkVoA).
- 🛠️ **Do:** From scratch: `Box<T>`, `static <T extends Comparable<T>> T max(List<T>)`, and `Repository<T, ID>` with `InMemoryRepository` (save, `findById` returning `Optional`, findAll, deleteById) for any `T extends Identifiable<ID>`. Write 6 tests. Done when: the same repository class stores both `Book` and `Member` with zero casts.

### Thursday 19 Nov · 60 min — Generics II: wildcards, PECS and type erasure
- 📚 **Learn:** `? extends T` = producer (read), `? super T` = consumer (write): PECS; unbounded `?`; why `List<Integer>` is not a `List<Number>`; type erasure: no `new T()`, no `instanceof List<String>`, no overloads differing only by type argument, bridge methods. Read: [Oracle: Wildcard guidelines](https://docs.oracle.com/javase/tutorial/java/generics/wildcardGuidelines.html). Optional: [dev.java: Type erasure](https://dev.java/learn/language/fp/generics/type-erasure/).
- 🛠️ **Do:** Write `copy(List<? super T> dst, List<? extends T> src)` and `sum(Collection<? extends Number>)`; trigger 3 intentional compile errors (add to `? extends`, two overloads `m(List<String>)`/`m(List<Integer>)`, `new T()`) and paste messages. Run `javap -c` on `Box` to see erased types. Done when: you explain PECS in two lines using your own code.

### Friday 20 Nov · 60 min — Collections, iterators, Comparator and a lambda-syntax primer
- 📚 **Learn:** List/Set/Queue/Deque/Map and choosing implementations; Iterator and `remove()`; fail-fast iterators (`modCount`, `ConcurrentModificationException`); Comparable (natural order) vs Comparator. 10-minute primer (full lambda week = W6): `(a, b) -> Integer.compare(a[0], b[0])` is a comparator written as a lambda; `Book::getAuthor` is a method reference; `Comparator.comparing(Book::getAuthor).thenComparing(Book::getYear).reversed()`; `list.removeIf(b -> b.getYear() < 2000)`; `optional.orElseThrow()`. Read: [Baeldung: Comparator and Comparable](https://www.baeldung.com/java-comparator-comparable). Optional: [Baeldung: Fail-fast vs fail-safe](https://www.baeldung.com/java-fail-safe-vs-fail-fast-iterator).
- 🛠️ **Do:** Reproduce `ConcurrentModificationException` by removing inside a for-each; fix it 3 ways (`Iterator.remove`, `removeIf` with a lambda, `CopyOnWriteArrayList`). Make `Book implements Comparable<Book>` by title, then sort by author ascending and year descending (`thenComparing(Book::getYear, Comparator.reverseOrder())`; a trailing `.reversed()` would flip the author order too), and sort an `int[][]` of intervals by start with `(a, b) -> Integer.compare(a[0], b[0])`. Done when: CME is fixed 3 ways and the sorting tests pass.

### Saturday 21 Nov · 60 min — BOSS BATTLE: Library Management System, 60 min timed
- 📚 **Learn:** Rules: 60-minute timer, fresh package `w04.boss`, docs allowed, no copy-paste or AI-generated code. Scope: OOP model + custom exceptions + generic `Repository<T, ID>` + collections + Comparator sorting + JUnit. Pass = all acceptance tests green inside 60 min. Reference: [Oracle: Collections trail](https://docs.oracle.com/javase/tutorial/collections/index.html). Optional: [Baeldung: Exception handling](https://www.baeldung.com/java-exceptions).
- 🛠️ **Do:** Console app: add book/member, borrow (max 3 per member), return, list available sorted by title, list a member's loans, search by author; generic in-memory repositories; clear checked/unchecked exception policy. Minimum 6 tests: borrow happy path, limit exceeded, double borrow, return unknown, sort order, search. Done when: `mvn test` is green within 60 min, a demo run shows every menu action, and the commit is tagged `boss-s1`.

## 📦 Deliverable (by Saturday night)
`w04` package with ExceptionPuzzles, generic repository, PECS demos, CME fixes, Comparator chains; Boss S1 Library Management System tagged `boss-s1` with tests green.

## ✅ Self-check (Sunday test preview)
- Checked vs unchecked exceptions: which would you use for a business rule violation in a Spring service, and why?
- In try-with-resources, what happens when both the body and close() throw?
- Explain PECS using the signature of `Collections.copy`.
- What is type erasure? Name two consequences you hit in real code.
- How do fail-fast iterators detect concurrent modification?
- How do you sort employees by department ascending, then salary descending?
- What does `(a, b) -> Integer.compare(a[0], b[0])` do, and where would you use it?
- Can you catch an Error? Should you? Name two Errors.

## 🚀 Stretch (optional)
Read the `java.util.Collections` Javadoc and list 5 utilities you will never hand-write again. Extras: a generic `Pair<K,V>`; pick the right collection for 5 written scenarios (LRU-ish recent list, unique tags, sorted leaderboard, task queue, undo stack) with one-line reasons.
