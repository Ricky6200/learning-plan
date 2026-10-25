# 🧩 DSA · Week 27 — Hard Bank: the deferred Hards

> 📅 **Mon 26 Apr 2027 → Sun 02 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 26](Week-26.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-27.md) · [Week 28 →](Week-28.md)

**Why this week:** All patterns are done; now face the Hards you skipped, one a day, so a Hard in a real interview feels familiar.

## 🧠 Concepts to master
- A Hard is usually two known patterns combined: name both before coding
- Monotonic stack (84); monotonic deque over prefix sums (862); merge-sort counting (493)
- BFS over routes instead of stops (815); memoized backtracking (140)
- Stock with k transactions (188); MST edge classification with DSU (1489)
- Optional: two virtual contests (90 min each) in bonus time this week or next; up-solve one Hard after each and explain it aloud

## 🎥 Learn from (pick ONE per topic — don't binge)
- [NeetCode practice list](https://neetcode.io/practice)
- [LeetCode contests](https://leetcode.com/contest/)
- [cp-algorithms](https://cp-algorithms.com/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (7 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 26 Apr | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | 40m | ☐ |
| Tue | 27 Apr | [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Hard | 40m | ☐ |
| Wed | 28 Apr | [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) | Hard | 40m | ☐ |
| Thu | 29 Apr | [815. Bus Routes](https://leetcode.com/problems/bus-routes/) | Hard | 40m | ☐ |
| Fri | 30 Apr | [140. Word Break II](https://leetcode.com/problems/word-break-ii/) | Hard | 40m | ☐ |
| Sat | 01 May | [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |
|  |  | [1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree](https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) (M) | 20m |
| Tue | [117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/) (M) | 20m |
| Wed | [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) (H) | 35m |
| Thu | [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) (M) | 20m |
| Fri | [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) (H) | 35m |
| Sat | [1146. Snapshot Array](https://leetcode.com/problems/snapshot-array/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) (H)
- [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) (H)
- [126. Word Ladder II](https://leetcode.com/problems/word-ladder-ii/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Largest Rectangle in Histogram: what do you compute for each bar?
- Shortest Subarray with Sum at Least K: why does a deque of prefix sums work with negatives?
- Reverse Pairs: why does merge sort help?
- Bus Routes: why BFS on routes instead of stops?
- Best Time to Buy and Sell Stock IV: what are the states?
- Critical edges in an MST: how do you test an edge with DSU?

## 💡 Tip
Hard-bank rules: 40-min first attempt; then read only the key idea, close it, code. If a re-solve is a Hard, cap it at 20 min. Weekly mock.
