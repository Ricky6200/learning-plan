# 🏗️ System Design · Week 22 — Video streaming and file sync

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** YouTube/Netflix and Dropbox/Drive are classic large-blob designs: uploads, processing pipelines, CDNs, chunking and sync conflicts all show up in product-company interviews. Holi is Monday 22 Mar: a lite day is fine - move Monday's sprint to Sunday if needed.

## 🗓️ Sessions

### Monday 22 Mar · 45 min — YouTube/Netflix: upload, transcoding, adaptive streaming
- 📚 **Learn:** Resumable uploads to object storage (W15), a transcoding pipeline (split into chunks, multiple codecs/resolutions, a DAG of tasks), HLS/DASH segments + manifests, adaptive bitrate (ABR) on the client, CDN + origin shield, metadata DB, view counting. Watch [How Netflix onboards new content (Gaurav Sen, 11 min)](https://www.youtube.com/watch?v=x9Hrn0oNmJM). Optional: [Design YouTube (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/youtube).
- 🛠️ **Do:** In `hld/08-video-streaming/README.md` do steps 1-5 solo in a 25-minute sprint, including storage per day for 500 hours of video uploaded per minute with 5 renditions (state your bitrate assumptions). Done when: the estimate and the upload -> transcode -> publish flow are written.

### Wednesday 24 Mar · 45 min — Video deep dives: transcoding at scale, CDN, view counts
- 📚 **Learn:** Parallel chunk transcoding with a queue + workers, idempotent and retryable jobs, CDN cache-hit ratio and egress cost, pre-warming popular titles, ABR switching logic, view-count aggregation with a stream job plus a nightly batch reconciliation (your W21 batch-vs-stream notes). Watch [Design YouTube (ByteByteGo, 7 min)](https://www.youtube.com/watch?v=jWRW2xGMqSw). Optional: [What is a CDN? (ByteByteGo, 4 min)](https://www.youtube.com/watch?v=RI9np1LWzqw).
- 🛠️ **Do:** Add 3 deep dives (transcoding pipeline, CDN strategy, view counting) + an Excalidraw diagram. Done when: the one-page write-up + PNG are committed and you can explain what the player does when bandwidth drops mid-video.

### Thursday 25 Mar · 45 min — Google Drive/Dropbox: chunking, dedupe, sync, conflicts
- 📚 **Learn:** Client chunking (e.g., 4 MB), content hashing + dedupe, presigned uploads, metadata service (files, versions, chunks), sync via notifications/long polling, versioning, conflicts (conflicted copies vs merges), sharing permissions. Read 'Functional Requirements' through 'API or System Interface' in [Design Dropbox (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox). Optional: [Dropbox system design (Engineering Digest, Hindi, 12 min)](https://www.youtube.com/watch?v=k8AObcX8azM).
- 🛠️ **Do:** Timer on, 25 minutes: framework steps 1-5 in `hld/09-file-sync/README.md` plus one paragraph on conflicts. Done when: you can explain what happens when two offline devices edit the same file and then reconnect.

### Saturday 27 Mar · 45 min — PRACTICE: Chunked upload + dedupe lab
- 📚 **Learn:** Content-addressed storage: chunk ID = SHA-256 of the bytes, a file version = ordered list of chunk IDs, unchanged chunks are never re-uploaded. Java APIs: `MessageDigest`, `HexFormat`, `Files.newInputStream` (Java W10 I/O). Context: the 'Great Solution' parts of [Design Dropbox (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox).
- 🛠️ **Do:** 25-min timer: `labs/chunkstore` - split a file into 4 MB chunks, store only unseen chunk hashes, keep a manifest per version, reassemble and verify the hash. Done when: tests prove uploading the same file twice stores its chunks once, a one-byte change uploads exactly one new chunk, and reassembly matches the original; polish both W22 diagrams on Sunday.

## 📦 Deliverable (by Saturday night)
`hld/08-video-streaming/` and `hld/09-file-sync/` (write-up + PNG + ADR each) and `labs/chunkstore` with passing tests.

## ✅ Self-check (Sunday test preview)
- Walk through what happens from video upload to the first viewer pressing play.
- What is adaptive bitrate streaming, and what do HLS/DASH manifests contain?
- How do you keep CDN egress cost under control?
- How would you count video views both fast and accurately?
- Why chunk files in Dropbox-like systems? What does it enable?
- How do you detect and resolve sync conflicts?
- How does content-hash deduplication work, and what are its privacy concerns?

## 🚀 Stretch (optional)
Add resumable upload to the chunk store: a client asks which chunks the server already has and sends only the missing ones. Extra: [Design Dropbox walkthrough (Hello Interview)](https://www.youtube.com/watch?v=_UZ1ngy-kOI).
