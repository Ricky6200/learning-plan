# 🧩 DSA · Week 22 — DP IV: Stocks, Intervals, Trees, Bitmask

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Advanced DP patterns appear in product rounds; knowing the state-machine and interval views is enough. Holi (Monday) is a one-problem day.

## 🧠 Concepts to master
- Stock state machines (hold/sold/cooldown; transaction fee)
- Partition DP; interval DP - think of the LAST action (burst balloons, guess-number minimax)
- DP on trees: return a pair (rob, skip)
- Bitmask: n <= 16 -> state = mask of used elements (698)
- Awareness: digit DP (count numbers <= N with a property; state = position + tight flag) and game DP (dp = best score difference; 486 in bonus) - both refreshed in Week 29

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [NeetCode - Dynamic Programming](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO)
- [cp-algorithms](https://cp-algorithms.com/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (9 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 22 Mar | [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) | Medium | 25m | ☐ |
| Tue | 23 Mar | [714. Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/) | Medium | 25m | ☐ |
|  |  | [337. House Robber III](https://leetcode.com/problems/house-robber-iii/) | Medium | 25m | ☐ |
| Wed | 24 Mar | [1043. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/) | Medium | 25m | ☐ |
|  |  | [375. Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) | Medium | 25m | ☐ |
| Thu | 25 Mar | [1626. Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/) | Medium | 25m | ☐ |
| Fri | 26 Mar | [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) | Medium | 25m | ☐ |
| Sat | 27 Mar | [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | 25m | ☐ |
|  |  | [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (M) | 20m |
| Tue | [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) (M) | 20m |
| Wed | [72. Edit Distance](https://leetcode.com/problems/edit-distance/) (M) | 20m |
| Thu | [97. Interleaving String](https://leetcode.com/problems/interleaving-string/) (M) | 20m |
| Fri | [1035. Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/) (M) | 20m |
| Sat | [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [123. Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/) (H)
- [968. Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/) (H)
- [486. Predict the Winner](https://leetcode.com/problems/predict-the-winner/) (M)
- [1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) (H)
- [847. Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) (H)
- [1000. Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) (H)
- [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Draw the state machine for Best Time to Buy and Sell Stock with Cooldown.
- Burst Balloons: why choose the LAST balloon to burst?
- House Robber III: what does each node return?
- Partition to K Equal Sum Subsets: how can a bitmask represent the used elements?
- Guess Number Higher or Lower II: why is it minimax interval DP?
- Best Team With No Conflicts: why sort first, and by what?

## 💡 Tip
If n <= 20, think bitmask; if the problem splits a range, think interval DP. Contest Sunday: explain your up-solve aloud; full-program practice this fortnight.
