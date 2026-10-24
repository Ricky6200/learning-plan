# 🧩 DSA · Week 21 — DP III: Strings & Subsequences

> 📅 **Mon 15 Mar 2027 → Sun 21 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 20](Week-20.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-21.md) · [Week 22 →](Week-22.md)

**Why this week:** LCS/edit distance families are asked at every level and are great for showing structured thinking.

## 🧠 Concepts to master
- LCS table and derived problems (delete operation, shortest common supersequence)
- Min insertions = n - LPS
- Edit distance (insert/delete/replace)
- Distinct subsequences, interleaving string
- Regex matching (wildcard as bonus); Russian doll = sort + LIS

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - DP series](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)
- [Aditya Verma - DP (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go)
- [NeetCode - Dynamic Programming](https://www.youtube.com/playlist?list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 15 Mar | [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | 25m | ☐ |
|  |  | [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/) | Medium | 25m | ☐ |
| Tue | 16 Mar | [72. Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | 25m | ☐ |
|  |  | [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Medium | 25m | ☐ |
| Wed | 17 Mar | [1312. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) | Hard | 40m | ☐ |
|  |  | [97. Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium | 25m | ☐ |
| Thu | 18 Mar | [115. Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Hard | 40m | ☐ |
|  |  | [718. Maximum Length of Repeated Subarray](https://leetcode.com/problems/maximum-length-of-repeated-subarray/) | Medium | 25m | ☐ |
| Fri | 19 Mar | [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | 40m | ☐ |
|  |  | [1035. Uncrossed Lines](https://leetcode.com/problems/uncrossed-lines/) | Medium | 25m | ☐ |
| Sat | 20 Mar | [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Easy | 15m | ☐ |
|  |  | [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/) | Medium | 25m | ☐ |
|  |  | [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [1092. Shortest Common Supersequence ](https://leetcode.com/problems/shortest-common-supersequence/) (H)
- [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) (H)
- [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/) (H)
- [1458. Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) (H)
- [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/) (H)
- [62. Unique Paths](https://leetcode.com/problems/unique-paths/) (M)
- [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Write the LCS recurrence.
- Edit distance: meaning of dp[i][j] and the three transitions?
- How is Longest Palindromic Subsequence related to LCS?
- Regex '*' handling: the two choices?
- Russian Doll Envelopes: why sort width asc and height desc?

## 💡 Tip
Fill a small DP table by hand before coding.
