# ☕ Java Backend · Week 01 — Java foundations rebuilt: JVM to methods

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** Every Java interview opens with JDK/JRE/JVM, pass-by-value and Integer-cache traps; fluent basic code (loops, methods, recursion, a first HashMap) is the base for everything you will write later.

## 🗓️ Sessions

### Monday 26 Oct · 60 min — Setup JDK 25 + IDE; javac to bytecode to JVM
- 📚 **Learn:** JDK vs JRE vs JVM; javac -> .class bytecode -> class loading -> interpreter + JIT; running a single-file program with `java Hello.java`; JShell for quick experiments. Read: [dev.java: Getting started](https://dev.java/learn/getting-started/) (about 15 min). Optional: [dev.java: javap disassembler](https://dev.java/learn/jvm/core-tools/javap/).
- 🛠️ **Do:** Make Corretto 25 this project's SDK (Section 5 of `03_SETUP_YOUR_LAPTOP.md`; work stays on JDK 11). Turn the `java-mastery` repo from your setup push test (in `C:\dev\personal`) into a Maven project (package `w01`). Write `Hello.java`, compile with `javac`, run, then `javap -c Hello` and annotate 3 bytecode lines in comments. Predict-then-try 5 JShell expressions. Done when: the first commit (Hello + javap notes) is on GitHub.

### Tuesday 27 Oct · 60 min — Primitives vs references, wrappers, autoboxing, Integer cache
- 📚 **Learn:** 8 primitives, ranges, defaults, widening/narrowing casts, overflow; reference variables; wrapper classes, autoboxing/unboxing, NPE when unboxing null, Integer cache -128..127 and `==` vs `equals`. Read: [dev.java: Primitive types](https://dev.java/learn/language/constructs/basics/primitive-types/) (about 10 min). Optional: [dev.java: Autoboxing](https://dev.java/learn/language/constructs/numbers-strings/autoboxing/).
- 🛠️ **Do:** Write `NumberTraps` with 10 predict-then-run snippets: int overflow, `(byte) 200`, `0.1 + 0.2`, `Integer` 127 vs 128 with `==`, unboxing a null `Integer`, `char + int`, integer division, `Math.round(-2.5)`, long literal without `L`, `'a' + 'b'`. Write prediction vs actual in comments. Done when: all 10 run and you can explain each surprise aloud in one sentence.

### Wednesday 28 Oct · 60 min — Operators incl. bitwise and shifts, control flow: kata day
- 📚 **Learn:** Precedence, `i++` vs `++i`, short-circuit `&&` vs `&`, ternary, compound-assignment casts; bitwise AND/OR/XOR/NOT (`& | ^ ~`) and shifts `<<`, `>>` (keeps the sign), `>>>` (fills with zeros) on ints, which W5's HashMap uses in `h ^ (h >>> 16)`; arrow `switch`, for/while/do-while, break/continue. Read: [dev.java: Using operators](https://dev.java/learn/language/constructs/basics/using-operators/) (including the bitwise and bit shift part). Optional: [dev.java: Control flow statements](https://dev.java/learn/language/constructs/basics/controlling-flow/).
- 🛠️ **Do:** From scratch in `w01.Katas`: FizzBuzz, reverse an int, digit sum, isPrime, iterative Fibonacci (n=30). Then in `w01.Bits` predict-then-run `5 & 3`, `5 | 3`, `5 ^ 3`, `~5`, `-16 >> 2` and `-16 >>> 28`, and write `isPowerOfTwo(n)` with `n > 0 && (n & (n - 1)) == 0`. No copy-paste. Done when: every kata prints correct output for 3 inputs (including 0 and a negative number where relevant) and all 6 bit predictions are checked and explained in comments.

### Thursday 29 Oct · 60 min — Methods, pass-by-value, overloading, recursion and the call stack
- 📚 **Learn:** Java is always pass-by-value (a copy of a primitive or of a reference), so `swap(a, b)` fails; overload resolution order: exact -> widening -> boxing -> varargs. Recursion: a method calls itself on a smaller input and stops at a base case; every call pushes a stack frame (parameters, locals, return point) and a missing base case ends in `StackOverflowError`. Read: [Baeldung: Pass-by-value](https://www.baeldung.com/java-pass-by-value-or-pass-by-reference). Optional: [Baeldung: Recursion in Java](https://www.baeldung.com/java-recursion).
- 🛠️ **Do:** Write `PassByValueDemo`: `swap(int,int)`, `reassign(int[])` vs `mutate(int[])`, `append(StringBuilder)`; predict each output first. Call `print(5)` with overloads `print(long)`, `print(Integer)`, `print(int...)` and delete one at a time. Then `w01.Recursion`: `factorial(n)`, `sumDigits(n)`, `power(b, e)`; draw the stack frames of `factorial(4)` on paper, step through it in the IntelliJ debugger (Frames view) and trigger a `StackOverflowError` by removing the base case. Done when: predictions are recorded and your drawing matches the debugger.

### Friday 30 Oct · 60 min — static vs instance, arrays, String basics
- 📚 **Learn:** Class-level vs object-level members, why `main` is static, no `this` in a static context; arrays (defaults, `length`, 2D, `Arrays.toString/sort/copyOf`); String basics (`charAt`, `substring`, `split`, `equals`, immutability preview). Read: [Oracle: Class members](https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html). Optional: [dev.java: Arrays](https://dev.java/learn/language/constructs/basics/arrays/).
- 🛠️ **Do:** Write `Ticket` with static `totalIssued` and instance `seatNo`; create 3 objects and print both. Then katas: second largest, rotate by k, palindrome string, vowel count, reverse the words of a sentence. Done when: all 5 katas pass your hand-checked inputs (including an empty array or string) and are committed.

### Saturday 31 Oct · 60 min — BUILD: CLI Expense Tracker v0 with HashMap totals
- 📚 **Learn:** Plan before coding: a menu loop with `Scanner`, arrays for the entries (objects arrive in W2), one static method per menu action, input validation. Your first map: `HashMap<String, Double>` with `totals.put(cat, totals.getOrDefault(cat, 0.0) + amount)` sums per category in one pass. Read: [MOOC 8.2: Hash map](https://java-programming.mooc.fi/part-8/2-hash-map) (first half). Optional: [MOOC 1.3: Reading input](https://java-programming.mooc.fi/part-1/3-reading).
- 🛠️ **Do:** Build `w01.expense.ExpenseTrackerApp`: menu 1 add, 2 list, 3 total, 4 total by category (a `HashMap<String, Double>` filled with `getOrDefault`), 5 highest expense, 0 exit; store up to 100 entries (amount, category, note) in arrays; reject negative amounts and unknown options without crashing. Push with a README (how to run + sample session). Done when: you add 5 expenses, see correct totals by category, and the commit is visible on GitHub.

## 📦 Deliverable (by Saturday night)
`java-mastery` on GitHub with package `w01`: Hello + javap notes, NumberTraps, Katas + Bits, PassByValueDemo + Recursion, Ticket, Expense Tracker v0 (HashMap totals) + README; Corretto 25, IntelliJ and Git working.

## ✅ Self-check (Sunday test preview)
- What is the difference between JDK, JRE and JVM, and what exactly does javac produce?
- Is Java pass-by-value or pass-by-reference? Prove it with an object example.
- Why does `Integer a = 128, b = 128; a == b` print false while 127 prints true?
- Given overloads m(long), m(Integer) and m(int...), which one does `m(5)` call and why?
- What do `-16 >> 2` and `-16 >>> 28` print, and why do they differ?
- What is a stack frame, and why does recursion without a base case end in StackOverflowError?
- Why is `main` static? Can a static method read an instance field directly?
- How does `getOrDefault` turn 'total per category' into a one-line update?

## 🚀 Stretch (optional)
Run `javap -c` on a class with a loop and an instance method call; explain `invokestatic` vs `invokevirtual` in two lines. Extra katas: number pyramid (n=5), Armstrong number, max/min and in-place reverse of an array; the next day, rewrite one kata from memory. Predict `System.out.println(1 + 2 + "3" + 4 + 5)`.
