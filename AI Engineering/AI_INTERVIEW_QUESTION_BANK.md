# 🎯 AI Engineering — Interview Question Bank (132 questions)

**How to use:** ⭐ = asked most often in AI-engineer / AI-backend interviews (India, 2026) · `(Wn)` = week that teaches it.
Answer every question in **≤ 2 minutes** with this frame: **Define → Why it matters → Example from *your* project → Trade-off → Metric/number.**
Track status in the Sunday test log: 🟢 can answer cold · 🟡 shaky · 🔴 cannot answer → becomes a Fix-it task.

---

## 1. LLM fundamentals
1. ⭐ What is a large language model, and what does "next-token prediction" mean? (W3)
2. ⭐ Explain the transformer at a high level: embeddings, attention, feed-forward layers, residual connections. (W3)
3. ⭐ Explain self-attention with queries, keys and values. Why multiple heads, and why scale by √d? (W3)
4. How does a transformer know word order (positional encodings, RoPE)? (W3)
5. ⭐ Pretraining vs SFT vs preference tuning (RLHF/DPO): what does each stage add? (W3)
6. ⭐ What are reasoning models, and what is the cost/latency trade-off of "thinking" tokens? (W3)
7. ⭐ What is a context window? What happens when you exceed it, and how do you handle long inputs? (W3, W4)
8. ⭐ Explain temperature, top-k and top-p. When would you use a low temperature? (W3)
9. ⭐ Why do LLMs hallucinate? List four mitigations. (W3, W7)
10. Why can outputs differ between runs even at temperature 0? (W3)
11. Encoder-only vs decoder-only vs encoder-decoder models: examples and typical uses. (W3)

## 2. Tokenization & embeddings
12. ⭐ What is a token, and how does byte-pair encoding work? (W3)
13. Why do Hindi text and source code consume more tokens than English prose, and what does that do to cost? (W3)
14. How do you count tokens before calling an API, and why would you? (W4)
15. ⭐ What is an embedding, and how is it different from a token ID? (W3, W6)
16. ⭐ Cosine similarity vs dot product vs Euclidean distance: when are they equivalent? (W6)
17. ⭐ How do you choose an embedding model? What is MTEB and what are its limits? (W6)
18. What must happen if you switch embedding models after indexing? (W6)

## 3. Prompt engineering
19. ⭐ Zero-shot vs few-shot prompting: trade-offs and costs. (W5)
20. What belongs in a good system prompt? (W5)
21. Why use delimiters or XML tags in prompts? (W5)
22. ⭐ Chain-of-thought prompting vs reasoning models: when does CoT still help? (W5)
23. What is prompt chaining, and when does it beat one big prompt? (W5, W11)
24. How do you version and regression-test prompts like code? (W5, W16)
25. How do you shorten a prompt without losing quality? (W16)

## 4. Structured output & tool calling
26. ⭐ JSON mode vs schema-constrained structured outputs: what is the difference? (W5)
27. How do you handle invalid model output (validation, repair retry, fallback)? (W5)
28. ⭐ Walk through the tool/function-calling loop step by step. (W5, W11)
29. Why must you validate tool arguments even though the model "chose" them? (W5, W15)
30. What are parallel tool calls, and when are they safe? (W5, W11)
31. What makes a tool well designed for an LLM (name, description, arguments, outputs, errors)? (W11)

## 5. RAG
32. ⭐ What is RAG, and when would you choose it over fine-tuning? (W7)
33. ⭐ Walk through a RAG pipeline end to end, from ingestion to the cited answer. (W7)
34. ⭐ How do you choose chunk size and overlap? Name three chunking strategies. (W7)
35. How do you make answers cite sources and refuse when the context is missing? (W7)
36. What is the "lost in the middle" effect, and how do you mitigate it? (W7)
37. ⭐ What is hybrid search, and why does it beat pure vector search on some queries? (W8)
38. ⭐ Explain Reciprocal Rank Fusion with a small example. (W8)
39. ⭐ What is re-ranking? Where does a cross-encoder sit in the pipeline, and what does it cost? (W8)
40. Query rewriting vs multi-query vs HyDE: when would you use each? (W8)
41. What is contextual retrieval, and why does it improve recall? (W8)
42. When is GraphRAG worth its cost? (W8)
43. ⭐ Long-context models vs RAG: when do you use which? (W8)
44. ⭐ A RAG system gives wrong answers. How do you debug it step by step? (W9)
45. Two-step RAG vs agentic RAG: differences and trade-offs. (W7, W12)

