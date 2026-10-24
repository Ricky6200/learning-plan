# 🧩 DSA · Week 22 — DP IV: Stocks, Intervals, Trees, Bitmask

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Advanced DP patterns appear in senior/product rounds; knowing the state-machine and interval views is enough.

## 🧠 Concepts to master
- Stock state machines (hold/sold/cooldown; k transactions)
- Partition DP; interval DP (think of the LAST action: burst balloons, cut stick)
- DP on trees (return a pair; 3-state cameras)
- Memoized DFS on grids (longest increasing path)
- Bitmask DP / BFS over (node, mask)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [NeetCode - Dynamic Programming](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO)
- [cp-algorithms](https://cp-algorithms.com/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 22 Mar | [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | 25m | ☐ |
|  |  | [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | 25m | ☐ |
| Tue | 23 Mar | [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | Medium | 25m | ☐ |
|  |  | [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) | Hard | 40m | ☐ |
| Wed | 24 Mar | [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/) | Hard | 40m | ☐ |
|  |  | [1043. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) | Medium | 25m | ☐ |
| Thu | 25 Mar | [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | 40m | ☐ |
|  |  | [1626. Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/) | Medium | 25m | ☐ |
| Fri | 26 Mar | [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) | Medium | 25m | ☐ |
|  |  | [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) | Hard | 40m | ☐ |
| Sat | 27 Mar | [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | Medium | 25m | ☐ |
|  |  | [375. Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) | Medium | 25m | ☐ |
|  |  | [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) (H)
- [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) (H)
- [1000. Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) (H)
- [902. Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) (H)
- [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) (H)
- [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) (H)
- [198. House Robber](https://leetcode.com/problems/house-robber/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Draw the state machine for stock with cooldown.
- Burst Balloons: why choose the LAST balloon to burst?
- House Robber III: what does each node return?
- Partition to K Equal Sum Subsets: how can a bitmask represent the used elements?
- When is bitmask DP feasible (n limit)?

## 💡 Tip
If n <= 20, think bitmask; if the problem is about splitting a range, think interval DP.
