# 🤖 AI Engineering · Week 20 — Open-Source Models and the Local Inference Boss

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Companies increasingly self-host models for cost, privacy and data residency. Quantization, serving and model selection let you discuss trade-offs beyond 'just call an API'. The season ends with a timed, measured model comparison, and this week you start applying for jobs.

## 🗓️ Sessions

### Monday 08 Mar · 45 min — Hugging Face Hub, model cards and licenses
- 📚 **Learn:** Hub basics (models, datasets, Spaces), reading model cards (intended use, training data, limitations, evals), licenses (Apache-2.0, MIT, community licenses with conditions, non-commercial), gated models, safetensors. Read: [Model cards](https://huggingface.co/docs/hub/model-cards). Optional: [Licenses](https://huggingface.co/docs/hub/repositories-licenses).
- 🛠️ **Do:** Shortlist 4 small instruct models (8B or less) and 2 embedding models for DocuMind. For each record parameters, context length, license (commercial use OK?), Hindi support, available quantizations and reported benchmarks. Done when: `11-oss-inference/model_shortlist.md` has the table and a reasoned top-2 pick.

### Tuesday 09 Mar · 45 min — transformers pipelines and chat templates
- 📚 **Learn:** `pipeline()` for text generation and classification, tokenizer + model loading, chat templates (each model expects its own special tokens), CPU vs GPU placement, generation parameters. Read: [Text generation with LLMs](https://huggingface.co/docs/transformers/llm_tutorial). Optional: [Pipelines tutorial](https://huggingface.co/docs/transformers/pipeline_tutorial).
- 🛠️ **Do:** In a [Google Colab](https://colab.research.google.com/) notebook (free GPU) run a chat-templated `pipeline('text-generation')` with a small instruct model and a zero-shot classifier on 10 job titles. Measure tokens per second on CPU vs GPU. Done when: the notebook is committed with timings and a note on why chat templates matter.

### Thursday 11 Mar · 45 min — Ollama, quantization, GGUF and 4/8-bit trade-offs
- 📚 **Learn:** Quantization trades precision for memory and speed (FP16 -> 8-bit -> 4-bit); GGUF is the llama.cpp/Ollama format; Q4_K_M is a common default; rough RAM rule: about 0.6 GB per billion parameters at 4-bit plus the KV cache; always re-check quality. Read: [GGUF on the Hub](https://huggingface.co/docs/hub/gguf). Optional: [Quantization overview](https://huggingface.co/docs/transformers/main/en/quantization/overview).
- 🛠️ **Do:** Pull two sizes of one model family in Ollama (e.g., 1B vs 3B). With a fixed prompt, record RAM use, load time, time-to-first-token and tokens/second from the timing fields of Ollama's native `/api/generate` response. Done when: a results table exists and you pick a default local model for your codespace.

### Friday 12 Mar · 45 min — Serving: vLLM, KV cache, continuous batching, model choice
- 📚 **Learn:** Prefill vs decode, KV-cache memory, continuous batching, PagedAttention, throughput vs latency; choose models by your own task evals first, then leaderboards (LMArena, Artificial Analysis), license, price per 1M tokens and latency. Read: [vLLM and PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html). Optional: [KV caching explained](https://huggingface.co/blog/not-lain/kv-caching).
- 🛠️ **Do:** Write `serving_notes.md`: prefill vs decode, the KV-cache size formula (2 x layers x kv_heads x head_dim x tokens x bytes) with an estimate for an 8B model at 8k context, and local-vs-API trade-offs for DocuMind. Then commit a `bench.py` skeleton that runs one golden question through a given `llmkit` provider and prints latency. Done when: the notes are committed and `bench.py` works for one model.

### Saturday 13 Mar · 45 min — BOSS BATTLE: local vs API model comparison in 45 minutes
- 📚 **Learn:** Rules: 45-minute timer, start from Friday's `bench.py`, docs allowed, no AI code generation. Method: identical prompts and retrieval, one warm-up run, 10 golden questions, median and p95 latency, tokens/second, quality, RAM. Rubric /100: fair method 25, complete table 25, quality scoring 20, chart 10, reasoned recommendation 20. Context: [Artificial Analysis](https://artificialanalysis.ai/).
- 🛠️ **Do:** Run 10 DocuMind golden questions through 2 local Ollama models (1B and 3B in the codespace, or Ollama on a Colab T4) and 1 API model via `llmkit`. Record correctness (judge or hand labels), median and p95 latency, tokens/second, RAM and estimated cost. Done when: the rubric score is 80+, `11-oss-inference/BENCHMARK.md` has the table, a chart and a recommendation, and tag `v1.0-local-bench` is pushed.

## 📦 Deliverable (by Saturday night)
`11-oss-inference/`: licensed model shortlist, pipelines notebook, quantization measurements, `serving_notes.md` and a boss-battle `BENCHMARK.md` comparing two local models with an API model on 10 golden questions.

## ✅ Self-check (Sunday test preview)
- What does quantization do, and what are the trade-offs of 4-bit vs 8-bit?
- What is GGUF, and which runtimes use it?
- Explain the KV cache and why long contexts are expensive.
- What are continuous batching and PagedAttention, and why does vLLM use them?
- How do you choose between a local open-weight model and an API model?
- What do you check in a model card and license before commercial use?

## 🚀 Stretch (optional)
Serve a small model with [vLLM](https://docs.vllm.ai/en/latest/) on a Colab or Kaggle GPU and call it through its OpenAI-compatible endpoint with `llmkit`, or extend the benchmark to all golden questions.
