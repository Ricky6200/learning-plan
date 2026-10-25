# 🤖 AI Engineering · Week 16 — MCP: Build the CareerPilot MCP Server

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** MCP is the standard plug for connecting AI apps to tools and data; IDEs, agent frameworks and clouds all speak it. Building and securing servers is a standout, very current skill. (AZ-104 exam week: Friday and Saturday are deliberately lighter.)

## 🗓️ Sessions

### Monday 08 Feb · 45 min — Why MCP: hosts, clients, servers and primitives
- 📚 **Learn:** The M x N integration problem; host, client and server roles; server primitives: tools (model-controlled), resources (application-controlled data), prompts (user-controlled templates); client features such as sampling, elicitation and roots. Read: [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture). Optional (Hindi): [CampusX MCP playlist](https://www.youtube.com/playlist?list=PLKnIA16_Rmva_oZ9F4ayUu9qcWgF7Fyc0).
- 🛠️ **Do:** Write `mcp_design.md` for CareerPilot: which features become tools (add_application, update_status, list_applications, search_jobs), resources (`applications://all`, `profile://me`) and prompts (`interview_prep`). Mark which actions need human confirmation and why. Done when: the design lists 4+ tools, 2 resources and 1 prompt with risk levels.

### Tuesday 09 Feb · 45 min — Transports, the 2026-07-28 revision and auth basics
- 📚 **Learn:** stdio (local subprocess) vs Streamable HTTP (remote); JSON-RPC messages; revision 2026-07-28 made MCP stateless (no initialize handshake or sessions, `server/discover`, multi-round-trip requests). OAuth primer: an authorization server issues access tokens; your remote MCP server only checks the bearer token on each request (you build this in W29). Read: [Key changes in 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/changelog). Optional: [Transports](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index).
- 🛠️ **Do:** Add `mcp[cli]` with uv in a separate project `10-careerpilot/mcp_server/`, create the 15-line `MCPServer` demo from the [Python SDK README](https://github.com/modelcontextprotocol/python-sdk), open it with `uv run mcp dev server.py` (MCP Inspector), call the tool and read the resource. Then serve it with `mcp.run(transport='streamable-http')`. Done when: the Inspector lists tools and resources and the `/mcp` HTTP endpoint answers.

### Thursday 11 Feb · 45 min — Build the CareerPilot MCP server with Python SDK v2
- 📚 **Learn:** SDK v2 `MCPServer` (formerly FastMCP; import from `mcp.server`): `@mcp.tool()`, `@mcp.resource()`, `@mcp.prompt()` (decorators, W3), type hints become JSON Schema, structured results, a `ctx: Context` parameter for logging and progress; keep tools small and safe. Read: [Python SDK docs](https://py.sdk.modelcontextprotocol.io/). Optional: [What's new in v2](https://py.sdk.modelcontextprotocol.io/whats-new/).
- 🛠️ **Do:** Implement `careerpilot-mcp` over your SQLite tracker: tools `add_application`, `update_status`, `list_applications(status)`, `search_jobs(query)`; resource `profile://me`; prompt `interview_prep(company, role)`. Validate inputs with pydantic and return structured results. Done when: everything works in MCP Inspector and invalid status values are rejected with clear errors.

### Friday 12 Feb · 45 min — Connect a client and study MCP security risks (light)
- 📚 **Learn:** Clients: VS Code (Copilot agent mode via `.vscode/mcp.json`) and, next week, your LangGraph agent. Note: `langchain-mcp-adapters` 0.3.2 still requires `mcp<2`, so keep the server in its own uv project and wrap the v2 `Client` tools yourself. Risks: tool poisoning, injection through tool results, over-permissioned tools, token passthrough, confused deputy. Read: [MCP security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices). Optional: [VS Code MCP servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers).
- 🛠️ **Do:** AZ-104 week, so 25 minutes: register `careerpilot-mcp` in `.vscode/mcp.json` and ask Copilot Chat to add an application, then add 4 risks with your mitigations to `mcp_design.md`. Done when: Copilot Chat calls your tool successfully and the 4 risks are committed.

### Saturday 13 Feb · 45 min — BUILD: CareerPilot MCP server with client tests
- 📚 **Learn:** Test MCP servers with the in-memory `Client` bound to the server object (no transport), plus contract tests for tool schemas and error cases. A2A (agent-to-agent protocol) complements MCP for agent-to-agent calls. Read: [SDK testing guide](https://py.sdk.modelcontextprotocol.io/get-started/testing/). Optional: [A2A and MCP](https://a2a-protocol.org/latest/topics/a2a-and-mcp/).
- 🛠️ **Do:** Ship `careerpilot-mcp` v1: stdio and Streamable HTTP modes, confirmation required for destructive actions (an explicit `confirm=true` argument), 6 pytest tests using the in-memory `Client`, and a README with the VS Code config. Done when: tests pass and tag `v1.0-careerpilot-mcp` is pushed (the demo recording can wait for the stretch).

## 📦 Deliverable (by Saturday night)
`10-careerpilot/mcp_server/` v1.0 (its own uv project): tools, resources and a prompt; stdio + Streamable HTTP; confirmations for risky actions; 6+ in-memory client tests; VS Code integration; security notes.

## ✅ Self-check (Sunday test preview)
- Explain MCP host, client and server with a concrete example.
- Tools vs resources vs prompts: who controls each?
- stdio vs Streamable HTTP: when do you use each?
- What is tool poisoning and how do you defend against it?
- What changed in MCP revision 2026-07-28, and why does statelessness help scaling?
- Why does the MCP server live in its own uv project in this plan?
- How does A2A differ from MCP?

## 🚀 Stretch (optional)
Record a 2-minute VS Code demo, add 2 more tests, or wrap a public jobs API (e.g., [Arbeitnow job board API](https://www.arbeitnow.com/api/job-board-api)) as a second MCP server.
