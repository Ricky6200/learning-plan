# ☕ Java Backend · Week 01 — Java foundations rebuilt: JVM to methods

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** Every Java interview opens with JDK/JRE/JVM, pass-by-value and Integer-cache traps; fluent basic code is the base for everything you will write later.

## 🗓️ Sessions

### Monday 26 Oct · 60 min — Setup JDK 25 + IDE; javac to bytecode to JVM
- 📚 **Learn:** JDK vs JRE vs JVM; javac -> .class bytecode -> class loading -> interpreter + JIT; running single-file source with `java Hello.java`; JShell for quick experiments. [dev.java: Getting started](https://dev.java/learn/getting-started/), [dev.java: javap disassembler](https://dev.java/learn/jvm/core-tools/javap/), [Amazon Corretto 25](https://docs.aws.amazon.com/corretto/latest/corretto-25-ug/what-is-corretto-25.html).
- 🛠️ **Do:** Make Corretto 25 this project's SDK (Section 5 of `03_SETUP_YOUR_LAPTOP.md`; work stays on JDK 11). Turn the `java-mastery` repo from your setup push test (in `C:\dev\personal`) into a Maven project (package `w01`). Write `Hello.java`, compile with `javac`, run, then `javap -c Hello` and annotate 3 bytecode lines in comments. Predict-then-try 5 JShell expressions. Done when: the first commit (Hello + javap notes) is on GitHub.

### Tuesday 27 Oct · 60 min — Primitives vs references, wrappers, autoboxing, Integer cache
- 📚 **Learn:** 8 primitives, ranges, defaults, widening/narrowing casts, overflow; reference variables; wrapper classes, autoboxing/unboxing, NPE when unboxing null, Integer cache -128..127 and `==` vs `equals`. [dev.java: Primitive types](https://dev.java/learn/language/constructs/basics/primitive-types/), [dev.java: Autoboxing](https://dev.java/learn/language/constructs/numbers-strings/autoboxing/), [MOOC 5.3: Primitive and reference variables](https://java-programming.mooc.fi/part-5/3-primitive-and-reference-variables).
- 🛠️ **Do:** Write `NumberTraps` with 10 predict-then-run snippets: int overflow, `(byte) 200`, `0.1 + 0.2`, `Integer` 127 vs 128 with `==`, unboxing a null `Integer`, `char + int`, integer division, `Math.round(-2.5)`, long literal without `L`, `'a' + 'b'`. Write prediction vs actual in comments. Done when: all 10 run and you can explain each surprise aloud in one sentence.

### Wednesday 28 Oct · 60 min — Operators, control flow and loops: kata day
- 📚 **Learn:** Precedence, `i++` vs `++i`, short-circuit `&&` vs `&`, ternary, compound assignment casts, classic and arrow `switch`, for/while/do-while, break/continue/labels. [dev.java: Using operators](https://dev.java/learn/language/constructs/basics/using-operators/), [dev.java: Control flow statements](https://dev.java/learn/language/constructs/basics/controlling-flow/).
- 🛠️ **Do:** From scratch in `w01.Katas`: FizzBuzz, reverse an int, digit sum, isPrime, iterative Fibonacci (n=30), number pyramid (n=5), Armstrong number. No copy-paste. After a 5-minute break, rewrite one kata from memory without looking. Done when: all 7 print correct output for 3 inputs each, including 0 and a negative number where relevant.

### Thursday 29 Oct · 60 min — Methods, pass-by-value, overloading resolution, varargs
- 📚 **Learn:** Method signatures and return types; Java is always pass-by-value (copy of a primitive or of a reference), why `swap(a, b)` fails; overload resolution order: exact -> widening -> boxing -> varargs. [Oracle: Passing information to a method](https://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html), [Baeldung: Pass-by-value](https://www.baeldung.com/java-pass-by-value-or-pass-by-reference), [MOOC 2.4: Methods](https://java-programming.mooc.fi/part-2/4-methods).
- 🛠️ **Do:** Write `PassByValueDemo`: `swap(int,int)`, `reassign(int[])` vs `mutate(int[])`, `append(StringBuilder)`; predict each output first. Then write overloads `print(long)`, `print(Integer)`, `print(int...)`, `print(Object)`, call `print(5)` and delete one overload at a time to watch resolution change. Done when: predictions are recorded and the resolution order is written in a comment from your own evidence.

### Friday 30 Oct · 60 min — static vs instance, arrays, String basics
- 📚 **Learn:** Class-level vs object-level members, why `main` is static, no `this` in static context; arrays (defaults, `length`, 2D, `Arrays.toString/sort/copyOf`); String basics (`charAt`, `substring`, `split`, `equals`, immutability preview). [Oracle: Class members](https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html), [dev.java: Arrays](https://dev.java/learn/language/constructs/basics/arrays/), [Coding with John: static vs non-static (video)](https://www.youtube.com/watch?v=-Y67pdWHr9Y).
- 🛠️ **Do:** Write `Ticket` with static `totalIssued` and instance `seatNo`; create 3 objects and print both. Then katas: max/min, reverse array in place, second largest, rotate by k, palindrome string, vowel count, reverse words in a sentence. Done when: all 7 katas pass your hand-checked inputs (including empty array/string) and are committed.

### Saturday 31 Oct · 60 min — BUILD: CLI Expense Tracker v0 pushed to GitHub
- 📚 **Learn:** Plan before coding: menu loop with `Scanner`, parallel arrays for data (you will refactor to objects in W2), one static method per menu action, input validation, README basics. [MOOC 1.3: Reading input](https://java-programming.mooc.fi/part-1/3-reading), [GitHub Docs: Hello World](https://docs.github.com/en/get-started/using-github/hello-world).
- 🛠️ **Do:** Build `w01.expense.ExpenseTrackerApp`: menu 1 add, 2 list, 3 total, 4 total by category, 5 highest expense, 0 exit; store up to 100 entries (amount, category, note) in arrays; reject negative amounts and unknown options without crashing. Push with a README (how to run + sample session). Done when: you add 5 expenses, see correct totals by category, and the commit is visible on GitHub.

## 📦 Deliverable (by Saturday night)
`java-mastery` on GitHub with package `w01`: Hello + javap notes, NumberTraps, Katas, PassByValueDemo, Ticket, Expense Tracker v0 + README; JDK 25, IntelliJ and Git working.

## ✅ Self-check (Sunday test preview)
- What is the difference between JDK, JRE and JVM, and what exactly does javac produce?
- Is Java pass-by-value or pass-by-reference? Prove it with an object example.
- Why does `Integer a = 128, b = 128; a == b` print false while 127 prints true?
- What happens when a null `Integer` is unboxed to `int`?
- Given overloads m(long), m(Integer) and m(int...), which one does `m(5)` call and why?
- Why is `main` static? Can a static method read an instance field directly?
- What does `System.out.println(1 + 2 + "3" + 4 + 5)` print?

## 🚀 Stretch (optional)
Run `javap -c` on a class with a loop and an instance method call; explain `invokestatic` vs `invokevirtual` in two lines.
