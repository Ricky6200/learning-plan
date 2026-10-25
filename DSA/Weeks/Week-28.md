# 🧩 DSA · Week 28 — Company-Frequency Sets

> 📅 **Mon 03 May 2027 → Sun 09 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 27](Week-27.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-28.md) · [Week 29 →](Week-29.md)

**Why this week:** Product companies and GCCs reuse a pool of favourites. Two mixed sets of frequently asked free problems you have not met yet, then your own target-company lists.

## 🧠 Concepts to master
- Company-wise lists (free on GitHub): pick 2-3 target companies, sort by frequency, skip Premium, solve the top ones you haven't done
- Read 5 recent LeetCode Discuss interview experiences per target company; note the round format and repeated problems
- Set A (Mon-Wed): stack, digits, tree paths and widths, tree-as-graph, heap simulation
- Set B (Thu-Sat): deque window, string-chain DP, Java threads with semaphores (1116), greedy digits, BFS with state (1293)
- Talking aloud: Sunday is a contest Sunday (explain your up-solve aloud); Week 29's Sunday mock uses your target-company list; add 1-2 peer mocks on Sets A/B if you can

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Company-wise LeetCode lists (free, GitHub)](https://github.com/snehasishroy/leetcode-companywise-interview-questions)
- [Company-wise interview problems (free, GitHub)](https://github.com/liquidslr/interview-company-wise-problems)
- [LeetCode Discuss - interview experiences](https://leetcode.com/discuss/interview-experience/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 03 May | [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | Medium | 25m | ☐ |
|  |  | [556. Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) | Medium | 25m | ☐ |
| Tue | 04 May | [2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) | Medium | 25m | ☐ |
|  |  | [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) | Medium | 25m | ☐ |
| Wed | 05 May | [2385. Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) | Medium | 25m | ☐ |
|  |  | [1834. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) | Medium | 25m | ☐ |
| Thu | 06 May | [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | Medium | 25m | ☐ |
|  |  | [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain/) | Medium | 25m | ☐ |
| Fri | 07 May | [1116. Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/) | Medium | 25m | ☐ |
| Sat | 08 May | [670. Maximum Swap](https://leetcode.com/problems/maximum-swap/) | Medium | 25m | ☐ |
|  |  | [1293. Shortest Path in a Grid with Obstacles Elimination](https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (H) | 35m |
| Tue | [862. Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) (H) | 35m |
| Wed | [493. Reverse Pairs](https://leetcode.com/problems/reverse-pairs/) (H) | 35m |
| Thu | [815. Bus Routes](https://leetcode.com/problems/bus-routes/) (H) | 35m |
| Fri | [140. Word Break II](https://leetcode.com/problems/word-break-ii/) (H) | 35m |
| Sat | [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) (M)
- [535. Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) (M)
- [1110. Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/) (M)
- [934. Shortest Bridge](https://leetcode.com/problems/shortest-bridge/) (M)
- [1530. Number of Good Leaf Nodes Pairs](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/) (M)
- [1405. Longest Happy String](https://leetcode.com/problems/longest-happy-string/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Remove All Adjacent Duplicates in String II: what does the stack store?
- Maximum Width of Binary Tree: how do you keep position indices from overflowing?
- Amount of Time for Binary Tree to Be Infected: why convert the tree to a graph?
- Single-Threaded CPU: which two orderings do you need?
- Print Zero Even Odd: how do semaphores hand the turn between threads?
- Shortest Path in a Grid with Obstacles Elimination: what is the BFS state?

## 💡 Tip
Weekly target: 3-5 problems from your target companies' lists in bonus time; log them in REVISION_TRACKER. Old favourites worth a re-solve: Vertical Order Traversal (987) and Candy (135).
