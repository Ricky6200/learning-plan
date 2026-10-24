# ☕ Java Backend · Week 05 — Collections internals: HashMap, TreeMap, heaps, LRU

> 📅 **Mon 23 Nov 2026 → Sun 29 Nov 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 04](Week-04.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-05.md) · [Week 06 →](Week-06.md)

**Why this week:** "How does HashMap work internally?" is the most-asked Indian Java interview question; building your own versions makes every answer concrete.

## 🗓️ Sessions

### Monday 23 Nov · 60 min — HashMap internals: hash spreading, buckets, load factor, resize
- 📚 **Learn:** `hashCode()` -> spread `h ^ (h >>> 16)` -> index `(n - 1) & hash`; bucket chains and collisions; capacity 16, load factor 0.75, threshold, resize doubling with split; treeify at 8 (table >= 64), untreeify at 6; null key in bucket 0. [Baeldung: HashMap under the hood](https://www.baeldung.com/java-hashmap-advanced), [HashMap Javadoc (JDK 25)](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/HashMap.html), [Concept && Coding: HashMap internals (Hindi video)](https://www.youtube.com/watch?v=AsAymWn7D40).
- 🛠️ **Do:** On paper, insert 6 keys with given hashes into a size-8 table and then resize to 16. In code, print `hashCode`, spread hash and bucket index for 10 String keys using HashMap's formula. Write `BadKey` with a constant hashCode, insert 20k entries and time `get` vs a good key. Done when: you can draw put/get/resize from memory and your timings show the bad-key slowdown.

### Tuesday 24 Nov · 60 min — Key mutability, HashSet, LinkedHashMap access-order LRU
- 📚 **Learn:** Mutable keys break lookups; equal objects must have equal hashes; HashSet is a HashMap with dummy values; LinkedHashMap insertion vs access order (`new LinkedHashMap<>(16, 0.75f, true)`) and `removeEldestEntry` for LRU. [LinkedHashMap Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/LinkedHashMap.html), [Baeldung: LRU cache](https://www.baeldung.com/java-lru-cache), [Baeldung: HashSet](https://www.baeldung.com/java-hashset).
- 🛠️ **Do:** Reproduce the mutable-key bug: put a `Person` key, change its name, `get` returns null and `containsKey` is false. Build `LruCache<K,V> extends LinkedHashMap` in about 10 lines (capacity 3). Done when: 4 tests pass: least-recently-used is evicted, `get` refreshes recency, capacity is respected, overwriting a key does not grow the size.

### Wednesday 25 Nov · 60 min — TreeMap, PriorityQueue binary heap, ArrayDeque
- 📚 **Learn:** TreeMap = red-black tree: O(log n), sorted keys, NavigableMap `floorKey/ceilingKey/headMap`; PriorityQueue = array-based binary heap (parent `(i-1)/2`, children `2i+1`, `2i+2`), iteration not sorted; ArrayDeque as stack and queue instead of Stack/LinkedList. [Baeldung: TreeMap](https://www.baeldung.com/java-treemap), [dev.java: Stacks and queues](https://dev.java/learn/api/collections-and-streams/collections-framework/stacks-queues/), [Baeldung: ArrayDeque](https://www.baeldung.com/java-array-deque).
- 🛠️ **Do:** TreeMap `ShowTimetable` answering next/previous show via `ceilingKey/floorKey`; PriorityQueue for top-3 earners out of 20; ArrayDeque balanced-brackets checker. Then write `MinHeap` (int array, offer/poll/peek, siftUp/siftDown) from scratch. Done when: MinHeap passes 5 tests, including polling 100 random ints in sorted order.

### Thursday 26 Nov · 60 min — Immutable and sequenced collections; ArrayList vs LinkedList
- 📚 **Learn:** `List.of` (immutable, null-hostile) vs `Collections.unmodifiableList` (read-only view) vs `List.copyOf`; Java 21 SequencedCollection/SequencedMap (`getFirst`, `getLast`, `reversed`, `pollLastEntry`); ArrayList growth (1.5x) vs LinkedList node overhead; `subList` is a view. [dev.java: Collection factory methods](https://dev.java/learn/api/collections-and-streams/collections-framework/factory-methods/), [JEP 431: Sequenced collections](https://openjdk.org/jeps/431), [dev.java: ArrayList vs LinkedList](https://dev.java/learn/api/collections-and-streams/collections-framework/arraylist-vs-linkedlist/).
- 🛠️ **Do:** Write tests proving: `List.of` throws on `add` and on null; an unmodifiable view changes when its backing list changes; `copyOf` does not. Use `reversed()`, `getFirst()` and `pollLastEntry()` on LinkedHashMap/TreeMap. Time `get(i)` in a loop on ArrayList vs LinkedList (100k). Done when: 6 tests are green and benchmark numbers are noted in a comment.

### Friday 27 Nov · 60 min — Write MyArrayList<E> test-first
- 📚 **Learn:** Dynamic array internals: backing `Object[]`, size vs capacity, growth `old + old/2`, `System.arraycopy` for insert/remove at index, bounds checks, fail-fast iterator using `modCount`. [MOOC 12.2: ArrayList and hash table](https://java-programming.mooc.fi/part-12/2-arraylist-and-hashtable), [Baeldung: ArrayList](https://www.baeldung.com/java-arraylist).
- 🛠️ **Do:** Implement `MyArrayList<E> implements Iterable<E>`: add, add(index), get, set, remove(index), size, contains, fail-fast iterator. Write each test before its method (TDD). Done when: at least 10 tests are green, including growth past the initial capacity, `IndexOutOfBoundsException`, and `ConcurrentModificationException` when modifying during iteration.

### Saturday 28 Nov · 60 min — BUILD: MyHashMap with chaining and an O(1) LRU cache
- 📚 **Learn:** Design `Node<K,V>[] table`, `hash()` spreading, put/get/remove/containsKey/size, resize at 0.75 with rehash, null-key support; LRU = hash map + hand-written doubly linked list for O(1) get/put (classic interview problem). [Baeldung: HashMap under the hood](https://www.baeldung.com/java-hashmap-advanced), [Baeldung: LRU cache](https://www.baeldung.com/java-lru-cache).
- 🛠️ **Do:** Implement `MyHashMap<K,V>` (separate chaining + resize) and `LruCacheDll<K,V>` using your map plus your own doubly linked list (no LinkedHashMap). Tests: collisions via `BadKey`, resize keeps all entries, null key, eviction order, `get` refreshes recency. Done when: 12+ tests are green and the README states the time complexity of every operation.

## 📦 Deliverable (by Saturday night)
`w05` package: hash/bucket demos, LruCache (LinkedHashMap), MinHeap, MyArrayList, MyHashMap, LruCacheDll with 30+ green tests.

## ✅ Self-check (Sunday test preview)
- Walk through `HashMap.put()` in Java 8+: hash spreading, index, collision, treeify, resize.
- Why is the default load factor 0.75, and why is the capacity always a power of two?
- What happens if a key's hashCode changes after insertion?
- How does LinkedHashMap support LRU? What does access-order mean?
- Compare HashMap, LinkedHashMap and TreeMap on ordering, complexity and null keys.
- How is PriorityQueue implemented, and is its iterator sorted?
- `List.of` vs `Collections.unmodifiableList` vs `List.copyOf`: what is the difference?

## 🚀 Stretch (optional)
Open `HashMap.putVal` and `resize` in IntelliJ (Ctrl+B) and annotate 10 lines in your notes.
