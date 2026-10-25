# 🤖 AI Engineering · Week 10 — RAG I: DocuMind v0 From Scratch

> 📅 **Mon 28 Dec 2026 → Sun 03 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 09](Week-09.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-10.md) · [Week 11 →](Week-11.md)

**Why this week:** RAG is the most widely deployed GenAI pattern in Indian product and service companies. Building it from scratch first means you can debug any framework later. (Fri 1 Jan is New Year's Day: a light session.)

## 🗓️ Sessions

### Monday 28 Dec · 45 min — RAG architecture and document ingestion
- 📚 **Learn:** Why RAG (fresh or private knowledge, citations, access control) vs fine-tuning; the pipeline: load, clean, chunk, embed, index, retrieve, assemble prompt, generate, cite; 2-step RAG vs agentic RAG. PDF pitfalls: headers, tables, scanned pages. Read: [LangChain retrieval concepts](https://docs.langchain.com/oss/python/deepagents/retrieval) (about 10 min). Optional: [pymupdf4llm](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/).
- 🛠️ **Do:** Create `09-documind`. Collect 5-10 public PDFs you care about (Spring/Java docs, public HR policies, RBI FAQs). Write `load.py` converting each PDF to clean Markdown with page markers (pymupdf4llm) and stripping repeated headers/footers. Done when: every PDF becomes a `.md` with page markers and a spot check shows headings and tables survived.

### Tuesday 29 Dec · 45 min — Chunking strategies and chunk metadata
- 📚 **Learn:** Fixed-size with overlap, recursive by separators, structure-aware (Markdown headings), semantic chunking, parent-child; chunk size vs recall vs context cost; keep metadata (source, page, heading). Read: [LangChain text splitters](https://docs.langchain.com/oss/python/integrations/splitters). Optional: the chunking notebooks in [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques).
- 🛠️ **Do:** Implement two chunkers yourself: fixed 800 characters with 100 overlap, and heading-aware (split on Markdown headings, then cap size). Store chunks with `{doc, page, heading, chunk_id}` and print stats (count, average tokens). Done when: both run on your corpus and you can show one example where heading-aware chunks read better.

### Thursday 31 Dec · 45 min — Retrieval and grounded prompts with citations
- 📚 **Learn:** Top-k retrieval, similarity thresholds, de-duplication, context ordering (lost in the middle), grounding prompt rules: answer only from sources, cite [doc:page], say 'I don't know'. Read: [Lost in the Middle](https://arxiv.org/abs/2307.03172) (abstract + figures). Optional: the original [RAG paper](https://arxiv.org/abs/2005.11401) (abstract).
- 🛠️ **Do:** Index chunks in pgvector (reuse W9 code). Write `ask(question)`: embed, retrieve top-5, build a prompt with numbered sources, generate an answer with citations, print sources. Test 10 questions including 2 that the documents cannot answer. Done when: answers cite real pages and both unanswerable questions return 'I don't know'.

### Friday 01 Jan · 45 min — LangChain 1.x equivalent (light)
- 📚 **Learn:** Framework building blocks: document loaders, text splitters, embeddings, vector stores, retrievers; frameworks speed up integrations but hide prompts. LlamaIndex is a data-centric alternative. Read: [LangChain semantic search tutorial](https://docs.langchain.com/oss/python/langchain/knowledge-base) (skim the code). Optional: [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) videos 1-4.
- 🛠️ **Do:** New Year's Day, so 20 minutes: rebuild retrieval with LangChain 1.x (`RecursiveCharacterTextSplitter`, an embeddings class, `InMemoryVectorStore`, a retriever) and run 5 of your questions. Done when: a short table compares lines of code, answer quality and debuggability with your scratch version.

### Saturday 02 Jan · 45 min — BUILD: DocuMind v0, RAG over your PDFs
- 📚 **Learn:** Ship a minimal, honest product: ingest command, ask command, citations, refusal on low similarity, config for chunker/k/model. Optional (Hindi): [CampusX Generative AI using LangChain](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) (RAG videos).
- 🛠️ **Do:** Package DocuMind v0: `documind ingest ./pdfs`, `documind ask '...'` and FastAPI `POST /ask` returning `{answer, citations[]}`. Add a similarity threshold for refusals and 5 pytest tests (chunker, prompt builder, refusal path). Done when: 8+ of 10 manual questions are correct with citations, tag `v0.1-documind` is pushed, and the README has an architecture diagram.

## 📦 Deliverable (by Saturday night)
`09-documind/` v0.1: PDF-to-Markdown ingestion, two chunkers, pgvector index, scratch and LangChain pipelines, CLI + `/ask` API with citations and refusals.

## ✅ Self-check (Sunday test preview)
- When would you choose RAG over fine-tuning, and when not?
- How do chunk size and overlap affect recall, precision and cost?
- What is the 'lost in the middle' effect and how do you mitigate it?
- How do you make the model cite sources and refuse when context is missing?
- Trade-offs of LangChain vs writing the RAG pipeline yourself?
- Which metadata would you store with each chunk, and why?

## 🚀 Stretch (optional)
Finish the LangChain version with `langchain-postgres` and all 10 questions, or compare [Docling](https://github.com/docling-project/docling) with pymupdf4llm on a table-heavy PDF.
