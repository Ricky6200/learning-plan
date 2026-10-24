# 🏗️ System Design · Week 20 — Video streaming and file sync

> 📅 **Mon 08 Mar 2027 → Sun 14 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Wed, Thu · 45 min + Sat 45 min PRACTICE · Sunday test: 30 min

[← Week 19](Week-19.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-20.md) · [Week 21 →](Week-21.md)

**Why this week:** YouTube/Netflix and Dropbox/Drive are classic large-blob designs: uploads, processing pipelines, CDNs, chunking and sync conflicts all show up in product-company interviews.

## 🗓️ Sessions

### Monday 08 Mar · 45 min — YouTube/Netflix: upload, transcoding, adaptive streaming
- 📚 **Learn:** Resumable uploads to object storage, transcoding pipeline (split into chunks, multiple codecs/resolutions, DAG of tasks), HLS/DASH segments + manifests, adaptive bitrate (ABR) on the client, CDN + origin shield, metadata DB, view counting. Read [Design YouTube (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/youtube); watch [How Netflix onboards new content (Gaurav Sen)](https://www.youtube.com/watch?v=x9Hrn0oNmJM).
- 🛠️ **Do:** In `hld/08-video-streaming/README.md` do steps 1-5 solo in 30 minutes, including storage per day for 500 hours of video uploaded per minute with 5 renditions (state your bitrate assumptions); then 15 minutes comparing with Hello Interview. Done when: the estimate and the upload -> transcode -> publish flow are written.

### Wednesday 10 Mar · 45 min — Video deep dives: transcoding at scale, CDN, ABR
- 📚 **Learn:** Parallel chunk transcoding with a queue + workers, idempotent and retryable jobs, CDN cache-hit ratio and egress cost, pre-warming popular titles, ABR switching logic, view-count aggregation (stream + batch). Watch [Design YouTube (ByteByteGo)](https://www.youtube.com/watch?v=jWRW2xGMqSw) and [What is a CDN? (ByteByteGo)](https://www.youtube.com/watch?v=RI9np1LWzqw).
- 🛠️ **Do:** Add 3 deep dives (transcoding pipeline, CDN strategy, view counting) + an Excalidraw diagram. Done when: the one-page write-up + PNG are committed and you can explain what the player does when bandwidth drops mid-video.

### Thursday 11 Mar · 45 min — Google Drive/Dropbox: chunking, dedupe, sync, conflicts
- 📚 **Learn:** Client chunking (e.g., 4 MB), content hashing + dedupe, presigned uploads, metadata service (files, versions, chunks), sync via notifications/long polling, versioning, conflicts (conflicted copies vs merges), sharing permissions. Read [Design Dropbox (Hello Interview)](https://www.hellointerview.com/learn/system-design/problem-breakdowns/dropbox); watch its [walkthrough](https://www.youtube.com/watch?v=_UZ1ngy-kOI); Hindi: [Dropbox system design (Engineering Digest)](https://www.youtube.com/watch?v=k8AObcX8azM).
- 🛠️ **Do:** Timer on: full framework in 40 minutes in `hld/09-file-sync/README.md`. Done when: all 7 sections are filled and you can explain what happens when two offline devices edit the same file and then reconnect.

### Saturday 13 Mar · 45 min — PRACTICE: Chunked upload + dedupe lab
- 📚 **Learn:** Content-addressed storage: chunk ID = SHA-256 of the bytes, a file version = ordered list of chunk IDs, unchanged chunks are never re-uploaded. Java APIs: `MessageDigest`, `HexFormat`, `Files.newInputStream`. Context: [Object storage in system design (Hello Interview)](https://www.youtube.com/watch?v=RvaMHMxHjp4).
- 🛠️ **Do:** 25 min: `labs/chunkstore` - split a file into 4 MB chunks, store only unseen chunk hashes, keep a manifest per version, reassemble and verify the hash. 20 min: polish both W20 diagrams. Done when: tests prove uploading the same file twice stores its chunks once, a one-byte change uploads exactly one new chunk, and reassembly matches the original.

## 📦 Deliverable (by Saturday night)
`hld/08-video-streaming/` and `hld/09-file-sync/` (write-up + PNG each) and `labs/chunkstore` with passing tests.

## ✅ Self-check (Sunday test preview)
- Walk through what happens from video upload to the first viewer pressing play.
- What is adaptive bitrate streaming, and what do HLS/DASH manifests contain?
- How do you keep CDN egress cost under control?
- Why chunk files in Dropbox-like systems? What does it enable?
- How do you detect and resolve sync conflicts?
- How does content-hash deduplication work, and what are its privacy concerns?

## 🚀 Stretch (optional)
Add resumable upload to the chunk store: a client asks which chunks the server already has and sends only the missing ones.
