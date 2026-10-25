# 🤖 AI Engineering · Week 29 — Advanced RAG, MCP Auth and Catch-up

> 📅 **Mon 10 May 2027 → Sun 16 May 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 28](Week-28.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-29.md) · [Week 30 →](Week-30.md)

**Why this week:** Agentic and multi-hop RAG are the 2026 follow-up questions after 'how does your RAG work?', and remote MCP servers must be authorised before anyone trusts them. This buffer week also gives you protected time to close red items before the final week.

## 🗓️ Sessions

### Monday 10 May · 45 min — Agentic RAG in LangGraph: grade, rewrite, retry
- 📚 **Learn:** Agentic (corrective) RAG lets the graph judge its own retrieval: retrieve -> grade each chunk's relevance -> if weak, rewrite the query and retrieve again -> generate with citations; it raises accuracy on hard questions at the price of extra calls and latency, so cap the loops. Read: [LangGraph agentic RAG](https://docs.langchain.com/oss/python/langgraph/agentic-rag). Optional: [Corrective RAG paper](https://arxiv.org/abs/2401.15884) (abstract).
- 🛠️ **Do:** Build `09-documind/agentic.py`: your v1 hybrid retriever as a tool, a grading node (LLM yes/no relevance per chunk), a rewrite node limited to 2 loops, and generation with citations. Run the 10 hardest golden questions through it and through v1. Done when: a table compares accuracy, LLM calls and latency, and no question exceeds 2 rewrites.

### Tuesday 11 May · 45 min — Multi-hop questions: query decomposition
- 📚 **Learn:** A multi-hop question needs facts from two or more passages ('Which policy changed after the 2024 audit, and what does it now require?'). Decompose it into sub-questions, retrieve for each (in parallel or in sequence, feeding earlier answers forward), then compose one cited answer. Watch: [RAG from scratch: Part 7, decomposition](https://www.youtube.com/watch?v=h0OPWlEOank).
- 🛠️ **Do:** Add a `decompose` node to Monday's graph that splits multi-hop questions into at most 3 sub-questions and answers them in sequence. Run it on your multi-hop golden items (write 3 more if you have fewer than 5) and compare with Monday's results. Done when: a per-question table shows the effect of decomposition and you can name one question it still fails.

### Thursday 13 May · 45 min — MCP authorization: your server as an OAuth resource server
- 📚 **Learn:** Over Streamable HTTP an MCP server is a resource server: a `TokenVerifier.verify_token` returns an `AccessToken` (or None) for each bearer token; `MCPServer(..., token_verifier=..., auth=AuthSettings(issuer_url, resource_server_url, required_scopes))` then serves the discovery metadata and answers 401 to bad tokens, and `get_access_token()` tells a tool who is calling. stdio and the in-memory `Client` skip auth, so test over HTTP. Read: [SDK authorization](https://py.sdk.modelcontextprotocol.io/run/authorization/). Optional: [MCP authorization spec](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index).
- 🛠️ **Do:** Protect `careerpilot-mcp`'s HTTP mode with a static dev verifier (two tokens: `applications:read`, and read + write) and check the write scope inside `update_status` via `get_access_token()`. Write 3 tests over HTTP. Done when: no token gets 401, the read token can list but not update, and the read + write token can update.

### Friday 14 May · 45 min — Catch-up: close your red items
- 📚 **Learn:** Spaced repetition beats rereading: take the 3 reddest AI topics from `WEAKNESS_TRACKER.md` and your Sunday-test notes, reopen each original session's main resource for 5 minutes, then prove the idea with code rather than notes. Read: your own tracker and the matching week files.
- 🛠️ **Do:** Close 2-3 red items: for each, write a 5-line explanation in `learning-log.md` and add one runnable proof (a test, notebook cell or small script) to the relevant project. Done when: the tracker shows those items as amber or green with links to the proofs.

### Saturday 15 May · 45 min — BUILD: DocuMind v3.1 with agentic RAG behind a flag
- 📚 **Learn:** Release discipline for a risky feature: ship it behind a configuration flag, compare it with the default on the same golden set in CI (your W19 gate), and document when to turn it on. Read: your W19 `eval.yml` and `EVAL_REPORT.md`.
- 🛠️ **Do:** Add `retriever_mode = classic | agentic` to DocuMind's settings, run both modes through the eval gate, and update `EVAL_REPORT.md` with accuracy, cost and latency for each plus a recommendation. Done when: CI is green for both modes, the report has the comparison and tag `v3.1-documind` is pushed.

## 📦 Deliverable (by Saturday night)
DocuMind v3.1 with agentic and multi-hop retrieval behind a flag (measured in CI), `careerpilot-mcp` protected with bearer tokens and scopes, and 2-3 closed weakness items with runnable proofs.

## ✅ Self-check (Sunday test preview)
- What does agentic (corrective) RAG add over two-step RAG, and what does it cost?
- How would you answer a multi-hop question with retrieval?
- How does an MCP server verify a bearer token, and what does the 401 response tell the client?
- Why are stdio servers and in-memory test clients not covered by MCP authorization?
- When would you keep an expensive feature behind a flag instead of making it the default?

## 🚀 Stretch (optional)
Replace the static verifier with JWT validation against a free identity provider or a local Keycloak, or add a text-to-SQL tool over the CareerPilot SQLite tracker with read-only credentials.
