# ☕ Java Backend · Week 03 — OOP II: inheritance, interfaces, Strings, JUnit

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Overriding rules, abstract class vs interface and the String pool are asked in nearly every round; composition-first design and unit tests are how real Spring code is built.

## 🗓️ Sessions

### Monday 09 Nov · 60 min — Inheritance, overriding rules, super, dynamic dispatch
- 📚 **Learn:** `extends`, `super.method()`; overriding rules: same signature, covariant return, access may widen not narrow, checked exceptions may not broaden; static methods hide, private/final never override; fields are not polymorphic; runtime type picks the method. [dev.java: Overriding and hiding](https://dev.java/learn/language/oop/inheritance/overriding/), [dev.java: Polymorphism](https://dev.java/learn/language/oop/inheritance/polymorphism/), [Coding with John: Polymorphism (video)](https://www.youtube.com/watch?v=jhDUxynEQRI).
- 🛠️ **Do:** In `w03.shapes` write `Shape` -> `Circle`, `Rectangle`, `Square extends Rectangle`; override `area()`/`toString()`, add a covariant `copy()`, a hidden static method and a shadowed field. Predict outputs for calls via `Shape s = new Square(2)`. Add 3 lines that must fail to compile (narrowed access, broader checked exception, overriding final) and paste the errors. Done when: every rule has your own code proof.

### Tuesday 10 Nov · 60 min — Abstract classes vs interfaces with default/static/private methods
- 📚 **Learn:** Abstract class: state, constructors, template methods. Interface: capability, multiple inheritance of type, default/static/private methods; resolving the default-method diamond with `X.super.m()`; when to choose which. [Oracle: Abstract classes](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html), [Oracle: Default methods](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html), [Coding with John: Abstract classes (video)](https://www.youtube.com/watch?v=HvPlEJ3LHgE).
- 🛠️ **Do:** Write interface `PaymentMethod` (abstract `pay`, default `currency()`, static factory `of(String)`, private helper) with `Card`, `Upi`, `Wallet`; abstract `Notifier` with template method `send()` calling abstract `format()`. Create two interfaces with the same default method and resolve the clash. Done when: it compiles and a comment table lists 6 differences in your own words.

### Wednesday 11 Nov · 60 min — Composition over inheritance; nested and anonymous classes; enums
- 📚 **Learn:** Is-a vs has-a and the fragile base class problem; static nested vs inner (holds outer reference: leak risk) vs local vs anonymous classes; enums with fields, constructors, per-constant behaviour, `values()`, `EnumMap`. [Baeldung: Inheritance vs composition](https://www.baeldung.com/java-inheritance-composition), [dev.java: Nested classes](https://dev.java/learn/language/oop/classes-objects/nested-classes/), [dev.java: Enums](https://dev.java/learn/language/oop/classes-objects/enums/).
- 🛠️ **Do:** Write `CountingSet extends HashSet` that counts adds; show `addAll` double-counts, then rewrite it with composition (wrap a `Set`). Write enum `BookingStatus` with `next()` and per-constant `canCancel()`, plus a static nested `Builder` for `Pizza`. Done when: the double-count bug is reproduced then fixed, and an illegal status transition throws.

### Thursday 12 Nov · 60 min — String deep dive: pool, immutability, StringBuilder, intern
- 📚 **Learn:** Literals live in the string pool; `new String(...)` creates a new object; `==` vs `equals`; `intern()`; compile-time constant folding vs runtime concatenation; why String is immutable (security, cached hash, thread-safety); StringBuilder vs synchronized StringBuffer. [Baeldung: String pool](https://www.baeldung.com/java-string-pool), [Baeldung: Why String is immutable](https://www.baeldung.com/java-string-immutable), [Baeldung: StringBuilder vs StringBuffer](https://www.baeldung.com/java-string-builder-string-buffer).
- 🛠️ **Do:** Write `StringPuzzles`: 10 predict-then-run `==`/`equals` cases (literals, `new`, `intern()`, `final` local constants, runtime concatenation). Time building a 100k-char string with `+=` vs `StringBuilder`. From scratch write `compress("aaabbc")` -> `a3b2c1`. Done when: all 10 predictions are explained in comments and `compress` handles empty and 1-char input.

### Friday 13 Nov · 60 min — JUnit basics: test the OOP code you wrote
- 📚 **Learn:** JUnit 6 (Jupiter, same API as JUnit 5): `@Test`, `@BeforeEach`, `@DisplayName`, `assertEquals/assertThrows/assertAll`, `@ParameterizedTest` + `@CsvSource`; Arrange-Act-Assert; JUnit BOM + Surefire in `pom.xml`; run with `mvn test`. [JUnit User Guide](https://docs.junit.org/current/user-guide/), [Baeldung: JUnit guide](https://www.baeldung.com/junit-5), [Coding with John: JUnit (video)](https://www.youtube.com/watch?v=vZm0lHciFsQ).
- 🛠️ **Do:** Add JUnit to `java-mastery`. Write tests for `Money` equals/hashCode, `Account.withdraw` overdraft (`assertThrows`), `compress` (parameterized, 5 rows) and `BookingStatus.next()`. Write one test first that fails, then make it pass (red -> green). Done when: `mvn test` shows at least 12 green tests.

### Saturday 14 Nov · 60 min — BUILD: Library domain model with JUnit tests
- 📚 **Learn:** Model: abstract `LibraryItem` -> `Book`, `Dvd`; `Member` + `MembershipType` enum (loan limits); immutable `Loan`; `LateFeePolicy` interface (strategy); `Library` service built by composition. [Baeldung: Composition, aggregation, association](https://www.baeldung.com/java-composition-aggregation-association), [MOOC 9.2: Interfaces](https://java-programming.mooc.fi/part-9/2-interface).
- 🛠️ **Do:** Implement `w03.library`: borrow/return/search-by-title (case-insensitive), per-membership limits, due dates, 2 late-fee policies. Write at least 10 JUnit tests (limit reached, double borrow rejected, late fee for both policies, search, return of unknown item). Done when: `mvn test` is green and the README has a small class diagram (ASCII or Mermaid).

## 📦 Deliverable (by Saturday night)
`w03` package: shapes + rule proofs, PaymentMethod/Notifier, CountingSet fix, BookingStatus enum, StringPuzzles, Library model; 22+ JUnit tests green.

## ✅ Self-check (Sunday test preview)
- List the overriding rules for return type, access modifier, checked exceptions and static methods.
- Abstract class vs interface in modern Java: give one situation where each is the right choice.
- Why prefer composition over inheritance? Explain the HashSet addAll double-count example.
- Static nested vs inner class: which can leak memory and why?
- `String s1 = "java"; String s2 = new String("java");` Are `s1 == s2` and `s1 == s2.intern()` true?
- When would you use StringBuilder vs StringBuffer vs `+`?
- What happens if you put `@Override` on a static method?

## 🚀 Stretch (optional)
Write a reusable `ForwardingSet<E>` (delegation wrapper) and rebuild `CountingSet` on top of it.
