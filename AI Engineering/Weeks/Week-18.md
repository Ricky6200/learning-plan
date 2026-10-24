# 🤖 AI Engineering · Week 18 — Fine-Tuning with LoRA: FineTune Lab

> 📅 **Mon 22 Feb 2027 → Sun 28 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 17](Week-17.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-18.md) · [Week 19 →](Week-19.md)

**Why this week:** Interviewers expect you to know when fine-tuning beats prompting or RAG and how LoRA/QLoRA work. A measured before/after experiment is strong resume evidence.

## 🗓️ Sessions

### Monday 22 Feb · 45 min — Fine-tune vs prompt vs RAG: the decision
- 📚 **Learn:** Prompting changes behaviour fast, RAG adds knowledge, fine-tuning fixes format/style or makes small models cheaper and faster on narrow tasks; needs data, evals and maintenance; SFT vs preference tuning (DPO) vs distillation (teacher -> student). Read: [Unsloth fine-tuning guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide) (what and when) and [Post-training of LLMs](https://www.deeplearning.ai/courses/post-training-of-llms) (overview).
- 🛠️ **Do:** Define the FineTune Lab task: JD text -> compact JSON (title, seniority, skills, years_min, remote). Write a one-page `09-finetune-lab/DECISION.md` comparing prompting, RAG and fine-tuning for it, with success metrics (JSON validity, field F1, latency, cost) and a hypothesis. Done when: the memo states measurable targets.

### Tuesday 23 Feb · 45 min — Dataset preparation and distillation from a teacher model
- 📚 **Learn:** Chat-format training data, train/validation/test splits, quality over quantity (300-1,000 clean examples), de-duplication and leakage checks, synthetic labels from a stronger teacher model plus human review, data licensing. Read: [TRL SFTTrainer](https://huggingface.co/docs/trl/sft_trainer) (dataset formats) and the [LLM course: supervised fine-tuning](https://huggingface.co/learn/llm-course/chapter11/1).
- 🛠️ **Do:** Collect 300-400 JDs (your W5 set plus pages from the free Arbeitnow jobs API), label them with a strong free model in a background script (several JDs per call to respect rate limits), hand-review 30 and fix systematic errors, then split 80/10/10 into chat-format JSONL. Done when: `DATA.md` documents sources, cleaning, split sizes and review findings.

### Thursday 25 Feb · 45 min — LoRA, QLoRA and PEFT on a free Colab GPU
- 📚 **Learn:** Full fine-tuning vs PEFT; LoRA adds low-rank adapters (rank r, alpha, target modules) to frozen weights; QLoRA = 4-bit base model + LoRA; memory math; merging adapters; free GPUs on Colab or Kaggle. Read: [PEFT LoRA guide](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora), [LoRA paper](https://arxiv.org/abs/2106.09685) and [QLoRA paper](https://arxiv.org/abs/2305.14314) abstracts.
- 🛠️ **Do:** Open an [Unsloth notebook](https://docs.unsloth.ai/get-started/unsloth-notebooks) for a small (about 1-4B) instruct model on a Colab T4 and run it unchanged on its sample data for a few steps. Record r, alpha, target modules, VRAM used and seconds per step. Done when: the training loop runs and your notes explain each LoRA setting.

### Friday 26 Feb · 45 min — Train on your data and evaluate against prompting
- 📚 **Learn:** Training hygiene: 1-3 epochs, watch train vs validation loss, learning rate, overfitting signs; evaluate on the held-out test split with the same metrics as the baseline; save adapters; optional GGUF export for Ollama. Read: [Practical tips for finetuning LLMs using LoRA (Sebastian Raschka)](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms).
- 🛠️ **Do:** Swap in your JSONL, train 1-2 epochs, plot losses, then evaluate on the 40-example test split: JSON validity and field-level F1 vs the same base model with your best prompt. Save the adapter to Drive or a private Hugging Face repo. Done when: the base+prompt vs fine-tuned metrics table is recorded.

### Saturday 27 Feb · 45 min — BUILD: FineTune Lab report, LoRA vs prompting
- 📚 **Learn:** Report like an engineer: hypothesis, data, setup (hyperparameters, GPU, time), results with caveats (small n), cost and latency, failure examples, recommendation. Awareness: preference tuning with the [TRL DPO trainer](https://huggingface.co/docs/trl/dpo_trainer).
- 🛠️ **Do:** Finalize `09-finetune-lab`: notebook plus `REPORT.md` comparing base+prompt, LoRA and a large API model on JSON validity, field F1, latency and estimated cost, with 5 error examples; optionally run the GGUF export in Ollama. Done when: the fine-tuned model beats its prompted baseline by 10+ F1 points or you explain why not, and tag `v1.0-finetune-lab` is pushed.

## 📦 Deliverable (by Saturday night)
`09-finetune-lab/`: decision memo, reviewed dataset with `DATA.md`, Colab/Unsloth training notebook, saved LoRA adapter and `REPORT.md` comparing prompting vs LoRA vs API.

## ✅ Self-check (Sunday test preview)
- When should you fine-tune instead of prompting or RAG?
- Explain LoRA: what are rank and alpha, and why is it parameter-efficient?
- How does QLoRA reduce GPU memory?
- What is DPO and how does it differ from SFT?
- What is distillation, and how did you use a teacher model?
- How do you detect overfitting during fine-tuning?

## 🚀 Stretch (optional)
Try a DPO pass on 100 preference pairs (valid vs invalid JSON) or the SFT unit of the [Hugging Face smol course](https://huggingface.co/learn/smol-course/unit0/1).