## 6. Vector databases
46. ⭐ How does HNSW work? What do `m` and `ef_search` control? (W6)
47. HNSW vs IVF indexes: trade-offs in build time, memory and recall. (W6)
48. ⭐ Why can filtered vector search return fewer than k results, and how do you fix it? (W6)
49. pgvector vs Qdrant vs a managed service (e.g., Azure AI Search): how do you choose? (W6, W22)
50. How would you scale a vector store to 100M vectors? (W23)
51. What is vector quantization (halfvec, binary, PQ), and what does it cost you? (W23)
52. How do you handle updates, deletes and re-embedding in production? (W23, W24)

## 7. Evaluation
53. ⭐ How do you evaluate a RAG system? Why evaluate retrieval and generation separately? (W9)
54. ⭐ Define recall@k, MRR and nDCG. When do you use each? (W9)
55. ⭐ What is faithfulness, and how is it measured? How does it differ from answer relevancy? (W9)
56. ⭐ What are the pitfalls of LLM-as-judge, and how do you mitigate them? (W9)
57. How do you build a golden dataset, and how big should it be? (W9)
58. What is error analysis, and why do it before choosing metrics? (W9)
59. Offline vs online evaluation: which production signals would you collect? (W16)
60. How do you run evals in CI without flaky failures? (W16)
61. ⭐ How do you evaluate an agent: task success, trajectory and tool-call accuracy? (W14)

## 8. Agents
62. ⭐ What is an AI agent? How is it different from a workflow? (W11)
63. ⭐ Explain prompt chaining, routing, parallelization, orchestrator-workers and evaluator-optimizer. (W11)
64. ⭐ What is ReAct? (W11)
65. How do you stop an agent from looping forever or overspending? (W11)
66. ⭐ Short-term vs long-term memory for agents: how do you implement each? (W11)
67. What is context engineering, and why does it matter for agents? (W11)
68. ⭐ Why use LangGraph? Explain state, nodes, edges and reducers. (W12)
69. ⭐ How do checkpointers enable persistence and human-in-the-loop (`interrupt`)? (W12)
70. ⭐ When is a multi-agent system justified? Supervisor vs handoffs, and common failure modes. (W14)
71. Compare LangGraph, OpenAI Agents SDK, Microsoft Agent Framework, Pydantic AI and CrewAI. (W14, W22)

## 9. MCP & agent protocols
72. ⭐ What is the Model Context Protocol, and what problem does it solve? (W13)
73. ⭐ Explain host, client and server. Tools vs resources vs prompts: who controls each? (W13)
74. stdio vs Streamable HTTP transports: when do you use each? (W13)
75. What changed in MCP revision 2026-07-28 (stateless requests, `server/discover`, multi-round-trip requests)? (W13)
76. ⭐ What is tool poisoning? Name three other MCP security risks and mitigations. (W13, W15)
77. How is a remote MCP server authorized? (W13)
78. MCP vs A2A vs plain function calling: when do you use which? (W13)

## 10. AI security
79. ⭐ Name the OWASP Top 10 for LLM Applications (2025) and give an example of three. (W15)
80. ⭐ Direct vs indirect prompt injection: give a RAG example of the indirect kind. (W15)
81. ⭐ What is the "lethal trifecta", and how do you break it? (W15)
82. How do you keep PII out of logs, traces and third-party LLM calls? (W15)
83. What is improper output handling? Give an XSS or SQL example. (W15)
84. ⭐ What is excessive agency, and how do least privilege and human approval limit it? (W15)
85. How do you red-team an LLM application? Which tools would you use? (W15)
86. Where do content-safety filters (e.g., Prompt Shields) fit, and why are they not enough on their own? (W15, W22)

## 11. LLMOps
87. ⭐ What would you log or trace for every LLM call, and what must you never log? (W16)
88. How do you version prompts and roll back safely? (W16)
89. ⭐ Name five levers to reduce LLM cost. (W16)
90. ⭐ How do you reduce latency (time-to-first-token and total time)? (W10, W16)
91. How does prompt caching work, and how should prompts be structured to benefit? (W16)
92. What are the OpenTelemetry GenAI semantic conventions, and why use them? (W16)
93. How do you upgrade to a new model version safely? (W16, W23)
94. Exact vs semantic caching of LLM responses: benefits and risks. (W10)

