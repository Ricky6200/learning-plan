# ☁️ Azure Cloud · Week 24 — Observability: OpenTelemetry, Application Insights, KQL

> 📅 **Mon 05 Apr 2027 → Sun 11 Apr 2027** · Season 6 — Final Boss: The Offer  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 23](Week-23.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-24.md) · [Week 25 →](Week-25.md)

**Why this week:** If you can't trace a request across services, you can't run AI features in production. AI-200 tests OpenTelemetry tracing and KQL, and interviewers ask how you would debug a slow RAG answer end to end.

## 🗓️ Sessions

### Tuesday 06 Apr · 45 min — OpenTelemetry concepts + the Microsoft OpenTelemetry Distro (Python)
- 📚 **Learn:** Traces, spans, attributes, metrics, logs, context propagation (W3C traceparent); exporting to Application Insights with the Microsoft OpenTelemetry Distro (`uv pip install microsoft-opentelemetry`; the older `azure-monitor-opentelemetry` distro still works). Use [Enable OpenTelemetry in Application Insights](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-enable?tabs=python), Learn's [Instrument an app with OpenTelemetry](https://learn.microsoft.com/en-us/training/modules/instrument-app-opentelemetry/) and the [OpenTelemetry Python docs](https://opentelemetry.io/docs/languages/python/).
- 🛠️ **Do:** Create a workspace-based Application Insights resource. Instrument a small FastAPI service with the distro (connection string from an environment variable), add a custom span around a fake 'retrieve' step with attributes (k, source) and a counter metric. Generate 50 requests and find them in Transaction search. Done when: spans with your attributes are visible and a screenshot is in `w24/`.

### Wednesday 07 Apr · 45 min — Distributed tracing across services and messaging
- 📚 **Learn:** Propagating context across HTTP calls and Service Bus messages, Application Map, the end-to-end transaction view, sampling and cost, and the Application Insights Java agent for TicketVerse (Java track) for polyglot traces. Use [Add and modify OpenTelemetry](https://learn.microsoft.com/en-us/azure/azure-monitor/app/opentelemetry-add-modify), [Application Map](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-map) and the exercise in [Instrument an app with OpenTelemetry](https://learn.microsoft.com/en-us/training/modules/instrument-app-opentelemetry/).
- 🛠️ **Do:** Build service A (FastAPI) -> service B (FastAPI) -> Service Bus -> worker, all instrumented; propagate the trace context through the message's application properties. Inject a 2-second delay in B and find it in the end-to-end transaction view and on the Application Map. Done when: one trace showing all 4 hops, including the delayed span, is captured in `w24/`.

### Friday 09 Apr · 45 min — KQL for logs and metrics: requests, dependencies, exceptions
- 📚 **Learn:** KQL over Application Insights data (requests, dependencies, exceptions, traces; AppRequests and friends in the workspace), where/project/extend/summarize/percentiles/bin/join/render, log search alerts on failures. Use the [KQL quick reference](https://learn.microsoft.com/en-us/kusto/query/kql-quick-reference), [Learn common KQL operators](https://learn.microsoft.com/en-us/kusto/query/tutorials/learn-common-operators) and Learn's [Analyze app telemetry with logs and metrics](https://learn.microsoft.com/en-us/training/modules/analyze-telemetry-logs-metrics/).
- 🛠️ **Do:** Write 6 KQL queries in `w24/kql.md`: p50/p95 latency per operation, failure rate per 5 minutes (render a timechart), slowest dependencies, top exceptions with counts, requests joined to their dependencies by operation ID, and filtering on your custom span attribute. Turn the failure-rate query into a log search alert. Done when: 6 queries with results and an alert rule are committed.

### Saturday 10 Apr · 60 min — LAB: Troubleshoot Container Apps from logs, events and KQL
- 📚 **Learn:** The exercises in Learn's [Manage containers in Azure Container Apps](https://learn.microsoft.com/en-us/training/modules/manage-containers-azure-container-apps/) ('Diagnose and fix a failing deployment') and [Analyze app telemetry with logs and metrics](https://learn.microsoft.com/en-us/training/modules/analyze-telemetry-logs-metrics/) ('Query logs with KQL'), plus [Troubleshooting in Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/troubleshooting).
- 🛠️ **Do:** Do the 'Diagnose and fix a failing deployment' exercise (~30 min). Then run a 20-minute self-made incident: deploy a revision with a bad environment variable and a failing probe, diagnose it only from the log stream, system logs and KQL (`ContainerAppConsoleLogs_CL`, `ContainerAppSystemLogs_CL`), fix it and write a 5-line postmortem. Delete the RG. Done when: exercise done, postmortem committed and the RG deleted.

## 📦 Deliverable (by Saturday night)
`w24/` instrumented services with custom spans, a 4-hop distributed trace, 6 KQL queries + an alert, and the Container Apps incident postmortem.

## ✅ Self-check (Sunday test preview)
- Trace vs span vs metric vs log: what is each for when debugging a slow RAG answer?
- How does trace context travel across an HTTP call and across a Service Bus message?
- What does sampling do to your bill and to what you can see?
- Write KQL for the p95 latency of each operation over the last hour.
- Why did Application Insights move from its classic SDKs to OpenTelemetry-based distros?
- Where do you look first when a container app revision fails to start?

## 🚀 Stretch (optional)
Watch the official [AI-200 exam prep 4 of 4 (secure, monitor, troubleshoot)](https://www.youtube.com/watch?v=K2F1uvc8Cr8) and attach the Application Insights Java agent to TicketVerse.
