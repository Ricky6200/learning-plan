# 🤖 AI Engineering · Week 11 — RAG II: Hybrid Search, Re-ranking, Query Tricks

> 📅 **Mon 04 Jan 2027 → Sun 10 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 10](Week-10.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-11.md) · [Week 12 →](Week-12.md)

**Why this week:** Naive RAG fails on keywords, acronyms and vague questions. Hybrid retrieval and re-ranking are standard interview topics and the biggest quality levers in production RAG.

## 🗓️ Sessions

### Monday 04 Jan · 45 min — Hybrid search: BM25 + vectors with RRF
- 📚 **Learn:** Lexical BM25 catches exact terms, IDs and error codes; dense vectors catch meaning; Reciprocal Rank Fusion merges rankings (score = sum of 1/(k + rank)). Read: [Hybrid search ranking with RRF (Azure AI Search)](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking). Optional: [rank_bm25](https://github.com/dorianbrown/rank_bm25).
- 🛠️ **Do:** Add BM25 over DocuMind chunks (rank_bm25 or Postgres full-text `tsvector`) and implement RRF with k = 60 to merge BM25 top-20 and vector top-20. Test 5 keyword-heavy questions (acronyms, error codes, section numbers). Done when: hybrid beats vector-only on at least 3 of the 5.

### Tuesday 05 Jan · 45 min — Re-ranking with cross-encoders
- 📚 **Learn:** Bi-encoders embed query and passage separately (fast); cross-encoders score the pair together (slower, more accurate); retrieve 30, re-rank, keep 5; mind the latency budget. Read: [Retrieve & Re-Rank](https://sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html). Optional: [CrossEncoder usage](https://sbert.net/docs/cross_encoder/usage/usage.html).
- 🛠️ **Do:** Add a re-rank stage with `CrossEncoder('cross-encoder/ms-marco-MiniLM-L6-v2')` over hybrid top-30. Measure added CPU latency per query and compare top-5 hits on 10 questions. Done when: a before/after table (hits@5 and milliseconds) exists and you decide whether re-ranking is worth it.

### Thursday 07 Jan · 45 min — Query rewriting and multi-query
- 📚 **Learn:** Rewrite chatty follow-ups into standalone search queries; multi-query (N paraphrases, union the results); HyDE (embed a hypothetical answer) and step-back questions are variants of the same idea; each adds LLM calls and latency. Watch: [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) videos 5-6 (query translation, about 12 min). Optional: [HyDE paper](https://arxiv.org/abs/2212.10496) (abstract).
- 🛠️ **Do:** Implement `rewrite()` (conversation to standalone query) and `multi_query(n=3)`. Run 10 vague questions through each and count hits@5, tracking extra tokens and latency. Done when: a comparison table shows which technique helps your corpus and at what cost.

### Friday 08 Jan · 45 min — Small-to-big retrieval: parent-child chunks
- 📚 **Learn:** Match small, precise chunks but give the model their larger parent section. Related ideas: Anthropic's contextual retrieval prepends chunk-specific context before embedding; GraphRAG targets global questions; long-context models compete with RAG on cost, latency, freshness and access control. Read: [Contextual Retrieval (Anthropic)](https://www.anthropic.com/research/contextual-retrieval) (introduction and results, about 10 min). Optional: [GraphRAG overview](https://microsoft.github.io/graphrag/).
- 🛠️ **Do:** Implement parent-child retrieval (index ~300-character children, return their ~1,500-character parents). Compare hits@5 on 10 questions against the W10 baseline. Done when: results are recorded in `experiments.md` with one example where the parent context fixed a wrong answer.

### Saturday 09 Jan · 45 min — BUILD: DocuMind v1 with hybrid search and re-ranking
- 📚 **Learn:** Make retrieval configurable and observable: pipeline config (retriever: vector or hybrid, rerank on/off, k) and logging of retrieved IDs and scores per request, which W12 evals need. Optional course: [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/courses/building-evaluating-advanced-rag).
- 🛠️ **Do:** Ship DocuMind v1: hybrid retrieval with RRF, optional cross-encoder re-rank, query rewrite for follow-ups, parent-child context, metadata filters (doc, year) and a debug flag returning retrieved chunks with scores. Done when: v1 beats v0 on hits@5 across 20 test questions, tag `v1.0-documind` is pushed, and the README has the pipeline diagram.

## 📦 Deliverable (by Saturday night)
`09-documind/` v1.0 with BM25 + vector hybrid search (RRF), cross-encoder re-ranking, query rewriting, parent-child retrieval, filters and `experiments.md` with measured gains.

## ✅ Self-check (Sunday test preview)
- Why does hybrid search beat pure vector search on IDs and acronyms?
- Explain Reciprocal Rank Fusion with a two-list example.
- Bi-encoder vs cross-encoder: speed/quality trade-off and where each sits in the pipeline?
- What is HyDE, and when can it hurt?
- What is contextual retrieval and why does it improve recall?
- When would you prefer a long-context model over RAG, and vice versa?

## 🚀 Stretch (optional)
Generate contextual prefixes for 30 chunks with a cheap model (cache them) and measure hits@5 against parent-child, or implement HyDE or corrective RAG from [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques).
