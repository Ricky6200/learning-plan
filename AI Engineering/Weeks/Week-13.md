# 🤖 AI Engineering · Week 13 — MCP: Build the CareerPilot MCP Server

> 📅 **Mon 18 Jan 2027 → Sun 24 Jan 2027** · Season 3 — Spring Citadel  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 12](Week-12.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-13.md) · [Week 14 →](Week-14.md)

**Why this week:** MCP is the standard plug for connecting AI apps to tools and data; IDEs, agent frameworks and clouds all speak it. Building and securing servers is a standout, very current skill.

## 🗓️ Sessions

### Monday 18 Jan · 45 min — Why MCP: hosts, clients, servers and primitives
- 📚 **Learn:** The M x N integration problem; host, client and server roles; server primitives: tools (model-controlled), resources (application-controlled data), prompts (user-controlled templates); client features such as sampling, elicitation and roots. Read: [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture) and [Server concepts](https://modelcontextprotocol.io/docs/learn/server-concepts); Hindi: [CampusX MCP playlist](https://www.youtube.com/playlist?list=PLKnIA16_Rmva_oZ9F4ayUu9qcWgF7Fyc0).
- 🛠️ **Do:** Write `mcp_design.md` for CareerPilot: which features become tools (add_application, update_status, list_applications, search_jobs), resources (`applications://all`, `profile://me`) and prompts (`interview_prep`). Mark which actions need human confirmation and why. Done when: the design lists 4+ tools, 2 resources and 1 prompt with risk levels.

### Tuesday 19 Jan · 45 min — Transports, the 2026-07-28 revision and auth basics
- 📚 **Learn:** stdio (local subprocess) vs Streamable HTTP (remote); JSON-RPC messages; revision 2026-07-28 made MCP stateless (no initialize handshake or sessions, `server/discover`, multi-round-trip requests); OAuth-based authorization for remote servers. Read: [Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index), [Key changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog), [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index) (overview).
- 🛠️ **Do:** Add `mcp[cli]` with uv, create the 15-line `MCPServer` demo from the [Python SDK README](https://github.com/modelcontextprotocol/python-sdk), open it with `uv run mcp dev server.py` (MCP Inspector), call the tool and read the resource. Then serve it with `--transport streamable-http`. Done when: the Inspector lists tools/resources and the `/mcp` HTTP endpoint answers.

### Thursday 21 Jan · 45 min — Build the CareerPilot MCP server with Python SDK v2
- 📚 **Learn:** SDK v2 `MCPServer` (formerly FastMCP; import from `mcp.server`): `@mcp.tool()`, `@mcp.resource()`, `@mcp.prompt()`, type hints become JSON Schema, structured results, a `Context` parameter for logging and progress; keep tools small and safe. Read: [Python SDK docs](https://py.sdk.modelcontextprotocol.io/) and [What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/).
- 🛠️ **Do:** Implement `careerpilot-mcp` over your SQLite tracker: tools `add_application`, `update_status`, `list_applications(status)`, `search_jobs(query)`; resource `profile://me`; prompt `interview_prep(company, role)`. Validate inputs with pydantic and return structured results. Done when: everything works in MCP Inspector and invalid status values are rejected with clear errors.

### Friday 22 Jan · 45 min — Connect clients and study MCP security risks
- 📚 **Learn:** Clients: VS Code (Copilot agent mode via `mcp.json`) and your LangGraph agent (LangChain MCP adapters). Risks: tool poisoning, prompt injection through tool results, over-permissioned tools, token passthrough, confused deputy; mitigations: allow-lists, least privilege, confirmations, pinned versions. Read: [VS Code MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers), [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices), [LangChain MCP](https://docs.langchain.com/oss/python/langchain/mcp).
- 🛠️ **Do:** Register `careerpilot-mcp` in `.vscode/mcp.json` and ask Copilot Chat to add an application; then load the same tools into CareerPilot via the MCP adapters. Create a test server with a poisoned tool description and observe behaviour. Done when: both clients call your tools and `mcp_design.md` lists 4 risks with your mitigations.

### Saturday 23 Jan · 45 min — BUILD: CareerPilot MCP server with client tests
- 📚 **Learn:** Test MCP servers with an in-memory `Client` bound to the server object (no transport), contract tests for tool schemas and error cases. A2A (agent-to-agent protocol) complements MCP for agent-to-agent calls. Read: [SDK testing guide](https://py.sdk.modelcontextprotocol.io/get-started/testing/) and [A2A and MCP](https://a2a-protocol.org/latest/topics/a2a-and-mcp/).
- 🛠️ **Do:** Ship `careerpilot-mcp` v1: stdio and Streamable HTTP modes, confirmation required for destructive actions (SDK elicitation or an explicit `confirm=true` argument), 8+ pytest tests using the in-memory `Client`, and README with VS Code config. Done when: tests pass, a VS Code + LangGraph demo is recorded and tag `v1.0-careerpilot-mcp` is pushed.

## 📦 Deliverable (by Saturday night)
`07-careerpilot/mcp_server/` v1.0: tools, resources and a prompt; stdio + Streamable HTTP; confirmations for risky actions; 8+ in-memory client tests; VS Code and LangGraph integration; security notes.

## ✅ Self-check (Sunday test preview)
- Explain MCP host, client and server with a concrete example.
- Tools vs resources vs prompts: who controls each?
- stdio vs Streamable HTTP: when do you use each?
- What is tool poisoning and how do you defend against it?
- What changed in MCP revision 2026-07-28, and why does statelessness help scaling?
- How does A2A differ from MCP?

## 🚀 Stretch (optional)
Wrap a public jobs API (e.g., [Arbeitnow job board API](https://www.arbeitnow.com/api/job-board-api)) as a second MCP server and let CareerPilot compose both servers.
