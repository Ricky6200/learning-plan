# 🤖 AI Engineering · Week 08 — RAG II: Hybrid Search, Re-ranking, Query Tricks

> 📅 **Mon 14 Dec 2026 → Sun 20 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 07](Week-07.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-08.md) · [Week 09 →](Week-09.md)

**Why this week:** Naive RAG fails on keywords, acronyms and vague questions. Hybrid retrieval and re-ranking are standard interview topics and the biggest quality levers in production RAG.

## 🗓️ Sessions

### Monday 14 Dec · 45 min — Hybrid search: BM25 + vectors with RRF
- 📚 **Learn:** Lexical BM25 catches exact terms, IDs and error codes; dense vectors catch meaning; Reciprocal Rank Fusion merges rankings (score = sum of 1/(k + rank)). Read: [Hybrid search ranking with RRF (Azure AI Search)](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking) and [rank_bm25](https://github.com/dorianbrown/rank_bm25); optional [Qdrant hybrid queries](https://qdrant.tech/documentation/concepts/hybrid-queries/).
- 🛠️ **Do:** Add BM25 over DocuMind chunks (rank_bm25 or Postgres full-text `tsvector`) and implement RRF with k = 60 to merge BM25 top-20 and vector top-20. Test 5 keyword-heavy questions (acronyms, error codes, section numbers). Done when: hybrid beats vector-only on at least 3 of the 5.

### Tuesday 15 Dec · 45 min — Re-ranking with cross-encoders
- 📚 **Learn:** Bi-encoders embed query and passage separately (fast); cross-encoders score the pair together (slower, more accurate); retrieve 30, re-rank, keep 5; mind the latency budget. Read: [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html), [CrossEncoder usage](https://sbert.net/docs/cross_encoder/usage/usage.html); model: [ms-marco-MiniLM-L6-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L6-v2).
- 🛠️ **Do:** Add a re-rank stage with `CrossEncoder('cross-encoder/ms-marco-MiniLM-L6-v2')` over hybrid top-30. Measure added CPU latency per query and compare top-5 hits on 10 questions. Done when: a before/after table (hits@5 and milliseconds) exists and you decide whether re-ranking is worth it.

### Thursday 17 Dec · 45 min — Query rewriting, multi-query and HyDE
- 📚 **Learn:** Rewrite chatty follow-ups into standalone search queries; multi-query (N paraphrases, union the results); HyDE (embed a hypothetical answer); step-back questions; each adds LLM calls and latency. Read the [HyDE paper](https://arxiv.org/abs/2212.10496) abstract; watch query-translation videos 5-9 of [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x).
- 🛠️ **Do:** Implement `rewrite()` (conversation to standalone query), `multi_query(n=3)` and `hyde()`. Run 10 vague questions through each and count hits@5, tracking extra tokens and latency. Done when: a comparison table shows which technique helps your corpus and at what cost.

### Friday 18 Dec · 45 min — Parent-child, contextual retrieval, GraphRAG, long context
- 📚 **Learn:** Match small chunks but return parent sections; Anthropic's contextual retrieval (prepend chunk-specific context before embedding and BM25); metadata filters; GraphRAG for global questions; long-context models vs RAG (cost, latency, freshness, access control). Read: [Contextual Retrieval](https://www.anthropic.com/research/contextual-retrieval) and the [GraphRAG overview](https://microsoft.github.io/graphrag/).
- 🛠️ **Do:** Implement parent-child retrieval (index ~300-character children, return their ~1,500-character parents). Generate contextual prefixes for 30 chunks with a cheap model (cache results). Compare hits@5 on 10 questions against the W7 baseline. Done when: results and cost per 1,000 chunks are recorded in `experiments.md`.

### Saturday 19 Dec · 45 min — BUILD: DocuMind v1 with hybrid search and re-ranking
- 📚 **Learn:** Make retrieval configurable and observable: pipeline config (retriever: vector or hybrid, rerank on/off, k) and logging of retrieved IDs and scores per request, which W9 evals need. Free course: [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag).
- 🛠️ **Do:** Ship DocuMind v1: hybrid retrieval with RRF, optional cross-encoder re-rank, query rewrite for follow-ups, parent-child context, metadata filters (doc, year) and a debug flag returning retrieved chunks with scores. Done when: v1 beats v0 on hits@5 across 20 test questions, tag `v1.0-documind` is pushed, and the README has the pipeline diagram.

## 📦 Deliverable (by Saturday night)
`06-documind/` v1.0 with BM25 + vector hybrid search (RRF), cross-encoder re-ranking, query rewriting, parent-child retrieval, filters and `experiments.md` with measured gains.

## ✅ Self-check (Sunday test preview)
- Why does hybrid search beat pure vector search on IDs and acronyms?
- Explain Reciprocal Rank Fusion with a two-list example.
- Bi-encoder vs cross-encoder: speed/quality trade-off and where each sits in the pipeline?
- What is HyDE, and when can it hurt?
- What is contextual retrieval and why does it improve recall?
- When would you prefer a long-context model over RAG, and vice versa?

## 🚀 Stretch (optional)
Implement one more technique from [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) (e.g., corrective RAG or RAPTOR-style summaries) and measure it.
