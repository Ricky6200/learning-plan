# ⌨️ LLD / Machine-Coding Framework (Java)

Machine-coding rounds (common at Indian product companies such as Flipkart, Swiggy, PhonePe, Razorpay and Uber India) give you a problem statement and **60–120 minutes (often 90)** to produce **working, extensible, readable code** — usually in-memory, no frameworks, demonstrated through a driver `main` or tests, followed by "now extend it…" questions. This playbook turns that into a routine.

> Your personal rule: **design on paper for ≤ 30% of the time, then code the happy path end to end before polishing anything.** Working code beats a beautiful diagram with half the code.

---

## 1. The 90-minute playbook (minute by minute)

| Clock | Phase | Output | Tips |
|---|---|---|---|
| 0–10 | **Clarify** | Must-have vs nice-to-have list; input/output format (driver, CLI, tests); assumptions written at the top of `DESIGN.md` | Ask the questions in Section 3; confirm scope out loud |
| 10–20 | **Entities & relationships** | Nouns → classes, verbs → methods, states → enums; ownership and multiplicity | Use the extraction method in Section 4 |
| 20–30 | **Class diagram + patterns** | Interfaces at variation points; package layout; key method signatures | Only add a pattern where something *varies* or must be *decoupled* |
| 30–55 | **Code the core (happy path)** | `model` → `repository` (in-memory) → `strategy` → `service` → driver | Compile every 5–10 minutes; no gold-plating |
| 55–70 | **Edge cases & errors** | Custom exceptions, validation, state-transition guards | Fail fast with clear messages |
| 70–80 | **Tests / demo** | 5–8 JUnit tests or a driver showing every requirement; one race test if state is shared | Deterministic time via injected `Clock` |
| 80–90 | **Refactor & explain** | Rename, extract, remove duplication; README of assumptions and extension points | Prepare 2–3 "how I'd extend" answers |

### 45-minute compressed version (used in this plan's sessions and boss battles)

| Clock | Phase |
|---|---|
| 0–5 | Requirements (top 4–5) + assumptions |
| 5–12 | Entities + quick class sketch (Mermaid or paper) |
| 12–35 | Core code for the happy path + the most important rule |
| 35–42 | 4–6 tests (happy path, 2 edge cases, invalid input, race if relevant) |
| 42–45 | Commit + note what you'd add next |

---

## 2. Before you start: project skeleton (have it ready)

```text
src/main/java/com/sdlab/lld/<problem>/
├─ model/        # entities, value objects (records), enums
├─ repository/   # interfaces + InMemory… implementations (ConcurrentHashMap)
├─ strategy/     # pluggable rules: allocation, pricing, split, dispatch…
├─ service/      # use cases; orchestrates model + repositories + strategies
├─ exception/    # domain exceptions (unchecked)
└─ Demo.java     # driver showing each requirement (optional if tests cover it)
src/test/java/com/sdlab/lld/<problem>/   # one test class per service
```

```java
// model
public enum VehicleType { BIKE, CAR, TRUCK }
public record Vehicle(String number, VehicleType type) { }

// repository
public interface TicketRepository {
    void save(Ticket ticket);
    Optional<Ticket> findById(String id);
}
public final class InMemoryTicketRepository implements TicketRepository {
    private final Map<String, Ticket> store = new ConcurrentHashMap<>();
    public void save(Ticket t) { store.put(t.id(), t); }
    public Optional<Ticket> findById(String id) { return Optional.ofNullable(store.get(id)); }
}

// strategy
public interface FeeStrategy { long feeInPaise(Duration parked, VehicleType type); }

// exception
public class ParkingFullException extends RuntimeException {
    public ParkingFullException(VehicleType type) { super("No free spot for " + type); }
}

// service: dependencies injected through the constructor (DIP), time injected for tests
public final class ParkingService {
    private final SpotAllocationStrategy allocation;
    private final FeeStrategy fees;
    private final TicketRepository tickets;
    private final Clock clock;

    public ParkingService(SpotAllocationStrategy allocation, FeeStrategy fees,
                          TicketRepository tickets, Clock clock) {
        this.allocation = allocation; this.fees = fees; this.tickets = tickets; this.clock = clock;
    }
    // public Ticket park(Vehicle v) { ... }   public long unpark(String ticketId) { ... }
}
```

