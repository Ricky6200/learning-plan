# 🎯 AI Engineering — Interview Question Bank (150 questions)

**How to use:** ⭐ = asked most often in AI-engineer / AI-backend interviews (India, 2026) · `(Wn)` = week of the 30-week plan that teaches it.
Answer every question in **≤ 2 minutes** with this frame: **Define → Why it matters → Example from *your* project → Trade-off → Metric/number.**
Track status in the Sunday test log: 🟢 can answer cold · 🟡 shaky · 🔴 cannot answer → becomes a Fix-it task.

---

## 1. Python for AI work
1. ⭐ List comprehension vs generator expression: what is the difference, and when does laziness matter? (W1, W3)
2. ⭐ How do `async`/`await` and `asyncio.gather` work, and why do they speed up I/O-bound but not CPU-bound work (the GIL)? (W2)
3. What is a decorator? Write one that retries a function or logs how long it takes. (W3)
4. When would you use a dataclass, a pydantic model or a `TypedDict`? (W2, W3)
5. How do you make Python call internet HTTPS behind a TLS-inspecting corporate proxy without disabling certificate checks? (W2)
6. How does FastAPI's `Depends` make code testable, and how do you stream tokens with Server-Sent Events? (W8, W13)

## 2. ML fundamentals
7. ⭐ Supervised vs unsupervised learning: give an example of each. (W4)
8. ⭐ Why do you need separate train, validation and test sets? What is data leakage? (W4)
9. ⭐ Define precision, recall and F1. When do you prefer high recall? (W4)
10. A model scores 99% accuracy on data with 1% positives. Is it good? What do you check? (W4)
11. ⭐ What is overfitting, and how do you detect and reduce it? (W4, W21)
12. What does k-fold cross-validation give you that a single split does not? (W4)
13. How does TF-IDF + logistic regression classify text, and when would you keep it instead of an LLM? (W4, W7)
14. What does backpropagation compute, and how does gradient descent use it? (W5)

## 3. LLM fundamentals
15. ⭐ What is a large language model, and what does "next-token prediction" mean? (W5)
16. ⭐ Explain the transformer at a high level: embeddings, attention, feed-forward layers, residual connections. (W5)
17. ⭐ Explain self-attention with queries, keys and values. Why multiple heads, and why scale by √d? (W5)
18. How does a transformer know word order (positional encodings, RoPE)? (W5)
19. ⭐ Pretraining vs SFT vs preference tuning (RLHF/DPO): what does each stage add? (W5)
20. ⭐ What are reasoning models, and what is the cost/latency trade-off of "thinking" tokens? (W5)
21. ⭐ What is a context window? What happens when you exceed it, and how do you handle long inputs? (W5, W6)
22. ⭐ Explain temperature, top-k and top-p. When would you use a low temperature? (W5)
23. ⭐ Why do LLMs hallucinate? List four mitigations. (W5, W10)
24. Why can outputs differ between runs even at temperature 0? (W5)
25. Encoder-only vs decoder-only vs encoder-decoder models: examples and typical uses. What is a mixture-of-experts model? (W5)

## 4. Tokenization & embeddings
26. ⭐ What is a token, and how does byte-pair encoding work? (W5)
27. Why do Hindi text and source code consume more tokens than English prose, and what does that do to cost? (W5)
28. How do you count tokens before calling an API, and why would you? (W6)
29. ⭐ What is an embedding, and how is it different from a token ID? (W5, W9)
30. ⭐ Cosine similarity vs dot product vs Euclidean distance: when are they equivalent? (W9)
31. ⭐ How do you choose an embedding model? What is MTEB and what are its limits? (W9)
32. What must happen if you switch embedding models after indexing? (W9)

## 5. Prompt engineering
33. ⭐ Zero-shot vs few-shot prompting: trade-offs and costs. (W7)
34. What belongs in a good system prompt? (W7)
35. Why use delimiters or XML tags in prompts? (W7)
36. ⭐ Chain-of-thought prompting vs reasoning models: when does CoT still help? (W7)
37. What is prompt chaining, and when does it beat one big prompt? (W7, W14)
38. How do you version and regression-test prompts like code? (W7, W19)
39. How do you shorten a prompt without losing quality? (W19)

## 6. Structured output & tool calling
40. ⭐ JSON mode vs schema-constrained structured outputs: what is the difference? (W7)
41. How do you handle invalid model output (validation, repair retry, fallback)? (W7)
42. ⭐ Walk through the tool/function-calling loop step by step. (W7, W14)
43. Why must you validate tool arguments even though the model "chose" them? (W7, W18)
44. What are parallel tool calls, and when are they safe? (W7, W14)
45. What makes a tool well designed for an LLM (name, description, arguments, outputs, errors)? (W14)

