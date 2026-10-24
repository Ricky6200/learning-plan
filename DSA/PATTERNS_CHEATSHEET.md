# ?? DSA Patterns Cheat-Sheet (Java)

> Every template below is **compiled and unit-tested** (JDK 11+). Re-type them from memory once a week ? speed comes from muscle memory.
> Use with the weekly files in [Weeks/](Weeks/). Languages: Java (interview default for backend roles).

## ?? Pattern recognition ? read the clue, pick the pattern

| Clue in the problem | Pattern to try first | Week |
|---|---|---|
| "pair/triplet with sum", sorted input | Two pointers | W3 |
| "longest/shortest substring/subarray", "at most K" | Sliding window | W4 |
| "count subarrays with sum = K" (negatives allowed) | Prefix sum + HashMap | W2, W5 |
| "maximum subarray" | Kadane | W5 |
| sorted / rotated array, "minimum X such that?" | Binary search (array or answer space) | W6 |
| "all subsets / permutations / combinations" | Backtracking | W8?W9 |
| linked list cycle / middle / reorder | Fast & slow pointers | W10 |
| "next greater/smaller", histogram | Monotonic stack | W11 |
| window max/min | Monotonic deque | W11 |
| tree path / depth / diameter | DFS returning a value to the parent | W12?W13 |
| "level by level", shortest steps unweighted | BFS | W12, W16 |
| "top K", "K closest", streaming median | Heap (PriorityQueue) | W14 |
| "minimum number of X", intervals by end time | Greedy (+ sort) | W15 |
| grid islands / regions / rotting | DFS/BFS on grid (multi-source BFS) | W16 |
| dependencies / prerequisites / ordering | Topological sort | W17 |
| weighted shortest path, non-negative weights | Dijkstra | W17 |
| "are they connected", merge groups, redundant edge | Union-Find (DSU) | W18 |
| "number of ways", "min/max cost", overlapping subproblems | Dynamic programming | W19?W22 |
| two strings: match / edit / common subsequence | 2D string DP | W21 |
| prefix search, autocomplete, word dictionary | Trie | W23 |
| range sum with updates | Fenwick tree / segment tree | W23 |
| "design a data structure with O(1) ops" | HashMap + linked list / array + index map | W24 |

## ?? Java toolkit you must know cold

```java
int[] a = new int[n]; Arrays.fill(a, -1); Arrays.sort(a);             // primitives: dual-pivot quicksort
Integer[] b = {3, 1, 2}; Arrays.sort(b, Collections.reverseOrder());   // objects: TimSort (stable)
int[][] iv = {{1, 3}, {0, 2}}; Arrays.sort(iv, (x, y) -> Integer.compare(x[0], y[0]));  // avoid x[0]-y[0] (overflow)
List<Integer> list = new ArrayList<>(); Map<String, Integer> map = new HashMap<>(); Set<Integer> set = new HashSet<>();
map.merge(key, 1, Integer::sum); map.getOrDefault(key, 0); map.computeIfAbsent(k, x -> new ArrayList<>()).add(v);
Deque<Integer> stack = new ArrayDeque<>(); stack.push(1); stack.pop(); stack.peek();      // use instead of Stack
Deque<Integer> queue = new ArrayDeque<>(); queue.offer(1); queue.poll(); queue.peek();
PriorityQueue<Integer> minHeap = new PriorityQueue<>(), maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
TreeMap<Integer, Integer> tm = new TreeMap<>(); tm.floorKey(x); tm.ceilingKey(x); tm.firstKey();
StringBuilder sb = new StringBuilder(); sb.append('a').reverse().toString(); char c = s.charAt(i); int d = c - '0';
long safe = (long) x * y; int mid = lo + (hi - lo) / 2; int max = Integer.MAX_VALUE;   // overflow guards
```

> The toolkit block is a reference list (not a compilable program). Everything below is compiled & tested.

## 1. Frequency counting (HashMap / int[26])

