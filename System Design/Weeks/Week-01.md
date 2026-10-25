# 🏗️ System Design · Week 01 — SD interviews, the web, and UML

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** LLD and HLD rounds both start from shared basics: how a request travels the web and how to sketch classes and interactions clearly. This week builds that vocabulary and your `system-design-lab` repo.

## 🗓️ Sessions

### Monday 26 Oct · 45 min — SD rounds decoded + what happens when you type a URL
- 📚 **Learn:** LLD/machine-coding rounds (60-120 min, working code) vs HLD rounds (45-60 min, whiteboard). URL journey: DNS -> TCP handshake -> TLS -> HTTP request -> load balancer/server -> response -> render. Watch [What happens when you type a URL (ByteByteGo, 5 min)](https://www.youtube.com/watch?v=AlkDbnbv7dk). Optional: [What is LLD (Concept && Coding, Hindi, 17 min)](https://www.youtube.com/watch?v=mQM3V8E13yc).
- 🛠️ **Do:** Create GitHub repo `system-design-lab`, clone it into `C:\dev\personal` and make it a Maven project (JDK 25 Corretto, the same company JFrog settings as `java-mastery`, JUnit 6 Jupiter + AssertJ test dependencies; folders `notes/`, `hld/`, `adr/`, `mocks/`, `boss/`; package `com.sdlab`). Add a one-assert `SmokeTest` copied from the [JUnit quick start](https://docs.junit.org/current/user-guide/#writing-tests). Write `notes/01-url-journey.md`: 10 numbered steps naming the protocol at each step. Done when: `mvn -q test` is green, the repo is pushed, and you can narrate the journey aloud in 3 minutes (voice memo).

### Wednesday 28 Oct · 45 min — UML class diagrams: relationships and multiplicity
- 📚 **Learn:** Class box (fields, methods, visibility), association vs aggregation vs composition, inheritance vs realization, dependency, multiplicity (1, 0..*, 1..*). Primer: inheritance = 'is-a' (`class Ebook extends Book`); an interface is a set of method signatures a class promises to implement; an enum is a fixed set of named constants (Java teaches all three properly in W2-W3). Watch [UML class diagrams (Lucid, 12 min)](https://www.youtube.com/watch?v=6XrL5jXmTwM). Optional: [Mermaid classDiagram syntax](https://mermaid.js.org/syntax/classDiagram.html).
- 🛠️ **Do:** In `notes/02-uml.md`, draw a Mermaid class diagram for a Library: `Library`, `Book`, `BookCopy`, `Member`, `Loan`, `Librarian`, enum `CopyStatus`, interface `SearchService`. Use at least one composition, aggregation, inheritance and realization. Done when: it renders on GitHub, every relationship has multiplicity, and you can justify composition vs aggregation for two arrows in one sentence each.

### Thursday 29 Oct · 45 min — Sequence diagrams + OOP pillars from a design view
- 📚 **Learn:** Sequence diagrams: lifelines, sync vs async messages, returns, `alt`/`loop` fragments. OOP as design tools: encapsulation protects invariants, abstraction hides details behind a small API, polymorphism replaces if/else, prefer composition over inheritance. Watch [How to make a UML sequence diagram (Lucid, 9 min)](https://www.youtube.com/watch?v=pCK6prSq8aw). Optional: [OOP concepts for LLD (Hello Interview)](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/oop-concepts).
- 🛠️ **Do:** Add two Mermaid sequence diagrams to `notes/02-uml.md`: (1) member borrows a book (Member -> LibraryService -> Inventory -> LoanRepository, with an `alt` for 'no copy available'); (2) Monday's URL journey. Then write one concrete example per OOP pillar from your Library model. Done when: both diagrams render and each pillar maps to a real class or method.

### Saturday 31 Oct · 45 min — PRACTICE: Hotel-booking class diagram + Java skeleton
- 📚 **Learn:** What interviewers check in a class diagram: clear responsibilities, correct relationships, enums for states, interfaces at extension points, no god classes. Code primer: `enum RoomStatus { AVAILABLE, BOOKED }` declares fixed constants; `interface PricingPolicy { long priceFor(Room room, int nights); }` declares a method that classes implement. See how good OOD answers are structured: [OOD solutions (system-design-primer)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/object_oriented_design).
- 🛠️ **Do:** Timebox 25 min. 5 min: 6 functional requirements for a small hotel (room types, search free rooms for dates, book, cancel, check-in/out, bill). 12 min: full class diagram (>= 7 classes, 1 enum, 1 interface). 8 min: Java skeleton in `com.sdlab.lld.hotel` (fields + method signatures only; methods return defaults). Done when: `mvn -q compile` passes and diagram + skeleton are committed with 2 self-review notes ('what changes if...').

## 📦 Deliverable (by Saturday night)
`system-design-lab` repo pushed (Maven build with a green `SmokeTest`) containing `notes/01-url-journey.md`, `notes/02-uml.md` (class diagram + 2 sequence diagrams) and a compiling hotel-booking skeleton.

## ✅ Self-check (Sunday test preview)
- Walk me through what happens after you type https://www.example.com and press Enter.
- How does an LLD/machine-coding round differ from an HLD round, and what is each scored on?
- Composition vs aggregation vs association: give one Library example of each.
- When do you prefer composition over inheritance? Give a Java example.
- What does TLS add to a TCP connection, and why does HTTPS need a certificate?
- In a sequence diagram, how do you show an if/else branch and a loop?

## 🚀 Stretch (optional)
Read the DNS and TLS parts of [alex/what-happens-when](https://github.com/alex/what-happens-when) and add 3 details you did not know to your URL-journey note.
