# 🧩 DSA Patterns Cheat-Sheet (Java)

> Every template below is **compiled and unit-tested** (JDK 11+). Re-type them from memory once a week — speed comes from muscle memory.
> Use with the weekly files in [Weeks/](Weeks/). Languages: Java (interview default for backend roles).

## 🔎 Pattern recognition — read the clue, pick the pattern

| Clue in the problem | Pattern to try first | Week |
|---|---|---|
| values in 1..n: missing / duplicate numbers in O(1) extra space | Cyclic sort / index-as-hash (#34) | W1, W9 |
| "pair/triplet with sum", sorted input | Two pointers | W3 |
| "sort it yourself", count inversions / reverse pairs | Merge sort, count while merging (#30) | W3, W27 |
| "longest/shortest substring/subarray", "at most K" | Sliding window | W4 |
| "count subarrays with sum = K" (negatives allowed) | Prefix sum + HashMap | W2, W5 |
| "maximum subarray" | Kadane | W5 |
| overlapping intervals: merge / insert | Sort by start + merge (#31) | W5 |
| many range updates, "max overlap", "minimum rooms/groups" | Difference array / sweep line with +1/−1 events (#32) | W5, W23 |
| sorted / rotated array, "minimum X such that …" | Binary search (array or answer space) | W6, W24 |
| "single number", power of two, count bits, add without + | Bit manipulation: XOR, n & (n − 1) (#33) | W7 |
| "all subsets / permutations / combinations" | Backtracking | W8–W9 |
| linked list cycle / middle / reorder | Fast & slow pointers | W10 |
| duplicate in 1..n without modifying the array | Floyd's cycle on index → value (#35) | W10 |
| "next greater/smaller", histogram | Monotonic stack | W11, W27 |
| window max/min, shortest subarray with sum ≥ K | Monotonic deque | W11, W27 |
| online assessment asks for a full program (stdin/stdout) | Fast I/O template (#36) | W12, W29 |
| tree path / depth / diameter | DFS returning a value to the parent | W12–W13 |
| "level by level", shortest steps unweighted | BFS | W12, W16 |
| "top K", "K closest", streaming median | Heap (PriorityQueue) | W14 |
| "Kth largest/smallest" in O(n) average | Quickselect, 3-way partition (#37) | W14 |
| "minimum number of X", intervals by end time | Greedy (+ sort) | W15 |
| grid islands / regions / rotting | DFS/BFS on grid (multi-source BFS) | W16 |
| prefix search, autocomplete, word dictionary | Trie | W16, W18, W23 |
| dependencies / prerequisites / ordering | Topological sort | W17 |
| weighted shortest path, non-negative weights | Dijkstra | W17 |
| edge weights only 0 or 1 (free moves vs costly moves) | 0-1 BFS with ArrayDeque (#38) | W17 |
| "are they connected", merge groups, redundant edge | Union-Find (DSU) | W18 |
| directed graph: groups where everyone reaches everyone | Strongly connected components, Kosaraju (#39, awareness) | W18, W29 |
| "number of ways", "min/max cost", overlapping subproblems | Dynamic programming | W19–W22 |
| two strings: match / edit / common subsequence | 2D string DP | W21 |
| find a pattern in text, longest prefix that is also a suffix | KMP (LPS array) / rolling hash | W23, W29 |
| range sum with updates | Fenwick tree / segment tree | W23 |
| "design a data structure with O(1) ops" | HashMap + linked list / array + index map | W10, W24 |

## 🧰 Java toolkit you must know cold

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

## 30. Merge sort (LC 912; count while merging for LC 493)

```java
void mergeSort(int[] a, int[] tmp, int lo, int hi) {   // sorts a[lo..hi]; call with tmp = new int[a.length]
    if (lo >= hi) return;                         // base case: 0 or 1 element
    int mid = lo + (hi - lo) / 2;
    mergeSort(a, tmp, lo, mid);                   // trust the smaller calls
    mergeSort(a, tmp, mid + 1, hi);
    int i = lo, j = mid + 1, k = lo;
    while (i <= mid && j <= hi) tmp[k++] = a[i] <= a[j] ? a[i++] : a[j++];   // <= keeps it stable
    while (i <= mid) tmp[k++] = a[i++];
    while (j <= hi) tmp[k++] = a[j++];
    System.arraycopy(tmp, lo, a, lo, hi - lo + 1);
}
// Counting (inversions, reverse pairs): both halves are sorted before the merge, so for each i in the
// left half move a pointer j through the right half and add (j - (mid + 1)) - O(n log n) in total.
```

## 31. Merge intervals (LC 56)

```java
int[][] merge(int[][] intervals) {
    Arrays.sort(intervals, (x, y) -> Integer.compare(x[0], y[0]));   // sort by start
    List<int[]> res = new ArrayList<>();
    for (int[] cur : intervals) {
        if (res.isEmpty() || res.get(res.size() - 1)[1] < cur[0]) res.add(cur);   // no overlap -> new block
        else res.get(res.size() - 1)[1] = Math.max(res.get(res.size() - 1)[1], cur[1]);   // overlap -> extend
    }
    return res.toArray(new int[0][]);             // List<int[]> -> int[][]
}
```

## 32. Difference array + sweep line (LC 1094, LC 2406)

```java
boolean carPooling(int[][] trips, int capacity) {  // trip = {passengers, from, to}; stops are 0..1000
    int[] diff = new int[1001];
    for (int[] t : trips) { diff[t[1]] += t[0]; diff[t[2]] -= t[0]; }   // +v where it starts, -v where it ends
    int load = 0;
    for (int d : diff) { load += d; if (load > capacity) return false; }   // prefix sum = load at this stop
    return true;
}

int minGroups(int[][] intervals) {                 // LC 2406: answer = maximum overlap of closed [l, r]
    TreeMap<Integer, Integer> events = new TreeMap<>();
    for (int[] iv : intervals) { events.merge(iv[0], 1, Integer::sum); events.merge(iv[1] + 1, -1, Integer::sum); }
    int cur = 0, best = 0;
    for (int delta : events.values()) { cur += delta; best = Math.max(best, cur); }   // sweep left to right
    return best;
}
```

## 33. Bit manipulation basics

```java
boolean isPowerOfTwo(int n) { return n > 0 && (n & (n - 1)) == 0; }   // exactly one set bit

int countSetBits(int n) { int c = 0; while (n != 0) { n &= n - 1; c++; } return c; }   // clears the lowest set bit

boolean isSet(int n, int i) { return ((n >> i) & 1) == 1; }

int setBit(int n, int i) { return n | (1 << i); }

int clearBit(int n, int i) { return n & ~(1 << i); }

int lowestSetBit(int n) { return n & -n; }

int singleNumber(int[] nums) { int x = 0; for (int v : nums) x ^= v; return x; }   // a ^ a = 0, a ^ 0 = a

int getSum(int a, int b) {                         // LC 371: add without + (XOR = sum, AND << 1 = carry)
    while (b != 0) { int carry = (a & b) << 1; a ^= b; b = carry; }
    return a;
}
// >> keeps the sign bit, >>> fills with 0; library helpers: Integer.bitCount(n), Integer.toBinaryString(n)
```

## 34. Cyclic sort / index-as-hash (values in 1..n: LC 41, 442, 448)

```java
int firstMissingPositive(int[] nums) {             // LC 41: put value v at index v - 1
    int n = nums.length;
    for (int i = 0; i < n; i++)
        while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i]) {   // in range and not home yet
            int j = nums[i] - 1, t = nums[i]; nums[i] = nums[j]; nums[j] = t;
        }
    for (int i = 0; i < n; i++) if (nums[i] != i + 1) return i + 1;   // first index without its value
    return n + 1;
}

List<Integer> findDuplicates(int[] nums) {         // LC 442: mark index |v| - 1 negative ("seen")
    List<Integer> res = new ArrayList<>();
    for (int v : nums) {
        int idx = Math.abs(v) - 1;
        if (nums[idx] < 0) res.add(idx + 1);       // already marked -> second occurrence
        else nums[idx] = -nums[idx];
    }
    return res;
}
```

## 35. Floyd's cycle on an array (LC 287) and the cycle start (LC 142)

```java
int findDuplicate(int[] nums) {                    // LC 287: i -> nums[i] is a linked list; the duplicate is the cycle entry
    int slow = 0, fast = 0;
    do { slow = nums[slow]; fast = nums[nums[fast]]; } while (slow != fast);   // phase 1: meet inside the cycle
    slow = 0;
    while (slow != fast) { slow = nums[slow]; fast = nums[fast]; }             // phase 2: same speed -> entry
    return slow;
}

ListNode detectCycle(ListNode head) {              // LC 142: same two phases on a real list
    ListNode slow = head, fast = head;
    while (fast != null && fast.next != null) {
        slow = slow.next; fast = fast.next.next;
        if (slow == fast) {
            slow = head;
            while (slow != fast) { slow = slow.next; fast = fast.next; }
            return slow;
        }
    }
    return null;
}
```

## 36. Fast I/O for online assessments (full stdin/stdout program)

```java
import java.io.*;
import java.util.*;

public class Main {                                // many OA platforms require the class name Main - read the instructions
    static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static String next() throws IOException {      // next token, even across line breaks
        while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
        return st.nextToken();
    }

    static int nextInt() throws IOException { return Integer.parseInt(next()); }

    static long nextLong() throws IOException { return Long.parseLong(next()); }

    public static void main(String[] args) throws IOException {
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int t = nextInt();                         // example input: t test cases, each = n then n numbers
        while (t-- > 0) {
            int n = nextInt();
            long sum = 0;
            for (int i = 0; i < n; i++) sum += nextLong();
            out.println(sum);                      // buffered - fast even for 10^5 lines
        }
        out.flush();                               // without flush nothing is printed
    }
}
```

## 37. Quickselect (LC 215, average O(n))

```java
int kthLargest(int[] nums, int k) {                // random pivot + 3-way partition (safe with many duplicates)
    int target = nums.length - k;                  // the answer's index in ascending order
    int lo = 0, hi = nums.length - 1;
    Random rnd = new Random();
    while (true) {
        int pivot = nums[lo + rnd.nextInt(hi - lo + 1)];
        int lt = lo, i = lo, gt = hi;              // [lo, lt) < pivot, [lt, i) == pivot, (gt, hi] > pivot
        while (i <= gt) {
            if (nums[i] < pivot) swap(nums, lt++, i++);
            else if (nums[i] > pivot) swap(nums, i, gt--);
            else i++;
        }
        if (target < lt) hi = lt - 1;
        else if (target > gt) lo = gt + 1;
        else return pivot;                         // target index is inside the == block
    }
}

void swap(int[] a, int i, int j) { int t = a[i]; a[i] = a[j]; a[j] = t; }
```

## 38. 0-1 BFS with ArrayDeque (LC 2290; LC 3286 is the same idea)

```java
int minimumObstacles(int[][] grid) {               // entering a 1-cell costs 1, a 0-cell costs 0
    int m = grid.length, n = grid[0].length;
    int[][] dist = new int[m][n];
    for (int[] row : dist) Arrays.fill(row, Integer.MAX_VALUE);
    int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    Deque<int[]> dq = new ArrayDeque<>();
    dist[0][0] = 0;
    dq.offerFirst(new int[]{0, 0});
    while (!dq.isEmpty()) {
        int[] cur = dq.pollFirst();
        for (int[] d : dirs) {
            int r = cur[0] + d[0], c = cur[1] + d[1];
            if (r < 0 || c < 0 || r >= m || c >= n) continue;
            int w = grid[r][c];                    // edge weight: 0 or 1
            if (dist[cur[0]][cur[1]] + w < dist[r][c]) {
                dist[r][c] = dist[cur[0]][cur[1]] + w;
                if (w == 0) dq.offerFirst(new int[]{r, c});   // weight 0 -> front (same distance)
                else dq.offerLast(new int[]{r, c});           // weight 1 -> back
            }
        }
    }
    return dist[m - 1][n - 1];
}
```

## 39. Strongly connected components - Kosaraju (awareness)

```java
int countSCC(int n, List<List<Integer>> g) {       // g = adjacency list of a directed graph
    boolean[] seen = new boolean[n];
    Deque<Integer> order = new ArrayDeque<>();     // finished nodes; the last finished is on top
    for (int i = 0; i < n; i++) if (!seen[i]) dfs1(i, g, seen, order);
    List<List<Integer>> rev = new ArrayList<>();
    for (int i = 0; i < n; i++) rev.add(new ArrayList<>());
    for (int u = 0; u < n; u++) for (int v : g.get(u)) rev.get(v).add(u);   // reverse every edge
    Arrays.fill(seen, false);
    int count = 0;
    while (!order.isEmpty()) {
        int u = order.pop();                       // highest finish time first
        if (!seen[u]) { dfs2(u, rev, seen); count++; }   // one DFS on the reversed graph = one SCC
    }
    return count;
}

void dfs1(int u, List<List<Integer>> g, boolean[] seen, Deque<Integer> order) {
    seen[u] = true;
    for (int v : g.get(u)) if (!seen[v]) dfs1(v, g, seen, order);
    order.push(u);                                 // push after all descendants are finished
}

void dfs2(int u, List<List<Integer>> rev, boolean[] seen) {
    seen[u] = true;
    for (int v : rev.get(u)) if (!seen[v]) dfs2(v, rev, seen);
}
// Recursion depth: for n around 10^5 use an iterative DFS (or run the solver in a Thread with a bigger stack).
```

## 🏋️ How to practise these templates
1. **Monday of each week:** re-type that week's template from memory (5 min) before solving.
2. **Every Saturday:** pick 2 random templates from earlier weeks and re-type them.
3. If a template takes > 5 minutes, mark it 🔴 in [REVISION_TRACKER.md](REVISION_TRACKER.md).
