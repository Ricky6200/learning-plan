# 🤖 AI Engineering · Week 12 — Evals: Prove DocuMind Works

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** 'How do you know it works?' is the number-one AI interview follow-up. Teams hire engineers who prove quality with datasets, metrics and traces, not vibes.

## 🗓️ Sessions

### Monday 11 Jan · 45 min — Golden datasets and error analysis
- 📚 **Learn:** Eval-driven development: build a golden set (question, reference answer, relevant chunk IDs) covering easy, hard, unanswerable and multi-hop cases; read outputs before trusting metrics; group failures into categories (error analysis). Read: [Your AI product needs evals (Hamel Husain)](https://hamel.dev/blog/posts/evals/) (about 15 min). Optional: [LLM evals FAQ](https://hamel.dev/blog/posts/evals-faq/).
- 🛠️ **Do:** Create `09-documind/evals/golden.jsonl` with 15 items (3+ unanswerable, 3+ multi-hop), each with expected chunk or page IDs. Run v1, read every answer and tag failures (retrieval miss, wrong citation, hallucination, wrong refusal). Done when: the 15 items exist and a failure-category count table is in `evals/README.md` (grow to 30 items via this week's stretch).

### Tuesday 12 Jan · 45 min — Retrieval metrics: recall@k, MRR, nDCG
- 📚 **Learn:** Recall@k (did we fetch the relevant chunks?), precision@k (the W4 precision idea, per ranked list), MRR (rank of the first hit), nDCG (graded relevance with a position discount); evaluate retrieval separately from generation. Read: [Evaluation measures in information retrieval](https://en.wikipedia.org/wiki/Evaluation_measures_%28information_retrieval%29) (precision/recall, MRR and nDCG sections).
- 🛠️ **Do:** Write `eval_retrieval.py` computing recall@5, recall@10, MRR and nDCG@10 from the golden set in pure Python, unit-tested against a tiny hand-computed example. Compare v0 (vector only) with v1 (hybrid + re-rank). Done when: tests pass and a v0-vs-v1 metrics table is printed.

### Thursday 14 Jan · 45 min — Generation metrics with RAGAS/DeepEval; judge pitfalls
- 📚 **Learn:** Faithfulness (claims supported by context), response relevancy, context precision/recall; LLM-as-judge pitfalls: position, verbosity and self-preference bias, non-determinism, cost; calibrate judges against human labels. Read: [RAGAS available metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/) (Faithfulness and Response Relevancy). Optional: [DeepEval metrics introduction](https://deepeval.com/docs/metrics-introduction).
- 🛠️ **Do:** Run RAGAS (Faithfulness, Response Relevancy) or DeepEval (FaithfulnessMetric) on 10 golden items with a free-tier judge model, pausing between calls to respect rate limits. Hand-label the same 10 for faithfulness and compute judge-human agreement. Done when: scores and agreement % are recorded with 2 examples where the judge was wrong.

### Friday 15 Jan · 45 min — Tracing and experiments with Langfuse
- 📚 **Learn:** Traces and spans per request (retrieve, re-rank, generate), tokens, cost and latency per step, attaching scores to traces, datasets and experiments; Langfuse's SDK is built on OpenTelemetry (you go deeper on OpenTelemetry in W19). Read: [Langfuse get started](https://langfuse.com/docs/observability/get-started); the free Hobby plan is enough. Optional: [Langfuse evaluation overview](https://langfuse.com/docs/evaluation/overview).
- 🛠️ **Do:** Instrument DocuMind with Langfuse (OpenAI drop-in wrapper or manual spans for retrieve, re-rank and generate). Run the golden set and attach your retrieval metrics as scores. Done when: Langfuse shows one trace per golden item with per-step latency, tokens and scores, and you identify the slowest step.

### Saturday 16 Jan · 45 min — BUILD: DocuMind eval report in 45 minutes
- 📚 **Learn:** Timed build: the report must support a decision (baseline vs improved, metric deltas, cost and latency, 3 annotated failures, next actions). Template: TL;DR, setup, metrics, errors, decision. Self-score /100: correct metrics 30, comparison 20, error analysis 20, cost/latency 15, clarity 15. Reference: [Patterns for building LLM systems](https://eugeneyan.com/writing/llm-patterns/) (evals section).
- 🛠️ **Do:** Run v0 and v1 on the golden set, auto-generate `EVAL_REPORT.md` tables with a script, add Langfuse screenshots and 3 annotated failures, then pick the default configuration with a justification. Done when: your self-score is 80+, the report is committed, and tag `eval-report-w12` is pushed.

## 📦 Deliverable (by Saturday night)
`09-documind/evals/`: golden set (15 items in session, 30 with the stretch), tested retrieval-metrics script, RAGAS/DeepEval run with judge calibration, Langfuse tracing and `EVAL_REPORT.md` (v0 vs v1).

## ✅ Self-check (Sunday test preview)
- What makes a good golden dataset for a RAG system?
- Define recall@k, MRR and nDCG, and say when you would use each.
- What does faithfulness measure, and how does it differ from answer relevancy?
- Name three biases of LLM-as-judge and how to mitigate them.
- Why evaluate retrieval and generation separately?
- What would you put on an eval dashboard for a RAG product?

## 🚀 Stretch (optional)
Grow the golden set to 30 items (15 more, including 2+ multi-hop), add a correct-refusal-rate metric for unanswerable questions, and compare 20 synthetic questions with your hand-written ones.
