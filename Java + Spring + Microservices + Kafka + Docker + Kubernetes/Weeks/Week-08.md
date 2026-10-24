# ☕ Java Backend · Week 08 — Multithreading I: threads, locks, JMM, executors

> 📅 **Mon 14 Dec 2026 → Sun 20 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 07](Week-07.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-08.md) · [Week 09 →](Week-09.md)

**Why this week:** Concurrency (synchronized vs volatile, deadlock, producer-consumer, thread pools) separates SDE-1 from SDE-2 answers, and it is one of your self-rated weak spots.

## 🗓️ Sessions

### Monday 14 Dec · 60 min — Threads: lifecycle, Runnable/Callable, sleep, join, interrupt, daemon
- 📚 **Learn:** Process vs thread (shared heap, own stack); states NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED; Thread vs Runnable vs Callable; `start()` vs `run()`; `sleep`, `join`; cooperative interruption (catch `InterruptedException`, restore the flag); daemon threads. [Oracle: Processes and threads](https://docs.oracle.com/javase/tutorial/essential/concurrency/procthread.html), [Baeldung: Thread lifecycle](https://www.baeldung.com/java-thread-lifecycle), [Oracle: Interrupts](https://docs.oracle.com/javase/tutorial/essential/concurrency/interrupt.html).
- 🛠️ **Do:** In `w08`, simulate 3 downloads in 3 threads, `join` them and print total time; repeat calling `run()` instead of `start()` and compare. Write a worker loop that stops cleanly on `interrupt()` and restores the flag; print `getState()` at 4 points; start a daemon thread and watch the JVM exit. Done when: your output shows NEW, RUNNABLE, TIMED_WAITING and TERMINATED.

### Tuesday 15 Dec · 60 min — Race conditions, synchronized, intrinsic locks, reentrancy
- 📚 **Learn:** Critical sections and read-modify-write races (`count++`); synchronized methods vs blocks; choosing the lock (`this` vs private final lock vs class lock); reentrancy; `static synchronized`; contention and the BLOCKED state. [Jenkov: Race conditions](https://jenkov.com/tutorials/java-concurrency/race-conditions-and-critical-sections.html), [Jenkov: Synchronized blocks](https://jenkov.com/tutorials/java-concurrency/synchronized.html), [Baeldung: synchronized keyword](https://www.baeldung.com/java-synchronized).
- 🛠️ **Do:** Increment a shared counter from 4 threads x 100,000 and print wrong totals in 3 runs; fix with a `synchronized` block on a private lock, then with `AtomicInteger`; time both. Write a `BankAccount` whose synchronized `transfer` calls another synchronized method (reentrancy). Done when: the unsafe version loses updates and both fixes print exactly 400000.

### Wednesday 16 Dec · 60 min — volatile, visibility, Java Memory Model, happens-before
- 📚 **Learn:** CPU caches and reordering; visibility vs atomicity; `volatile` gives visibility and ordering, not atomicity; happens-before rules (program order, unlock -> lock, volatile write -> read, `start`, `join`); safe publication; why double-checked locking needs volatile. [Jenkov: Java Memory Model](https://jenkov.com/tutorials/java-concurrency/java-memory-model.html), [Jenkov: Happens-before](https://jenkov.com/tutorials/java-concurrency/java-happens-before-guarantee.html), [Defog Tech: JMM in 10 minutes (video)](https://www.youtube.com/watch?v=Z4hMFBvCDV4).
- 🛠️ **Do:** Write the stop-flag demo: a busy `while (!stop)` loop that may never end without `volatile` (try a few runs), then fix it with volatile. Implement a lazy singleton 3 ways: synchronized method, double-checked locking with volatile, holder-class idiom. Done when: all 3 singletons return one instance across 100 threads in a test and you can say which you would use and why.

### Thursday 17 Dec · 60 min — wait/notify, producer-consumer, deadlock detection with jstack
- 📚 **Learn:** Guarded blocks: `wait()` inside a `while` loop (spurious wakeups) while holding the monitor; `notify` vs `notifyAll`; bounded-buffer producer-consumer; the 4 deadlock conditions, lock ordering, `tryLock` preview; detection with `jstack` or `jcmd <pid> Thread.print`. [Oracle: Guarded blocks](https://docs.oracle.com/javase/tutorial/essential/concurrency/guardmeth.html), [Baeldung: wait and notify](https://www.baeldung.com/java-wait-notify), [Jenkov: Deadlock prevention](https://jenkov.com/tutorials/java-concurrency/deadlock-prevention.html).
- 🛠️ **Do:** Write `BoundedBuffer<T>` (capacity 5) with synchronized `put/take` using wait/notifyAll; run 2 producers and 2 consumers for 1,000 items and assert none are lost. Create a deadlock with two locks taken in opposite order, capture `jstack <pid>` showing the deadlock, then fix with global lock ordering. Done when: the jstack excerpt is saved in `notes/deadlock.txt` and the fixed version finishes.

### Friday 18 Dec · 60 min — ExecutorService, ThreadPoolExecutor parameters, rejection policies, Future
- 📚 **Learn:** Why pools; hidden unbounded queues in `Executors` factories; `ThreadPoolExecutor(core, max, keepAlive, queue, threadFactory, handler)` flow: core -> queue -> max -> reject; 4 rejection policies; `submit` vs `execute`; `Future.get` with timeout; `invokeAll`; `shutdown` vs `shutdownNow` + `awaitTermination`. [ThreadPoolExecutor Javadoc](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/concurrent/ThreadPoolExecutor.html), [Baeldung: ExecutorService](https://www.baeldung.com/java-executor-service-tutorial), [Defog Tech: ExecutorService (video)](https://www.youtube.com/watch?v=6Oo-9Can3H8).
- 🛠️ **Do:** Create `new ThreadPoolExecutor(2, 4, 30, SECONDS, new ArrayBlockingQueue<>(2), namedFactory, new CallerRunsPolicy())`; submit 10 slow tasks and log thread names; switch to `AbortPolicy` and catch `RejectedExecutionException`. Run 5 Callables with `invokeAll` and one `Future.get(1, SECONDS)` timeout. Done when: the log matches your written prediction of core -> queue -> max -> reject.

### Saturday 19 Dec · 60 min — BUILD: odd-even printer, producer-consumer twice, deadlock fix
- 📚 **Learn:** Classic interview programs: two threads printing odd/even alternately, producer-consumer with `BlockingQueue` (`put/take`, poison-pill shutdown), deadlock demo and fix via lock ordering; testing concurrent code without flakiness. [Jenkov: Producer-consumer pattern](https://jenkov.com/tutorials/java-concurrency/producer-consumer.html), [Baeldung: Producer-consumer](https://www.baeldung.com/java-producer-consumer-problem).
- 🛠️ **Do:** In `w08.build`: `OddEvenPrinter` (1-20 strictly alternating), `ProducerConsumerWaitNotify`, `ProducerConsumerBlockingQueue` (poison pill), `DeadlockDemo` + `DeadlockFixed`. JUnit: printed sequence equals 1..20, consumers receive all 1,000 items, fixed version completes within 2 s (`assertTimeoutPreemptively`). Done when: all tests pass 5 runs in a row (flaky means not done).

## 📦 Deliverable (by Saturday night)
`w08` package: thread lifecycle demos, race fixes, singleton x3, BoundedBuffer, jstack deadlock evidence, ThreadPoolExecutor experiment, Saturday classics with stable tests.

## ✅ Self-check (Sunday test preview)
- Name the thread states. What causes BLOCKED vs WAITING?
- synchronized vs volatile: is `volatile int count; count++` thread-safe?
- Why must wait() be called in a loop and inside a synchronized block?
- What are the four deadlock conditions? How do you prevent one and detect one in production?
- Explain the ThreadPoolExecutor task flow and the four rejection policies.
- Why can `Executors.newFixedThreadPool` hurt you in production?
- start() vs run(); what happens if you call start() twice?

## 🚀 Stretch (optional)
Read the Oracle tutorial page on [liveness](https://docs.oracle.com/javase/tutorial/essential/concurrency/liveness.html) and write a tiny livelock demo.
