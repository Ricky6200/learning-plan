# 🧩 DSA · Week 20 — DP II: Grids & Knapsack + Mixed Review - BOSS week

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Knapsack variants (subset sum, partition, target sum, coin change II) are interview staples. Saturday's boss mixes Season 4 graphs and DP. Job applications start this week.

## 🧠 Concepts to master
- Grid DP with obstacles; min path sum; triangle bottom-up
- Maximal square: dp = 1 + min(top, left, diagonal)
- 0/1 knapsack: subset sum, equal partition, target sum, last stone weight II
- Unbounded knapsack: coin change II (coins in the outer loop = combinations)
- Memoized DFS on a grid = DP on a DAG (329)
- Company-style prep from now on: pick 2-3 target companies, take their top-frequency free problems from a GitHub company-wise list and read LeetCode Discuss interview experiences

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Aditya Verma - DP (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [Company-wise LeetCode lists (free, GitHub)](https://github.com/snehasishroy/leetcode-companywise-interview-questions)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 08 Mar | [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | 25m | ☐ |
|  |  | [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Medium | 25m | ☐ |
| Tue | 09 Mar | [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | 25m | ☐ |
|  |  | [120. Triangle](https://leetcode.com/problems/triangle/) | Medium | 25m | ☐ |
| Wed | 10 Mar | [221. Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | 25m | ☐ |
|  |  | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 25m | ☐ |
| Thu | 11 Mar | [494. Target Sum](https://leetcode.com/problems/target-sum/) | Medium | 25m | ☐ |
|  |  | [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | 25m | ☐ |
| Fri | 12 Mar | [1049. Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) | Medium | 25m | ☐ |
| Sat | 13 Mar | [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) | Medium | 25m | ☐ |
|  |  | [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (E) | 10m |
| Tue | [198. House Robber](https://leetcode.com/problems/house-robber/) (M) | 20m |
| Wed | [91. Decode Ways](https://leetcode.com/problems/decode-ways/) (M) | 20m |
| Thu | [139. Word Break](https://leetcode.com/problems/word-break/) (M) | 20m |
| Fri | [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/) (M) | 20m |
| Sat | [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [931. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) (M)
- [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) (M)
- [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) (M)
- [1463. Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/) (H)
- [879. Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) (H)
- [1155. Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) (M)
- [576. Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) (M)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Coin Change II: why does the loop order matter (combinations vs permutations)?
- Reduce Target Sum to subset sum - derive the formula.
- How do you space-optimize 0/1 knapsack to 1D? Why iterate capacity backwards?
- Maximal Square: what is the transition?
- Last Stone Weight II: why is it a partition problem?
- Longest Increasing Path in a Matrix: why is memoized DFS enough (no visited set)?

## 💡 Tip
BOSS Saturday: LC 1091 + LC 329 timed (60 min, no hints). Online-assessment simulation #2 this week (90 min, full programs). From now on you talk aloud every week: a mock on non-contest Sundays, and on contest Sundays you explain your contest up-solve aloud.
