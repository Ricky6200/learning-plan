# 🗓️ Week 09 · 21 Dec → 27 Dec 2026 · Season 2 — Concurrency Crucible

> ⚔️ **BOSS WEEK** — Saturday blocks are timed Boss Battles; beat the boss on Sunday for +300 XP  
> 🏁 Milestone: ⚔️ Boss S2  
> 🐳 **Docker needed from Mon 28 Dec** (Java Week 10). Not approved on the company laptop yet? Run the Java container weeks in a Codespace on your personal GitHub account. Next Wednesday's VisualVM/JMC aren't installed — the JDK's own `jcmd` and `jfr` tools cover the exercise.  
> 🎉 Fri 25 Dec: 🎄 **Christmas** — Lite day allowed (1 DSA problem + 30 min Java); catch up in Sunday's preview slot  
> ⭐ XP available: ~810 (blocks 250 · DSA 160 · test 100 · boss 300)  

**Open the details:** [🧩 DSA](../DSA/Weeks/Week-09.md) · [☕ Java Backend](../Java%20%2B%20Spring%20%2B%20Microservices%20%2B%20Kafka%20%2B%20Docker%20%2B%20Kubernetes/Weeks/Week-09.md) · [🤖 AI Engineering](../AI%20Engineering/Weeks/Week-09.md) · [🏗️ System Design](../System%20Design/Weeks/Week-09.md) · [☁️ Azure Cloud](../Azure%20Cloud/Weeks/Week-09.md)  
**Tracker:** [Dashboard](../00_Progress_Tracker/PROGRESS_DASHBOARD.md) · [Daily log](../00_Progress_Tracker/DAILY_LOG.md) · [Weakness tracker](../00_Progress_Tracker/WEAKNESS_TRACKER.md)

## 🎯 This week's mission
| Track | Theme |
|---|---|
| 🧩 DSA | Backtracking II + Season 2 Review - BOSS week |
| ☕ Java Backend | Concurrency II: locks, atomics, async, virtual threads |
| 🤖 AI Engineering | Evals: Prove DocuMind Works |
| 🏗️ System Design | Splitwise, library, message queues (Boss week) |
| ☁️ Azure Cloud | Storage II: Files, blob protection + Boss |

## 🔧 Fix-it items (added by your AI mentor after last Sunday's test)
- [ ] _none yet — the mentor fills this in after each test_

## Monday · 21 Dec · 3.5 h
- [ ] 🧩 **DSA · 60m** — Solve: [LC 79 · Word Search](https://leetcode.com/problems/word-search/) (M) · [LC 131 · Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (M)
- [ ] ☕ **Java · 60m** — ReentrantLock, tryLock, fairness, Condition, ReadWriteLock, StampedLock
- [ ] 🤖 **AI Engineering · 45m** — Golden datasets and error analysis
- [ ] 🏗️ **System Design · 45m** — Message queues & streaming: Kafka vs RabbitMQ vs Service Bus

## Tuesday · 22 Dec · 3.5 h
- [ ] 🧩 **DSA · 60m** — Solve: [LC 51 · N-Queens](https://leetcode.com/problems/n-queens/) (H) · [LC 473 · Matchsticks to Square](https://leetcode.com/problems/matchsticks-to-square/) (M)
- [ ] ☕ **Java · 60m** — Atomics, CAS, LongAdder and ConcurrentHashMap internals
- [ ] ☁️ **Azure Cloud · 45m** — Azure Files: shares, snapshots, soft delete, identity-based access
- [ ] 🤖 **AI Engineering · 45m** — Retrieval metrics: recall@k, MRR, nDCG

## Wednesday · 23 Dec · 3.5 h
- [ ] 🧩 **DSA · 60m** — Solve: [LC 37 · Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) (H) · [LC 93 · Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/) (M)
- [ ] ☕ **Java · 60m** — Concurrent collections and synchronizers: latch, barrier, semaphore
- [ ] 🏗️ **System Design · 45m** — Splitwise LLD: expenses, split types, balances
- [ ] ☁️ **Azure Cloud · 45m** — Blob containers, tiers, soft delete and versioning

## Thursday · 24 Dec · 3.5 h
- [ ] 🧩 **DSA · 60m** — Solve: [LC 16 · 3Sum Closest](https://leetcode.com/problems/3sum-closest/) (M) · [LC 1838 · Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element/) (M)
- [ ] ☕ **Java · 60m** — CompletableFuture: compose, combine, allOf, errors, custom executors
- [ ] 🤖 **AI Engineering · 45m** — Generation metrics with RAGAS/DeepEval; judge pitfalls
- [ ] 🏗️ **System Design · 45m** — Simplify debts + Library management core

## Friday · 25 Dec · 3.5 h · 🎉
> 🎄 **Christmas** — Lite day allowed (1 DSA problem + 30 min Java); catch up in Sunday's preview slot

- [ ] 🧩 **DSA · 60m** — Solve: [LC 287 · Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) (M) · [LC 41 · First Missing Positive](https://leetcode.com/problems/first-missing-positive/) (H)
- [ ] ☕ **Java · 60m** — ForkJoin work stealing, virtual threads deep dive, ThreadLocal pitfalls
- [ ] ☁️ **Azure Cloud · 45m** — Blob lifecycle management + Boss prep cheat sheet
- [ ] 🤖 **AI Engineering · 45m** — Tracing and experiments with Langfuse

## Saturday · 26 Dec · 4.5 h
- [ ] 🧩 **DSA · 60m** — Solve: [LC 1208 · Get Equal Substrings Within Budget](https://leetcode.com/problems/get-equal-substrings-within-budget/) (M) · [LC 1760 · Minimum Limit of Balls in a Bag](https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/) (M) · [LC 1239 · Maximum Length of a Concatenated String with Unique Characters](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/) (M) 🔥 weekend challenge
- [ ] ☕ **Java · 60m** — BOSS BATTLE: Concurrency gauntlet, 60 min timed
- [ ] 🤖 **AI Engineering · 45m** — BOSS BATTLE: DocuMind eval report in 45 minutes
- [ ] 🏗️ **System Design · 45m** — BOSS BATTLE: Timed Splitwise core + 5 rapid HLD questions
- [ ] ☁️ **Azure Cloud · 60m** — BOSS BATTLE: Identity + storage admin challenge (timed, CLI only)

## Sunday · 27 Dec · 3.5 h — ⚔️ BOSS BATTLE TEST
- [ ] (Optional, 8:00 AM IST) [LeetCode Weekly Contest](https://leetcode.com/contest/) — great practice from Week 8 onward
- [ ] 📝 **Weekly test · 150m** — start a session and paste: `Read 00_Progress_Tracker\AI_MEMORY.md and WEEKLY_TEST_PROTOCOL.md. Run my Week 9 test now.`
- [ ] 🔍 **Retro · 30m** — mentor updates scoreboard, weak areas, XP; you note 1 win + 1 fix
- [ ] 👀 **Preview & revise · 30m** — finish the 🔥 weekend challenge if pending · DSA spaced revision (in the DSA week file) · skim next week

## 📊 Scorecard (filled after the test)
| Track | Score /100 | Status | Weak topics |
|---|---|---|---|
| DSA | | | |
| Java | | | |
| System Design | | | |
| AI | | | |
| Azure | | | |
| **Overall** | | | |

[← Week 08](Week-08.md) · [Master calendar](../01_MASTER_CALENDAR.md) · [Week 10 →](Week-10.md)
