# 🤖 AI Engineering · Week 17 — Open-Source Models and Local Inference

> 📅 **Mon 15 Feb 2027 → Sun 21 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 16](Week-16.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-17.md) · [Week 18 →](Week-18.md)

**Why this week:** Companies increasingly self-host models for cost, privacy and data residency. Quantization, serving and model selection let you discuss trade-offs beyond 'just call an API'.

## 🗓️ Sessions

### Monday 15 Feb · 45 min — Hugging Face Hub, model cards and licenses
- 📚 **Learn:** Hub basics (models, datasets, Spaces), reading model cards (intended use, training data, limitations, evals), licenses (Apache-2.0, MIT, community licenses with conditions, non-commercial), gated models, safetensors. Read: [Model cards](https://huggingface.co/docs/hub/model-cards) and [Licenses](https://huggingface.co/docs/hub/repositories-licenses).
- 🛠️ **Do:** Shortlist 4 small instruct models (8B or less) and 2 embedding models for DocuMind. For each record parameters, context length, license (commercial use OK?), Hindi support, available quantizations and reported benchmarks. Done when: `08-oss-inference/model_shortlist.md` has the table and a reasoned top-2 pick.

### Tuesday 16 Feb · 45 min — transformers pipelines and chat templates
- 📚 **Learn:** `pipeline()` for text generation and classification, tokenizer + model loading, chat templates, CPU vs GPU placement, generation parameters. Read: [Pipelines tutorial](https://huggingface.co/docs/transformers/pipeline_tutorial) and [Text generation with LLMs](https://huggingface.co/docs/transformers/llm_tutorial).
- 🛠️ **Do:** In a [Google Colab](https://colab.research.google.com/) notebook (free GPU) or locally on CPU with a tiny model, run a chat-templated `pipeline('text-generation')` and a zero-shot classifier on 10 job titles. Measure tokens per second on CPU vs GPU. Done when: the notebook is committed with timings and a note on why chat templates matter.

### Thursday 18 Feb · 45 min — Ollama, quantization, GGUF and 4/8-bit trade-offs
- 📚 **Learn:** Quantization trades precision for memory and speed (FP16 -> 8-bit -> 4-bit); GGUF is the llama.cpp/Ollama format; Q4_K_M is a common default; rough RAM rule: about 0.6 GB per billion parameters at 4-bit plus KV cache; always re-check quality. Read: [Quantization overview](https://huggingface.co/docs/transformers/main/en/quantization/overview), [GGUF on the Hub](https://huggingface.co/docs/hub/gguf), [Ollama library](https://ollama.com/library).
- 🛠️ **Do:** Pull two sizes or quantizations of one model family in Ollama (e.g., 1B vs 4B). With a fixed prompt, record RAM use, load time, time-to-first-token and tokens/second using the timing fields in Ollama's API response. Done when: a results table exists and you pick a default model for your laptop.

### Friday 19 Feb · 45 min — Serving: vLLM, KV cache, continuous batching, model choice
- 📚 **Learn:** Prefill vs decode, KV-cache memory, continuous batching, PagedAttention, throughput vs latency; choose models by your own task evals first, then leaderboards (LMArena, Artificial Analysis), license, price per 1M tokens and latency. Read: [vLLM and PagedAttention](https://blog.vllm.ai/2023/06/20/vllm.html), [Continuous batching](https://www.anyscale.com/blog/continuous-batching-llm-inference), [KV caching explained](https://huggingface.co/blog/not-lain/kv-caching).
- 🛠️ **Do:** Write `serving_notes.md`: explain prefill vs decode, the KV-cache size formula (2 x layers x kv_heads x head_dim x tokens x bytes) and why continuous batching raises throughput; estimate KV memory for an 8B model at 8k context. List local-vs-API trade-offs for DocuMind. Done when: you can explain PagedAttention in 60 seconds.

### Saturday 20 Feb · 45 min — BUILD: benchmark two local models on your eval set
- 📚 **Learn:** Benchmark methodology: identical prompts and retrieval, warm-up runs, median and p95 latency, tokens/second, quality on your golden set, memory; compare against a free API baseline. Public speed/price context: [Artificial Analysis](https://artificialanalysis.ai/).
- 🛠️ **Do:** Run DocuMind's 30-item golden set with 2 local Ollama models and 1 API model through your `llmkit` switch. Record accuracy/faithfulness, median and p95 latency, tokens/second, RAM and estimated cost. Done when: `08-oss-inference/BENCHMARK.md` has the table, a chart and a local-vs-API recommendation with reasons.

## 📦 Deliverable (by Saturday night)
`08-oss-inference/`: licensed model shortlist, pipelines notebook, quantization measurements, `serving_notes.md` and `BENCHMARK.md` comparing two local models with an API model on your golden set.

## ✅ Self-check (Sunday test preview)
- What does quantization do, and what are the trade-offs of 4-bit vs 8-bit?
- What is GGUF, and which runtimes use it?
- Explain the KV cache and why long contexts are expensive.
- What are continuous batching and PagedAttention, and why does vLLM use them?
- How do you choose between a local open-weight model and an API model?
- What do you check in a model card and license before commercial use?

## 🚀 Stretch (optional)
Serve a small model with [vLLM](https://docs.vllm.ai/en/latest/) on a Colab/Kaggle GPU and call it through its OpenAI-compatible endpoint with `llmkit`.