`pom.xml` essentials (versions as of Oct 2026): JDK **25** (`<maven.compiler.release>25</maven.compiler.release>`), `org.junit:junit-bom` **6.1.x** + `junit-jupiter` (test scope), `org.assertj:assertj-core` **3.27.x**, `maven-surefire-plugin` **3.5.x**.

---

## 3. Requirement-clarification questions

| Area | Ask |
|---|---|
| Scope | Which 3–4 features are must-have? What can I skip (payments, UI, persistence)? |
| Actors | Who uses it — customer, admin, system/cron? Do admins configure things at runtime? |
| Rules | What exactly happens on edge cases (full lot, insufficient balance, duplicate request)? |
| Scale & concurrency | Multiple users at the same time? Multiple entry gates / ATMs / threads? |
| Persistence | In-memory OK? Should storage be swappable (repository interface)? |
| I/O | Driver `main`, CLI commands, or tests? Any fixed input format to parse? |
| Extensibility | Which dimension is likely to change (new vehicle type, new split type, new pricing rule)? |
| Non-functional | Any time-based behaviour (expiry, fines) — can I inject a clock? |

---

## 4. Entity & relationship extraction (10 minutes)

1. **Underline nouns** in the statement → candidate classes (drop synonyms and pure attributes).
2. **Circle verbs** → methods on the class that owns the data, or a service if it spans entities.
3. **States and types** (`AVAILABLE/HELD/BOOKED`, `BIKE/CAR`) → enums; behaviour that changes per state → **State** pattern.
4. **"Can be one of several ways"** (pricing, allocation, dispatch, split) → interface + **Strategy**.
5. **Ownership** → composition (Floor owns Spots); **references** → association (Ticket refers to Vehicle); write multiplicities.
6. **Identify shared mutable state** now (seats, spots, balances) — you will need a concurrency plan for it.

Example (Parking Lot): nouns → `ParkingLot`, `Floor`, `Spot`, `Vehicle`, `Ticket`, `Gate`, `Payment`; verbs → `park`, `unpark`, `calculateFee`, `pay`; types → `VehicleType`, `SpotType`, `SpotStatus`; variation points → `SpotAllocationStrategy`, `FeeStrategy`; shared state → spot occupancy.

---

## 5. Which pattern when

| Signal in the problem | Pattern | Example in this plan |
|---|---|---|
| Algorithm/rule varies or is chosen at runtime | **Strategy** | Fees (Parking Lot), split types (Splitwise), dispatch (Elevator), pricing kata |
| Behaviour depends on current state; illegal actions per state | **State** | Vending Machine, ATM, order lifecycle, elevator car |
| Others must react to an event | **Observer** | Reservation available (Library), order status (Food delivery), notifications |
| Request passes through ordered handlers | **Chain of Responsibility** | Logger levels/handlers, ATM cash dispenser, ticket escalation |
| Undo/redo, queue or log actions | **Command** | Text editor, chess move history |
| Fixed algorithm skeleton, varying steps | **Template Method** | Report exporters, notification rendering |
| Create one of many types without `switch` | **Factory (registry map)** | Notification senders, payment processors |
| Many optional parameters, immutable result | **Builder** | `Notification`, `Booking` requests |
| Exactly one shared instance | **Singleton** (prefer DI; enum if needed) | Logger, ID generator |
| Add behaviour by wrapping | **Decorator** | Retrying/rate-limited senders, I/O streams |
| Control access (cache, lazy, auth) | **Proxy** | Caching price proxy |
| Incompatible external API | **Adapter** | Legacy payment SDK |
| Part–whole trees | **Composite** | File system sizes |
| Central coordinator between many objects | **Mediator** | Auction room, chat room |
| Snapshot and restore | **Memento** | Editor checkpoints |

**Anti-pattern alert:** a pattern you can't justify in one sentence is noise. Interviewers reward *appropriate* patterns, not *many*.

---

## 6. Concurrency checklist (run it for every problem with shared state)

