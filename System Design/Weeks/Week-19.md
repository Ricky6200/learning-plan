# 🏗️ System Design · Week 19 — Chat system and web crawler (Boss week)

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** Chat (real-time connections, ordering, delivery states) and web crawling (queues, politeness, dedupe) cover most distributed-systems building blocks; the boss is your first full solo HLD mock.

## 🗓️ Sessions

### Monday 01 Mar · 45 min — Chat system (WhatsApp): connections, delivery, presence
- 📚 **Learn:** WebSocket gateways + connection registry, 1:1 and group message flow, per-chat ordering with sequence numbers, delivery states (sent/delivered/read), offline inbox + push notification, presence/last seen, media via object storage, end-to-end encryption (awareness). Read [Design WhatsApp (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp); watch [WhatsApp system design (Gaurav Sen)](https://www.youtube.com/watch?v=vvhC64hQZMk); Hindi: [WhatsApp system design (Concept && Coding)](https://www.youtube.com/watch?v=a8KUKOh3YXk).
- 🛠️ **Do:** In `hld/06-chat/README.md` do the full framework in 35 minutes, then 10 minutes comparing with Hello Interview. Done when: you can explain, step by step, how a message reaches a user who is offline and then comes online on two devices.

### Wednesday 03 Mar · 45 min — Chat deep dives: storage, groups, multi-device, scaling sockets
- 📚 **Learn:** Message storage partitioned by chat ID + time bucket (Cassandra/ScyllaDB), group fan-out limits, multi-device sync cursors, client message IDs for idempotency, routing between gateway servers with pub/sub, hot groups. Read [How Discord stores trillions of messages (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/discord-messages-scylladb); watch [Design a chat system (ByteByteGo)](https://www.youtube.com/watch?v=okrR1KXNLtA).
- 🛠️ **Do:** Add 3 deep dives + an Excalidraw diagram to `hld/06-chat/`, then rehearse a 5-minute verbal summary twice (record the second). Done when: the diagram shows the gateway-to-gateway routing path and the message table's partition key is justified.

### Thursday 04 Mar · 45 min — Web crawler: frontier, politeness, dedupe
- 📚 **Learn:** URL frontier (priority queues + per-host politeness queues), robots.txt, DNS caching, fetchers, parsers, content dedupe (hash/SimHash), URL-seen test with a Bloom filter, recrawl scheduling, crawler traps, fault tolerance via queues. Read [Design a web crawler (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/web-crawler); watch [Design a web crawler (ByteByteGo)](https://www.youtube.com/watch?v=6u25GckPhLU).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/07-web-crawler/README.md`, with estimates for crawling 1B pages/month (pages/s, bandwidth at 500 KB/page, storage). Show where your W14 Bloom filter fits. Done when: all 7 sections are filled and politeness is enforced per host in the design.

### Saturday 06 Mar · 45 min — BOSS BATTLE: 45-min solo HLD mock - design WhatsApp
- 📚 **Learn:** Boss rules: blank Excalidraw, no notes, screen + voice recording, framework time splits (requirements 5, estimation 5, API 5, data model 5, high-level design 10, deep dives 12, wrap-up 3). Refresh the delivery flow: [Delivery framework (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery).
- 🛠️ **Do:** Run the mock end to end, speaking aloud as if to an interviewer. Afterwards score 0-3 on 8 rubric lines (requirements, estimation, API, data model, diagram, deep dives, trade-offs, communication). Done when: recording + scorecard are in `boss/W19.md`; >= 16/24 clears the boss, otherwise book a re-run with your AI mentor or a peer next week.

## 📦 Deliverable (by Saturday night)
`hld/06-chat/` and `hld/07-web-crawler/` (write-up + PNG each) and the Boss recording + scorecard in `boss/W19.md`.

## ✅ Self-check (Sunday test preview)
- How does a message reach a recipient connected to a different chat server?
- How do you guarantee message ordering within a chat?
- How do delivered/read receipts work, and how are they stored?
- What is the partition key for the messages table, and why?
- Web crawler: how do you enforce politeness per host?
- How do you avoid crawling the same URL or the same content twice?
- Estimate the bandwidth needed to crawl 1B pages a month.

## 🚀 Stretch (optional)
Watch the [Design WhatsApp walkthrough (Hello Interview)](https://www.youtube.com/watch?v=cr6p0n0N-VA) after your mock and list 3 things to adopt.
