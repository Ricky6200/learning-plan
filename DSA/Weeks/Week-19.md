# 🧩 DSA · Week 19 — Dynamic Programming I: 1D - BOSS week

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** DP is the most feared topic; a fixed method (recursion -> memo -> table -> space) makes it predictable.

## 🧠 Concepts to master
- State + transition + base case; recursion -> memoization -> tabulation -> space optimization
- Stairs / house robber (incl. circular)
- Decode ways, coin change (min coins), word break
- LIS O(n^2) and O(n log n) (patience sorting)
- Counting with order (combination sum IV) vs without order

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [Aditya Verma - DP (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)
- [NeetCode - Dynamic Programming](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

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
| Fri | 05 Mar | [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/) | Medium | 25m | ☐ |
|  |  | [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) | Medium | 25m | ☐ |
| Sat | 06 Mar | [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/) | Medium | 25m | ☐ |
|  |  | [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | Easy | 15m | ☐ |
|  |  | [2140. Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/) 🔥 *weekend challenge — finish Sunday if needed* | Medium | 25m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/) (M)
- [368. Largest Divisible Subset](https://leetcode.com/problems/largest-divisible-subset/) (M)
- [1048. Longest String Chain](https://leetcode.com/problems/longest-string-chain/) (M)
- [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/) (H)
- [1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) (H)
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Define the DP state for House Robber II.
- Coin Change: why is greedy wrong?
- LIS in O(n log n): what does the tails array mean?
- Memoization vs tabulation - pros/cons?
- Word Break: what is dp[i]?

## 💡 Tip
BOSS: Saturday problems must be solved recursion-first, then memoized, then tabulated.
