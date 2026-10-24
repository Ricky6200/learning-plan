# 🏗️ System Design · Week 26 — TicketVerse story and final mocks (Final Boss)

> 📅 **Mon 19 Apr 2027 → Sun 25 Apr 2027** · Season 6 — Final Boss: The Offer · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 25](Week-25.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-26.md)

**Why this week:** Your strongest interview story is the system you built: TicketVerse, explained with trade-offs, numbers and failure modes, plus two final mocks to prove readiness.

## 🗓️ Sessions

### Monday 19 Apr · 45 min — TicketVerse architecture as an interview story
- 📚 **Learn:** Story arc: problem -> requirements and scale -> architecture evolution (monolith -> microservices -> Kafka saga + outbox -> Kubernetes -> Azure -> AI assistant) -> key decisions with alternatives rejected -> numbers -> what you would do next. Anchor the booking part on [Design Ticketmaster (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/ticketmaster) and the reliability part on the [Azure Well-Architected disaster recovery guide](https://learn.microsoft.com/en-us/azure/well-architected/reliability/disaster-recovery).
- 🛠️ **Do:** Write `hld/19-ticketverse/README.md`: a one-page architecture story with a current-state diagram, 5 key decisions (decision, alternatives, why), and real numbers from your load tests or reasonable estimates. Done when: you can tell the story in 5 minutes without notes (record it).

### Wednesday 21 Apr · 45 min — TicketVerse at 10x and 100x: bottlenecks and failure modes
- 📚 **Learn:** Capacity planning: find the first bottleneck at each scale (DB writes, seat-hold contention, Kafka partitions, gateway). Failure-mode analysis: component -> failure -> detection -> mitigation -> user impact. Reference: [Static stability using Availability Zones (AWS Builders' Library)](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) and [Circuit Breaker pattern (Azure)](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker).
- 🛠️ **Do:** Add to the TicketVerse write-up: a 10x and a 100x plan (what breaks first and the fix: read replicas, sharding bookings by event, more partitions, waiting room, multi-region) and an FMEA table with >= 8 rows. Done when: each row has detection + mitigation and the 100x plan names its biggest cost.

### Thursday 22 Apr · 45 min — Final rapid-fire round + LLD design-only drill
- 📚 **Learn:** Rapid-fire: 20 concept questions in 20 minutes from all self-checks (AI mentor picks; mix LLD patterns, concurrency, databases, caching, queues, consistency). Drill: design-only LLD (diagram + interfaces, no code) in 20 minutes. Revise from your `HLD_INTERVIEW_FRAMEWORK.md`, `LLD_MACHINE_CODING_FRAMEWORK.md` and the [Hello Interview LLD delivery guide](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/delivery).
- 🛠️ **Do:** 20 min rapid-fire (answer each in under a minute; mark misses), 20 min LLD design drill on a random unseen problem, 5 min logging. Done when: misses are added to the weakness tracker with a 1-line correct answer each.

### Saturday 24 Apr · 45 min — BOSS BATTLE: Final LLD + HLD mock (TicketVerse)
- 📚 **Learn:** Final boss rules: an AI mentor or peer interviews you; 20 min LLD (seat-hold classes + a concurrency-safe `hold()` sketch in Java) then 25 min HLD (TicketVerse at 100x with trade-offs and failure handling). Use your Monday story; quick refresher: [Concurrency in LLD interviews (Hello Interview)](https://www.youtube.com/watch?v=d8rmosXttTE).
- 🛠️ **Do:** Run the 45-minute mock, recorded, with at least 4 interviewer follow-ups. Score LLD (model, code, concurrency: 0-3 each) and HLD (8-line rubric). Done when: `boss/W26.md` has both scores; >= 7/9 LLD and >= 18/24 HLD clears the final boss and you are interview-ready.

## 📦 Deliverable (by Saturday night)
`hld/19-ticketverse/` (story, diagrams, 10x/100x plan, FMEA), the rapid-fire log, and the Final Boss recording + scorecard in `boss/W26.md`.

## ✅ Self-check (Sunday test preview)
- Tell me about a system you designed end to end (TicketVerse) in 5 minutes.
- What breaks first in TicketVerse at 100x traffic, and how do you fix it?
- Why did you use a saga instead of distributed transactions for booking + payment?
- How do you guarantee a seat is never sold twice across services?
- What would you change if you rebuilt TicketVerse today?
- Which trade-off in TicketVerse are you least sure about, and why?

## 🚀 Stretch (optional)
Turn the TicketVerse story into a 1-page README section for your portfolio and a 2-minute version for the 'tell me about a project' question.