## 12. Fine-tuning
95. ⭐ When should you fine-tune instead of prompting or using RAG? (W18)
96. ⭐ Explain LoRA: rank, alpha, target modules, and why it is parameter-efficient. (W18)
97. What does QLoRA add on top of LoRA? (W18)
98. SFT vs DPO vs RLHF: what is each for? (W3, W18)
99. What is distillation, and how would you use a teacher model? (W18)
100. How do you prepare a fine-tuning dataset, and how many examples do you need? (W18)

## 13. Open-source models & inference
101. ⭐ What is quantization? Compare 4-bit and 8-bit. (W17)
102. What is GGUF, and which runtimes use it? (W17)
103. ⭐ Explain the KV cache. Why are long contexts expensive? (W17)
104. What are prefill/decode, continuous batching and PagedAttention? (W17)
105. ⭐ How do you choose between an open-weight model and an API model? (W17)
106. What do you check in a model card and licence before commercial use? (W17)

## 14. Multimodal & document AI
107. How do vision-language models process images, and what drives their token cost? (W19)
108. ⭐ Text-layer extraction vs OCR vs VLM for documents: when do you use each? (W19)
109. How do you make document extraction reliable (schemas, retries, confidence, human review)? (W19)
110. How would you build a low-latency voice assistant (speech-to-text → LLM → text-to-speech)? (W19)
111. Design a pipeline that processes 1M invoices per month. (W19, W23)

## 15. Spring AI & Java
112. ⭐ What is Spring AI's `ChatClient`, and how does it relate to `ChatModel`? (W20)
113. ⭐ What are advisors in Spring AI? Give three examples. (W20)
114. How do you implement per-conversation chat memory in Spring AI? (W20)
115. ⭐ How does `@Tool` tool calling work end to end in Spring AI? (W21)
116. `QuestionAnswerAdvisor` vs `RetrievalAugmentationAdvisor`: when do you use each? (W21)
117. How do you expose Spring beans as MCP tools? (W21)
118. Spring AI vs LangChain4j: how would you choose for a team? (W20, W21)

## 16. Azure AI
119. ⭐ What is Microsoft Foundry? How do projects, deployments and the model catalog relate? (W22)
120. ⭐ How does keyless authentication with managed identity work for Foundry/Azure OpenAI models? (W22)
121. ⭐ Azure AI Search: explain vector search, hybrid search with RRF and the semantic ranker. (W22)
122. Foundry Agent Service vs your own LangGraph app on Container Apps: when do you choose which? (W22)
123. What is Microsoft Agent Framework, and what does it replace? (W14, W22)
124. Which Azure services would you use for a production RAG app, and why? (W22, W23)

## 17. AI system design
125. ⭐ Design an LLM gateway for a 2,000-employee company. (W23)
126. ⭐ Design enterprise RAG over 10M documents with document-level ACLs (Hindi + English). (W23)
127. ⭐ Design a customer-support agent with tools and human handoff. (W23)
128. Design a ChatGPT-like chat service for 1M daily users. (W23)
129. How do you isolate tenants in a multi-tenant RAG system? (W23)
130. Where do you place guardrails in an agentic system? (W23)
131. How do you model LLM costs and cut them by 50%? (W23)
132. Design semantic search and an AI booking assistant for a ticketing platform. (W24)

---

## Bonus: practice prompts for W26

**AI coding round (45 minutes each, docs allowed, no AI generation):**
- Mini RAG over 3 text files with citations and 3 tests (W26 Thu).
- A tool-calling agent with 2 tools, a max-steps guard and a trace log (W11).
- A JD → JSON extractor with pydantic validation and one repair retry (W5).
- A FastAPI endpoint that streams LLM tokens over SSE with a timeout and fallback provider (W10).
- An evaluator that computes recall@5 and MRR from a JSONL golden set, with unit tests (W9).

**Project deep-dive prompts (answer with numbers):**
- "Walk me through DocuMind's architecture. What improved recall the most, and by how much?"
- "How does CareerPilot stop an agent from doing something irreversible?"
- "Why did (or didn't) your LoRA model beat prompting?"
- "How does TicketVerse AI guarantee no booking happens without the user's confirmation?"
- "What would break first at 100× traffic, and how would you fix it?"
