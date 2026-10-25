# ☕ Java Backend · Week 02 — OOP I: constructors, encapsulation, object contracts

> 📅 **Mon 02 Nov 2026 → Sun 08 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 01](Week-01.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-02.md) · [Week 03 →](Week-03.md)

**Why this week:** Constructors, initialization order, equals/hashCode and immutability are top Core Java questions, and they underpin every Spring bean and JPA entity you will write; this week also starts the habit of proving code with tests.

## 🗓️ Sessions

### Monday 02 Nov · 60 min — Constructors and this() chaining; ArrayList; first JUnit tests
- 📚 **Learn:** Class vs object, fields and methods; the default constructor exists only if you declare none; overloaded constructors chained with `this(...)` to one master constructor; `new` allocates on the heap. `ArrayList<Expense>` grows as you `add`; loop over it with for-each. A JUnit test is a `@Test` method that calls `assertEquals(expected, actual)`, and `mvn test` runs it. Read: [dev.java: Providing constructors](https://dev.java/learn/language/oop/classes-objects/defining-constructors/). Optional: [MOOC 3.2: Lists](https://java-programming.mooc.fi/part-3/2-lists).
- 🛠️ **Do:** Write `w02.Product` with 3 constructors that all delegate via `this(...)` to one validating master constructor, plus `toString`. Refactor the W1 tracker into an `Expense` class kept in an `ArrayList<Expense>` with `total()` and `totalFor(category)`. Add `junit-jupiter` (test scope) to the POM and write 2 tests: the total of 3 expenses and the total for one category. Done when: every constructor delegates, invalid input throws `IllegalArgumentException`, and `mvn test` shows 2 green tests.

### Tuesday 03 Nov · 60 min — Initialization order: static/instance blocks and super() chain
- 📚 **Learn:** Class init runs once: static fields and blocks top-to-bottom. On `new`: super constructor first, then instance fields/blocks, then the constructor body. Calling an overridable method from a constructor sees uninitialized subclass fields. Read: [Oracle: Initializing fields](https://docs.oracle.com/javase/tutorial/java/javaOO/initial.html). Optional: [Baeldung: Static vs instance initializer blocks](https://www.baeldung.com/java-static-instance-initializer-blocks).
- 🛠️ **Do:** Write `Parent` and `Child`, each with a static block, instance block, field initializer that prints, and a constructor. Predict on paper the full output of `new Child(); new Child();`, then run. Next, call an overridden method from `Parent`'s constructor and explain why it prints null/0. Done when: your predicted order matches the real output for both objects.

### Wednesday 04 Nov · 60 min — final, access modifiers, packages; interface preview
- 📚 **Learn:** `final` variables, methods and classes; private/default/protected/public visibility; packages and imports; why fields stay private. Preview: an `interface` lists methods a class promises to implement (`class FlatFee implements Fee`), so other code can depend on the interface type instead of a concrete class; the full story is W3 Tue. Read: [Oracle: Controlling access](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html). Optional: [dev.java: Interfaces](https://dev.java/learn/language/oop/interfaces/).
- 🛠️ **Do:** Create packages `w02.bank.model` and `w02.bank.app`; make `Account` fields `private final` where possible; access protected and default members from the other package (and from a subclass there) and paste the compile errors as comments. Interface preview: `interface Fee { double apply(double amount); }` with `FlatFee` and `PercentFee`; `Account.withdraw` charges whichever `Fee` it was given. Done when: your access table is filled from compiler evidence and the same `Account` code works with both fees.

### Thursday 05 Nov · 60 min — Encapsulation and the equals/hashCode/toString contract
- 📚 **Learn:** Encapsulation = protecting invariants through behaviour methods, not blind setters. The equals contract (reflexive, symmetric, transitive, consistent, non-null) and the hashCode contract; overriding equals without hashCode breaks HashSet/HashMap. Read: [Baeldung: equals and hashCode contracts](https://www.baeldung.com/java-equals-hashcode-contracts). Optional: [Coding with John: equals vs == (video)](https://www.youtube.com/watch?v=AoUVdLWLFQw).
- 🛠️ **Do:** Hand-write (no IDE generation) `Money(amount, currency)` with `equals`, `hashCode`, `toString`. Version A overrides only `equals`: add two equal objects to a `HashSet` and print size 2; version B fixes it: size 1. Give `Account` `deposit/withdraw` that keep balance >= 0. Done when: both set sizes are printed and explained in a comment, and withdraw rejects overdraft.

### Friday 06 Nov · 60 min — Immutable class recipe and defensive copies
- 📚 **Learn:** Recipe: final class, private final fields, no setters, validate in the constructor, defensive copies of mutable inputs and outputs, `withX(...)` methods returning new objects; why String and Integer are immutable; immutability gives free thread-safety. Read: [Baeldung: Immutable objects](https://www.baeldung.com/java-immutable-object). Optional: [Oracle: Immutable objects](https://docs.oracle.com/javase/tutorial/essential/concurrency/immutable.html).
- 🛠️ **Do:** Write a naive `Order(id, List<String> items, LocalDate date)`, then break it from `main` by mutating the list you passed in and the list returned by the getter. Fix with `List.copyOf` and add `withItem(String)` returning a new `Order`. Done when: every break attempt leaves the original order unchanged and you can recite the 5-step recipe.

### Saturday 07 Nov · 60 min — BUILD: Bank Account System with clean OOP
- 📚 **Learn:** Design first: `Customer`, `Account`, `SavingsAccount`, immutable `Transaction`, `Bank` service; list responsibilities and invariants; keep console I/O separate from logic. Read: [MOOC 6.2: Separating UI from logic](https://java-programming.mooc.fi/part-6/2-separating-user-interface-from-program-logic). Optional: [Oracle: Classes and objects lesson](https://docs.oracle.com/javase/tutorial/java/javaOO/index.html).
- 🛠️ **Do:** Build `w02.bank`: open account, deposit, withdraw (reject overdraft), transfer (both-or-nothing), a statement kept as an `ArrayList` of immutable `Transaction`s; `Account` equality by account number. A scripted `main` runs 10 operations including 2 rejected ones, plus 2 JUnit tests (overdraft rejected, a failed transfer changes no balance). Done when: the printed statement and balances are correct, the logic has no `Scanner`/`println`, tests are green and it is pushed.

## 📦 Deliverable (by Saturday night)
`w02` package: Product, Expense list with the first 2 JUnit tests, init-order demo, access-table notes, Fee interface preview, Money with correct equals/hashCode, immutable Order, Bank Account System with tests pushed.

## ✅ Self-check (Sunday test preview)
- When does Java add a default constructor, and what changes if you add a parameterized one?
- State the execution order of static blocks, instance blocks and constructors for Parent and Child.
- Why must hashCode be overridden whenever equals is? What exactly breaks in a HashMap?
- List the steps to make a class immutable. Why are defensive copies needed?
- Can a subclass in another package access a protected member through a parent-type reference?
- What does a class promise when it `implements` an interface, and why depend on the interface type?
- What do `this(...)` and `super(...)` do, and where must they appear?
- Can a constructor be private, final or static? When is a private constructor useful?

## 🚀 Stretch (optional)
Read the class-initialization rules in [JLS 12.4](https://docs.oracle.com/javase/specs/jls/se25/html/jls-12.html) and find one case where touching a class does NOT initialize it. Extras: `Rectangle` with 3 delegating constructors (default 1x1, square, full); `final class MoneyUtils` with a private constructor and static `round2`; a minimum-balance rule for savings accounts.
