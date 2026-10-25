# 🏗️ System Design · Week 28 — Machine-coding mocks: hotel booking, digital wallet

> 📅 **Mon 03 May 2027 → Sun 09 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 27](Week-27.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-28.md) · [Week 29 →](Week-29.md)

**Why this week:** Indian product companies still screen with 90-minute machine-coding rounds; two more full-length unseen mocks (one API-style, one command-line) make your W10 lessons stick before the final boss. TicketVerse goes live on Azure in the Java track this week.

## 🗓️ Sessions

### Monday 03 May · 45 min — Unseen mock A part 1: hotel booking (minutes 0-45)
- 📚 **Learn:** Mock rules as in W10: 90 minutes over Monday and Wednesday, no references, the playbook clock. This one is API-style: no CLI, demonstrate everything through JUnit tests. Use `LocalDate` (Java W7) and half-open stays [checkIn, checkOut). Read only after Wednesday: [Hotel management problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/hotel-management-system.md).
- 🛠️ **Do:** Problem (OYO-style): hotels have rooms of type STANDARD/DELUXE/SUITE with nightly prices; `search(city, type, checkIn, checkOut)` returns hotels with a free room, cheapest first; `book(user, hotelId, type, rooms, checkIn, checkOut)` is all-or-nothing; `cancel(bookingId, today)` refunds 100% if >= 2 days before check-in, else 50%; two users racing for the last room - exactly one wins. Today: assumptions, class diagram, model classes and `search`. Done when: the design is committed in `lld/mock-w28-hotel/` and 2 search tests pass.

### Wednesday 05 May · 45 min — Unseen mock A part 2: hotel booking (minutes 45-90) + score
- 📚 **Learn:** Second half: 45-70 `book` and `cancel` (overlap rule `checkIn < otherOut && otherIn < checkOut`, one lock per hotel or per room type), 70-80 tests including a race test, 80-90 refactor + README of assumptions and extension points. Score 0-3 on requirements, model, patterns, working code, tests, concurrency, communication. Afterwards compare with the [Hotel management problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/hotel-management-system.md) write-up.
- 🛠️ **Do:** Finish `book` + `cancel` with refunds, then write tests for overlapping stays, a back-to-back stay (allowed), the refund rule, and 20 threads booking the last room. Done when: all tests pass, the 7-line scorecard is in `mocks/W28-hotel.md`, and 2 extension answers (dynamic pricing, room upgrades) are written.

### Thursday 06 May · 45 min — Unseen mock B part 1: digital wallet CLI (minutes 0-45)
- 📚 **Learn:** Mock rules again, now with command-line input (as in W10). Money is `long` paise. A transfer touches two wallets: lock both in a fixed order (W10 Mon) and make it all-or-nothing. Read only after Saturday: [Digital wallet problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/digital-wallet-service.md).
- 🛠️ **Do:** Problem (PhonePe/Razorpay-style wallet CLI). Commands: `CREATE_WALLET <user> <amount>`, `TRANSFER <from> <to> <amount>` (reject insufficient balance and amounts below 0.01), `STATEMENT <user>` (newest first), `OVERVIEW` (all balances), `OFFER2` (top 3 users by transaction count get Rs 10/5/2 cashback). Offer 1: a transfer that leaves both users with equal balances credits each Rs 10. Today: assumptions, model, parser, `CREATE_WALLET` + `TRANSFER` in `lld/mock-w28-wallet/`. Done when: a sample input file runs those two commands correctly.

### Saturday 08 May · 45 min — PRACTICE: Unseen mock B part 2 (minutes 45-90) + review
- 📚 **Learn:** Second half: 45-70 `STATEMENT`, `OVERVIEW`, both offers; 70-80 tests: a scripted input file plus a race test (100 threads transferring in both directions between two wallets must not deadlock or lose money); 80-90 refactor + score. Compare both W28 scorecards with W10's (what improved, what still costs you time?), then read [Digital wallet problem (awesome-low-level-design)](https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/digital-wallet-service.md).
- 🛠️ **Do:** Finish the remaining commands and tests, then run the full input file. Done when: total money is conserved in the race test, the output matches your expected file, the scorecard is in `mocks/W28-wallet.md`, and `mocks/W28-review.md` lists 3 habits that improved since W10 and 2 still to fix.

## 📦 Deliverable (by Saturday night)
Two complete 90-minute mocks (`lld/mock-w28-hotel/`, `lld/mock-w28-wallet/`) with tests, input files and scorecards in `mocks/`, plus the W10-vs-W28 review.

## ✅ Self-check (Sunday test preview)
- How do you model a hotel stay so that back-to-back bookings are allowed but overlaps are not?
- Two users try to book the last DELUXE room at the same time. Walk through your locking.
- Why do you lock two wallets in a fixed order during a transfer?
- How would you make `TRANSFER` idempotent if the client retries?
- How did you structure the command parser so a new command touches only one place?
- Where did you lose time in the two mocks compared with W10?

## 🚀 Stretch (optional)
Add idempotent transfers (a `requestId` per `TRANSFER`) and a `REVERSE <txnId>` command to the wallet; add dynamic weekend pricing to the hotel mock.
