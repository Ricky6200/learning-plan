# ☁️ Azure Cloud · Week 18 — Cosmos DB vectors, change feed, PostgreSQL basics

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** Vector search inside your operational database and reacting to data changes are core AI-backend patterns; Azure Database for PostgreSQL is AI-200's other data pillar and the database Java teams most often migrate to.

## 🗓️ Sessions

### Tuesday 23 Feb · 45 min — Cosmos DB vector search: embeddings and VectorDistance
- 📚 **Learn:** Vector embedding policy (path, data type, dimensions, distance function), vector index types (flat, quantizedFlat, diskANN), `VectorDistance()` with `TOP N`, combining similarity with metadata filters. Read [Index and query vectors in Python](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-python-vector-index-query). Optional: [Vector search in Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/vector-search).
- 🛠️ **Do:** In your W17 account (vector search already enabled), create a container whose vector embedding policy matches the AI track's model - Ollama `nomic-embed-text` (768 dimensions) or `all-MiniLM-L6-v2` via sentence-transformers (384) - with cosine distance and a quantizedFlat or diskANN index. Download models on the personal laptop or in a Codespace, not on the company network. Embed and store 30 event descriptions, then run `SELECT TOP 5 ... ORDER BY VectorDistance(c.embedding, @q)` with and without a city filter. Done when: top-5 results for 3 queries plus RU per query are logged in `w18/`.

### Wednesday 24 Feb · 45 min — Change feed: detect and handle new or updated items
- 📚 **Learn:** Change feed modes (latest version vs all versions and deletes), the change feed processor model (monitored container, lease container, compute instance, delegate), the Python pull model with continuation tokens, and the Functions Cosmos DB trigger. Read [Change feed in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/change-feed). Optional: [Change feed processor](https://learn.microsoft.com/en-us/azure/cosmos-db/change-feed-processor).
- 🛠️ **Do:** Write `py/change_feed.py`: read the `events` container's change feed (`query_items_change_feed`), save the continuation token to a file as your checkpoint, and recompute the embedding of every new or updated event. Insert 3 and update 2 items, run twice and prove nothing is processed twice. Note when you'd use a Functions trigger instead. Done when: idempotent-processing evidence and the note are committed.

### Friday 26 Feb · 45 min — PostgreSQL Flexible Server: connect, schema design, indexes
- 📚 **Learn:** Compute tiers (Burstable, General Purpose, Memory Optimized), Entra or password auth, firewall vs private access, psycopg 3 connections, schema and data types (uuid, jsonb, timestamptz), B-tree and GIN indexes, EXPLAIN ANALYZE. Read [Connect with Python](https://learn.microsoft.com/en-us/azure/postgresql/connectivity/connect-python). Optional: [Create a Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/configure-maintain/quickstart-create-server).
- 🛠️ **Do:** Create a Burstable B1ms server (12-month free hours; allow only your IP) and connect with psql and with `py/pg_basics.py` (psycopg 3). Create `events(id uuid, city text, starts_at timestamptz, meta jsonb)`, load 10k rows, then compare EXPLAIN ANALYZE for `city = 'Pune'` before and after a B-tree index, and for a jsonb filter with a GIN index. Stop the server when done. Done when: plans and timings are in `w18/pg.md`.

### Saturday 27 Feb · 60 min — LAB: PostgreSQL agent-tool backend + connection pooling
- 📚 **Learn:** The exercise in Learn's [Build and query with Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/training/modules/build-query-azure-database-postgresql/) ('Build an agent tool backend'). Optional: [PgBouncer in Flexible Server](https://learn.microsoft.com/en-us/azure/postgresql/connectivity/concepts-pgbouncer) - the built-in PgBouncer listens on port 6432 but isn't supported on the Burstable tier.
- 🛠️ **Do:** Complete the 'Build an agent tool backend on Azure Database for PostgreSQL' exercise (~30 min). Then add client-side pooling with `psycopg_pool.ConnectionPool` to your Friday script, fire 200 concurrent queries with and without the pool, and record connection counts and latency. Write when you'd switch to built-in PgBouncer (General Purpose tier, port 6432). Done when: exercise done, pooling comparison committed and your server stopped (W19 reuses it).

## 📦 Deliverable (by Saturday night)
`w18/` vector query results, idempotent `change_feed.py`, PostgreSQL EXPLAIN comparisons, the agent-tool backend exercise and the connection-pooling comparison; the B1ms server stopped for W19.

## ✅ Self-check (Sunday test preview)
- Which Cosmos DB vector index type would you choose for a million vectors, and what is the trade-off vs flat?
- How do you combine vector similarity with a metadata filter in a single Cosmos DB query?
- How does a change feed consumer avoid reprocessing items after a restart?
- Burstable vs General Purpose PostgreSQL: which capabilities, such as built-in PgBouncer, do you lose on Burstable?
- When would you choose a GIN index over a B-tree index?
- Why does connection pooling matter for Python or Spring Boot apps that talk to PostgreSQL?

## 🚀 Stretch (optional)
Do the exercises in the official AI-200 module [Implement vector search on Cosmos DB](https://learn.microsoft.com/en-us/training/modules/implement-vector-search-azure-cosmos-db/), try Cosmos DB [hybrid search](https://learn.microsoft.com/en-us/azure/cosmos-db/gen-ai/hybrid-search) (full-text + vector, RRF), or watch Savill's [Azure PostgreSQL Flexible Deep Dive](https://www.youtube.com/watch?v=aP-kn76-emI) and enable Microsoft Entra authentication on your server.
