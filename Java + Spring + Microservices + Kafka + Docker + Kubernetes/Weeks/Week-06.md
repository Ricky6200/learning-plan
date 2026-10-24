# ☕ Java Backend · Week 06 — Functional Java: lambdas, streams, Optional drills

> 📅 **Mon 30 Nov 2026 → Sun 06 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 05](Week-05.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-06.md) · [Week 07 →](Week-07.md)

**Why this week:** Stream coding questions (group, count, second-highest, frequency) appear in almost every Indian Java interview; fluency here also makes your Spring code shorter and clearer.

## 🗓️ Sessions

### Monday 30 Nov · 60 min — Lambdas, functional interfaces, method references
- 📚 **Learn:** Lambda syntax and effectively-final capture; `java.util.function` (Predicate, Function, Supplier, Consumer, BiFunction, UnaryOperator, BinaryOperator), primitive specializations; composing with `andThen`, `compose`, `and`, `negate`; 4 kinds of method references. [dev.java: Lambda expressions](https://dev.java/learn/language/fp/lambdas/), [Baeldung: Method references](https://www.baeldung.com/java-method-references), [Coding with John: Lambdas (video)](https://www.youtube.com/watch?v=tj5sLSFjVj4).
- 🛠️ **Do:** Create immutable `w06.Employee` (id, name, dept, gender, salary, age, city, joinDate, skills) and `EmployeeData.list()` with 20 varied employees. Write your own `@FunctionalInterface TriFunction`, convert 5 anonymous classes to lambdas and then to method references, and compose `Predicate`s. Done when: the dataset exists and 8 functional-interface mini-exercises print expected results.

### Tuesday 01 Dec · 60 min — Streams core: lazy pipelines, map/filter/reduce (exercises 1-10)
- 📚 **Learn:** Source -> lazy intermediate ops -> one terminal op; streams are single-use; short-circuiting (`findFirst`, `anyMatch`, `limit`); `map` vs `flatMap`; `reduce` identity and accumulator; `IntStream` sum/average; `peek` for debugging laziness. [dev.java: The Stream API](https://dev.java/learn/api/collections-and-streams/streams/), [Baeldung: Stream API tutorial](https://www.baeldung.com/java-8-streams), [Defog Tech: Streams API (video)](https://www.youtube.com/watch?v=N3gQdIn90CI).
- 🛠️ **Do:** Exercises 1-10: IT employee names; count of women over 30; total and average salary; highest-paid employee; distinct cities sorted; first to join after 2022; any salary above 2 lakh; all distinct skills (flatMap); names uppercased and comma-joined; sum of ages with `reduce`. Add `peek` to prove laziness. Done when: all 10 are correct and 2 are cross-checked by hand.

### Wednesday 02 Dec · 60 min — Collectors: groupingBy, partitioningBy, toMap, joining (exercises 11-20)
- 📚 **Learn:** `groupingBy` with downstream collectors (`counting`, `averagingDouble`, `mapping`, `maxBy`, `toSet`), `partitioningBy`, `toMap` merge function and duplicate-key `IllegalStateException`, map suppliers like `TreeMap::new`, `joining`, `summarizingDouble`, `collectingAndThen`, `teeing`. [Baeldung: Guide to Collectors](https://www.baeldung.com/java-collectors), [Baeldung: groupingBy collector](https://www.baeldung.com/java-groupingby-collector).
- 🛠️ **Do:** Exercises 11-20: count per dept; average salary per dept; highest-paid per dept (unwrap Optional with `collectingAndThen`); names per city; partition by salary > 50k; dept -> sorted names; `toMap` id -> name and handle a duplicate key; salary statistics; employees per join year (TreeMap); oldest per gender. Done when: all 10 maps are correct and the duplicate-key crash is reproduced and fixed.

### Thursday 03 Dec · 60 min — Comparator chains and Optional best practices (exercises 21-30)
- 📚 **Learn:** `Comparator.comparing(...).thenComparing(...).reversed()`, `nullsFirst`; Optional: `map/flatMap/filter/orElse/orElseGet/orElseThrow/ifPresentOrElse`; `orElse` is eager, `orElseGet` lazy; never call `get()` blindly; avoid Optional fields and parameters. [dev.java: Writing comparators](https://dev.java/learn/language/fp/lambdas/writing-comparators/), [dev.java: Using Optionals](https://dev.java/learn/api/collections-and-streams/streams/optionals/), [Baeldung: Optional as return type](https://www.baeldung.com/java-optional-return).
- 🛠️ **Do:** Exercises 21-30: sort by dept, salary desc, name; top-3 earners; second-highest distinct salary; generic nth-highest method; youngest per dept; employees sharing a salary; longest name; `findById` returning Optional chained to city or "NA"; `orElse` vs `orElseGet` side-effect demo; Optional-returning repository method. Done when: all 10 are asserted in JUnit tests.

### Friday 04 Dec · 60 min — Parallel stream caveats and classic stream katas (31-40)
- 📚 **Learn:** Parallel streams use the common ForkJoinPool; they help only for large, CPU-bound, easily split, stateless work; they hurt with I/O, small data, LinkedList, ordering and shared mutable state; `forEach` vs `forEachOrdered`. [dev.java: Parallelizing streams](https://dev.java/learn/api/collections-and-streams/streams/parallel-streams/), [Baeldung: When to use parallel streams](https://www.baeldung.com/java-when-to-use-parallel-stream).
- 🛠️ **Do:** Exercises 31-40: char frequency; first non-repeated char; duplicates in a list; word count; sum of squares of evens; merge two sorted lists; reverse each word; partition primes; max/min with IntStream; flatten `List<List<Integer>>` sorted. Show the race in `parallel().forEach(list::add)` and fix it with `collect`. Done when: at least 7 of 10 are solved without looking anything up.

### Saturday 05 Dec · 60 min — BUILD: Sales analytics over a CSV using streams
- 📚 **Learn:** Read files with `Files.lines` inside try-with-resources; parse CSV rows into objects; skip and count bad lines; `BigDecimal` for money; build reports with collectors. [dev.java: Reading and writing text files](https://dev.java/learn/api/io/java-io/reading-writing/buffered-text/), [dev.java: Common I/O tasks in modern Java](https://dev.java/learn/api/io/modernio/).
- 🛠️ **Do:** Generate `sales.csv` (200+ rows: date, region, product, category, qty, unitPrice) with a small Java method. Build `SalesReport`: revenue by region, top-5 products, monthly revenue sorted by month, category share %, best day, invalid-row count. Write 8 tests on a tiny fixture CSV. Done when: the report prints in under 1 second, tests are green, and it is pushed.

## 📦 Deliverable (by Saturday night)
`w06` package: Employee dataset, 40 stream exercises with tests, Sales analytics report over CSV.

## ✅ Self-check (Sunday test preview)
- What makes streams lazy, and which operations are short-circuiting?
- Explain map vs flatMap with an example.
- Write (verbally) a stream that finds the second-highest salary.
- groupingBy vs partitioningBy: how do you get the highest-paid employee per department?
- What happens with duplicate keys in `Collectors.toMap`, and how do you fix it?
- orElse vs orElseGet: which is lazy? Why should Optional not be used as a field?
- When should you NOT use parallel streams?

## 🚀 Stretch (optional)
Write a custom `Collector` returning an immutable summary record, and use a JDK 24+ `Gatherer` (`Gatherers.windowFixed(3)`).
