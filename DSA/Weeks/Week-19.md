# 🧩 DSA · Week 19 — Dynamic Programming I: 1D

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** DP is the most feared topic; a fixed method (recursion -> memo -> table -> space) makes it predictable.

## 🧠 Concepts to master
- State + transition + base case; recursion -> memoization -> tabulation -> space optimization
- Stairs / house robber (incl. circular)
- Decode ways, coin change (min coins), word break
- LIS O(n^2) and O(n log n) (patience sorting)
- Counting with order (combination sum IV) vs without order
- Weighted interval scheduling: sort by end + binary search the last compatible job (1235)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [Aditya Verma - DP (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)
- [NeetCode - Dynamic Programming](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 01 Mar | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | 15m | ☐ |
|  |  | [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | Easy | 15m | ☐ |
| Tue | 02 Mar | [198. House Robber](https://leetcode.com/problems/house-robber/) | Medium | 25m | ☐ |
|  |  | [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) | Medium | 25m | ☐ |
| Wed | 03 Mar | [91. Decode Ways](https://leetcode.com/problems/decode-ways/) | Medium | 25m | ☐ |
|  |  | [322. Coin Change](https://leetcode.com/problems/coin-change/) | Medium | 25m | ☐ |
| Thu | 04 Mar | [139. Word Break](https://leetcode.com/problems/word-break/) | Medium | 25m | ☐ |
|  |  | [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | 25m | ☐ |
| Fri | 05 Mar | [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Medium | 25m | ☐ |
| Sat | 06 Mar | [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/) | Medium | 25m | ☐ |
|  |  | [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) (M) | 20m |
| Tue | [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) (M) | 20m |
| Wed | [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) (M) | 20m |
| Thu | [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/) (M) | 20m |
| Fri | [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/) (M) | 20m |
| Sat | [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/) (M)
- [2140. Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/) (M)
- [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) (E)
- [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) (M)
- [368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Define the DP state for House Robber II.
- Coin Change: why is greedy wrong?
- LIS in O(n log n): what does the tails array mean?
- Delete and Earn: how does it reduce to House Robber?
- Word Break: what is dp[i]?
- Maximum Profit in Job Scheduling: what do you binary search for?

## 💡 Tip
Solve every problem recursion-first, then memoize, then tabulate. Online-assessment simulation #1 this fortnight: 90 min, 2-3 unseen problems, full stdin/stdout programs (use a Sunday slot).
