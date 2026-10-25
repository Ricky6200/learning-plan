# ☕ Java Backend · Week 06 — Functional Java: lambdas, streams, Optional drills

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** Stream coding questions (group, count, second-highest, frequency) appear in almost every Indian Java interview; fluency here also makes your Spring code shorter and clearer.

## 🗓️ Sessions

### Monday 30 Nov · 60 min — Lambdas, functional interfaces, method references
- 📚 **Learn:** Lambda syntax and effectively-final capture; `java.util.function` (Predicate, Function, Supplier, Consumer, BiFunction, UnaryOperator, BinaryOperator) and primitive specializations; composing with `andThen`, `compose`, `and`, `negate`; the 4 kinds of method references. Read: [dev.java: Lambda expressions](https://dev.java/learn/language/fp/lambdas/). Optional: [Coding with John: Lambdas (video)](https://www.youtube.com/watch?v=tj5sLSFjVj4).
- 🛠️ **Do:** Create immutable `w06.Employee` (id, name, dept, gender, salary, age, city, joinDate, skills) and `EmployeeData.list()` with 12 varied employees. Write your own `@FunctionalInterface TriFunction`, convert 3 anonymous classes to lambdas and then to method references, and compose two `Predicate`s with `and`/`negate`. Done when: the dataset exists and 6 functional-interface mini-exercises print the expected results.

### Tuesday 01 Dec · 60 min — Streams core: lazy pipelines, map/filter/reduce (exercises 1-6)
- 📚 **Learn:** Source -> lazy intermediate ops -> one terminal op; streams are single-use; short-circuiting (`findFirst`, `anyMatch`, `limit`); `map` vs `flatMap`; `reduce` identity and accumulator; `IntStream` sum/average; `peek` to watch laziness. Read: [dev.java: The Stream API](https://dev.java/learn/api/collections-and-streams/streams/). Optional: [Defog Tech: Streams API (video)](https://www.youtube.com/watch?v=N3gQdIn90CI).
- 🛠️ **Do:** Exercises 1-6: IT employee names; count of women over 30; total and average salary; highest-paid employee; distinct cities sorted; all distinct skills (`flatMap`). Add `peek` to one pipeline to prove laziness. Done when: all 6 are correct and 2 are cross-checked by hand.

### Wednesday 02 Dec · 60 min — Collectors: groupingBy, partitioningBy, toMap (exercises 11-16)
- 📚 **Learn:** `groupingBy` with downstream collectors (`counting`, `averagingDouble`, `mapping`, `maxBy`), `partitioningBy`, `toMap` with a merge function (duplicate keys throw `IllegalStateException`), map suppliers like `TreeMap::new`, `joining`, `collectingAndThen`. Read: [Baeldung: Guide to Collectors](https://www.baeldung.com/java-collectors). Optional: [Baeldung: groupingBy collector](https://www.baeldung.com/java-groupingby-collector).
- 🛠️ **Do:** Exercises 11-16: count per dept; average salary per dept; highest-paid per dept (unwrap the Optional with `collectingAndThen`); partition by salary > 50k; employees per join year in a `TreeMap`; `toMap` id -> name, then reproduce and fix the duplicate-key crash. Done when: all 6 maps are correct and the duplicate-key fix is explained in a comment.

### Thursday 03 Dec · 60 min — Comparator chains and Optional best practices (exercises 21-26)
- 📚 **Learn:** `Comparator.comparing(...).thenComparing(...).reversed()`, `nullsFirst`; Optional: `map/flatMap/filter/orElse/orElseGet/orElseThrow/ifPresentOrElse`; `orElse` is eager, `orElseGet` lazy; never call `get()` blindly; avoid Optional fields and parameters. Read: [dev.java: Using Optionals](https://dev.java/learn/api/collections-and-streams/streams/optionals/). Optional: [dev.java: Writing comparators](https://dev.java/learn/language/fp/lambdas/writing-comparators/).
- 🛠️ **Do:** Exercises 21-26: sort by dept, salary desc, name; top-3 earners; second-highest distinct salary; youngest per dept; `findById` returning Optional chained to the city or "NA"; an `orElse` vs `orElseGet` side-effect demo. Done when: all 6 are asserted in JUnit tests.

### Friday 04 Dec · 60 min — Parallel stream caveats, katas, and Python comprehensions
- 📚 **Learn:** Parallel streams use the common ForkJoinPool; they help only for large, CPU-bound, easily split, stateless work and hurt with I/O, small data, ordering and shared mutable state; `forEach` vs `forEachOrdered`. Bridge: the Python list/dict comprehensions from your AI W1 Thu do filter + map in one eager expression, while a Java stream is a lazy, single-use pipeline. Read: [dev.java: Parallelizing streams](https://dev.java/learn/api/collections-and-streams/streams/parallel-streams/). Optional: [Python tutorial: Data structures (list comprehensions)](https://docs.python.org/3/tutorial/datastructures.html).
- 🛠️ **Do:** Katas 31-34: char frequency map; first non-repeated char; duplicates in a list; word count. Show the race in `parallel().forEach(list::add)` and fix it with `collect`. Bridge: rewrite 2 of your katas as Python comprehensions (run them with `py`) and write 3 differences (laziness, typing, reusing the result). Done when: the race is reproduced and fixed, and both Python versions print the same results as Java.

### Saturday 05 Dec · 60 min — BUILD: Sales analytics over a CSV using streams
- 📚 **Learn:** Read files with `Files.lines` inside try-with-resources (file I/O in depth in W10); parse CSV rows into objects; skip and count bad lines; `BigDecimal` for money; build reports with collectors. Read: [dev.java: Common I/O tasks in modern Java](https://dev.java/learn/api/io/modernio/). Optional: [dev.java: Reading and writing text files](https://dev.java/learn/api/io/java-io/reading-writing/buffered-text/).
- 🛠️ **Do:** Generate `sales.csv` (200+ rows: date, region, product, category, qty, unitPrice) with a small Java method. Build `SalesReport`: revenue by region, top-5 products, monthly revenue sorted by month, category share %, invalid-row count. Write 5 tests on a tiny fixture CSV. Done when: the report prints in under 1 second, tests are green, and it is pushed.

## 📦 Deliverable (by Saturday night)
`w06` package: Employee dataset, 28 stream exercises and katas with tests, a parallel-stream race fix, 2 katas rewritten as Python comprehensions, Sales analytics report over CSV.

## ✅ Self-check (Sunday test preview)
- What makes streams lazy, and which operations are short-circuiting?
- Explain map vs flatMap with an example.
- Write (verbally) a stream that finds the second-highest salary.
- groupingBy vs partitioningBy: how do you get the highest-paid employee per department?
- What happens with duplicate keys in `Collectors.toMap`, and how do you fix it?
- orElse vs orElseGet: which is lazy? Why should Optional not be used as a field?
- When should you NOT use parallel streams?
- Name 3 differences between a Java stream pipeline and a Python list comprehension.

## 🚀 Stretch (optional)
Remaining drills: 7-10 (first to join after 2022, any salary above 2 lakh, names uppercased and comma-joined, sum of ages with `reduce`), 17-20 (names per city, dept -> sorted names, salary statistics, oldest per gender), 27-30 (generic nth-highest, employees sharing a salary, longest name, Optional-returning repository method), 35-40 (sum of squares of evens, merge two sorted lists, reverse each word, partition primes, IntStream max/min, flatten `List<List<Integer>>`). Then a custom `Collector` returning an immutable summary record and a JDK 24+ `Gatherer` (`Gatherers.windowFixed(3)`).
