# 🤖 AI Engineering · Week 12 — Agents II: LangGraph and CareerPilot v0

> 📅 **Mon 11 Jan 2027 → Sun 17 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 11](Week-11.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-12.md) · [Week 13 →](Week-13.md)

**Why this week:** LangGraph is the most requested agent framework in 2026 job descriptions. Its typed state, persistence and human-in-the-loop features fix exactly what your scratch agent struggled with.

## 🗓️ Sessions

### Monday 11 Jan · 45 min — LangGraph state, nodes and edges
- 📚 **Learn:** A graph is typed state (TypedDict or pydantic) + nodes (functions returning state updates) + edges; reducers such as `add_messages`; `START` and `END`; compile, then invoke or stream. Read: [Thinking in LangGraph](https://docs.langchain.com/oss/python/langgraph/thinking-in-langgraph); course: [LangChain Academy: Introduction to LangGraph](https://academy.langchain.com/courses/intro-to-langgraph) Module 1, lessons 1-4.
- 🛠️ **Do:** Build a 3-node graph `parse_jd -> gap_analysis -> summarize` reusing your W5 parser and W11 gap tool; state holds `jd_text`, `job`, `gaps`, `summary`. Print updates with `graph.stream(..., stream_mode='updates')`. Done when: one JD flows through all nodes and you can point to each state update.

### Tuesday 12 Jan · 45 min — Conditional routing, ToolNode and prebuilt agents
- 📚 **Learn:** `add_conditional_edges` with routing functions, `ToolNode` executing tool calls, recursion limits, `Command` for update + goto; LangChain 1.x `create_agent` is a prebuilt agent built on LangGraph. Read: [Graph API overview](https://docs.langchain.com/oss/python/langgraph/graph-api) (conditional edges, Command) and [LangChain agents](https://docs.langchain.com/oss/python/langchain/agents); Academy Module 1, lessons 5-6.
- 🛠️ **Do:** Rebuild the W11 agent as a graph: `agent` node (model with tools bound) and a `ToolNode`, with a conditional edge that loops to tools while the last message has tool calls. Add a router sending chit-chat straight to `END`. Done when: your 8 W11 scenarios pass at least as often as before.

### Thursday 14 Jan · 45 min — Checkpointers, persistence, memory and streaming
- 📚 **Learn:** Checkpointers save state per `thread_id` (InMemorySaver for tests, SqliteSaver/PostgresSaver for real use), resume conversations, inspect history and time-travel; stores for long-term memory; stream modes `updates`, `messages`, `values`. Read: [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) and [Streaming](https://docs.langchain.com/oss/python/langgraph/streaming); Academy Module 2.
- 🛠️ **Do:** Add `SqliteSaver` (package `langgraph-checkpoint-sqlite`) so CareerPilot resumes conversations per `thread_id` after a restart, and stream LLM tokens with `stream_mode='messages'`. Inspect `get_state_history` and replay from an earlier checkpoint. Done when: a restarted app continues the same thread and you demo one time-travel replay.

### Friday 15 Jan · 45 min — Human-in-the-loop interrupts and subgraphs
- 📚 **Learn:** `interrupt()` pauses a node and surfaces a payload; resume with `Command(resume=...)`; approve, edit and reject patterns; interrupts require a checkpointer; subgraphs compose features or teams. Read: [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) and [Subgraphs](https://docs.langchain.com/oss/python/langgraph/use-subgraphs); Academy Module 3 (breakpoints, human feedback).
- 🛠️ **Do:** Add an `approve_plan` node calling `interrupt({'plan': plan})`. The CLI shows the plan, accepts approve/edit/reject and resumes with `Command(resume=...)`. Move gap analysis into a subgraph. Done when: reject regenerates, edit uses your text, approve saves the plan, and all of it survives a restart.

### Saturday 16 Jan · 45 min — BUILD: CareerPilot v0 graph with human approval
- 📚 **Learn:** Product slice: input a JD, output an approved 2-week prep plan saved to your tracker; deterministic steps as plain nodes, LLM calls only where judgement is needed. Hindi option: [CampusX Agentic AI using LangGraph](https://www.youtube.com/playlist?list=PLKnIA16_RmvYsvB8qkUQuJmJNuiCUJFPL).
- 🛠️ **Do:** Ship CareerPilot v0: `parse_jd -> gap_analysis (subgraph) -> draft_plan -> approve_plan (interrupt) -> save`, SqliteSaver persistence, streaming output and Langfuse tracing. Expose `POST /runs` and `POST /runs/{id}/resume` in FastAPI. Done when: 3 real JDs produce approved plans, traces appear in Langfuse and tag `v0.1-careerpilot` is pushed.

## 📦 Deliverable (by Saturday night)
`07-careerpilot/` v0.1 on LangGraph: typed state, conditional routing, ToolNode loop, SQLite persistence, interrupt-based approval, a subgraph, FastAPI run/resume endpoints and Langfuse traces.

## ✅ Self-check (Sunday test preview)
- What problems does LangGraph solve compared with a hand-written while-loop agent?
- What is a reducer in LangGraph state, and why does `add_messages` exist?
- How does a checkpointer enable both memory and human-in-the-loop?
- Explain `interrupt()` and `Command(resume=...)` with an example.
- When would you use a subgraph?
- Which streaming modes exist, and when do you use each?

## 🚀 Stretch (optional)
Finish Academy Module 4 and add a parallel fan-out that researches two companies at once with a map-reduce step.