## 7. RAG
46. ⭐ What is RAG, and when would you choose it over fine-tuning? (W10)
47. ⭐ Walk through a RAG pipeline end to end, from ingestion to the cited answer. (W10)
48. ⭐ How do you choose chunk size and overlap? Name three chunking strategies. (W10)
49. How do you make answers cite sources and refuse when the context is missing? (W10)
50. What is the "lost in the middle" effect, and how do you mitigate it? (W10)
51. ⭐ What is hybrid search, and why does it beat pure vector search on some queries? (W11)
52. ⭐ Explain Reciprocal Rank Fusion with a small example. (W11)
53. ⭐ What is re-ranking? Where does a cross-encoder sit in the pipeline, and what does it cost? (W11)
54. Query rewriting vs multi-query vs HyDE: when would you use each? (W11)
55. What is contextual retrieval, and why does it improve recall? (W11)
56. When is GraphRAG worth its cost? (W11)
57. ⭐ Long-context models vs RAG: when do you use which? (W11)
58. ⭐ A RAG system gives wrong answers. How do you debug it step by step? (W12)
59. Two-step RAG vs agentic RAG: differences and trade-offs. (W10, W29)
60. ⭐ What does agentic (corrective) RAG add (grading, query rewriting, retrying), and how do you cap its cost? (W29)
61. How would you answer a multi-hop question with retrieval (query decomposition)? (W29)

## 8. Vector databases
62. ⭐ How does HNSW work? What do `m` and `ef_search` control? (W9)
63. HNSW vs IVF indexes: trade-offs in build time, memory and recall. (W9)
64. ⭐ Why can filtered vector search return fewer than k results, and how do you fix it? (W9)
65. pgvector vs Qdrant vs a managed service (e.g., Azure AI Search): how do you choose? (W9, W25)
66. How would you scale a vector store to 100M vectors? (W26)
67. What is vector quantization (halfvec, binary, PQ), and what does it cost you? (W26)
68. How do you handle updates, deletes and re-embedding in production? (W26, W27)

## 9. Evaluation
69. ⭐ How do you evaluate a RAG system? Why evaluate retrieval and generation separately? (W12)
70. ⭐ Define recall@k, MRR and nDCG. When do you use each? (W12)
71. ⭐ What is faithfulness, and how is it measured? How does it differ from answer relevancy? (W12)
72. ⭐ What are the pitfalls of LLM-as-judge, and how do you mitigate them? (W12)
73. How do you build a golden dataset, and how big should it be? (W12)
74. What is error analysis, and why do it before choosing metrics? (W12)
75. Offline vs online evaluation: which production signals would you collect? (W19)
76. How do you run evals in CI without flaky failures? (W19)
77. ⭐ How do you evaluate an agent: task success, trajectory and tool-call accuracy? (W17)

## 10. Agents
78. ⭐ What is an AI agent? How is it different from a workflow? (W14)
79. ⭐ Explain prompt chaining, routing, parallelization, orchestrator-workers and evaluator-optimizer. (W14)
80. ⭐ What is ReAct? (W14)
81. How do you stop an agent from looping forever or overspending? (W14)
82. ⭐ Short-term vs long-term memory for agents: how do you implement each? (W14)
83. What is context engineering, and why does it matter for agents? (W14)
84. ⭐ Why use LangGraph? Explain state, nodes, edges and reducers. (W15)
85. ⭐ How do checkpointers enable persistence and human-in-the-loop (`interrupt`)? (W15)
86. ⭐ When is a multi-agent system justified? Supervisor vs handoffs, and common failure modes. (W17)
87. Compare LangGraph, OpenAI Agents SDK, Microsoft Agent Framework, Pydantic AI and CrewAI. (W17, W25)

## 11. MCP & agent protocols
88. ⭐ What is the Model Context Protocol, and what problem does it solve? (W16)
89. ⭐ Explain host, client and server. Tools vs resources vs prompts: who controls each? (W16)
90. stdio vs Streamable HTTP transports: when do you use each? (W16)
91. What changed in MCP revision 2026-07-28 (stateless requests, `server/discover`, multi-round-trip requests)? (W16)
92. ⭐ What is tool poisoning? Name three other MCP security risks and mitigations. (W16, W18)
93. How is a remote MCP server authorized? (W16, W29)
94. How does an MCP server verify a bearer token, what does its 401 response tell the client, and why are stdio servers not covered? (W29)
95. MCP vs A2A vs plain function calling: when do you use which? (W16)

## 12. AI security
96. ⭐ Name the OWASP Top 10 for LLM Applications (2025) and give an example of three. (W18)
97. ⭐ Direct vs indirect prompt injection: give a RAG example of the indirect kind. (W18)
98. ⭐ What is the "lethal trifecta", and how do you break it? (W18)
99. How do you keep PII out of logs, traces and third-party LLM calls? (W18)
100. What is improper output handling? Give an XSS or SQL example. (W18)
101. ⭐ What is excessive agency, and how do least privilege and human approval limit it? (W18)
102. How do you red-team an LLM application? Which tools would you use? (W18)
103. Where do content-safety filters (e.g., Prompt Shields) fit, and why are they not enough on their own? (W18, W25)

