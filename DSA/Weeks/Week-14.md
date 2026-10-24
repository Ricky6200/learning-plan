# 🧩 DSA · Week 14 — Heaps / Priority Queue - BOSS week

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Top-K, scheduling, k-way merge and streaming medians are heap problems; they come up in system-flavoured rounds too.

## 🧠 Concepts to master
- Java PriorityQueue: min-heap by default; max-heap via Comparator.reverseOrder()
- Top-K with a size-k heap (O(n log k))
- K-way merge (lists, sorted matrix)
- Two heaps for running median
- Greedy + heap scheduling (task scheduler, reorganize string)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver A2Z DSA Sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet)
- [NeetCode practice list](https://neetcode.io/practice)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 25 Jan | [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | 15m | ☐ |
|  |  | [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | 15m | ☐ |
| Tue | 26 Jan | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | 25m | ☐ |
|  |  | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | 25m | ☐ |
| Wed | 27 Jan | [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | Medium | 25m | ☐ |
|  |  | [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) | Medium | 25m | ☐ |
| Thu | 28 Jan | [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | 25m | ☐ |
|  |  | [767. Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | 25m | ☐ |
| Fri | 29 Jan | [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | 40m | ☐ |
|  |  | [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | 25m | ☐ |
| Sat | 30 Jan | [355. Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | 25m | ☐ |
|  |  | [1642. Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) | Medium | 25m | ☐ |
|  |  | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) (M)
- [502. IPO](https://leetcode.com/problems/ipo/) (H)
- [632. Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) (H)
- [1834. Single-Threaded CPU](https://leetcode.com/problems/single-threaded-cpu/) (M)
- [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (H)
- [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) (M)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Top-K largest: min-heap or max-heap of size K? Why?
- Running median: invariant between the two heaps?
- Merge K sorted lists: complexity with a heap?
- Quickselect vs heap for Kth largest - trade-offs?
- How do you write a comparator for int[] {dist, x, y} in Java?

## 💡 Tip
BOSS: Saturday 3 problems timed (60 min). Explain each heap choice aloud.
