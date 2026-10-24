# ☁️ Azure Cloud · Week 17 — Cosmos DB for NoSQL I: model, RUs, SDK

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Data services are AI-200's largest domain (30-35%). Partition keys, request-unit cost and consistency levels are exam favourites and classic system-design interview topics for any high-scale booking or chat system.

## 🗓️ Sessions

### Tuesday 16 Feb · 45 min — Resource model, partition keys and request units
- 📚 **Learn:** Account > database > container > item; logical vs physical partitions; choosing a partition key (high cardinality, even writes, query patterns) and hierarchical keys; request units; provisioned, autoscale and serverless; free tier (1000 RU/s + 25 GB, one account per subscription). Use [Partitioning](https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning), [Request units](https://learn.microsoft.com/en-us/azure/cosmos-db/request-units) and [Free tier](https://learn.microsoft.com/en-us/azure/cosmos-db/free-tier).
- 🛠️ **Do:** Design containers for TicketVerse AI features in `w17/cosmos-model.md`: `events`, `bookings` and `chat-history`. For each pick a partition key, list the 3 main queries and mark whether each is single-partition. Look up the RU cost of a 1 KB point read and compare it with a cross-partition query. Note hot-partition risks. Done when: the model with justified keys is committed.

### Wednesday 17 Feb · 45 min — Python SDK: keyless connect, CRUD and parameterized queries
- 📚 **Learn:** `azure-cosmos` client hierarchy (CosmosClient > database > container), keyless auth with DefaultAzureCredential + Cosmos data-plane RBAC, upsert/read_item/query_items, parameterized SQL, reading the request charge. Use the [Python quickstart](https://learn.microsoft.com/en-us/azure/cosmos-db/quickstart-python), [Connect with RBAC and Entra ID](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-connect-role-based-access-control) and Learn's [Build queries for Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/training/modules/build-query-azure-cosmos-db/).
- 🛠️ **Do:** Create a free-tier (or serverless) Cosmos DB for NoSQL account and grant yourself the built-in data contributor role. In `py/cosmos_crud.py`: create a database and container `events` (partition key `/city`), upsert 50 items, point-read one, run a parameterized query, and print the request charge for each call. Done when: the script runs keyless and RU per operation is logged in `w17/`.

### Friday 19 Feb · 45 min — Indexing policies and consistency levels to cut RUs
- 📚 **Learn:** Default index-everything policy, included/excluded paths, composite indexes for ORDER BY, vector indexes; the five consistency levels (strong, bounded staleness, session, consistent prefix, eventual) and their latency/RU trade-offs. Use [Indexing policies](https://learn.microsoft.com/en-us/azure/cosmos-db/index-policy), [Consistency levels](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) and [Optimize request cost](https://learn.microsoft.com/en-us/azure/cosmos-db/optimize-cost-reads-writes).
- 🛠️ **Do:** Insert 200 items with the default policy and log the average write RU; switch to a policy that excludes `/*` and includes only `/city/?` and `/date/?`, re-insert and compare. Add a composite index for `ORDER BY c.city, c.date` and compare that query's RU before and after. Write which consistency level you'd pick for bookings vs an event catalog, and why. Done when: a before/after RU table and the consistency note are in `w17/`.

### Saturday 20 Feb · 60 min — LAB: Cosmos DB RAG document store (official AI-200 exercise)
- 📚 **Learn:** The exercise in Learn's [Build queries for Cosmos DB for NoSQL](https://learn.microsoft.com/en-us/training/modules/build-query-azure-cosmos-db/) ('Build a RAG document store') and the indexing units of [Optimize query performance for Cosmos DB](https://learn.microsoft.com/en-us/training/modules/optimize-query-performance-azure-cosmos-db/). Optional video: [The fundamentals of using Python with Cosmos DB](https://www.youtube.com/watch?v=opx_XNHmxEo).
- 🛠️ **Do:** Complete the 'Build a RAG document store on Azure Cosmos DB for NoSQL' exercise (~30 min) in your subscription. Extend it: add a `source` metadata field, query chunks filtered by source, and capture each query's RU charge. Delete the resource group at the end. Done when: the exercise is finished, your extension is committed under `py/` and the RG is deleted.

## 📦 Deliverable (by Saturday night)
`w17/cosmos-model.md`, keyless `py/cosmos_crud.py`, RU before/after table, consistency note, and the RAG document-store exercise with your extension.

## ✅ Self-check (Sunday test preview)
- What makes a good partition key for a bookings container, and what is a hot partition?
- Why is a point read the cheapest Cosmos DB operation, and roughly what does a 1 KB point read cost?
- How does excluding paths from the indexing policy change write RU and query behaviour?
- Session vs strong consistency: what does each guarantee, and what does it cost?
- Provisioned vs autoscale vs serverless throughput: which fits a spiky dev workload?
- How do you connect to Cosmos DB without keys, and which built-in role grants data read/write?

## 🚀 Stretch (optional)
Watch Savill's [Cosmos DB Optimization](https://www.youtube.com/watch?v=RbH5F_3w47E) and try hierarchical partition keys (`/tenantId`, `/userId`) on a new container.