```java
Map<Character, Integer> frequency(String s) {
    Map<Character, Integer> freq = new HashMap<>();
    for (char c : s.toCharArray()) freq.merge(c, 1, Integer::sum);
    return freq;
}

boolean isAnagram(String a, String b) {          // lowercase letters only
    if (a.length() != b.length()) return false;
    int[] cnt = new int[26];
    for (int i = 0; i < a.length(); i++) { cnt[a.charAt(i) - 'a']++; cnt[b.charAt(i) - 'a']--; }
    for (int c : cnt) if (c != 0) return false;
    return true;
}
```

## 2. Two pointers (opposite ends on a sorted array)

```java
int[] pairWithSum(int[] a, int target) {
    int l = 0, r = a.length - 1;
    while (l < r) {
        int sum = a[l] + a[r];
        if (sum == target) return new int[]{l, r};
        if (sum < target) l++; else r--;
    }
    return new int[]{-1, -1};
}
```

## 3. Read/write pointers (in-place filtering)

```java
int removeElement(int[] a, int val) {
    int w = 0;                                    // next write position
    for (int r = 0; r < a.length; r++) if (a[r] != val) a[w++] = a[r];
    return w;                                     // new length
}
```

## 4. Sliding window (fixed size k)

```java
int maxSumOfWindow(int[] a, int k) {
    int sum = 0, best = Integer.MIN_VALUE;
    for (int i = 0; i < a.length; i++) {
        sum += a[i];
        if (i >= k) sum -= a[i - k];              // drop element leaving the window
        if (i >= k - 1) best = Math.max(best, sum);
    }
    return best;
}
```

## 5. Sliding window (variable size)

```java
int longestSubstringWithoutRepeats(String s) {
    int[] cnt = new int[128];
    int left = 0, best = 0;
    for (int right = 0; right < s.length(); right++) {
        char c = s.charAt(right);
        cnt[c]++;
        while (cnt[c] > 1) {                      // window invalid -> shrink from the left
            cnt[s.charAt(left)]--;
            left++;
        }
        best = Math.max(best, right - left + 1);  // window valid -> record answer
    }
    return best;
}
```

## 6. Prefix sum + HashMap (count subarrays with sum k)

```java
int subarraySum(int[] nums, int k) {
    Map<Integer, Integer> seen = new HashMap<>();
    seen.put(0, 1);                               // empty prefix
    int sum = 0, count = 0;
    for (int x : nums) {
        sum += x;
        count += seen.getOrDefault(sum - k, 0);
        seen.merge(sum, 1, Integer::sum);
    }
    return count;
}
```

## 7. Kadane (maximum subarray)

```java
int maxSubArray(int[] nums) {
    int best = nums[0], cur = 0;
    for (int x : nums) {
        cur = Math.max(x, cur + x);               // extend or restart
        best = Math.max(best, cur);
    }
    return best;
}
```

## 8. Binary search (lower bound)

```java
int lowerBound(int[] a, int target) {             // first index with a[i] >= target, or a.length
    int lo = 0, hi = a.length;                    // search space [lo, hi)
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] >= target) hi = mid; else lo = mid + 1;
    }
    return lo;
}
```

## 9. Binary search on the answer (monotonic predicate)

```java
int minEatingSpeed(int[] piles, int h) {          // LC 875 Koko
    int lo = 1, hi = Arrays.stream(piles).max().getAsInt();
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (canFinish(piles, h, mid)) hi = mid;   // mid works -> try smaller
        else lo = mid + 1;
    }
    return lo;
}

boolean canFinish(int[] piles, int h, int speed) {
    long hours = 0;
    for (int p : piles) hours += (p + speed - 1) / speed;   // ceil division
    return hours <= h;
}
```

## 10. Backtracking (subsets with duplicates; sort nums first)

```java
void subsets(int start, int[] nums, List<Integer> path, List<List<Integer>> res) {
    res.add(new ArrayList<>(path));
    for (int i = start; i < nums.length; i++) {
        if (i > start && nums[i] == nums[i - 1]) continue;   // skip duplicates at the same depth
        path.add(nums[i]);                                  // choose
        subsets(i + 1, nums, path, res);                    // explore
        path.remove(path.size() - 1);                       // un-choose
    }
}
```

