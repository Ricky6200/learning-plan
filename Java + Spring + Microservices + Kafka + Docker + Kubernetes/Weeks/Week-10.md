# ☕ Java Backend · Week 10 — Core Java gaps: I/O, copies, reflection, Mockito, regex

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** Interviewers still probe file I/O, serialization, deep copies and how annotations work, and every Spring codebase is tested with Mockito and AssertJ; closing these gaps now means Spring's 'magic' (reflection, proxies, mocks) is familiar before you meet it.

## 🗓️ Sessions

### Monday 28 Dec · 60 min — File I/O and NIO.2: Path, Files, buffered text
- 📚 **Learn:** Byte streams vs character readers/writers, buffering, always passing a charset (UTF-8); NIO.2: `Path.of`, `Files.readAllLines`, `Files.lines` (close it with try-with-resources), `Files.newBufferedReader/Writer`, `Files.writeString`, `Files.walk`, `Files.copy/move` with `REPLACE_EXISTING`; `NoSuchFileException`. Read: [dev.java: Java I/O API](https://dev.java/learn/java-io/) (file system and reading/writing parts, about 15 min). Optional: [JUnit: built-in extensions (@TempDir)](https://docs.junit.org/current/writing-tests/built-in-extensions.html).
- 🛠️ **Do:** In `w10.io` write `NotesStats`: walk a folder with `Files.walk`, count lines and words per `.md`/`.txt` file with a buffered UTF-8 reader, write `summary.csv` with `Files.writeString`, and copy the largest file to `archive/` with `REPLACE_EXISTING`. Add 3 JUnit tests using `@TempDir` (missing folder, empty file, non-ASCII text such as Hindi). Done when: tests are green and the summary for your own `notes/` folder matches a manual count for one file.

### Tuesday 29 Dec · 60 min — Serialization, transient, and shallow vs deep copy
- 📚 **Learn:** `Serializable`, `ObjectOutputStream/ObjectInputStream`, `serialVersionUID`; `transient` and static fields are not written (transient fields come back as 0/null); Java serialization is a known security risk (deserialization attacks), so APIs exchange JSON (Jackson) instead. A shallow copy shares nested objects (default `clone()`, copying a list reference); a deep copy duplicates the object graph (copy constructors or factories). Read: [Baeldung: Introduction to Java serialization](https://www.baeldung.com/java-serialization). Optional: [Baeldung: How to make a deep copy](https://www.baeldung.com/java-deep-copy).
- 🛠️ **Do:** Serialize `Session(user, transient password, List<String> cart)` to a file and back; show `password` returns null; change the class's `serialVersionUID` and watch the old file fail to load. Then give `Order` a mutable `List<Item>`: shallow-copy it and mutate an item to prove sharing, then add a deep-copying copy constructor. Done when: transient, serialVersionUID and shallow vs deep behaviour are each proven by a passing test.

### Wednesday 30 Dec · 60 min — Reflection and annotations: a 50-line DI container
- 📚 **Learn:** `Class<?>` objects, `getDeclaredConstructors/Fields/Methods`, `newInstance`, `setAccessible`; annotations are metadata: `@Retention(RUNTIME)` keeps them for reflection and `@Target` limits where they go; Spring, JUnit and Jackson scan classes and read annotations this way; reflection is slower and skips compile-time checks. Read: [dev.java: Reflection](https://dev.java/learn/reflection/) (intro, classes, constructors). Optional: [Baeldung: Creating a custom annotation](https://www.baeldung.com/java-custom-annotation).
- 🛠️ **Do:** In `w10.di` define `@Component` (RUNTIME, TYPE) and write `MiniContainer` (about 50 lines): given a list of classes, keep the `@Component` ones, create each through its only constructor, resolve constructor parameters recursively and cache singletons in a `Map<Class<?>, Object>`. Wire `OrderService -> PaymentGateway + Notifier`. Done when: `get(OrderService.class)` returns a fully wired object, the same instance twice, and a missing dependency fails with a clear message.

### Thursday 31 Dec · 60 min — Test doubles with Mockito and AssertJ
- 📚 **Learn:** Test doubles: stub (canned answers), fake (light working version), spy (real object that records calls), mock (verifies interactions). Mockito: `@ExtendWith(MockitoExtension.class)`, `@Mock`, `@InjectMocks`, `when(...).thenReturn/thenThrow`, `verify(mock, times(1))`, `never()`, `ArgumentCaptor`. AssertJ: `assertThat(x).isEqualTo(...)`, `containsExactly`, `assertThatThrownBy(...)`. On JDK 21+ add Mockito as a Surefire `-javaagent` to silence its self-attach warning (Mockito Javadoc section 0.3). Read: [Baeldung: Mockito annotations](https://www.baeldung.com/mockito-annotations). Optional: [Martin Fowler: Test double](https://martinfowler.com/bliki/TestDouble.html).
- 🛠️ **Do:** Add `mockito-junit-jupiter` and `assertj-core` (test scope) to `java-mastery`. Give the W4 library service a `LoanRepository` and a `Notifier` constructor dependency. With mocks, test: a borrow saves one loan and notifies once (`verify`); a member at the limit gets an exception and nothing is saved (`never()`); an `ArgumentCaptor` checks the saved loan's due date. Rewrite 3 old assertions in AssertJ style. Done when: 5 Mockito tests pass and no test touches real storage.

### Friday 01 Jan · 60 min — Regex essentials, plus a concurrency re-drill
- 📚 **Learn:** Compile a `Pattern` once and reuse it; `matcher.matches()` (whole string) vs `find()` (anywhere); classes `\d \w \s` and `[A-Z]`; quantifiers `* + ? {n,m}`; greedy `.*` vs lazy `.*?`; anchors `^ $`; groups and named groups `(?<level>...)`; `String.split` takes a regex, so escape `.` and `|`. Read: [dev.java: Regular expressions](https://dev.java/learn/regex/) (about 15 min). Optional: [regex101](https://regex101.com/) to test patterns (pick the Java flavor).
- 🛠️ **Do:** In `w10.regex` parse 5 log lines like `2027-01-01 10:15:02 ERROR [booking] Seat 12 failed` into a record using named groups. Validate Indian formats with `@ParameterizedTest` (3 valid + 3 invalid each): PAN (`ABCDE1234F`: 5 letters, 4 digits, 1 letter), IFSC (4 letters, a 0, 6 letters or digits), a 10-digit mobile starting with 6-9. Re-drill from memory (10 min): main waits on a `CountDownLatch` for 3 worker threads. New Year lite day: the log parser alone is enough. Done when: all parameterized cases pass and the latch demo prints 'all done' last.

### Saturday 02 Jan · 60 min — BUILD: Timed rewrite of the W4 library: records, streams, mocks
- 📚 **Learn:** Rewrite, don't patch: a 35-minute timer, fresh package `w10.library`, no peeking at W4 code. Use records for value types (`Book`, `Loan`), streams and collectors for queries, an injected `Clock` for due dates (W7), a mocked `Notifier` (Thursday), AssertJ assertions and a regex ISBN check (Friday); then compare with your W4 boss version to see how far you have come. Reference: [AssertJ documentation](https://assertj.github.io/doc/) (core assertions guide).
- 🛠️ **Do:** Rebuild: `Book(isbn, title, author, year)` validates a 13-digit ISBN in its compact constructor; `LibraryService(repo, notifier, clock)` with borrow (max 3 per member, no double borrow), return, `search(text)` via streams and `overdueByMember()` via `groupingBy`; 6 AssertJ/Mockito tests. Afterwards, write a 5-line comparison with W4 (lines of code, test count, what got simpler). Done when: the tests are green within the 35-minute timer and the comparison is in the README.

## 📦 Deliverable (by Saturday night)
`w10` package: NotesStats (NIO.2) with `@TempDir` tests, serialization and deep-copy tests, MiniContainer (reflective DI), Mockito/AssertJ library tests, regex log parser and validators, a timed library rewrite with a W4-vs-W10 comparison.

## ✅ Self-check (Sunday test preview)
- Why must a `Files.lines` stream be closed, and how do you do it safely?
- What happens to `transient` and static fields during serialization? What is `serialVersionUID` for?
- Shallow vs deep copy: describe a bug that a shallow copy causes.
- How do frameworks like Spring and JUnit use reflection and annotations? Why `@Retention(RUNTIME)`?
- Mock vs stub vs fake vs spy: when would you use each?
- What should you not mock (value objects, types you don't own), and why?
- Greedy vs lazy: what do `<.*>` and `<.*?>` match in `<a><b>`? Why does `"a.b".split(".")` return an empty array?

## 🚀 Stretch (optional)
MiniContainer extras: detect dependency cycles with a clear message and resolve an interface to its single implementation. Serialize the `Session` record to JSON with Jackson and compare it with Java serialization. Try Mockito `spy` vs `mock` on a real `ArrayList`. Read why validating email addresses with a regex is a trap and what to do instead.
