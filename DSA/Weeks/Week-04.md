# 🧩 DSA · Week 04 — Sliding Window (fixed & variable) - BOSS week

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Substring/subarray problems with 'longest/shortest/at most K' are sliding window 80% of the time. Saturday's boss closes Season 1.

## 🧠 Concepts to master
- Fixed window: add right, remove left
- Variable window: expand right, shrink left while invalid, record the answer
- Window state via int[128] or HashMap counts
- Counting windows: each valid right end adds (right - left + 1) subarrays (713); exactly K = atMost(K) - atMost(K-1)
- Minimum Window Substring template ('have' vs 'need')

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Aditya Verma - Sliding Window (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj)
- [NeetCode - Sliding Window](https://www.youtube.com/playlist?list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV)
- [Striver - Two Pointer & Sliding Window playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 16 Nov | [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | 15m | ☐ |
|  |  | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | 25m | ☐ |
| Tue | 17 Nov | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | 15m | ☐ |
|  |  | [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | 25m | ☐ |
| Wed | 18 Nov | [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/) | Medium | 25m | ☐ |
| Thu | 19 Nov | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | 25m | ☐ |
|  |  | [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | 25m | ☐ |
| Fri | 20 Nov | [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | 25m | ☐ |
|  |  | [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | 25m | ☐ |
| Sat | 21 Nov | [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Medium | 25m | ☐ |
|  |  | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (M) | 20m |
| Tue | [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (M) | 20m |
| Wed | [15. 3Sum](https://leetcode.com/problems/3sum/) (M) | 20m |
| Thu | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) (M) | 20m |
| Fri | [912. Sort an Array](https://leetcode.com/problems/sort-an-array/) (M) | 20m |
| Sat | [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) (E)
- [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) (M)
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) (M)
- [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) (M)
- [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) (M)
- [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) (H)
- [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) (M)
- [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) (M)
- [30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Which clue in a problem statement says 'sliding window'?
- Why does sliding window fail for 'subarray sum = K' with negative numbers?
- Subarray Product Less Than K: why do you add right - left + 1 at every step?
- Longest Repeating Character Replacement: what is the window validity condition?
- Maximum Points You Can Obtain from Cards: why is it a window on the complement?
- Minimum Window Substring: when do you shrink, and when do you record the answer?

## 💡 Tip
BOSS Saturday: LC 1423 + LC 76 timed, 60 min total, no hints - don't open them before the timer starts. Log your times; do the 2 re-solves after the boss.
