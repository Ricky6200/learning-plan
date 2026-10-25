# 🏗️ System Design · Week 20 — Chat, web crawler, unseen HLD mock (Boss week)

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** Chat (real-time connections, ordering, delivery states) and web crawling (queues, politeness, dedupe) cover most distributed-systems building blocks; the boss is your first full solo HLD mock on a case you have never designed - and job applications start this week.

## 🗓️ Sessions

### Monday 08 Mar · 45 min — Chat system (WhatsApp): connections, delivery, presence
- 📚 **Learn:** WebSocket gateways + connection registry, 1:1 and group message flow, per-chat ordering with sequence numbers, delivery states (sent/delivered/read), offline inbox + push notification, presence/last seen, media via object storage, end-to-end encryption (awareness). Read [Pushing realtime updates (Hello Interview)](https://www.hellointerview.com/learn/system-design/patterns/realtime-updates). Optional: [WhatsApp system design (Gaurav Sen, 25 min)](https://www.youtube.com/watch?v=vvhC64hQZMk).
- 🛠️ **Do:** In `hld/06-chat/README.md` do framework steps 1-5 in a 25-minute sprint. Done when: you can explain, step by step, how a message reaches a user who is offline and then comes online on two devices.

### Wednesday 10 Mar · 45 min — Chat deep dives: storage, groups, multi-device, scaling sockets
- 📚 **Learn:** Message storage partitioned by chat ID + time bucket (Cassandra/ScyllaDB), group fan-out limits, multi-device sync cursors, client message IDs for idempotency, routing between gateway servers with pub/sub, hot groups. Read [How Discord stores trillions of messages (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-the-wild/discord-messages-scylladb). Optional: the 'Data Modeling' section of [Cassandra deep dive (Hello Interview)](https://www.hellointerview.com/learn/system-design/deep-dives/cassandra).
- 🛠️ **Do:** Add 3 deep dives + an Excalidraw diagram to `hld/06-chat/`, then rehearse a 5-minute verbal summary once (recorded). Done when: the diagram shows the gateway-to-gateway routing path and the message table's partition key is justified.

### Thursday 11 Mar · 45 min — Web crawler: frontier, politeness, dedupe
- 📚 **Learn:** URL frontier (priority queues + per-host politeness queues), robots.txt, DNS caching, fetchers, parsers, content dedupe (hash/SimHash), recrawl scheduling, crawler traps, fault tolerance via queues. URL-seen test with a Bloom filter: a bit array + k hashes answering 'definitely new' or 'probably seen' in tiny memory. Watch [Design a web crawler (ByteByteGo, 6 min)](https://www.youtube.com/watch?v=6u25GckPhLU). Optional: [Design a web crawler (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/web-crawler).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-5 in `hld/07-web-crawler/README.md`, with estimates for crawling 1B pages/month (pages/s, bandwidth at 500 KB/page, storage) and the Bloom filter placed in the URL-seen check. Done when: politeness is enforced per host in the design and your 3 deep-dive topics are listed for the stretch.

### Saturday 13 Mar · 45 min — BOSS BATTLE: 45-min unseen HLD mock - FB Live comments
- 📚 **Learn:** Boss rules: an UNSEEN case - design live comments on a Facebook Live video (millions of viewers, comments appear in near real time, newest first). Blank Excalidraw, no notes, screen + voice recording, framework time splits (requirements 5, estimation 5, API 5, data model 5, high-level design 10, deep dives 12, wrap-up 3). Refresh the flow: [Delivery framework (Hello Interview)](https://www.hellointerview.com/learn/system-design/in-a-hurry/delivery). Optional: read [FB live comments (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/fb-live-comments) only after the mock.
- 🛠️ **Do:** Run the mock end to end, speaking aloud as if to an interviewer. Afterwards score 0-3 on 8 rubric lines (requirements, estimation, API, data model, diagram, deep dives, trade-offs, communication). Done when: recording + scorecard are in `boss/W20.md`; >= 16/24 clears the boss, otherwise book a re-run with your AI mentor or a peer next week.

## 📦 Deliverable (by Saturday night)
`hld/06-chat/` and `hld/07-web-crawler/` (write-up + PNG each) and the Boss recording + scorecard in `boss/W20.md`.

## ✅ Self-check (Sunday test preview)
- How does a message reach a recipient connected to a different chat server?
- How do you guarantee message ordering within a chat?
- How do delivered/read receipts work, and how are they stored?
- What is the partition key for the messages table, and why?
- Web crawler: how do you enforce politeness per host?
- How do you avoid crawling the same URL or the same content twice? Why can a Bloom filter never give a false negative?
- Estimate the bandwidth needed to crawl 1B pages a month.

## 🚀 Stretch (optional)
Write the 3 crawler deep dives. Compare your chat design with [Design WhatsApp (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp) or its [walkthrough video](https://www.youtube.com/watch?v=cr6p0n0N-VA) and list 3 things to adopt. Build a tiny Spring Boot `SseEmitter` endpoint (Java W13 skills) that pushes a counter every second and watch it in the browser. Extra: [Design a chat system (ByteByteGo)](https://www.youtube.com/watch?v=okrR1KXNLtA); [WhatsApp system design (Concept && Coding, Hindi)](https://www.youtube.com/watch?v=a8KUKOh3YXk).