## 11. Backtracking (permutations)

```java
void permute(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> res) {
    if (path.size() == nums.length) { res.add(new ArrayList<>(path)); return; }
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true; path.add(nums[i]);
        permute(nums, used, path, res);
        path.remove(path.size() - 1); used[i] = false;
    }
}
```

## 12. Linked list (reverse + fast/slow)

```java
ListNode reverse(ListNode head) {
    ListNode prev = null, cur = head;
    while (cur != null) {
        ListNode next = cur.next;                 // save
        cur.next = prev;                          // reverse link
        prev = cur;                               // advance
        cur = next;
    }
    return prev;
}

ListNode middle(ListNode head) {
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) { slow = slow.next; fast = fast.next.next; }
    return slow;
}
```

## 13. Monotonic stack (next greater element)

```java
int[] nextGreater(int[] a) {
    int[] res = new int[a.length];
    Arrays.fill(res, -1);
    Deque<Integer> st = new ArrayDeque<>();       // indices; values decreasing from bottom to top
    for (int i = 0; i < a.length; i++) {
        while (!st.isEmpty() && a[st.peek()] < a[i]) res[st.pop()] = a[i];
        st.push(i);
    }
    return res;
}
```

## 14. Monotonic deque (sliding window maximum)

```java
int[] maxSlidingWindow(int[] a, int k) {
    int[] res = new int[a.length - k + 1];
    Deque<Integer> dq = new ArrayDeque<>();       // indices; values decreasing
    for (int i = 0; i < a.length; i++) {
        if (!dq.isEmpty() && dq.peekFirst() <= i - k) dq.pollFirst();      // out of window
        while (!dq.isEmpty() && a[dq.peekLast()] <= a[i]) dq.pollLast();   // useless elements
        dq.offerLast(i);
        if (i >= k - 1) res[i - k + 1] = a[dq.peekFirst()];
    }
    return res;
}
```

## 15. Tree DFS (return to parent, record global answer)

```java
int height(TreeNode node) {
    if (node == null) return 0;
    int l = height(node.left), r = height(node.right);
    diameter = Math.max(diameter, l + r);         // record global answer
    return 1 + Math.max(l, r);                    // return what the parent needs
}
```

## 16. Tree BFS (level order)

```java
List<List<Integer>> levelOrder(TreeNode root) {
    List<List<Integer>> res = new ArrayList<>();
    if (root == null) return res;
    Queue<TreeNode> q = new ArrayDeque<>();
    q.offer(root);
    while (!q.isEmpty()) {
        int size = q.size();                      // nodes in this level
        List<Integer> level = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            TreeNode node = q.poll();
            level.add(node.val);
            if (node.left != null) q.offer(node.left);
            if (node.right != null) q.offer(node.right);
        }
        res.add(level);
    }
    return res;
}
```

## 17. Heap (top-K with a size-k min-heap)

```java
int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    for (int x : nums) {
        minHeap.offer(x);
        if (minHeap.size() > k) minHeap.poll();   // keep only the k largest
    }
    return minHeap.peek();
}
// Max-heap: new PriorityQueue<>(Comparator.reverseOrder())
// Arrays:   new PriorityQueue<int[]>((x, y) -> Integer.compare(x[0], y[0]))
```

## 18. Grid BFS (multi-source, shortest steps)

```java
static final int[][] DIRS = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int bfsSteps(int[][] grid, List<int[]> sources) {
    int m = grid.length, n = grid[0].length, steps = 0;
    boolean[][] seen = new boolean[m][n];
    Deque<int[]> q = new ArrayDeque<>();
    for (int[] s : sources) { q.offer(s); seen[s[0]][s[1]] = true; }   // all sources first
    while (!q.isEmpty()) {
        for (int size = q.size(); size > 0; size--) {
            int[] cur = q.poll();
            for (int[] d : DIRS) {
                int r = cur[0] + d[0], c = cur[1] + d[1];
                if (r < 0 || c < 0 || r >= m || c >= n || seen[r][c] || grid[r][c] == 0) continue;
                seen[r][c] = true;                // mark when ENQUEUING
                q.offer(new int[]{r, c});
            }
        }
        steps++;
    }
    return steps;                                 // levels processed; distance to the farthest cell = steps - 1
}
```

