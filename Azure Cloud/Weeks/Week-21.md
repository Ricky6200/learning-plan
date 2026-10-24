# ☁️ Azure Cloud · Week 21 — Azure Functions: serverless APIs and event handlers

> 📅 **Mon 15 Mar 2027 → Sun 21 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 20](Week-20.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-21.md) · [Week 22 →](Week-22.md)

**Why this week:** Functions are the glue of event-driven AI backends - HTTP APIs, queue workers and timers without managing servers. AI-200 tests triggers, bindings, configuration and deployment, and interviewers love 'cold start vs scale' trade-offs.

## 🗓️ Sessions

### Tuesday 16 Mar · 45 min — Functions concepts, hosting plans and the Python v2 model
- 📚 **Learn:** Triggers vs input/output bindings, the Python v2 decorator programming model, hosting options (Flex Consumption is recommended for new serverless apps; Premium; Dedicated; Container Apps; Consumption is legacy and retired on Linux), scaling and cold starts. Use [Triggers and bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings), [Hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale) and the [Flex Consumption plan](https://learn.microsoft.com/en-us/azure/azure-functions/flex-consumption-plan).
- 🛠️ **Do:** Make `w21/hosting.md` comparing Flex Consumption, Premium, Dedicated and Container Apps on scale to zero, cold start, VNet support, max scale and billing. Choose a plan for (a) a spiky public API, (b) a 20-minute nightly batch, (c) a private API behind a VNet. Install Functions Core Tools 4.x and run `func --version`. Done when: the table + 3 choices are committed and Core Tools works.

### Wednesday 17 Mar · 45 min — Build locally: HTTP trigger, Service Bus trigger, output binding
- 📚 **Learn:** Core Tools workflow (`func init`, `func new`, `func start`, local.settings.json), HTTP trigger, Service Bus trigger, Cosmos DB output binding, identity-based connections. Use the [Python developer reference](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python), [Develop locally with Core Tools](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local) and [Service Bus bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-service-bus).
- 🛠️ **Do:** Create a Python v2 function app with `POST /jobs` (HTTP trigger) that validates JSON and sends it to the `embed-jobs` queue through an output binding, plus a Service Bus-triggered function that processes each job and writes a result document to Cosmos DB (output binding). Run it locally against your Azure resources. Done when: one HTTP call produces one Cosmos document, shown in `w21/`.

### Friday 19 Mar · 45 min — Configure and deploy: settings, identity, Durable Functions awareness
- 📚 **Learn:** Deployment (`func azure functionapp publish`, zip deploy), app settings and Key Vault references, managed identity with identity-based connections instead of connection strings, host.json basics, Durable Functions (orchestrator, activities, fan-out/fan-in). Use [Create a function app from the command line](https://learn.microsoft.com/en-us/azure/azure-functions/how-to-create-function-azure-cli?pivots=programming-language-python), [Deployment technologies](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies) and the [Durable Functions overview](https://learn.microsoft.com/en-us/azure/durable-task/durable-functions/durable-functions-overview).
- 🛠️ **Do:** Create a Flex Consumption function app with a system-assigned managed identity, grant it Service Bus and Cosmos DB data roles, replace connection strings with identity-based settings (e.g., `ServiceBusConnection__fullyQualifiedNamespace`), deploy Wednesday's app and test it end to end. Sketch a Durable fan-out/fan-in flow that summarizes 10 documents. Done when: the deployed app works with zero secrets in app settings and the sketch is in `w21/`.

### Saturday 20 Mar · 60 min — LAB: Serverless AI backend - an MCP server on Azure Functions
- 📚 **Learn:** The exercise in Learn's [Build serverless AI backends with Azure Functions](https://learn.microsoft.com/en-us/training/modules/build-backends-azure-functions/) ('Create an MCP server with Azure Functions') - it ties directly to the MCP servers you build in the AI track. Quick plan comparison: [Should I pick Flex Consumption?](https://www.youtube.com/watch?v=9_9O3ma2sU0).
- 🛠️ **Do:** Complete the MCP-server exercise (~25 min). Then add one tool that reads TicketVerse events from Cosmos DB (input binding or SDK) and call it from the MCP client you use in the AI track. Check Application Insights for the invocation traces. Delete the RG. Done when: the tool answers from your client, traces are visible and the RG is deleted.

## 📦 Deliverable (by Saturday night)
`w21/` hosting comparison, a local function app (HTTP -> queue -> Cosmos), a deployed Flex Consumption app using identity-based connections, and the MCP-server exercise with your extra tool.

## ✅ Self-check (Sunday test preview)
- Trigger vs binding: name one input and one output binding you would use in an AI backend.
- Why is Flex Consumption the default for new serverless apps, and what changed for Linux Consumption?
- How do identity-based connections remove secrets from Functions app settings?
- What causes cold starts, and how can you reduce them?
- When would you choose Durable Functions over chaining queues?
- How do you run and debug a Service Bus-triggered function locally?

## 🚀 Stretch (optional)
Do the Durable Functions exercise in Learn's [Orchestrate durable AI workflows with Azure Durable Functions](https://learn.microsoft.com/en-us/training/modules/orchestrate-durable-functions/).
