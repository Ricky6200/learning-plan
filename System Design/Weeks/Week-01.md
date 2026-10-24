# 🏗️ System Design · Week 01 — SD interviews, the web, and UML

> 📅 **Mon 26 Oct 2026 → Sun 01 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-01.md) · [Week 02 →](Week-02.md)

**Why this week:** LLD and HLD rounds both start from shared basics: how a request travels the web and how to sketch classes and interactions clearly. This week builds that vocabulary and your `system-design-lab` repo.

## 🗓️ Sessions

### Monday 26 Oct · 45 min — SD rounds decoded + what happens when you type a URL
- 📚 **Learn:** LLD/machine-coding rounds (60-120 min, working code) vs HLD rounds (45-60 min, whiteboard). URL journey: DNS -> TCP handshake -> TLS -> HTTP request -> load balancer/server -> response -> render. Watch [What happens when you type a URL (ByteByteGo)](https://www.youtube.com/watch?v=AlkDbnbv7dk) and [What is LLD (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=mQM3V8E13yc); skim [alex/what-happens-when](https://github.com/alex/what-happens-when).
- 🛠️ **Do:** Create GitHub repo `system-design-lab` and clone it into `C:\dev\personal` (Maven, JDK 25 - until it arrives use JDK 11 with `maven.compiler.release` 11 - JUnit 6 Jupiter + AssertJ; folders `notes/`, `hld/`, `boss/`, package `com.sdlab`). Write `notes/01-url-journey.md`: 10 numbered steps naming the protocol at each step, plus a Mermaid sequence diagram (Browser, DNS resolver, Server). Done when: the repo is pushed and you can narrate the journey aloud in 3 minutes without notes (record a voice memo).

### Wednesday 28 Oct · 45 min — UML class diagrams: relationships and multiplicity
- 📚 **Learn:** Class box (fields, methods, visibility), association vs aggregation vs composition, inheritance vs realization (interface), dependency, multiplicity (1, 0..*, 1..*). Watch [UML class diagrams (Lucid)](https://www.youtube.com/watch?v=6XrL5jXmTwM); syntax reference: [Mermaid classDiagram](https://mermaid.js.org/syntax/classDiagram.html).
- 🛠️ **Do:** In `notes/02-uml.md`, draw a Mermaid class diagram for a Library: `Library`, `Book`, `BookCopy`, `Member`, `Loan`, `Librarian`, enum `CopyStatus`, interface `SearchService`. Use at least one composition, aggregation, inheritance and realization. Done when: it renders on GitHub, every relationship has multiplicity, and you can justify composition vs aggregation for two arrows in one sentence each.

### Thursday 29 Oct · 45 min — Sequence diagrams + OOP pillars from a design view
- 📚 **Learn:** Sequence diagrams: lifelines, sync vs async messages, returns, `alt`/`loop` fragments. OOP as design tools: encapsulation protects invariants, abstraction = interfaces, polymorphism replaces if/else, prefer composition over inheritance. Watch [How to make a UML sequence diagram (Lucid)](https://www.youtube.com/watch?v=pCK6prSq8aw); read [OOP concepts for LLD (Hello Interview)](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/oop-concepts).
- 🛠️ **Do:** Add two Mermaid sequence diagrams to `notes/02-uml.md`: (1) member borrows a book (Member -> LibraryService -> Inventory -> LoanRepository, with an `alt` for 'no copy available'); (2) Monday's URL journey. Then write one concrete example per OOP pillar from your Library model. Done when: both diagrams render and each pillar maps to a real class or method.

### Saturday 31 Oct · 45 min — PRACTICE: Bank or Library class diagram + Java skeleton
- 📚 **Learn:** What interviewers check in a class diagram: clear responsibilities, correct relationships, enums for states, interfaces at extension points, no god classes. References: [Library management problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/library-management-system.md) and [OOD solutions (system-design-primer)](https://github.com/donnemartin/system-design-primer/tree/master/solutions/object_oriented_design).
- 🛠️ **Do:** Timebox 45 min. 10 min: 6 functional requirements for a Bank (accounts, deposit/withdraw, transfer, statement) or Library. 20 min: full class diagram (>= 8 classes, 1 enum, 1 interface). 15 min: Java skeleton in `com.sdlab.lld.bank` (fields + method signatures only). Done when: `mvn -q compile` passes and diagram + skeleton are committed with 2 self-review notes ('what changes if...').

## 📦 Deliverable (by Saturday night)
`system-design-lab` repo pushed with `notes/01-url-journey.md`, `notes/02-uml.md` (class diagram + 2 sequence diagrams) and a compiling Bank or Library skeleton.

## ✅ Self-check (Sunday test preview)
- Walk me through what happens after you type https://www.example.com and press Enter.
- How does an LLD/machine-coding round differ from an HLD round, and what is each scored on?
- Composition vs aggregation vs association: give one Library example of each.
- When do you prefer composition over inheritance? Give a Java example.
- What does TLS add to a TCP connection, and why does HTTPS need a certificate?
- In a sequence diagram, how do you show an if/else branch and a loop?

## 🚀 Stretch (optional)
Read the DNS and TLS parts of alex/what-happens-when and add 3 details you did not know to your URL-journey note.
