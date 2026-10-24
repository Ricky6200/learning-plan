# 🧩 DSA · Week 20 — DP II: Grids & Knapsack

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Knapsack variants (subset sum, partition, target sum, coin change II) are interview staples.

## 🧠 Concepts to master
- Grid DP with obstacles; min path sum; triangle bottom-up
- Maximal square / count squares
- 0/1 knapsack: subset sum, equal partition, target sum (count subsets with difference)
- Unbounded knapsack: coin change II (loop order = combinations)
- 2-capacity knapsack (ones and zeroes); 3D DP intro (cherry pickup)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Aditya Verma - DP (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [NeetCode - Dynamic Programming](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 08 Mar | [62. Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | 25m | ☐ |
|  |  | [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Medium | 25m | ☐ |
| Tue | 09 Mar | [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | 25m | ☐ |
|  |  | [120. Triangle](https://leetcode.com/problems/triangle/) | Medium | 25m | ☐ |
| Wed | 10 Mar | [931. Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | Medium | 25m | ☐ |
|  |  | [221. Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | 25m | ☐ |
| Thu | 11 Mar | [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 25m | ☐ |
|  |  | [494. Target Sum](https://leetcode.com/problems/target-sum/) | Medium | 25m | ☐ |
| Fri | 12 Mar | [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | 25m | ☐ |
|  |  | [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | Medium | 25m | ☐ |
| Sat | 13 Mar | [1049. Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) | Medium | 25m | ☐ |
|  |  | [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Medium | 25m | ☐ |
|  |  | [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1463. Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/) (H)
- [879. Profitable Schemes](https://leetcode.com/problems/profitable-schemes/) (H)
- [1155. Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/) (M)
- [576. Out of Boundary Paths](https://leetcode.com/problems/out-of-boundary-paths/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [198. House Robber](https://leetcode.com/problems/house-robber/) (M)
- [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) (M)
- [127. Word Ladder](https://leetcode.com/problems/word-ladder/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Coin Change II: why does the loop order matter (combinations vs permutations)?
- Reduce Target Sum to subset-sum - derive the formula.
- How do you space-optimize a 0/1 knapsack to 1D? Why iterate capacity backwards?
- Maximal Square transition?
- Last Stone Weight II: why is it a partition problem?

## 💡 Tip
Aditya Verma's knapsack lectures map 1:1 to this week.
