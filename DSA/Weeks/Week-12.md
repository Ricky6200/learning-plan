# 🧩 DSA · Week 12 — Binary Trees I: traversals & depth

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** Trees are in almost every product-company loop. Traversals + 'return a value from the children' is the core skill.

## 🧠 Concepts to master
- DFS pre/in/post order - recursive and iterative (ArrayDeque as the stack)
- BFS level order with queue size per level
- Height/depth; diameter via post-order returning height
- Balanced / same / subtree checks (572 reuses Same Tree)
- Global-max pattern (max path sum)
- Online assessments: some platforms want a full program - learn the fast-I/O template (BufferedReader + StringTokenizer + PrintWriter, flush at the end)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Tree series](https://www.youtube.com/playlist?list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu)
- [NeetCode - Trees](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
- [USACO Guide - Input & Output in Java (fast I/O)](https://usaco.guide/general/input-output?lang=java)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (12 new)

| Day | Date | Problem | Difficulty | First-attempt time-box | Done (☐→✅) |
|---|---|---|---|---|---|
| Mon | 11 Jan | [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) | Easy | 15m | ☐ |
|  |  | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) | Easy | 15m | ☐ |
| Tue | 12 Jan | [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) | Easy | 15m | ☐ |
|  |  | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | 25m | ☐ |
| Wed | 13 Jan | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | 15m | ☐ |
|  |  | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) | Easy | 15m | ☐ |
| Thu | 14 Jan | [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | 15m | ☐ |
|  |  | [100. Same Tree](https://leetcode.com/problems/same-tree/) | Easy | 15m | ☐ |
| Fri | 15 Jan | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | 15m | ☐ |
|  |  | [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) | Easy | 15m | ☐ |
| Sat | 16 Jan | [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | 25m | ☐ |
|  |  | [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## 🔁 Daily re-solve (first 10–12 min of the block · from memory · timed)
Spaced repetition: weekdays re-solve one problem from 7 days ago; Saturday re-solves one or two quick ones (Easy/Medium, ~10 min each) from 3 weeks ago (one when Saturday already has a 🔥 Hard); problems you've re-solved least come first. Beat the target time without notes; if you can't, mark it 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md) and it comes back on Sunday.

| Day | Re-solve | Target |
|---|---|---|
| Mon | [155. Min Stack](https://leetcode.com/problems/min-stack/) (M) | 20m |
| Tue | [394. Decode String](https://leetcode.com/problems/decode-string/) (M) | 20m |
| Wed | [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) (M) | 20m |
| Thu | [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/) (M) | 20m |
| Fri | [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) (M) | 20m |
| Sat | [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) (M) | 20m |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) (E)
- [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) (M)
- [112. Path Sum](https://leetcode.com/problems/path-sum/) (E)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/) (M)
- [637. Average of Levels in Binary Tree](https://leetcode.com/problems/average-of-levels-in-binary-tree/) (E)
- [222. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) (M)
- [987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) (H)

## ⏱️ The 60-minute routine
1. **10–20 min** — re-solve today's problem(s) above from memory, timed.
2. **~40 min** — solve today's problems. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory. A 🔥 Saturday Hard may finish on Sunday.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

**Sunday:** re-solve everything you marked 🔴 this week (preview slot).

## ✅ Self-check (Sunday test preview)
- Write iterative inorder traversal from memory.
- How do you compute the diameter in one pass?
- Right Side View: BFS or DFS - explain both.
- Subtree of Another Tree: what is the worst-case complexity of the simple solution?
- Max path sum: what does the recursive function return vs what does it record?
- Full program: how do you read n and then n integers fast in Java?

## 💡 Tip
Ask: 'What should each node return to its parent?' New fortnightly habit: re-solve one problem as a full stdin/stdout Java program with the fast-I/O template.