## 19. Topological sort (Kahn's algorithm)

```java
List<Integer> topoSort(int n, int[][] edges) {     // edge {u, v} means u -> v
    List<List<Integer>> g = new ArrayList<>();
    for (int i = 0; i < n; i++) g.add(new ArrayList<>());
    int[] indeg = new int[n];
    for (int[] e : edges) { g.get(e[0]).add(e[1]); indeg[e[1]]++; }
    Deque<Integer> q = new ArrayDeque<>();
    for (int i = 0; i < n; i++) if (indeg[i] == 0) q.offer(i);
    List<Integer> order = new ArrayList<>();
    while (!q.isEmpty()) {
        int u = q.poll();
        order.add(u);
        for (int v : g.get(u)) if (--indeg[v] == 0) q.offer(v);
    }
    return order.size() == n ? order : Collections.emptyList();   // empty => cycle
}
```

## 20. Dijkstra (PriorityQueue + lazy deletion)

```java
int[] dijkstra(int n, List<List<int[]>> g, int src) {   // g.get(u) = list of {v, weight}
    int[] dist = new int[n];
    Arrays.fill(dist, Integer.MAX_VALUE);
    dist[src] = 0;
    PriorityQueue<int[]> pq = new PriorityQueue<>((x, y) -> Integer.compare(x[1], y[1]));
    pq.offer(new int[]{src, 0});
    while (!pq.isEmpty()) {
        int[] cur = pq.poll();
        int u = cur[0], d = cur[1];
        if (d > dist[u]) continue;                // stale entry
        for (int[] e : g.get(u)) {
            int v = e[0], nd = d + e[1];
            if (nd < dist[v]) { dist[v] = nd; pq.offer(new int[]{v, nd}); }
        }
    }
    return dist;
}
```

## 21. Union-Find / DSU (path compression + union by size)

```java
static class DSU {
    final int[] parent, size;

    DSU(int n) {
        parent = new int[n]; size = new int[n];
        for (int i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
    }

    int find(int x) { return parent[x] == x ? x : (parent[x] = find(parent[x])); }

    boolean union(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return false;               // already connected (edge makes a cycle)
        if (size[ra] < size[rb]) { int t = ra; ra = rb; rb = t; }
        parent[rb] = ra; size[ra] += size[rb];
        return true;
    }
}
```

## 22. DP (recursion -> memo -> tabulation -> O(1) space)

```java
int robMemo(int i, int[] a, Integer[] memo) {      // House Robber, top-down
    if (i >= a.length) return 0;
    if (memo[i] != null) return memo[i];
    return memo[i] = Math.max(a[i] + robMemo(i + 2, a, memo), robMemo(i + 1, a, memo));
}

int robTab(int[] a) {                             // bottom-up, O(1) space
    int next1 = 0, next2 = 0;                     // dp[i+1], dp[i+2]
    for (int i = a.length - 1; i >= 0; i--) {
        int cur = Math.max(a[i] + next2, next1);
        next2 = next1; next1 = cur;
    }
    return next1;
}
```

## 23. 0/1 knapsack in 1D (iterate capacity backwards)

```java
boolean canPartition(int[] nums) {
    int total = Arrays.stream(nums).sum();
    if (total % 2 != 0) return false;
    int target = total / 2;
    boolean[] dp = new boolean[target + 1];
    dp[0] = true;
    for (int x : nums)
        for (int c = target; c >= x; c--)          // backwards => each item used at most once
            dp[c] = dp[c] || dp[c - x];
    return dp[target];
}
```

## 24. LCS (2D string DP)

