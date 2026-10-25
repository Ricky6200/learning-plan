# ☁️ Azure Cloud · Week 20 — Service Bus, Event Grid, Event Hubs + Boss

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Queues and events decouple slow AI work (embedding, summarizing, notifying) from user requests. Service Bus and Event Grid are a big part of AI-200's 'connect and consume' domain, and Event Hubs' Kafka endpoint is how the Kafka code you start in Java W20 runs on Azure. Season 4 ends with a timed messaging Boss.

## 🗓️ Sessions

### Tuesday 09 Mar · 45 min — Service Bus queues: peek-lock, settlement, dead-letter queue
- 📚 **Learn:** Namespaces and tiers (Basic supports queues only; Standard adds topics, sessions and duplicate detection), peek-lock vs receive-and-delete, complete/abandon/dead-letter/defer, lock renewal, max delivery count and the dead-letter queue. Read the [Python queues quickstart](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-python-how-to-use-queues). Optional: [Dead-letter queues](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-dead-letter-queues).
- 🛠️ **Do:** Create a Standard namespace and queue `embed-jobs` (max delivery count 3) and grant yourself the Azure Service Bus Data Owner role (keyless). In `py/sb_queue.py` send 10 JSON jobs with message IDs; a peek-lock receiver completes good jobs and abandons a 'poison' job until it lands in the DLQ. Read the DLQ and print the dead-letter reason. Also book AI-200 for Fri 23 Apr 2027 with your voucher (deadline: this week). Done when: 9 completed and 1 dead-lettered with its reason are logged in `w20/` and the booking is confirmed.

### Wednesday 10 Mar · 45 min — Topics, subscriptions, filters and sessions
- 📚 **Learn:** Topics and subscriptions (fan-out), SQL and correlation filters, rule actions, message sessions for ordered or grouped processing, duplicate detection. Read the [Python topics quickstart](https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-python-how-to-use-topics-subscriptions). Optional: [Message sessions](https://learn.microsoft.com/en-us/azure/service-bus-messaging/message-sessions).
- 🛠️ **Do:** Create topic `booking-events` with subscriptions `email` (all events), `analytics` (SQL filter `eventType = 'Cancelled'`) and `per-user` (sessions enabled, session ID = user ID). Publish 12 events for 3 users, verify each subscription's message count, and show that a session receiver processes one user's events in order. Done when: counts and ordered session output are committed in `w20/`.

### Friday 12 Mar · 45 min — Event Grid: custom events, filters, retries, dead-lettering
- 📚 **Learn:** Topics, event subscriptions and handlers, Event Grid vs CloudEvents schemas, subject and advanced filters, retries (exponential backoff for up to 24 hours by default), max delivery attempts, dead-lettering to blob; plus a primer for tomorrow - Event Hubs exposes a Kafka endpoint on Standard tier and above. Read [Event filtering](https://learn.microsoft.com/en-us/azure/event-grid/event-filtering). Optional: [Event Hubs for Apache Kafka](https://learn.microsoft.com/en-us/azure/event-hubs/azure-event-hubs-apache-kafka-overview).
- 🛠️ **Do:** Create a custom topic and a subscription that delivers to a Storage queue, with an advanced filter (`data.priority` equals high) and a blob dead-letter container. Publish 10 events from Python and confirm only high-priority ones reach the queue. Then delete the queue, publish again and find the events in the dead-letter container. Done when: filter and dead-letter evidence are in `w20/`.

### Saturday 13 Mar · 60 min — BOSS BATTLE: Timed messaging - Service Bus, Event Grid, Event Hubs Kafka
- 📚 **Learn:** Season 4 messaging under the clock: Event Grid routing into Service Bus, settlement and dead-lettering, and a Kafka client on Event Hubs (bootstrap `<namespace>.servicebus.windows.net:9093`, SASL_SSL with PLAIN, username `$ConnectionString`, password = the namespace connection string; prefer Entra OAuth in production). Use the [Event Hubs Kafka quickstart](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-quickstart-kafka-enabled-event-hubs). Optional: [Compare messaging services](https://learn.microsoft.com/en-us/azure/service-bus-messaging/compare-messaging-services).
- 🛠️ **Do:** 60-minute timer, your W20 scripts allowed. 0-20: a custom Event Grid topic routes 'upload' events to a Service Bus queue; a Python worker completes 9 and dead-letters 1 (reason logged). 20-40: an Event Hubs Standard namespace with hub `bookings` (2 partitions); produce 10 events through the Kafka endpoint with `confluent-kafka` (on Windows set `ssl.ca.location` to `certifi.where()`) and consume them, printing partition and offset. 40-50: draw the flow and when you'd pick each service. 50-60: delete the RG. Done when: both logs, the diagram and the RG deletion are in `w20/boss.md`.

## 📦 Deliverable (by Saturday night)
`w20/` DLQ evidence, topic/subscription/session results, Event Grid filter + dead-letter evidence, `boss.md` with the Event Grid -> Service Bus log and the Kafka produce/consume log (partitions and offsets), the messaging diagram, and the AI-200 booking.

## ✅ Self-check (Sunday test preview)
- Peek-lock vs receive-and-delete: which can lose messages, and when?
- Name three reasons a Service Bus message is dead-lettered, and how you would reprocess it.
- When do you need sessions, and how do they guarantee ordering?
- Service Bus vs Event Grid vs Event Hubs: pick one for a command, a notification and a telemetry stream.
- How does Event Grid retry delivery, and what happens when retries or the time-to-live run out?
- What changes when a Kafka client talks to Event Hubs instead of a self-managed Kafka cluster?
- Why are idempotent consumers essential with at-least-once delivery?

## 🚀 Stretch (optional)
Do the exercises in the official AI-200 modules [Queue and process AI operations with Azure Service Bus](https://learn.microsoft.com/en-us/training/modules/queue-process-operations-service-bus/) and [Develop event-driven AI workflows with Event Grid](https://learn.microsoft.com/en-us/training/modules/event-driven-workflows-event-grid/); after Java W21 (Spring Kafka), point a TicketVerse producer at an Event Hubs Kafka endpoint.