- [ ] **List shared mutable state** (spots, seats, balances, stock, queues, counters).
- [ ] Prefer **immutability** (records, `List.copyOf`) and **confinement** (one owner thread) where possible.
- [ ] Use **atomic map operations** — `ConcurrentHashMap.compute/merge/putIfAbsent` — instead of check-then-act (`if (!map.containsKey(k)) map.put(k, v)` is a race).
- [ ] For compound updates across objects, use **one lock per aggregate** (`ReentrantLock` per show/room/account) and **acquire multiple locks in a fixed order** (sorted IDs) to avoid deadlock.
- [ ] Counters → `AtomicLong`/`LongAdder`; flags → `volatile` or atomics.
- [ ] **Never hold a lock during slow I/O** (payment calls, sleeps) — reserve under lock, call outside, confirm under lock.
- [ ] Time-based rules (holds, TTL, fines) use an injected **`Clock`**; expiry is checked lazily and/or by a scheduled sweeper.
- [ ] Make operations **idempotent** where retries are possible (request IDs).
- [ ] Executors are **shut down**; blocking queues are **bounded** (backpressure).
- [ ] Write at least one **race test** (below) and repeat it (`@RepeatedTest(20)`).

```java
@RepeatedTest(20)
void onlyOneUserGetsTheLastSeat() throws Exception {
    ExecutorService pool = Executors.newFixedThreadPool(16);
    CountDownLatch start = new CountDownLatch(1);
    AtomicInteger wins = new AtomicInteger();
    List<Future<Object>> results = new ArrayList<>();
    for (int i = 0; i < 100; i++) {
        String user = "u" + i;
        results.add(pool.submit(() -> {
            start.await();                                   // all threads start together
            try { holds.hold("show-1", List.of("A1"), user); wins.incrementAndGet(); }
            catch (SeatUnavailableException expected) { }
            return null;
        }));
    }
    start.countDown();
    for (Future<Object> f : results) f.get();                // surfaces unexpected exceptions
    pool.shutdown();
    assertThat(wins.get()).isEqualTo(1);
}
```

---

## 7. Testing checklist

- [ ] One test class per service; names like `park_assignsNearestSpot_whenLotHasSpace()`
- [ ] **Happy path** for every must-have requirement
- [ ] **Boundaries**: empty, capacity reached, exact limit, zero/negative amounts, rounding (money in paise or `BigDecimal`)
- [ ] **Invalid input** → specific exception (`assertThatThrownBy(...).isInstanceOf(...)`)
- [ ] **State transitions**: every illegal action in every state throws
- [ ] **Time**: fixed/adjustable `Clock` instead of `Thread.sleep`
- [ ] **Concurrency**: race test when state is shared
- [ ] Tests run in < 5 s; `mvn -q test` is green before you commit

---

## 8. How interviewers evaluate (typical rubric)

Synthesised from common machine-coding guidelines — use it to self-score every problem (0–3 per line).

| Dimension | Weight (approx.) | What "3" looks like |
|---|---|---|
| Working, complete code | 30% | All must-haves run; demo/tests prove it |
| Design & extensibility | 25% | Clear responsibilities; interfaces at variation points; adding a type touches one class |
| Code quality | 15% | Good names, small methods, no duplication, no public mutable fields, enums over strings |
| Correctness & edge cases | 10% | Validation, meaningful exceptions, state guards |
| Concurrency | 10% | Shared state identified and protected; no check-then-act races |
| Tests / demo | 5% | Focused, deterministic tests |
| Communication | 5% | Clarified scope, stated assumptions, explained trade-offs |

---

## 9. LLD problems in this plan

