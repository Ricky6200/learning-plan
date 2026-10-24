# 🧩 DSA · Week 12 — Binary Trees I: traversals & depth

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Sat · 60 min (Block A, first thing) · Sunday test: 45 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** Trees are in almost every product-company loop. Traversals + 'return value from children' is the core skill.

## 🧠 Concepts to master
- DFS pre/in/post order - recursive and iterative
- BFS level order with queue size per level
- Height/depth; diameter via post-order returning height
- Balanced / same / symmetric trees
- Global-max pattern (max path sum)

## 🎥 Learn from (pick ONE per topic — don't binge)
- [Striver - Tree series](https://www.youtube.com/playlist?list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu)
- [NeetCode - Trees](https://www.youtube.com/playlist?list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg)
- [VisuAlgo (animations)](https://visualgo.net/en)

Templates: [PATTERNS_CHEATSHEET.md](../PATTERNS_CHEATSHEET.md)

## 🗓️ Daily problems — Core (13)

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
|  |  | [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | Easy | 15m | ☐ |
| Sat | 16 Jan | [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/) | Medium | 25m | ☐ |
|  |  | [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | Medium | 25m | ☐ |
|  |  | [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) 🔥 *weekend challenge — finish Sunday if needed* | Hard | 40m | ☐ |

## ➕ Bonus (only after Core is done — great for weekends/holidays)
- [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) (E)
- [112. Path Sum](https://leetcode.com/problems/path-sum/) (E)
- [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/) (M)
- [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/) (M)
- [987. Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/) (H)

## 🔁 Spaced revision (Sunday preview slot, ~15 min, from memory)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (H)
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) (H)
- [51. N-Queens](https://leetcode.com/problems/n-queens/) (H)
- Plus anything marked 🔴 in [REVISION_TRACKER.md](../REVISION_TRACKER.md)

## ⏱️ The 60-minute routine
1. **5 min** — re-read yesterday's notes (pattern + insight).
2. **2 × 25 min** — solve. Time-box the first attempt (see table). Stuck? Watch ONLY the intuition part of a video, close it, code from memory.
3. **5 min** — log in [REVISION_TRACKER.md](../REVISION_TRACKER.md): pattern, key insight, time, 🟢/🟡/🔴.

## ✅ Self-check (Sunday test preview)
- Write iterative inorder traversal from memory.
- How do you compute diameter in one pass?
- Right side view: BFS or DFS - explain both.
- Max path sum: what does the recursive function return vs what does it record?
- Time and space complexity of DFS on a skewed tree?

## 💡 Tip
Ask yourself: 'What should each node return to its parent?'
