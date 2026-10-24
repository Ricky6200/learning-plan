# 🧩 DSA · Week 04 — Sliding Window (fixed & variable) - BOSS week

> 📅 **Mon 16 Nov 2026 → Sun 22 Nov 2026** · Season 1 — Foundation Forge · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 03](Week-03.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-04.md) · [Week 05 →](Week-05.md)

**Why this week:** Substring/subarray problems with 'longest/shortest/at most K' are sliding-window 80% of the time.

## 🧠 Concepts to master
- Fixed window: add right, remove left
- Variable window: expand right, shrink left while invalid, record answer
- Window state via int[128]/HashMap counts
- Exactly K = atMost(K) - atMost(K-1)
- Minimum Window Substring template ('have' vs 'need')

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Aditya Verma - Sliding Window (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWeM8BDJmIYDaoQ5zuwyxnfj)
- [NeetCode - Sliding Window](https://www.youtube.com/playlist?list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV)
- [Striver - Two Pointer & Sliding Window playlist](https://www.youtube.com/playlist?list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 16 Nov | [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | 15m | ☐ |
|  |  | [1456. Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | Medium | 25m | ☐ |
| Tue | 17 Nov | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | 15m | ☐ |
|  |  | [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Easy | 15m | ☐ |
| Wed | 18 Nov | [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | 25m | ☐ |
|  |  | [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | 25m | ☐ |
| Thu | 19 Nov | [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | 25m | ☐ |
|  |  | [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | 25m | ☐ |
| Fri | 20 Nov | [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | 25m | ☐ |
|  |  | [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | 25m | ☐ |
| Sat | 21 Nov | [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | 25m | ☐ |
|  |  | [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) | Medium | 25m | ☐ |
|  |  | [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/) (M)
- [1248. Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/) (M)
- [992. Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) (H)
- [1358. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/) (M)
- [2461. Maximum Sum of Distinct Subarrays With Length K](https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/) (M)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (H)
- [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (M)
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/) (M)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Which clue in a problem statement says 'sliding window'?
- Why does sliding window fail for 'subarray sum = K' with negative numbers?
- How do you count subarrays with exactly K distinct integers?
- Longest repeating character replacement: what is the window validity condition?
- Maximum points from cards: why is it a window on the complement?

## 💡 Tip
BOSS weekend: Saturday's 3 problems are timed (60 min total, no hints). Log your times.
