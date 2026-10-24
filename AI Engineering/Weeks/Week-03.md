# 🤖 AI Engineering · Week 03 — How LLMs Actually Work

> 📅 **Mon 09 Nov 2026 → Sun 15 Nov 2026** · Season 1 — Foundation Forge  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 02](Week-02.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-03.md) · [Week 04 →](Week-04.md)

**Why this week:** Interviewers probe fundamentals: tokens, attention, training stages, sampling and hallucinations. Intuition here lets you reason about cost, latency and quality instead of guessing.

## 🗓️ Sessions

### Monday 09 Nov · 45 min — AI/ML/DL/GenAI map and gradient descent intuition
- 📚 **Learn:** AI > ML > deep learning > GenAI; supervised learning, training vs inference, loss, gradient descent, overfitting. Watch 3Blue1Brown [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs) (8 min) and [Gradient descent](https://www.youtube.com/watch?v=IHZwWFHWa-w) (first 12 min). Reference: [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) linear regression module.
- 🛠️ **Do:** In `02-llm-playground/01_gradient_descent.ipynb`, fit y = 3x + 2 on noisy data with hand-written gradient descent in NumPy (about 20 lines). Plot loss per epoch and try 3 learning rates. Done when: learned w is about 3 and b about 2, and you note what happens when the learning rate is too high.

### Tuesday 10 Nov · 45 min — Tokenization: BPE, vocabularies and token costs
- 📚 **Learn:** Tokens are not words: byte-pair encoding, vocabulary size, special tokens, why Hindi and code cost more tokens, tokens drive cost and context limits. Play with [Tiktokenizer](https://tiktokenizer.vercel.app/); read the [tiktoken README](https://github.com/openai/tiktoken). Optional: Karpathy [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) (first 15 min).
- 🛠️ **Do:** In `02_tokens.ipynb` use `tiktoken.get_encoding('o200k_base')` to count tokens for: an English paragraph, the same text in Hindi (Devanagari), Hinglish, a JSON object and a Java method. Tabulate tokens per character and estimated cost at a sample price per 1M tokens. Done when: the table is filled and you can explain why Hindi costs more tokens.

### Thursday 12 Nov · 45 min — Embeddings, transformers and attention
- 📚 **Learn:** Embeddings turn tokens into meaning vectors; attention lets each token weigh the others (query/key/value), multi-head attention, positional information, next-token prediction. Watch 3Blue1Brown [Transformers, the tech behind LLMs](https://www.youtube.com/watch?v=wjZofJX0v4M) at 1.25x; explore the interactive [Transformer Explainer](https://poloclub.github.io/transformer-explainer/); skim [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/).
- 🛠️ **Do:** Write a 10-line 'attention explained to a Java developer' note, then compute toy scaled dot-product attention in NumPy for 3 tokens (random Q, K, V, softmax, weighted sum) in `03_attention.ipynb`. Done when: each row of attention weights sums to 1 and your note explains Q/K/V in your own words.

### Friday 13 Nov · 45 min — Pretraining, SFT, RLHF, reasoning models, hallucinations
- 📚 **Learn:** Pretraining (next-token prediction on internet text), SFT (instruction data), preference tuning (RLHF/DPO), reasoning models (RL on verifiable tasks, thinking tokens), context windows, why hallucinations happen. Watch Karpathy [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) 0:00-25:00 at 1.25x; skim [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).
- 🛠️ **Do:** Create `llm_lifecycle.md` with a Mermaid diagram from raw data to deployed chat model, labelling data, objective and rough cost at each stage. Add 3 causes of hallucination and 3 mitigations you will build later (RAG with citations, refusals, evals). Done when: the diagram renders on GitHub and you can explain it aloud in 2 minutes.

### Saturday 14 Nov · 45 min — BUILD: tokenizer + sampling playground notebook
- 📚 **Learn:** Decoding strategies: greedy, temperature, top-k, top-p (nucleus), repetition penalties; why temperature 0 is still not guaranteed deterministic across providers. Read the sampling sections of [How to generate text](https://huggingface.co/blog/how-to-generate).
- 🛠️ **Do:** Build `04_sampling_playground.ipynb`: from a hand-made next-token probability table (10 tokens), implement greedy, temperature (0.2/1.0/1.5), top-k and top-p sampling; draw 1,000 samples each and plot the distributions. Include your W3 token-cost table and a findings section. Done when: plots show how temperature and top-p reshape the distribution and the notebook is pushed.

## 📦 Deliverable (by Saturday night)
`02-llm-playground/` with gradient-descent, tokens, attention and sampling notebooks plus `llm_lifecycle.md` (diagram + hallucination notes).

## ✅ Self-check (Sunday test preview)
- What is a token, and why do token counts differ across languages?
- Explain self-attention (Q, K, V) in three sentences.
- What do pretraining, SFT and preference tuning (RLHF/DPO) each add?
- How do temperature and top-p change outputs? When would you keep temperature low?
- What is a context window, and what happens when a conversation exceeds it?
- Why do LLMs hallucinate? Name two mitigations.
- How do reasoning models differ from standard chat models in cost and latency?

## 🚀 Stretch (optional)
Watch Karpathy's [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) in 30-minute chunks over the next three weekends, keeping timestamped notes.
