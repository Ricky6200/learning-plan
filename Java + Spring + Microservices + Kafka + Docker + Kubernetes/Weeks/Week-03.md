# ☕ Java Backend · Week 03 — OOP II: inheritance, interfaces, Strings, JUnit

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Overriding rules, abstract class vs interface and the String pool are asked in nearly every round; composition-first design and unit tests are how real Spring code is built.

## 🗓️ Sessions

### Monday 09 Nov · 60 min — Inheritance, overriding rules, super, dynamic dispatch
- 📚 **Learn:** `extends`, `super.method()`; overriding rules: same signature, covariant return, access may widen not narrow, checked exceptions may not broaden (exceptions in W4); static methods hide, private/final never override; fields are not polymorphic; the runtime type picks the method. Read: [dev.java: Overriding and hiding](https://dev.java/learn/language/oop/inheritance/overriding/). Optional: [Coding with John: Polymorphism (video)](https://www.youtube.com/watch?v=jhDUxynEQRI).
- 🛠️ **Do:** In `w03.shapes` write `Shape` -> `Circle`, `Rectangle`, `Square extends Rectangle`; override `area()`/`toString()` and add a hidden static method. Predict outputs for calls via `Shape s = new Square(2)`. Add 3 lines that must fail to compile (narrowed access, broader checked exception, overriding a final method) and paste the errors. Done when: every rule has your own code proof.

### Tuesday 10 Nov · 60 min — Abstract classes vs interfaces with default/static methods
- 📚 **Learn:** Abstract class: state, constructors, template methods. Interface: a capability, multiple inheritance of type, default/static/private methods; resolve the default-method diamond with `X.super.m()`; when to choose which. Read: [Oracle: Default methods](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html). Optional: [Oracle: Abstract classes](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html).
- 🛠️ **Do:** Write interface `PaymentMethod` (abstract `pay`, default `currency()`, static factory `of(String)`) with `Card` and `Upi`; abstract `Notifier` with template method `send()` calling abstract `format()`. Create two interfaces with the same default method and resolve the clash. Done when: it compiles and a comment table lists 6 differences between abstract classes and interfaces in your own words.

### Wednesday 11 Nov · 60 min — Enums, nested classes and composition over inheritance
- 📚 **Learn:** Enums with fields, constructors, per-constant behaviour, `values()`, `EnumMap`; static nested vs inner (holds an outer reference: leak risk) vs anonymous classes; is-a vs has-a and the fragile base class problem. Read: [dev.java: Enums](https://dev.java/learn/language/oop/classes-objects/enums/). Optional: [Baeldung: Inheritance vs composition](https://www.baeldung.com/java-inheritance-composition).
- 🛠️ **Do:** Write enum `BookingStatus` with `next()` and per-constant `canCancel()`; an illegal transition throws `IllegalStateException`. Then write `CountingSet extends HashSet` that counts adds, show `addAll` double-counts, and rewrite it with composition (wrap a `Set`). Done when: the enum transitions print correctly and the double-count bug is reproduced, then fixed.

### Thursday 12 Nov · 60 min — String deep dive: pool, immutability, StringBuilder, intern
- 📚 **Learn:** Literals live in the string pool; `new String(...)` creates a new object; `==` vs `equals`; `intern()`; compile-time constant folding vs runtime concatenation; why String is immutable (security, cached hash, thread-safety); StringBuilder vs synchronized StringBuffer. Read: [Baeldung: String pool](https://www.baeldung.com/java-string-pool). Optional: [Baeldung: StringBuilder vs StringBuffer](https://www.baeldung.com/java-string-builder-string-buffer).
- 🛠️ **Do:** Write `StringPuzzles`: 10 predict-then-run `==`/`equals` cases (literals, `new`, `intern()`, `final` local constants, runtime concatenation). Time building a 100k-char string with `+=` vs `StringBuilder`. From scratch write `compress("aaabbc")` -> `a3b2c1`. Done when: all 10 predictions are explained in comments and `compress` handles empty and 1-char input.

### Friday 13 Nov · 60 min — JUnit basics: test the OOP code you wrote
- 📚 **Learn:** JUnit 6 (Jupiter, same API as JUnit 5): `@Test`, `@BeforeEach`, `@DisplayName`, `assertEquals/assertThrows/assertAll`, `@ParameterizedTest` + `@CsvSource`; Arrange-Act-Assert; JUnit BOM + Surefire in `pom.xml`. In `assertThrows(X.class, () -> account.withdraw(500))` the `() -> ...` part is a lambda: code passed as a value (full story in W6). Read: [JUnit User Guide: Writing tests](https://docs.junit.org/current/writing-tests/intro.html). Optional: [Coding with John: JUnit (video)](https://www.youtube.com/watch?v=vZm0lHciFsQ).
- 🛠️ **Do:** Switch `java-mastery` to the JUnit BOM (you added `junit-jupiter` in W2). Write tests for `Money` equals/hashCode, `Account.withdraw` overdraft (`assertThrows`), `compress` (parameterized, 5 rows) and `BookingStatus.next()`. Write one test first that fails, then make it pass (red -> green). Done when: `mvn test` shows at least 12 green tests.

### Saturday 14 Nov · 60 min — BUILD: Library domain model with JUnit tests
- 📚 **Learn:** Model: abstract `LibraryItem` -> `Book`, `Dvd`; `Member` + `MembershipType` enum (loan limits); immutable `Loan`; `LateFeePolicy` interface (strategy); `Library` service built by composition. Read: [MOOC 9.2: Interfaces](https://java-programming.mooc.fi/part-9/2-interface). Optional: [Baeldung: Composition, aggregation, association](https://www.baeldung.com/java-composition-aggregation-association).
- 🛠️ **Do:** Implement `w03.library`: borrow/return/search-by-title (case-insensitive), per-membership limits, due dates and 2 late-fee policies. Write 8 JUnit tests (limit reached, double borrow rejected, late fee for both policies, search, return of an unknown item). Done when: `mvn test` is green and the code is pushed.

## 📦 Deliverable (by Saturday night)
`w03` package: shapes + rule proofs, PaymentMethod/Notifier, BookingStatus enum, CountingSet fix, StringPuzzles, Library model; 20+ JUnit tests green.

## ✅ Self-check (Sunday test preview)
- List the overriding rules for return type, access modifier, checked exceptions and static methods.
- Abstract class vs interface in modern Java: give one situation where each is the right choice.
- Why prefer composition over inheritance? Explain the HashSet addAll double-count example.
- Static nested vs inner class: which can leak memory and why?
- `String s1 = "java"; String s2 = new String("java");` Are `s1 == s2` and `s1 == s2.intern()` true?
- When would you use StringBuilder vs StringBuffer vs `+`?
- What happens if you put `@Override` on a static method?

## 🚀 Stretch (optional)
Write a reusable `ForwardingSet<E>` (delegation wrapper) and rebuild `CountingSet` on top of it. Extras: a covariant `copy()` and a shadowed field in the shapes hierarchy; a static nested `Pizza.Builder`; a `Wallet` payment method; a Mermaid class diagram of the library in the README.
