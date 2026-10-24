# ☕ Java Backend · Week 12 — Data layer: JDBC, JPA/Hibernate, Flyway, SQL

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** N+1, lazy loading, persistence context and indexing questions are guaranteed in backend interviews, and most production incidents start in the data layer.

## 🗓️ Sessions

### Monday 11 Jan · 60 min — JDBC basics to ORM: PreparedStatement, transactions, HikariCP
- 📚 **Learn:** JDBC: DataSource, Connection, PreparedStatement vs Statement (SQL injection), ResultSet mapping, manual transactions (`setAutoCommit(false)`, commit/rollback); connection pooling with HikariCP; JPA (spec) vs Hibernate (implementation) vs Spring Data JPA (repositories). [Marco Behler: JDBC guide](https://www.marcobehler.com/guides/jdbc), [Marco Behler: Java and databases overview](https://www.marcobehler.com/guides/java-databases), [Concept && Coding: JDBC to JPA (Hindi video)](https://www.youtube.com/watch?v=p0zuY_OeEh0).
- 🛠️ **Do:** In a scratch test, write a plain-JDBC `VenueDao` against your Postgres container: insert/find with PreparedStatement; demonstrate SQL injection with string-concatenated `Statement` (`' OR '1'='1`); run two inserts in one manual transaction and force a rollback. Done when: injection is shown then blocked, and the rollback leaves zero rows.

### Tuesday 12 Jan · 60 min — Entities, relationships, fetch types, Flyway migrations
- 📚 **Learn:** `@Entity`, `@Id` + sequence generation, `@ManyToOne(fetch = LAZY)` by default choice, `@OneToMany(mappedBy)` bidirectional helpers, cascade and orphanRemoval, why EAGER is a smell; Flyway versioned migrations (`V1__init.sql`), Boot 4 needs `spring-boot-starter-flyway`; `ddl-auto=validate`. [Vlad Mihalcea: Best @OneToMany mapping](https://vladmihalcea.com/the-best-way-to-map-a-onetomany-association-with-jpa-and-hibernate/), [Spring Data JPA: Getting started](https://docs.spring.io/spring-data/jpa/reference/jpa/getting-started.html), [Baeldung: Flyway migrations](https://www.baeldung.com/database-migrations-with-flyway).
- 🛠️ **Do:** Replace JdbcClient code with entities: Venue 1-N Screen 1-N Seat, Event 1-N Show, Show N-1 Screen; write `V1__catalog.sql` by hand (FKs, NOT NULL, unique constraints) and `V2__seed.sql`; set `ddl-auto=validate`; create Spring Data repositories. Done when: the app boots with Flyway applying V1 and V2 and Hibernate validation passing.

### Wednesday 13 Jan · 60 min — N+1 problem, JOIN FETCH, EntityGraph, JPQL, native, projections
- 📚 **Learn:** How N+1 happens with lazy associations; fixes: `JOIN FETCH`, `@EntityGraph`, batch fetching; JPQL vs native queries; derived queries; interface and record (DTO) projections; `Pageable` and the count query. [Vlad Mihalcea: N+1 query problem](https://vladmihalcea.com/n-plus-1-query-problem/), [Spring Data JPA: Projections](https://docs.spring.io/spring-data/jpa/reference/repositories/projections.html), [Baeldung: JPA entity graph](https://www.baeldung.com/jpa-entity-graph).
- 🛠️ **Do:** Enable SQL logging and Hibernate statistics; list 20 shows with venue and screen names and count the queries (N+1). Fix once with JOIN FETCH and once with `@EntityGraph`; add a `ShowSummary` record projection and a paged `findByEventCity(city, Pageable)`. Done when: query count drops from 21+ to 1 or 2 and a test asserts the statement count.

### Thursday 14 Jan · 60 min — Persistence context, dirty checking, entity states, lazy loading pitfalls
- 📚 **Learn:** Entity states (transient, managed, detached, removed); first-level cache; dirty checking at flush; `save` vs `merge`; `LazyInitializationException` and why Open Session in View hides it (`spring.jpa.open-in-view=false`); equals/hashCode for entities. [Vlad Mihalcea: Entity state transitions](https://vladmihalcea.com/a-beginners-guide-to-jpa-hibernate-entity-state-transitions/), [Vlad Mihalcea: Dirty checking](https://vladmihalcea.com/the-anatomy-of-hibernate-dirty-checking/), [Baeldung: Hibernate entity lifecycle](https://www.baeldung.com/hibernate-entity-lifecycle).
- 🛠️ **Do:** Write `@DataJpaTest` tests proving: a managed entity changed inside a transaction is updated without calling `save`; the same id loaded twice returns the same instance; a detached change is lost until `merge`; touching a lazy collection outside a transaction throws. Disable open-in-view. Done when: 4 tests pass and you can explain each from the SQL log.

### Friday 15 Jan · 60 min — PostgreSQL indexes, EXPLAIN ANALYZE, SQL interview drills
- 📚 **Learn:** B-tree and composite indexes (column order), covering and partial indexes, when indexes are not used; reading `EXPLAIN ANALYZE` (Seq Scan vs Index Scan, rows, cost); SQL drills: joins, GROUP BY/HAVING, window functions (`ROW_NUMBER`, `DENSE_RANK`, running totals), nth-highest salary. [PostgreSQL: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), [Use The Index, Luke](https://use-the-index-luke.com/), [techTFQ: SQL window functions (video)](https://www.youtube.com/watch?v=Ww71knvhQ-s).
- 🛠️ **Do:** Load 1M `show_seat` rows with `generate_series`; run `EXPLAIN ANALYZE` for 'available seats of a show' before and after a composite index `(show_id, status)` and record timings. Solve 5 problems from LeetCode SQL 50 including nth-highest salary with `DENSE_RANK` and a department top-3. Done when: the plan switches to an index scan and the 5 queries are saved in `sql/drills.sql`.

### Saturday 16 Jan · 60 min — BUILD: TicketVerse data model, migrations, Testcontainers tests
- 📚 **Learn:** Booking data model: `venue`, `screen`, `seat`, `show`, `show_seat` (status, price, `version`), `booking`, `booking_seat`; constraints as the last line of defense (unique show+seat); `@DataJpaTest` with real Postgres via Testcontainers 2.x and `@ServiceConnection`. [Spring Boot: Testcontainers](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html), [Testcontainers: Replace H2 with a real database](https://testcontainers.com/guides/replace-h2-with-real-database-for-testing/).
- 🛠️ **Do:** Add migrations V3 (`show_seat`, `booking`, `booking_seat` with UNIQUE(show_id, seat_id)) and V4 (indexes); entities and repositories; seed one show with 100 seats. Tests on Testcontainers Postgres: available-seats query, unique-constraint violation on a duplicate booking_seat, paging. Done when: `./mvnw verify` is green with Docker running and the ER diagram (Mermaid) is in the README.

## 📦 Deliverable (by Saturday night)
TicketVerse on JPA/Hibernate with Flyway V1-V4, N+1 fixed with tests, persistence-context tests, indexed show_seat with EXPLAIN evidence, SQL drills, Testcontainers-backed `@DataJpaTest` suite.

## ✅ Self-check (Sunday test preview)
- JPA vs Hibernate vs Spring Data JPA: what is each?
- What is the N+1 problem and three ways to fix it?
- Explain entity states and dirty checking. When is `save()` unnecessary?
- Why does LazyInitializationException happen, and why is Open Session in View considered an anti-pattern?
- When does PostgreSQL ignore an index? How do you read EXPLAIN ANALYZE?
- Write (verbally) a query for the 3rd highest salary per department.
- Why test with Testcontainers instead of H2?

## 🚀 Stretch (optional)
Read Vlad Mihalcea's [FetchType EAGER is a code smell](https://vladmihalcea.com/eager-fetching-is-a-code-smell/) and remove any remaining EAGER mapping.
