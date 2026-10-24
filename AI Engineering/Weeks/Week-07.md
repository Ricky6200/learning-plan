# 🤖 AI Engineering · Week 07 — RAG I: DocuMind v0 From Scratch

> 📅 **Mon 07 Dec 2026 → Sun 13 Dec 2026** · Season 2 — Concurrency Crucible  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 06](Week-06.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-07.md) · [Week 08 →](Week-08.md)

**Why this week:** RAG is the most widely deployed GenAI pattern in Indian product and service companies. Building it from scratch first means you can debug any framework later.

## 🗓️ Sessions

### Monday 07 Dec · 45 min — RAG architecture and document ingestion
- 📚 **Learn:** Why RAG (fresh/private knowledge, citations, access control) vs fine-tuning; pipeline: load, clean, chunk, embed, index, retrieve, assemble prompt, generate, cite. PDF pitfalls: headers, tables, scanned pages. Read: [LangChain retrieval concepts](https://docs.langchain.com/oss/python/deepagents/retrieval) (2-step vs agentic RAG) and [pymupdf4llm](https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/).
- 🛠️ **Do:** Create `06-documind`. Collect 5-10 PDFs you care about (Spring/Java docs, public HR policies, RBI FAQs). Write `load.py` converting each PDF to clean Markdown with page markers (pymupdf4llm or Docling) and stripping repeated headers/footers. Done when: every PDF becomes a `.md` with page markers and a spot check shows headings and tables survived.

### Tuesday 08 Dec · 45 min — Chunking strategies and chunk metadata
- 📚 **Learn:** Fixed-size with overlap, recursive by separators, structure-aware (Markdown headings), semantic chunking, parent-child; chunk size vs recall vs context cost; keep metadata (source, page, heading). Read: [LangChain text splitters](https://docs.langchain.com/oss/python/integrations/splitters); skim chunking notebooks in [RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques).
- 🛠️ **Do:** Implement two chunkers yourself: fixed 800 characters with 100 overlap, and heading-aware (split on Markdown headings, then cap size). Store chunks with `{doc, page, heading, chunk_id}` and print stats (count, average tokens). Done when: both run on your corpus and you can show one example where heading-aware chunks read better.

### Thursday 10 Dec · 45 min — Retrieval and grounded prompts with citations
- 📚 **Learn:** Top-k retrieval, similarity thresholds, de-duplication, context ordering (lost in the middle), grounding prompt rules: answer only from sources, cite [doc:page], say 'I don't know'. Read: [Lost in the Middle](https://arxiv.org/abs/2307.03172) (abstract + figures) and the original [RAG paper](https://arxiv.org/abs/2005.11401) (abstract).
- 🛠️ **Do:** Index chunks in pgvector (reuse W6 code). Write `ask(question)`: embed, retrieve top-5, build a prompt with numbered sources, generate an answer with citations, print sources. Test 10 questions including 2 that the documents cannot answer. Done when: answers cite real pages and both unanswerable questions return 'I don't know'.

### Friday 11 Dec · 45 min — LangChain 1.x equivalent and LlamaIndex awareness
- 📚 **Learn:** Framework building blocks: document loaders, text splitters, embeddings, vector stores, retrievers; frameworks help with integrations but hide prompts. LlamaIndex is a data-centric alternative. Follow the [LangChain semantic search tutorial](https://docs.langchain.com/oss/python/langchain/knowledge-base); watch [RAG From Scratch](https://www.youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x) videos 1-4 (about 20 min).
- 🛠️ **Do:** Re-implement the pipeline with LangChain 1.x: loader (or your Markdown), `RecursiveCharacterTextSplitter`, an embeddings class, a vector store (`langchain-postgres` PGVector or in-memory) and a retriever. Run the same 10 questions and diff answers with your scratch version. Done when: a table compares lines of code, answer quality and debuggability.

### Saturday 12 Dec · 45 min — BUILD: DocuMind v0, RAG over your PDFs
- 📚 **Learn:** Ship a minimal, honest product: ingest command, ask command, citations, refusal on low similarity, config for chunker/k/model. Hindi option: [CampusX Generative AI using LangChain](https://www.youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0) (RAG videos).
- 🛠️ **Do:** Package DocuMind v0: `documind ingest ./pdfs`, `documind ask '...'` and FastAPI `POST /ask` returning `{answer, citations[]}`. Add a similarity threshold for refusals and 5 pytest tests (chunker, prompt builder, refusal path). Done when: 8+ of 10 manual questions are correct with citations, tag `v0.1-documind` is pushed, and the README has an architecture diagram.

## 📦 Deliverable (by Saturday night)
`06-documind/` v0.1: PDF-to-Markdown ingestion, two chunkers, pgvector index, scratch and LangChain pipelines, CLI + `/ask` API with citations and refusals.

## ✅ Self-check (Sunday test preview)
- When would you choose RAG over fine-tuning, and when not?
- How do chunk size and overlap affect recall, precision and cost?
- What is the 'lost in the middle' effect and how do you mitigate it?
- How do you make the model cite sources and refuse when context is missing?
- Trade-offs of LangChain vs writing the RAG pipeline yourself?
- Which metadata would you store with each chunk, and why?

## 🚀 Stretch (optional)
Compare [Docling](https://github.com/docling-project/docling) with pymupdf4llm on a table-heavy PDF and note which preserves tables better.
