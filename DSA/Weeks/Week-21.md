# 🧩 DSA · Week 21 — DP III: Strings & Subsequences

> 📅 **Mon 15 Mar 2027 → Sun 21 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 20](Week-20.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-21.md) · [Week 22 →](Week-22.md)

**Why this week:** LCS/edit-distance families are asked at every level and are great for showing structured thinking.

## 🧠 Concepts to master
- LCS table and derived problems (delete operation, minimum ASCII delete sum, uncrossed lines)
- Longest palindromic subsequence = LCS(s, reverse(s))
- Edit distance (insert/delete/replace)
- Interleaving string; longest common substring (718) resets to 0 on a mismatch
- Regex matching: '*' means zero copies or one more copy (10)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [Aditya Verma - DP (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)
- [NeetCode - Dynamic Programming](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (10 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 15 Mar | [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Easy | 15m | ☐ |
|  |  | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 25m | ☐ |
| Tue | 16 Mar | [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | Medium | 25m | ☐ |
|  |  | [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | Medium | 25m | ☐ |
| Wed | 17 Mar | [72. Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | 25m | ☐ |
|  |  | [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Medium | 25m | ☐ |
| Thu | 18 Mar | [97. Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium | 25m | ☐ |
|  |  | [718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | Medium | 25m | ☐ |
| Fri | 19 Mar | [1035. Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/) | Medium | 25m | ☐ |
| Sat | 20 Mar | [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [62. Unique Paths](https://leetcode.com/problems/unique-paths/) (M) | 20m |
| Tue | [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) (M) | 20m |
| Wed | [221. Maximal Square](https://leetcode.com/problems/maximal-square/) (M) | 20m |
| Thu | [494. Target Sum](https://leetcode.com/problems/target-sum/) (M) | 20m |
| Fri | [1049. Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) (M) | 20m |
| Sat | [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/) (M) · [990. Satisfiability of Equality Equations](https://leetcode.com/problems/satisfiability-of-equality-equations/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) (H)
- [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) (H)
- [1092. Shortest Common Supersequence ](https://leetcode.com/problems/shortest-common-supersequence/) (H)
- [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) (H)
- [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) (H)
- [1458. Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) (H)
- [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Write the LCS recurrence.
- Edit Distance: meaning of dp[i][j] and the three transitions?
- How is Longest Palindromic Subsequence related to LCS?
- Maximum Length of Repeated Subarray vs LCS: what changes in the recurrence?
- Uncrossed Lines: why is it LCS in disguise?
- Regular Expression Matching: what are the two choices for '*'?

## 💡 Tip
Fill a small DP table by hand before coding. Weekly mock; Regex Matching is Saturday's weekend challenge.
