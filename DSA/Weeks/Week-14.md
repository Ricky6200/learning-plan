# 🧩 DSA · Week 14 — Heaps / Priority Queue

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** Top-K, scheduling, k-way merge and streaming medians are heap problems; they come up in system-flavoured rounds too.

## 🧠 Concepts to master
- Java PriorityQueue: min-heap by default; max-heap via Comparator.reverseOrder(); for int[] use (a, b) -> Integer.compare(a[0], b[0]) - not a[0] - b[0], which can overflow
- Top-K with a size-k heap (O(n log k)); quickselect as the O(n) average alternative (215)
- K-way merge: sorted matrix (378), merging users' feeds in Design Twitter (355)
- Two heaps for the running median (295)
- Greedy + heap scheduling (task scheduler, reorganize string, furthest building)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Aditya Verma - Heap (Hindi)](https://www.youtube.com/playlist?list=PL_z_8CaSLPWdtY9W22VjnPxG30CXNZpI9)
- [NeetCode practice list](https://neetcode.io/practice)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (11 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 25 Jan | [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | 15m | ☐ |
|  |  | [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Easy | 15m | ☐ |
| Tue | 26 Jan | [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | 25m | ☐ |
|  |  | [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | 25m | ☐ |
| Wed | 27 Jan | [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) | Medium | 25m | ☐ |
|  |  | [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | Medium | 25m | ☐ |
| Thu | 28 Jan | [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | 25m | ☐ |
|  |  | [767. Reorganize String](https://leetcode.com/problems/reorganize-string/) | Medium | 25m | ☐ |
| Fri | 29 Jan | [355. Design Twitter](https://leetcode.com/problems/design-twitter/) | Medium | 25m | ☐ |
| Sat | 30 Jan | [1642. Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/) | Medium | 25m | ☐ |
|  |  | [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) (M) | 20m |
| Tue | [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) (M) | 20m |
| Wed | [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (M) | 20m |
| Thu | [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) (M) | 20m |
| Fri | [450. Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) (M) | 20m |
| Sat | [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) (M)
- [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) (M)
- [502. IPO](https://leetcode.com/problems/ipo/) (H)
- [632. Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/) (H)
- [2402. Meeting Rooms III](https://leetcode.com/problems/meeting-rooms-iii/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Top-K largest: min-heap or max-heap of size K? Why?
- Kth Smallest Element in a Sorted Matrix: what goes into the heap first?
- Design Twitter: why is getNewsFeed a k-way merge?
- Running median: what invariant holds between the two heaps?
- Quickselect vs heap for Kth largest - trade-offs?
- Why is (a, b) -> a[0] - b[0] a risky comparator in Java?

## 💡 Tip
Practise thinking aloud this week: record a 2-minute explanation of one problem every day. Sunday is a contest Sunday; your first talk-aloud mock is next Sunday's test (Week 15), and mocks then alternate with contest Sundays. Tuesday is Republic Day - use any extra time for the bonus list.
