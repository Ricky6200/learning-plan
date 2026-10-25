# 🤖 AI Engineering · Week 15 — Agents II: LangGraph and the CareerPilot Boss

> 📅 **Mon 01 Feb 2027 → Sun 07 Feb 2027** · Season 3 — Spring Citadel · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 14](Week-14.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-15.md) · [Week 16 →](Week-16.md)

**Why this week:** LangGraph is the most requested agent framework in 2026 job descriptions. Its typed state, persistence and human-in-the-loop features fix exactly what your scratch agent struggled with, and the season ends with a timed CareerPilot build.

## 🗓️ Sessions

### Monday 01 Feb · 45 min — LangGraph state, nodes and edges
- 📚 **Learn:** A graph is typed state (a `TypedDict` from W3, or pydantic) + nodes (functions returning state updates) + edges; reducers such as `add_messages` are attached with `Annotated`; `START` and `END`; compile, then invoke or stream. Read: [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph). Optional: [LangChain Academy: Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) Module 1, lessons 1-4.
- 🛠️ **Do:** Build a 3-node graph `parse_jd -> gap_analysis -> summarize` reusing your W7 parser and W14 gap tool; state holds `jd_text`, `job`, `gaps`, `summary`. Print updates with `graph.stream(..., stream_mode='updates')`. Done when: one JD flows through all nodes and you can point to each state update.

### Tuesday 02 Feb · 45 min — Conditional routing, ToolNode and prebuilt agents
- 📚 **Learn:** `add_conditional_edges` with routing functions, `ToolNode` executing tool calls, recursion limits, `Command` for update + goto; LangChain 1.x `create_agent` is a prebuilt agent built on LangGraph. Read: [Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api) (conditional edges, Command). Optional: [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents).
- 🛠️ **Do:** Rebuild the W14 agent as a graph: an `agent` node (model with tools bound) and a `ToolNode`, with a conditional edge that loops to tools while the last message has tool calls. Add a router sending chit-chat straight to `END`. Done when: your 8 W14 scenarios pass at least as often as before.

### Thursday 04 Feb · 45 min — Checkpointers, persistence, memory and streaming
- 📚 **Learn:** Checkpointers save state per `thread_id` (InMemorySaver for tests, SqliteSaver or PostgresSaver for real use), resume conversations, inspect history and time-travel; stores hold long-term memory; stream modes `updates`, `messages`, `values`. Read: [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence). Optional: [Streaming](https://docs.langchain.com/oss/python/langgraph/streaming).
- 🛠️ **Do:** Add `SqliteSaver` (package `langgraph-checkpoint-sqlite`) so CareerPilot resumes conversations per `thread_id` after a restart, and stream LLM tokens with `stream_mode='messages'`. Inspect `get_state_history` and replay from an earlier checkpoint. Done when: a restarted app continues the same thread and you demo one time-travel replay.

### Friday 05 Feb · 45 min — Human-in-the-loop interrupts and subgraphs
- 📚 **Learn:** `interrupt()` pauses a node and surfaces a payload; resume with `Command(resume=...)`; approve, edit and reject patterns; interrupts require a checkpointer; subgraphs package a feature as a reusable graph. Read: [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts). Optional: [Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs).
- 🛠️ **Do:** Add an `approve_plan` node calling `interrupt({'plan': plan})`; the CLI shows the plan, accepts approve/edit/reject and resumes with `Command(resume=...)`. Move gap analysis into a subgraph. Commit the result as the skeleton for Saturday. Done when: reject regenerates, edit uses your text, approve saves the plan, and all of it survives a restart.

### Saturday 06 Feb · 45 min — BOSS BATTLE: CareerPilot v0 graph in 45 minutes
- 📚 **Learn:** Rules: 45-minute timer, start from Friday's skeleton, docs allowed, no AI code generation, commit every 15 minutes. Rubric /100: complete flow (parse -> gap subgraph -> draft plan -> approval -> save) 30, interrupt and resume 25, persistence across restarts 20, 3 tests 15, README 10. Optional (Hindi): [CampusX Agentic AI using LangGraph](https://www.youtube.com/playlist?list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL).
- 🛠️ **Do:** Ship CareerPilot v0: `parse_jd -> gap_analysis (subgraph) -> draft_plan -> approve_plan (interrupt) -> save`, with SqliteSaver persistence and streaming output, run on 3 real JDs; add 3 tests (graph compiles, interrupt payload, resume saves). Done when: the rubric score is 80+, 3 JDs produce approved plans and tag `v0.1-careerpilot` is pushed.

## 📦 Deliverable (by Saturday night)
`10-careerpilot/` v0.1 on LangGraph: typed state, conditional routing, ToolNode loop, SQLite persistence, interrupt-based approval and a subgraph (boss tag `v0.1-careerpilot`).

## ✅ Self-check (Sunday test preview)
- What problems does LangGraph solve compared with a hand-written while-loop agent?
- What is a reducer in LangGraph state, and why does `add_messages` exist?
- How does a checkpointer enable both memory and human-in-the-loop?
- Explain `interrupt()` and `Command(resume=...)` with an example.
- When would you use a subgraph?
- Which streaming modes exist, and when do you use each?

## 🚀 Stretch (optional)
Expose `POST /runs` and `POST /runs/{id}/resume` in FastAPI with Langfuse tracing, or finish Academy Module 4 and add a parallel fan-out that researches two companies at once.
