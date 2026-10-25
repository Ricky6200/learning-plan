# 🧩 DSA · Week 29 — Advanced Topics + Online Assessments

> 📅 **Mon 10 May 2027 → Sun 16 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 28](Week-28.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-29.md) · [Week 30 →](Week-30.md)

**Why this week:** Some rounds and online assessments go beyond the core patterns. Learn the advanced tools at awareness level and practise full programs under OA conditions.

## 🧠 Concepts to master
- SCC awareness: Kosaraju = DFS finish order, reverse graph, DFS again; the condensation is a DAG (1557 uses its zero-indegree idea)
- Morris traversal: thread the inorder predecessor back to the current node for O(1) space (99)
- KMP refresh (1392, 214); rolling hash from Week 23
- Digit DP with position + tight flag (902); bitmask DP over subsets (1986, 526)
- Full programs with the fast-I/O template (BufferedReader + StringTokenizer + PrintWriter): solve 2 CSES problems that read stdin and print stdout
- Two online-assessment simulations (90 min, 2-3 problems) in bonus time; no contest this week - Sunday's test opens with a talk-aloud mock

## 🎥 Learn from (pick ONE per topic — don't binge)
- [cp-algorithms - Strongly connected components (Kosaraju)](https://cp-algorithms.com/graph/strongly-connected-components.html)
- [GfG practice - Strongly Connected Components (Kosaraju)](https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1)
- [GfG - Morris inorder traversal (no stack, no recursion)](https://www.geeksforgeeks.org/dsa/inorder-tree-traversal-without-recursion-and-without-stack/)
- [cp-algorithms - Prefix function (KMP)](https://cp-algorithms.com/string/prefix-function.html)
- [CSES Problem Set (full stdin/stdout programs)](https://cses.fi/problemset/)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (8 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 10 May | [1557. Minimum Number of Vertices to Reach All Nodes](https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/) | Medium | 25m | ☐ |
|  |  | [99. Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/) | Medium | 25m | ☐ |
| Tue | 11 May | [1392. Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | Hard | 40m | ☐ |
| Wed | 12 May | [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | Hard | 40m | ☐ |
| Thu | 13 May | [902. Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/) | Hard | 40m | ☐ |
| Fri | 14 May | [1986. Minimum Number of Work Sessions to Finish the Tasks](https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/) | Medium | 25m | ☐ |
|  |  | [526. Beautiful Arrangement](https://leetcode.com/problems/beautiful-arrangement/) | Medium | 25m | ☐ |
| Sat | 15 May | [68. Text Justification](https://leetcode.com/problems/text-justification/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) (M) | 20m |
| Tue | [2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/) (M) | 20m |
| Wed | [2385. Amount of Time for Binary Tree to Be Infected](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/) (M) | 20m |
| Thu | [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) (M) | 20m |
| Fri | [1116. Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/) (M) | 20m |
| Sat | [373. Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) (M) · [274. H-Index](https://leetcode.com/problems/h-index/) (M) | 20m / 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [357. Count Numbers with Unique Digits](https://leetcode.com/problems/count-numbers-with-unique-digits/) (M)
- [2360. Longest Cycle in a Graph](https://leetcode.com/problems/longest-cycle-in-a-graph/) (H)
- [2050. Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/) (H)
- [1125. Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Kosaraju: why process nodes in reverse finish order on the reversed graph?
- Recover Binary Search Tree with Morris traversal: how do you detect the two swapped nodes?
- Longest Happy Prefix: how do you read the answer straight from the LPS array?
- Shortest Palindrome: which string do you build the LPS array on?
- Numbers At Most N Given Digit Set: what does 'tight' mean?
- Text Justification: how do you distribute the extra spaces?

## 💡 Tip
OA mode: 2 timed simulations this week (90 min each, full programs, no autocomplete). Sunday: talk-aloud mock. Text Justification on Saturday doubles as a full-program exercise.