```java
int lcs(String a, String b) {
    int m = a.length(), n = b.length();
    int[][] dp = new int[m + 1][n + 1];
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            dp[i][j] = a.charAt(i - 1) == b.charAt(j - 1)
                    ? dp[i - 1][j - 1] + 1
                    : Math.max(dp[i - 1][j], dp[i][j - 1]);
    return dp[m][n];
}
```

## 25. LIS in O(n log n) (patience sorting)

```java
int lengthOfLIS(int[] nums) {
    int[] tails = new int[nums.length];           // tails[k] = smallest tail of an increasing subsequence of length k+1
    int len = 0;
    for (int x : nums) {
        int lo = 0, hi = len;
        while (lo < hi) { int mid = (lo + hi) >>> 1; if (tails[mid] < x) lo = mid + 1; else hi = mid; }
        tails[lo] = x;
        if (lo == len) len++;
    }
    return len;
}
```

## 26. Trie

```java
static class Trie {
    private final Trie[] next = new Trie[26];
    private boolean end;

    void insert(String w) {
        Trie node = this;
        for (char c : w.toCharArray()) {
            int i = c - 'a';
            if (node.next[i] == null) node.next[i] = new Trie();
            node = node.next[i];
        }
        node.end = true;
    }

    boolean search(String w) { Trie n = walk(w); return n != null && n.end; }

    boolean startsWith(String p) { return walk(p) != null; }

    private Trie walk(String s) {
        Trie node = this;
        for (char c : s.toCharArray()) { node = node.next[c - 'a']; if (node == null) return null; }
        return node;
    }
}
```

## 27. Fenwick tree / BIT (point update, prefix sum)

```java
static class Fenwick {
    private final long[] bit;                     // 1-indexed internally

    Fenwick(int n) { bit = new long[n + 1]; }

    void add(int i, long delta) { for (i++; i < bit.length; i += i & -i) bit[i] += delta; }

    long prefix(int i) { long s = 0; for (i++; i > 0; i -= i & -i) s += bit[i]; return s; }   // sum of [0..i]

    long range(int l, int r) { return prefix(r) - (l > 0 ? prefix(l - 1) : 0); }
}
```

## 28. KMP prefix function (LPS array)

```java
int[] lps(String p) {
    int[] lps = new int[p.length()];
    for (int i = 1, len = 0; i < p.length(); ) {
        if (p.charAt(i) == p.charAt(len)) lps[i++] = ++len;
        else if (len > 0) len = lps[len - 1];      // fall back, don't move i
        else lps[i++] = 0;
    }
    return lps;
}
```

## 29. LRU cache (interview version: HashMap + doubly linked list)

```java
static class LRUCache {
    private static class Node { int key, val; Node prev, next; Node(int k, int v) { key = k; val = v; } }
    private final int capacity;
    private final Map<Integer, Node> map = new HashMap<>();
    private final Node head = new Node(0, 0), tail = new Node(0, 0);   // sentinels

    LRUCache(int capacity) { this.capacity = capacity; head.next = tail; tail.prev = head; }

    int get(int key) {
        Node n = map.get(key);
        if (n == null) return -1;
        remove(n); addFirst(n);                   // mark as most recently used
        return n.val;
    }

    void put(int key, int value) {
        Node n = map.get(key);
        if (n != null) { n.val = value; remove(n); addFirst(n); return; }
        if (map.size() == capacity) { Node lru = tail.prev; remove(lru); map.remove(lru.key); }
        n = new Node(key, value);
        map.put(key, n); addFirst(n);
    }

    private void remove(Node n) { n.prev.next = n.next; n.next.prev = n.prev; }

    private void addFirst(Node n) { n.next = head.next; n.prev = head; head.next.prev = n; head.next = n; }
}
```

## ?? How to practise these templates
1. **Monday of each week:** re-type that week's template from memory (5 min) before solving.
2. **Every Saturday:** pick 2 random templates from earlier weeks and re-type them.
3. If a template takes > 5 minutes, mark it ?? in [REVISION_TRACKER.md](REVISION_TRACKER.md).