| Week | Problem | Key patterns & skills | Extension question to practise |
|---|---|---|---|
| W1 | Bank / Library (diagram + skeleton) | UML, OOP pillars | Add a new account type |
| W2 | `OrderManager` God-class refactor | SRP, OCP, DIP, characterization tests | Swap email for SMS without touching the service |
| W3 | Notification factory kata | Factory registry, Builder | Add Slack in one class |
| W4 | LRU cache with TTL (Boss) | HashMap + DLL, `ReentrantLock`, `Clock` | Switch to LFU |
| W5 | Pricing + notifications kata | Strategy, Observer | Add a new discount rule |
| W6 | Tic-Tac-Toe | O(1) win detection, Game/Board/Player | N players, undo |
| W6 | Snake & Ladder | Strategy (dice), queue of players | Multiple dice, crooked dice |
| W7 | Parking Lot | Strategy (allocation, fees), Factory | Multiple gates concurrently, EV charging |
| W7 | Vending Machine | State | New coin type, refunds |
| W8 | Elevator | State, Strategy (LOOK/nearest car) | Add express elevators |
| W8 | Logging framework | Chain of Responsibility, Singleton, Strategy (formatter) | Async logging |
| W9 | Splitwise | Strategy (split types), heaps for simplify debts | Groups, currency |
| W9 | Library management | Observer (reservations), Strategy (fines) | Multiple branches |
| W10 | BookMyShow seat holds | Per-show locks, TTL holds, race tests | Seat hold across two screens |
| W12 | Kafka-like pub-sub | Partitions, offsets, consumer groups, DLQ | Retention, compaction |
| W12 | Job scheduler | `DelayQueue`, thread pool, retries with backoff | Cron expressions, priorities |
| W13 | ATM | State, Chain of Responsibility (cash) | New denomination |
| W13 | Meeting-room scheduler | `TreeMap` interval checks, Strategy (room choice) | Recurring meetings |
| W14 | Chess (or Cricbuzz) | Polymorphism, Command (history) | Castling, undo |
| W14 | Inventory / order management | Reservations with TTL, order State, no-oversell | Multi-warehouse allocation |
| W15 | Notification system | Factory, Template Method, Decorator (retry, rate limit), bounded queue | Per-channel circuit breaker |
| W15 | Food delivery | Order State, Strategy (assignment), Observer | Batch two orders per rider |
| W16 | Thread-safe KV store with TTL | Atomic ops, lazy + active expiry, LRU eviction | Persistence via append-only log |
| W25 | Unseen problem (e.g., Amazon Locker) — mock | Everything | Interviewer's choice |

Compare your solution afterwards with [awesome-low-level-design problems](https://github.com/ashishps1/awesome-low-level-design) and the free Hello Interview LLD breakdowns ([Connect Four](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/connect-four), [Elevator](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/elevator), [Amazon Locker](https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/amazon-locker)).

---

## 10. Handling "now extend it…" questions

1. Repeat the change in one sentence and name the **variation point** it hits.
2. Show that it is **one new class + one registration** (Strategy/Factory) — that is the payoff of your design.
3. If it doesn't fit, say what you'd refactor (e.g., "extract `PricingRule` interface") rather than hacking an `if`.
4. For "make it concurrent": point to the shared state list and the lock/atomic you'd use (Section 6).
5. For "persist it": swap the in-memory repository for a JDBC/JPA one behind the same interface.

## 11. Common mistakes

| Mistake | Fix |
|---|---|
| 40 minutes of diagrams, 20 minutes of code | Stop designing at minute 30, whatever happens |
| God service with all logic | Push behaviour into the entity that owns the data |
| `String` status fields and `if/else` ladders | Enums + State/Strategy |
| Public mutable fields, setters everywhere | Constructor-initialised, final fields; records for values |
| Ignoring concurrency until asked | Note shared state at design time; protect it |
| No way to demo | Driver `main` or tests from the start |
| `Thread.sleep` in tests | Injected `Clock` |
| Over-patterning | One sentence of justification per pattern, or remove it |

## 12. `DESIGN.md` template (one per problem)

```markdown
# <Problem> — LLD (Week NN)
## Requirements (must-have / nice-to-have) and assumptions
## Entities & relationships (Mermaid class diagram)
## Patterns used — and why (one line each)
## Concurrency plan (shared state → protection)
## Test list
## Extension points
## Mistakes I made (update after each attempt)
```

Useful references: [Hello Interview — LLD delivery framework](https://www.hellointerview.com/learn/low-level-design/in-a-hurry/delivery) · [Concurrency in LLD interviews (Hello Interview video)](https://www.youtube.com/watch?v=d8rmosXttTE) · [Low-level design interview tips (Gaurav Sen)](https://www.youtube.com/watch?v=VdwkFAhLEHo) · Hindi: [Low Level Design playlist (Concept && Coding)](https://www.youtube.com/playlist?list=PL6W8uoQQ2c61X_9e6Net0WdYZidm7zooW).
