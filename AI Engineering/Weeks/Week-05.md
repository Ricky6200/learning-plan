# 🤖 AI Engineering · Week 05 — How LLMs Actually Work

> 📅 **Mon 23 Nov 2026 → Sun 29 Nov 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 04](Week-04.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-05.md) · [Week 06 →](Week-06.md)

**Why this week:** Interviewers probe fundamentals: tokens, attention, training stages, sampling and hallucinations. Intuition here lets you reason about cost, latency and quality instead of guessing. (AZ-900 exam on Fri 27 Nov, so Friday is deliberately light.)

## 🗓️ Sessions

### Monday 23 Nov · 45 min — Neural networks, gradient descent and backprop intuition
- 📚 **Learn:** A neural network is layers of weighted sums plus non-linearities; training minimises a loss by gradient descent, and backpropagation computes every weight's gradient with the chain rule, layer by layer. Deep learning = many such layers; LLMs are very large networks trained on next-token prediction. Watch: [Backpropagation, intuitively (3Blue1Brown)](https://www.youtube.com/watch?v=Ilg3gGewQ5U) (about 13 min). Optional: [Gradient descent (3Blue1Brown)](https://www.youtube.com/watch?v=IHZwWFHWa-w).
- 🛠️ **Do:** In `04-llm-playground/01_gradient_descent.ipynb` fit y = 3x + 2 on noisy data with hand-written gradient descent in NumPy (about 20 lines: predictions, MSE loss, two gradients, update). Plot loss per epoch and try 3 learning rates. Done when: learned w is about 3 and b about 2, and you note what happens when the learning rate is too high.

### Tuesday 24 Nov · 45 min — Tokenization: BPE, vocabularies and token costs
- 📚 **Learn:** Tokens are not words: byte-pair encoding, vocabulary size, special tokens, why Hindi and code cost more tokens, and why tokens drive both cost and context limits. Read: [tiktoken README](https://github.com/openai/tiktoken) (about 5 min). Optional: Karpathy [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) (first 15 min).
- 🛠️ **Do:** Paste 3 sentences into [Tiktokenizer](https://tiktokenizer.vercel.app/) to see the splits. Then in `02_tokens.ipynb` use `tiktoken.get_encoding('o200k_base')` to count tokens for an English paragraph, the same text in Hindi (Devanagari), Hinglish, a JSON object and a Java method. Tabulate tokens per character and estimated cost at a sample price per 1M tokens. Done when: the table is filled and you can explain why Hindi costs more tokens.

### Thursday 26 Nov · 45 min — Embeddings, transformers and attention
- 📚 **Learn:** Embeddings turn tokens into meaning vectors; attention lets each token weigh the others (query/key/value), multi-head attention, positional information (RoPE in most modern LLMs), next-token prediction. Encoder-only models (BERT-style, like the embedding models of W9) read a whole text at once; decoder-only models (GPT-style chat LLMs) generate left to right. Read: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) (up to 'Self-Attention in Detail'). Optional: interactive [Transformer Explainer](https://poloclub.github.io/transformer-explainer/).
- 🛠️ **Do:** Write a 10-line 'attention explained to a Java developer' note, then compute toy scaled dot-product attention in NumPy for 3 tokens (random Q, K, V, softmax, weighted sum) in `03_attention.ipynb`. Done when: each row of attention weights sums to 1 and your note explains Q/K/V in your own words.

### Friday 27 Nov · 45 min — Training stages, reasoning models and hallucinations (light)
- 📚 **Learn:** Pretraining (next-token prediction on internet text), SFT (instruction data), preference tuning (RLHF/DPO), reasoning models (RL on verifiable tasks, thinking tokens), context windows, why hallucinations happen. Awareness: mixture-of-experts (MoE) models activate only a few expert layers per token, so they run cheaper than their total size suggests. Watch: Karpathy [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) 0:00-15:00. Optional: [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).
- 🛠️ **Do:** AZ-900 exam day, so stop after 20 minutes: create `llm_lifecycle.md` with a 4-box Mermaid diagram (raw data -> pretraining -> SFT -> preference tuning) and list 3 causes of hallucination plus 3 mitigations you will build later (RAG with citations, refusals, evals). Done when: the diagram renders on GitHub and the 6 bullets are committed.

### Saturday 28 Nov · 45 min — BUILD: tokenizer + sampling playground notebook
- 📚 **Learn:** Decoding strategies: greedy, temperature, top-k, top-p (nucleus), repetition penalties; why temperature 0 is still not guaranteed to be deterministic across providers. Read: [How to generate text](https://huggingface.co/blog/how-to-generate) (the sampling sections).
- 🛠️ **Do:** Build `04_sampling_playground.ipynb`: from a hand-made next-token probability table (10 tokens), implement greedy, temperature (0.2/1.0/1.5), top-k and top-p sampling; draw 1,000 samples each and plot the distributions. Include your W5 token-cost table and a findings section. Done when: the plots show how temperature and top-p reshape the distribution and the notebook is pushed.

## 📦 Deliverable (by Saturday night)
`04-llm-playground/` with gradient-descent, tokens, attention and sampling notebooks plus `llm_lifecycle.md` (diagram + hallucination notes).

## ✅ Self-check (Sunday test preview)
- What does backpropagation compute, and why is it needed for gradient descent?
- What is a token, and why do token counts differ across languages?
- Explain self-attention (Q, K, V) in three sentences.
- Encoder-only vs decoder-only models: which powers chat LLMs, which powers your embedding models?
- What do pretraining, SFT and preference tuning (RLHF/DPO) each add?
- How do temperature and top-p change outputs? When would you keep temperature low?
- Why do LLMs hallucinate? Name two mitigations.
- How do reasoning models differ from standard chat models in cost and latency?

## 🚀 Stretch (optional)
Watch the rest of Karpathy's Intro to LLMs, then [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) in 30-minute chunks over the next weekends, keeping timestamped notes.
