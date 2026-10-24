# ☁️ Azure Cloud · Week 20 — Messaging with Service Bus and Event Grid

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Queues and events decouple slow AI work (embedding, summarizing, notifying) from user requests. Service Bus and Event Grid are a big part of AI-200's 'connect and consume' domain and the Azure counterparts of the Kafka patterns you build in the Java track.

## 🗓️ Sessions

### Tuesday 09 Mar · 45 min — Service Bus queues: peek-lock, settlement, dead-letter queue
- 📚 **Learn:** Namespaces and tiers (Basic supports queues only; Standard adds topics, sessions and duplicate detection), peek-lock vs receive-and-delete, complete/abandon/dead-letter/defer, lock renewal, max delivery count and the dead-letter queue. Use the [Service Bus overview](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-messaging-overview), the [Python queues quickstart](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-python-how-to-use-queues) and [Dead-letter queues](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues).
- 🛠️ **Do:** Create a Standard namespace and queue `embed-jobs` (max delivery count 3) and grant yourself the Azure Service Bus Data Owner role (keyless). In `py/sb_queue.py` send 10 JSON jobs with message IDs; a peek-lock receiver completes good jobs and abandons a 'poison' job until it lands in the DLQ. Read the DLQ and print the dead-letter reason. Done when: 9 completed and 1 dead-lettered with its reason, logged in `w20/`.

### Wednesday 10 Mar · 45 min — Topics, subscriptions, filters and sessions
- 📚 **Learn:** Topics and subscriptions (fan-out), SQL and correlation filters, rule actions, message sessions for ordered or grouped processing, duplicate detection. Use the [Python topics quickstart](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-python-how-to-use-topics-subscriptions), [Message sessions](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions) and Learn's [Queue and process AI operations with Azure Service Bus](https://learn.microsoft.com/en-us/training/modules/queue-process-operations-service-bus/).
- 🛠️ **Do:** Create topic `booking-events` with subscriptions `email` (all events), `analytics` (SQL filter `eventType = 'Cancelled'`) and `per-user` (sessions enabled, session ID = user ID). Publish 12 events for 3 users, verify each subscription's message count, and show that a session receiver processes one user's events in order. Done when: counts and ordered session output are committed in `w20/`.

### Friday 12 Mar · 45 min — Event Grid: custom events, filters, retries, dead-lettering
- 📚 **Learn:** Topics, event subscriptions and handlers, Event Grid vs CloudEvents schemas, subject and advanced filters, retries (exponential backoff for up to 24 hours by default), max delivery attempts, dead-lettering to blob; Event Hubs' Kafka endpoint (Standard tier and above). Use [Event filtering](https://learn.microsoft.com/en-us/azure/event-grid/event-filtering), [Delivery and retry](https://learn.microsoft.com/en-us/azure/event-grid/delivery-and-retry) and [Event Hubs for Apache Kafka](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview).
- 🛠️ **Do:** Create a custom topic and a subscription that delivers to a Storage queue, with an advanced filter (`data.priority` equals high) and a blob dead-letter container. Publish 10 events from Python and confirm only high-priority ones reach the queue. Then delete the queue, publish again and find the events in the dead-letter container. Done when: filter and dead-letter evidence are in `w20/`.

### Saturday 13 Mar · 60 min — LAB: Python producer/consumer with Service Bus + Event Grid
- 📚 **Learn:** The exercises in Learn's [Queue and process AI operations with Service Bus](https://learn.microsoft.com/en-us/training/modules/queue-process-operations-service-bus/) and [Develop event-driven AI workflows with Event Grid](https://learn.microsoft.com/en-us/training/modules/event-driven-workflows-event-grid/), plus the decision guide [Compare messaging services](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services).
- 🛠️ **Do:** Do the Service Bus exercise (~30 min). Then wire a mini pipeline: an 'upload' event published to Event Grid is routed to a Service Bus queue handler; a Python worker pulls it, 'summarizes' it (stub) and completes or dead-letters it. Draw the flow and write when you'd use Event Hubs (Kafka) instead. Delete the RG. Done when: the end-to-end log, diagram and RG deletion are in `w20/`.

## 📦 Deliverable (by Saturday night)
`w20/` DLQ evidence, topic/subscription/session results, Event Grid filter + dead-letter evidence, pipeline diagram and end-to-end log.

## ✅ Self-check (Sunday test preview)
- Peek-lock vs receive-and-delete: which can lose messages, and when?
- Name three reasons a Service Bus message is dead-lettered, and how you would reprocess it.
- When do you need sessions, and how do they guarantee ordering?
- Service Bus vs Event Grid vs Event Hubs: pick one for a command, a notification and a telemetry stream.
- How does Event Grid retry delivery, and what happens when retries or the time-to-live run out?
- Why are idempotent consumers essential with at-least-once delivery?

## 🚀 Stretch (optional)
Point a Kafka client from TicketVerse (Java track) at an Event Hubs Standard namespace's Kafka endpoint, or watch Microsoft Learn's [Event Grid module video](https://www.youtube.com/watch?v=-0GX-jciUDE).
