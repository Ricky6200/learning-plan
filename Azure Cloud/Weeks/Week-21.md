# ☁️ Azure Cloud · Week 21 — Azure Functions: serverless APIs and event handlers

> 📅 **Mon 15 Mar 2027 → Sun 21 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 20](Week-20.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-21.md) · [Week 22 →](Week-22.md)

**Why this week:** Functions are the glue of event-driven AI backends - HTTP APIs, queue workers and timers without managing servers. AI-200 tests triggers, bindings, configuration and deployment, and interviewers love 'cold start vs scale' trade-offs.

## 🗓️ Sessions

### Tuesday 16 Mar · 45 min — Functions concepts, hosting plans and the Python v2 model
- 📚 **Learn:** Triggers vs input/output bindings, the Python v2 decorator programming model, hosting options (Flex Consumption is recommended for new serverless apps; Premium; Dedicated; Container Apps; Consumption is legacy and retired on Linux), scaling and cold starts. Read [Hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale). Optional: the [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan).
- 🛠️ **Do:** Make `w21/hosting.md` comparing Flex Consumption, Premium, Dedicated and Container Apps on scale to zero, cold start, VNet support, max scale and billing. Choose a plan for (a) a spiky public API, (b) a 20-minute nightly batch, (c) a private API behind a VNet. Install Functions Core Tools 4.x on the personal laptop and run `func --version`. Done when: the table + 3 choices are committed and Core Tools works.

### Wednesday 17 Mar · 45 min — Build locally: HTTP trigger, Service Bus trigger, output binding
- 📚 **Learn:** Core Tools workflow (`func init`, `func new`, `func start`, local.settings.json), HTTP trigger, Service Bus trigger, Cosmos DB output binding, identity-based connections. Read [Develop locally with Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local). Optional: [Service Bus bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus).
- 🛠️ **Do:** Create a Python v2 function app with `POST /jobs` (HTTP trigger) that validates JSON and sends it to an `embed-jobs` queue (new Standard namespace) through an output binding, plus a Service Bus-triggered function that processes each job and writes a result document to your W17 Cosmos DB account (output binding). Run it locally against your Azure resources. Done when: one HTTP call produces one Cosmos document, shown in `w21/`.

### Friday 19 Mar · 45 min — Configure and deploy: settings, identity, deployment
- 📚 **Learn:** Deployment (`func azure functionapp publish`, zip deploy), app settings and Key Vault references, managed identity with identity-based connections instead of connection strings, host.json basics, and Durable Functions awareness (orchestrator, activities, fan-out/fan-in). Read [Create a function app from the command line](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-python). Optional: [Deployment technologies](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies).
- 🛠️ **Do:** Create a Flex Consumption function app with a system-assigned managed identity, grant it Service Bus and Cosmos DB data roles, replace connection strings with identity-based settings (e.g., `ServiceBusConnection__fullyQualifiedNamespace`), deploy Wednesday's app and test it end to end. Done when: the deployed app works with zero secrets in app settings and the settings list is captured in `w21/`.

### Saturday 20 Mar · 60 min — LAB: MCP server on Azure Functions + Application Insights
- 📚 **Learn:** The exercise in Learn's [Build serverless AI backends with Azure Functions](https://learn.microsoft.com/en-us/training/modules/build-backends-azure-functions/) ('Create an MCP server with Azure Functions'), tied to the MCP servers from AI W16. Application Insights primer: a workspace-based resource your app reports to through its connection string; Live Metrics shows requests as they happen; Transaction search finds one end-to-end trace. Optional: [Application Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview).
- 🛠️ **Do:** Complete the MCP-server exercise (~25 min). Then add one tool that reads TicketVerse events from your W17 Cosmos DB account (input binding or SDK) and call it from the MCP client you use in the AI track while watching Live Metrics; find that call's end-to-end trace in Transaction search. Delete the RG, the Service Bus namespace and the W17 Cosmos account. Done when: the tool answers from your client, the trace screenshot is committed and all three are deleted.

## 📦 Deliverable (by Saturday night)
`w21/` hosting comparison, a local function app (HTTP -> queue -> Cosmos), a deployed Flex Consumption app using identity-based connections, and the MCP-server exercise with your extra tool and its Application Insights trace.

## ✅ Self-check (Sunday test preview)
- Trigger vs binding: name one input and one output binding you would use in an AI backend.
- Why is Flex Consumption the default for new serverless apps, and what changed for Linux Consumption?
- How do identity-based connections remove secrets from Functions app settings?
- What causes cold starts, and how can you reduce them?
- When would you choose Durable Functions over chaining queues?
- Live Metrics vs Transaction search in Application Insights: what does each show you?
- How do you run and debug a Service Bus-triggered function locally?

## 🚀 Stretch (optional)
Sketch a Durable Functions fan-out/fan-in flow that summarizes 10 documents, then do the exercise in Learn's [Orchestrate durable AI workflows with Azure Durable Functions](https://learn.microsoft.com/en-us/training/modules/orchestrate-durable-functions/).
