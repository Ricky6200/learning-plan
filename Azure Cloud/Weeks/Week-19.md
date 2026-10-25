# ☁️ Azure Cloud · Week 19 — pgvector, Managed Redis and a RAG data layer

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** pgvector tuning, RAG retrieval with metadata filters and Redis caching are what make AI features fast and affordable in production - and they are heavily weighted in AI-200. Saturday's lab assembles them into a real RAG data layer on Azure.

## 🗓️ Sessions

### Tuesday 02 Mar · 45 min — pgvector on Azure: enable, store, HNSW vs IVFFlat
- 📚 **Learn:** Allowlisting `vector` in `azure.extensions`, `CREATE EXTENSION vector`, vector columns, distance operators (<->, <=>, <#>), HNSW (m, ef_construction, ef_search) vs IVFFlat (lists, probes), DiskANN awareness. Read [Vector search with pgvector](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-use-pgvector). Optional: [Optimize pgvector performance](https://learn.microsoft.com/en-us/azure/postgresql/extensions/how-to-optimize-performance-pgvector).
- 🛠️ **Do:** Start your W18 server, allowlist `vector` and create the extension; load 2,000 chunks with embeddings (reuse DocuMind or SemanticSearch data from the AI track; `vector(768)` for nomic-embed-text, `vector(384)` for MiniLM). Time a top-5 cosine query with no index, with HNSW and with IVFFlat (lists about rows/1000), then try two `hnsw.ef_search` values and compare recall against the exact result. Done when: a 5-row timing/recall table is in `w19/pgvector.md`.

### Wednesday 03 Mar · 45 min — RAG retrieval with metadata filters, sizing and connections
- 📚 **Learn:** Retrieval that combines vector similarity with SQL metadata filters (tenant, date, source), how filters interact with approximate indexes, memory for index builds (`maintenance_work_mem`), compute/memory/storage sizing for vector workloads, connection optimization. Read Learn's [Optimize vector search in Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/training/modules/optimize-vector-search-azure-database-postgresql/). Optional: Pamela Fox's [pgvector on Azure](https://www.youtube.com/watch?v=sCX_sB2dQHY).
- 🛠️ **Do:** Write `py/retrieve.py` with `retrieve(question, source=None, after=None, k=5)`: embed the question and run one parameterized SQL query combining `ORDER BY embedding <=> %s` with WHERE filters; add a B-tree index on the filter column and compare plans. Then write a sizing note: index size vs RAM, and when to move from B1ms to General Purpose. Stop the server. Done when: the function returns filtered results and the note is in `w19/`.

### Friday 05 Mar · 45 min — Azure Managed Redis: caching, expiration, invalidation
- 📚 **Learn:** Tiers (Memory Optimized, Balanced, Compute Optimized, Flash Optimized), Entra auth, redis-py, cache-aside with TTL, invalidation on write, key design. Vector indexing uses the RediSearch module, which you can only add at creation and which needs the Enterprise clustering policy and the NoEviction eviction policy. Read [What is Azure Managed Redis?](https://learn.microsoft.com/en-us/azure/redis/overview). Optional: Learn's [Implement vector storage in Azure Managed Redis](https://learn.microsoft.com/en-us/training/modules/implement-vector-storage-azure-managed-redis/).
- 🛠️ **Do:** Create the smallest Balanced SKU with RediSearch (Enterprise clustering, NoEviction) and note creation time and hourly price. With redis-py: cache `retrieve()` results under `rag:<hash>` with a 10-minute TTL, measure hit vs miss latency, and invalidate the key when a source document changes. Delete the cache today - Saturday re-creates it at minute 0. Done when: hit/miss timings and the invalidation test are in `w19/redis.md` and the cache is deleted.

### Saturday 06 Mar · 60 min — LAB: RAG data layer - pgvector, Redis cache and vector index
- 📚 **Learn:** Assemble the week: vector search with metadata filters, pooling, cache-aside and a RediSearch vector index. Use your `py/retrieve.py` and the [Azure RAG design guide](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide) for review. Optional: the [AI-200 practice assessment](https://aiskillsnavigator.microsoft.com/credentials/cert-c8bca807654f6efc31cadb95ede6b0729abd1efb29cbb608f768b4de78edf92b) on AI Skills Navigator (sign-in required).
- 🛠️ **Do:** Minute 0: create Azure Managed Redis (smallest Balanced, RediSearch) and start your PostgreSQL server. Then expose `ask(question, source)` that serves repeats from the cache with a TTL and logs DB vs cache latency; prove invalidation. Build a small RediSearch vector index (`FT.CREATE`, DIM matching your model) over 100 embeddings and run a KNN query. Finish with 10 AI-200 practice questions on data services, logging misses. Delete the cache and your PostgreSQL server (W25 uses a local pgvector container). Done when: the demo log, KNN output and score are committed.

## 📦 Deliverable (by Saturday night)
`w19/` pgvector timing/recall table, `retrieve.py` with filters, Redis cache-aside + invalidation evidence, the RAG data-layer demo log with a RediSearch KNN query, and the practice-question score.

## ✅ Self-check (Sunday test preview)
- HNSW vs IVFFlat: which builds slower, which needs data before building, and which parameters trade recall for speed?
- Why must you allowlist an extension on Azure Database for PostgreSQL before CREATE EXTENSION?
- How can metadata filters hurt recall with an approximate vector index, and how do you mitigate it?
- What is cache-aside, and how do you invalidate a cached RAG answer when a source document changes?
- Which Azure Managed Redis tier fits a small dev cache vs a large vector index, and which clustering and eviction policies does RediSearch need?
- How would you size memory for a vector workload in PostgreSQL?

## 🚀 Stretch (optional)
Do the exercises in the official AI-200 module [Implement vector search with Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/training/modules/implement-vector-search-azure-database-postgresql/), attempt the hosted Applied Skills lab [Build AI-powered solutions by using Azure Database for PostgreSQL](https://learn.microsoft.com/en-us/credentials/applied-skills/build-ai-powered-solutions-by-using-microsoft-azure-database-for-postgresql/) or watch Savill's [Azure Managed Redis Deep Dive](https://www.youtube.com/watch?v=jIpJplSaFQM).
