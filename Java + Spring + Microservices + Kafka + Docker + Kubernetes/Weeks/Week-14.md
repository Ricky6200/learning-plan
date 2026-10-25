# ☕ Java Backend · Week 14 — Data layer: JDBC, JPA/Hibernate, Flyway, SQL, first CI

> 📅 **Mon 25 Jan 2027 → Sun 31 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon–Fri · 60 min (Block B) + Sat 60 min BUILD · Sunday test: 30 min

[← Week 13](Week-13.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-14.md) · [Week 15 →](Week-15.md)

**Why this week:** N+1, lazy loading, persistence context and indexing questions are guaranteed in backend interviews, and most production incidents start in the data layer; a first CI workflow keeps every later change honest.

## 🗓️ Sessions

### Monday 25 Jan · 60 min — JDBC basics to ORM: PreparedStatement, transactions, HikariCP
- 📚 **Learn:** JDBC: DataSource, Connection, PreparedStatement vs Statement (SQL injection), ResultSet mapping, manual transactions (`setAutoCommit(false)`, commit/rollback); connection pooling with HikariCP; JPA (spec) vs Hibernate (implementation) vs Spring Data JPA (repositories). Read: [Marco Behler: JDBC guide](https://www.marcobehler.com/guides/jdbc). Optional: [Concept && Coding: JDBC to JPA (Hindi video)](https://www.youtube.com/watch?v=p0zuY_OeEh0).
- 🛠️ **Do:** In a scratch test, write a plain-JDBC `VenueDao` against your Postgres container: insert/find with PreparedStatement; demonstrate SQL injection with string-concatenated `Statement` (`' OR '1'='1`); run two inserts in one manual transaction and force a rollback. Done when: injection is shown then blocked, and the rollback leaves zero rows.

### Tuesday 26 Jan · 60 min — Entities, relationships, fetch types, Flyway migrations
- 📚 **Learn:** `@Entity`, `@Id` + sequence generation, `@ManyToOne(fetch = LAZY)` as the default choice, `@OneToMany(mappedBy)` bidirectional helpers, cascade and orphanRemoval, why EAGER is a smell; Flyway versioned migrations (`V1__init.sql`), Boot 4 needs `spring-boot-starter-flyway`; `ddl-auto=validate`. Read: [Vlad Mihalcea: Best @OneToMany mapping](https://vladmihalcea.com/the-best-way-to-map-a-onetomany-association-with-jpa-and-hibernate/). Optional: [Baeldung: Flyway migrations](https://www.baeldung.com/database-migrations-with-flyway).
- 🛠️ **Do:** Replace JdbcClient code with entities: Venue 1-N Screen 1-N Seat, Event 1-N Show, Show N-1 Screen; write `V1__catalog.sql` by hand (FKs, NOT NULL, unique constraints) and `V2__seed.sql`; set `ddl-auto=validate`; create Spring Data repositories. Done when: the app boots with Flyway applying V1 and V2 and Hibernate validation passing.

### Wednesday 27 Jan · 60 min — N+1 problem, JOIN FETCH, EntityGraph, projections, keyset paging
- 📚 **Learn:** How N+1 happens with lazy associations; fixes: `JOIN FETCH`, `@EntityGraph`, batch fetching; JPQL vs native vs derived queries; interface and record (DTO) projections; `Pageable` uses OFFSET plus a count query and gets slow on deep pages, while keyset (seek) pagination `WHERE id > :lastId` stays fast (Spring Data `Window`/`ScrollPosition`); `Specification`s compose dynamic filters (you use them in W25). Read: [Vlad Mihalcea: N+1 query problem](https://vladmihalcea.com/n-plus-1-query-problem/). Optional: [Spring Data JPA: Projections](https://docs.spring.io/spring-data/jpa/reference/repositories/projections.html).
- 🛠️ **Do:** Enable SQL logging and Hibernate statistics; list 20 shows with venue and screen names and count the queries (N+1). Fix once with JOIN FETCH and once with `@EntityGraph`; add a `ShowSummary` record projection and a paged `findByEventCity(city, Pageable)`. Done when: query count drops from 21+ to 1 or 2 and a test asserts the statement count.

### Thursday 28 Jan · 60 min — Persistence context, dirty checking, entity states, lazy loading pitfalls
- 📚 **Learn:** Entity states (transient, managed, detached, removed); the first-level cache (one per persistence context); dirty checking at flush; `save` vs `merge`; `LazyInitializationException` and why Open Session in View hides it (`spring.jpa.open-in-view=false`); equals/hashCode for entities. The optional second-level cache is shared across sessions, opt-in per entity and costly to keep consistent, so it is rarely the first fix. Read: [Vlad Mihalcea: Entity state transitions](https://vladmihalcea.com/a-beginners-guide-to-jpa-hibernate-entity-state-transitions/). Optional: [Vlad Mihalcea: Dirty checking](https://vladmihalcea.com/the-anatomy-of-hibernate-dirty-checking/).
- 🛠️ **Do:** Write `@DataJpaTest` tests proving: a managed entity changed inside a transaction is updated without calling `save`; the same id loaded twice returns the same instance; a detached change is lost until `merge`; touching a lazy collection outside a transaction throws. Disable open-in-view. Done when: 4 tests pass and you can explain each from the SQL log.

### Friday 29 Jan · 60 min — PostgreSQL indexes, EXPLAIN ANALYZE, SQL interview drills
- 📚 **Learn:** B-tree and composite indexes (column order), covering and partial indexes, when indexes are not used; reading `EXPLAIN ANALYZE` (Seq Scan vs Index Scan, rows, cost); SQL drills: joins, GROUP BY/HAVING, window functions (`ROW_NUMBER`, `DENSE_RANK`, running totals), nth-highest salary. Read: [PostgreSQL: Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html). Optional: [Use The Index, Luke](https://use-the-index-luke.com/).
- 🛠️ **Do:** Load 1M `show_seat` rows with `generate_series`; run `EXPLAIN ANALYZE` for 'available seats of a show' before and after a composite index `(show_id, status)` and record timings. Solve 3 problems from LeetCode SQL 50, including nth-highest salary with `DENSE_RANK` and a department top-3. Done when: the plan switches to an index scan and the 3 queries are saved in `sql/drills.sql`.

### Saturday 30 Jan · 60 min — BUILD: Data model, migrations, Testcontainers tests, first CI workflow
- 📚 **Learn:** Booking data model: `show_seat` (status, price, `version`), `booking`, `booking_seat`; constraints as the last line of defence (UNIQUE show + seat); `@DataJpaTest` on real Postgres via Testcontainers 2.x + `@ServiceConnection`. First CI: a workflow YAML in `.github/workflows/` runs on push and pull request on `ubuntu-latest`, where Docker is preinstalled, so Testcontainers tests run there too. Read: [GitHub Docs: Building and testing Java with Maven](https://docs.github.com/en/actions/tutorials/build-and-test-code/java-with-maven). Optional: [GitHub Docs: Adding a workflow status badge](https://docs.github.com/en/actions/how-tos/monitor-workflows/add-a-status-badge).
- 🛠️ **Do:** Add migrations V3 (`show_seat`, `booking`, `booking_seat` with UNIQUE(show_id, seat_id)) and V4 (indexes), entities, repositories and a seed show with 100 seats; write 2 `@DataJpaTest` tests on Testcontainers Postgres (available-seats query; a duplicate booking_seat violates the constraint). Then add `.github/workflows/ci.yml` (about 15 min): `actions/setup-java` (Temurin 25, Maven cache) and `./mvnw -B verify` on push and PR, plus a status badge in the README. Done when: the first workflow run on GitHub is green and the badge shows passing.

## 📦 Deliverable (by Saturday night)
TicketVerse on JPA/Hibernate with Flyway V1-V4, N+1 fixed with tests, persistence-context tests, indexed show_seat with EXPLAIN evidence, SQL drills, a Testcontainers-backed `@DataJpaTest` suite and a first GitHub Actions `ci.yml` with a README badge.

## ✅ Self-check (Sunday test preview)
- JPA vs Hibernate vs Spring Data JPA: what is each?
- What is the N+1 problem and three ways to fix it?
- Explain entity states and dirty checking. When is `save()` unnecessary?
- Why does LazyInitializationException happen, and why is Open Session in View considered an anti-pattern?
- Offset vs keyset pagination: why does keyset stay fast on page 10,000? When would you reach for Specifications or a second-level cache?
- When does PostgreSQL ignore an index? How do you read EXPLAIN ANALYZE?
- Why test with Testcontainers instead of H2, and how do those tests run in GitHub Actions?

## 🚀 Stretch (optional)
Read Vlad Mihalcea's [FetchType EAGER is a code smell](https://vladmihalcea.com/eager-fetching-is-a-code-smell/) and remove any remaining EAGER mapping. Extras: 2 more SQL 50 problems (a `LAG` comparison and a running total); a Mermaid ER diagram in the README; a keyset-paginated `GET /api/events?after=` endpoint.
