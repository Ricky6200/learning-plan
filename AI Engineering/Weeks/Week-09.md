# 🤖 AI Engineering · Week 09 — Evals: Prove DocuMind Works

> 📅 **Mon 21 Dec 2026 → Sun 27 Dec 2026** · Season 2 — Concurrency Crucible · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 08](Week-08.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-09.md) · [Week 10 →](Week-10.md)

**Why this week:** 'How do you know it works?' is the number-one AI interview follow-up. Teams hire engineers who prove quality with datasets, metrics and traces, not vibes.

## 🗓️ Sessions

### Monday 21 Dec · 45 min — Golden datasets and error analysis
- 📚 **Learn:** Eval-driven development: build a golden set (question, reference answer, relevant chunk IDs) covering easy, hard, unanswerable and multi-hop cases; read outputs before trusting metrics; error analysis into failure categories. Read: [Your AI product needs evals (Hamel Husain)](https://hamel.dev/blog/posts/evals/); skim the [LLM evals FAQ](https://hamel.dev/blog/posts/evals-faq/).
- 🛠️ **Do:** Create `06-documind/evals/golden.jsonl` with 30 items (5+ unanswerable, 5+ multi-hop), each with expected chunk or page IDs. Run v1, read every answer and tag failures (retrieval miss, wrong citation, hallucination, wrong refusal). Done when: the 30 items exist and a failure-category count table is in `evals/README.md`.

### Tuesday 22 Dec · 45 min — Retrieval metrics: recall@k, MRR, nDCG
- 📚 **Learn:** Recall@k (did we fetch the relevant chunks?), precision@k, MRR (rank of the first hit), nDCG (graded relevance with position discount); evaluate retrieval separately from generation. Read: [Evaluation measures in information retrieval](https://en.wikipedia.org/wiki/Evaluation_measures_%28information_retrieval%29) (precision/recall, MRR, nDCG sections).
- 🛠️ **Do:** Write `eval_retrieval.py` computing recall@5, recall@10, MRR and nDCG@10 from the golden set in pure Python, unit-tested against a tiny hand-computed example. Compare v0 (vector only) with v1 (hybrid + re-rank). Done when: tests pass and a v0-vs-v1 metrics table is printed.

### Thursday 24 Dec · 45 min — Generation metrics with RAGAS/DeepEval; judge pitfalls
- 📚 **Learn:** Faithfulness (claims supported by context), response relevancy, context precision/recall; LLM-as-judge pitfalls: position, verbosity and self-preference bias, non-determinism, cost; calibrate judges against human labels. Read: [RAGAS available metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/) and [DeepEval metrics introduction](https://deepeval.com/docs/metrics-introduction).
- 🛠️ **Do:** Run RAGAS (Faithfulness, Response Relevancy, Context Precision) or DeepEval (FaithfulnessMetric, AnswerRelevancyMetric) on 15 golden items with a free-tier judge model. Hand-label the same 15 for faithfulness and compute judge-human agreement. Done when: scores and agreement % are recorded with 2 examples where the judge was wrong.

### Friday 25 Dec · 45 min — Tracing and experiments with Langfuse
- 📚 **Learn:** Traces and spans per request (retrieve, re-rank, generate), tokens, cost and latency per step, attaching scores to traces, datasets and experiments; Langfuse's SDK is OpenTelemetry-based. Read: [Langfuse get started](https://langfuse.com/docs/observability/get-started) and [Langfuse evaluation overview](https://langfuse.com/docs/evaluation/overview); use the free [Hobby plan](https://langfuse.com/pricing) or self-host.
- 🛠️ **Do:** Instrument DocuMind with Langfuse (OpenAI drop-in wrapper or manual spans for retrieve, re-rank and generate). Run the golden set and attach your retrieval metrics as scores. Done when: Langfuse shows 30 traces with per-step latency, tokens and scores, and you identify the slowest step.

### Saturday 26 Dec · 45 min — BOSS BATTLE: DocuMind eval report in 45 minutes
- 📚 **Learn:** Rules: 45 minutes using your golden set and scripts; the report must support a decision: baseline vs improved, metric deltas, cost and latency, 3 annotated failures, next actions. Template: TL;DR, setup, metrics, errors, decision. Rubric /100: correct metrics 30, comparison 20, error analysis 20, cost/latency 15, clarity 15. Reference: [Patterns for building LLM systems](https://eugeneyan.com/writing/llm-patterns/).
- 🛠️ **Do:** Run v0 and v1 on the golden set, auto-generate `EVAL_REPORT.md` tables with a script, add Langfuse screenshots and 3 annotated failures, then pick the default configuration with justification. Done when: rubric score is 80+, the report is committed, and tag `eval-report-w9` is pushed.

## 📦 Deliverable (by Saturday night)
`06-documind/evals/`: 30-item golden set, tested retrieval-metrics script, RAGAS/DeepEval run with judge calibration, Langfuse tracing and `EVAL_REPORT.md` (v0 vs v1).

## ✅ Self-check (Sunday test preview)
- What makes a good golden dataset for a RAG system?
- Define recall@k, MRR and nDCG, and say when you would use each.
- What does faithfulness measure, and how does it differ from answer relevancy?
- Name three biases of LLM-as-judge and how to mitigate them.
- Why evaluate retrieval and generation separately?
- What would you put on an eval dashboard for a RAG product?

## 🚀 Stretch (optional)
Add a correct-refusal-rate metric for unanswerable questions and generate 20 synthetic questions; compare their difficulty with your hand-written set.