## 13. LLMOps
104. ⭐ What would you log or trace for every LLM call, and what must you never log? (W19)
105. What are traces, spans and the OpenTelemetry GenAI semantic conventions, and why use them? (W19)
106. How do you version prompts and roll back safely? (W19)
107. ⭐ Name five levers to reduce LLM cost. (W19)
108. ⭐ How do you reduce latency (time-to-first-token and total time)? (W13, W19)
109. How does prompt caching work, and how should prompts be structured to benefit? (W19)
110. How do you upgrade to a new model version safely? (W19, W26)
111. Exact vs semantic caching of LLM responses: benefits and risks. (W13)
112. How would you ship a cheap, safe public demo of an AI app (secrets, rate limits, cost)? (W19)

## 14. Fine-tuning
113. ⭐ When should you fine-tune instead of prompting or using RAG? (W21)
114. ⭐ Explain LoRA: rank, alpha, target modules, and why it is parameter-efficient. (W21)
115. What does QLoRA add on top of LoRA? (W21)
116. SFT vs DPO vs RLHF: what is each for? (W5, W21)
117. What is distillation, and how would you use a teacher model? (W21)
118. How do you prepare a fine-tuning dataset, and how many examples do you need? (W21)

## 15. Open-source models & inference
119. ⭐ What is quantization? Compare 4-bit and 8-bit. (W20)
120. What is GGUF, and which runtimes use it? (W20)
121. ⭐ Explain the KV cache. Why are long contexts expensive? (W20)
122. What are prefill/decode, continuous batching and PagedAttention? (W20)
123. ⭐ How do you choose between an open-weight model and an API model? (W20)
124. What do you check in a model card and licence before commercial use? (W20)

## 16. Multimodal & document AI
125. How do vision-language models process images, and what drives their token cost? (W22)
126. ⭐ Text-layer extraction vs OCR vs VLM for documents: when do you use each? (W22)
127. How do you make document extraction reliable (schemas, retries, confidence, human review)? (W22)
128. How would you build a low-latency voice assistant (speech-to-text → LLM → text-to-speech)? (W22)
129. Design a pipeline that processes 1M invoices per month. (W22, W26)

## 17. Spring AI & Java
130. ⭐ What is Spring AI's `ChatClient`, and how does it relate to `ChatModel`? (W23)
131. ⭐ What are advisors in Spring AI? Give three examples. (W23)
132. How do you implement per-conversation chat memory in Spring AI? (W23)
133. ⭐ How does `@Tool` tool calling work end to end in Spring AI? (W24)
134. `QuestionAnswerAdvisor` vs `RetrievalAugmentationAdvisor`: when do you use each? (W24)
135. How do you expose Spring beans as MCP tools? (W24)
136. Spring AI vs LangChain4j: how would you choose for a team? (W23, W24)

## 18. Azure AI
137. ⭐ What is Microsoft Foundry? How do projects, deployments and the model catalog relate? (W25)
138. ⭐ How does keyless authentication with managed identity work for Foundry/Azure OpenAI models? (W25)
139. ⭐ Azure AI Search: explain vector search, hybrid search with RRF and the semantic ranker. (W25)
140. Foundry Agent Service vs your own LangGraph app on Container Apps: when do you choose which? (W25)
141. What is Microsoft Agent Framework, and what does it replace? (W17, W25)
142. Which Azure services would you use for a production RAG app, and why? (W25, W26)

## 19. AI system design
143. ⭐ Design an LLM gateway for a 2,000-employee company. (W26)
144. ⭐ Design enterprise RAG over 10M documents with document-level ACLs (Hindi + English). (W26)
145. ⭐ Design a customer-support agent with tools and human handoff. (W26)
146. Design a ChatGPT-like chat service for 1M daily users. (W26)
147. How do you isolate tenants in a multi-tenant RAG system? (W26)
148. Where do you place guardrails in an agentic system? (W26)
149. How do you model LLM costs and cut them by 50%? (W26)
150. Design semantic search and an AI booking assistant for a ticketing platform. (W27)

---

## Bonus: practice prompts for W30

**AI coding round (45 minutes each, docs allowed, no AI generation):**
- Mini RAG over 3 text files with citations and 3 tests (W30 Thu).
- A TF-IDF + logistic regression classifier with an honest stratified split, P/R/F1 and a baseline (W4).
- A tool-calling agent with 2 tools, a max-steps guard and a trace log (W14).
- A JD → JSON extractor with pydantic validation and one repair retry (W7).
- A FastAPI endpoint that streams LLM tokens over SSE with a timeout and an error event (W13).
- An evaluator that computes recall@5 and MRR from a JSONL golden set, with unit tests (W12).

**Project deep-dive prompts (answer with numbers):**
- "Walk me through DocuMind's architecture. What improved recall the most, and by how much?"
- "Did the LLM beat your TF-IDF classifier in W7? At what cost and latency?"
- "How does CareerPilot stop an agent from doing something irreversible?"
- "Why did (or didn't) your LoRA model beat prompting?"
- "How does TicketVerse AI guarantee no booking happens without the user's confirmation?"
- "What would break first at 100× traffic, and how would you fix it?"
