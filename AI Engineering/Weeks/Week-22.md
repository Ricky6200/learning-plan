# 🤖 AI Engineering · Week 22 — Multimodal and Document AI

> 📅 **Mon 22 Mar 2027 → Sun 28 Mar 2027** · Season 5 — Cloud Ascension  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 21](Week-21.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-22.md) · [Week 23 →](Week-23.md)

**Why this week:** Enterprise data lives in PDFs, scans, images and audio. Extracting reliable JSON from them (KYC, invoices, resumes, claims) is high-demand work in Indian companies. (Mon 22 Mar is Holi: a light session.)

## 🗓️ Sessions

### Monday 22 Mar · 45 min — Vision-language models: image question answering (light)
- 📚 **Learn:** VLMs encode images into tokens the LLM attends to; images go into chat messages (base64 or URL); resolution drives token cost; OCR-free extraction has limits (tiny text, dense tables, invented fields). Read: [Ollama vision models](https://ollama.com/blog/vision-models). Optional: [Gemini PDF/files notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/PDF_Files.ipynb).
- 🛠️ **Do:** Holi, so 20 minutes: send 1 image to a local `qwen3-vl:2b` (slow on CPU, so just one) and 4 images (screenshot, receipt, chart, resume photo) to Gemini, asking the same 2 questions each, and score correctness. Done when: `13-resume-jd-extractor/vlm_tests.md` has the comparison table and one failure example.

### Tuesday 23 Mar · 45 min — PDF and OCR to structured JSON
- 📚 **Learn:** Three paths: text-layer extraction (PyMuPDF, Docling, MarkItDown), OCR for scans, or a VLM directly; layout and tables; schema-first extraction with pydantic; confidence and human review queues. Read: [Docling](https://github.com/docling-project/docling) (README). Optional: [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview) (awareness).
- 🛠️ **Do:** Build `extract_resume(pdf) -> Resume` (name, contact redacted in logs with your W18 module, skills, experience, education): text layer + structured output first, VLM fallback for scanned pages. Test on 5 resumes (yours plus public samples). Done when: all 5 give schema-valid JSON and you note which path each took.

### Thursday 25 Mar · 45 min — Speech: Whisper speech-to-text and text-to-speech
- 📚 **Learn:** Speech-to-text with Whisper or faster-whisper locally vs API transcription; timestamps, language detection and Hindi-English code-mixing; text-to-speech for voice output; latency budgets for voice agents. Read: [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (README usage). Optional: [Gemini transcription notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_transcribe.ipynb).
- 🛠️ **Do:** Record a 1-minute Hinglish voice note describing your target job. Transcribe it with faster-whisper (small model, CPU) and with an API, compare errors, then feed the transcript to your extractor to produce a `TargetJob` JSON. Done when: both transcripts are compared and the JSON validates.

### Friday 26 Mar · 45 min — Extractor design: routing, validation and recorded fixtures
- 📚 **Learn:** Route each input to the cheapest reliable path (text PDF -> LLM structured output, scan or image -> VLM, audio -> STT), validate with pydantic plus one repair retry, and record real model responses as test fixtures so CI runs offline. Awareness: diffusion models generate images by iterative denoising; rarely core for backend roles. Read: [pytest monkeypatch](https://docs.pytest.org/en/stable/how-to/monkeypatch.html). Optional: [Diffusers docs](https://huggingface.co/docs/diffusers/index).
- 🛠️ **Do:** Prepare tomorrow's skeleton: `extract(path, kind)` router, pydantic `Resume` and `JobDescription` schemas, a validator with one repair retry, 6 test files with expected JSON, and recorded responses for each saved under `tests/fixtures/`. Done when: the skeleton runs with TODO stubs and the tests fail for the right reasons without network access.

### Saturday 27 Mar · 45 min — BUILD: Resume/JD multimodal extractor
- 📚 **Learn:** Timed build (45 minutes) from your skeleton; inputs: 3 PDFs (text and scanned) and 3 images; output: validated JSON plus a resume-JD match score. Self-score /100: schema validity 30, field accuracy 30, routing/fallback 15, match score 15, README/demo 10. Recap: [Ollama structured outputs](https://ollama.com/blog/structured-outputs) (works with vision models too).
- 🛠️ **Do:** Implement routing (text -> LLM structured output; image or scan -> VLM), validation with one repair retry, a `match(resume, jd)` skill-overlap score and the CLI `extract file.pdf --type resume`. Run the 6 test files offline. Done when: 100% of outputs are schema-valid, field accuracy is 85%+ on labelled fields, and tag `v1.0-resume-jd-extractor` is pushed.

## 📦 Deliverable (by Saturday night)
`13-resume-jd-extractor/` v1.0: VLM comparison, text/OCR/VLM routing, pydantic schemas with repair retry, offline fixtures, Whisper transcription demo and resume-JD match scoring.

## ✅ Self-check (Sunday test preview)
- How do vision-language models consume images, and what drives their token cost?
- Text-layer extraction vs OCR vs VLM: when do you use each?
- How do you make extraction reliable (schemas, retries, confidence, human review)?
- Where does Whisper struggle with Indian English or Hinglish audio?
- Design a pipeline that processes 1M invoices per month.
- What do Azure Document Intelligence or Content Understanding give you over a DIY pipeline?

## 🚀 Stretch (optional)
Compare your extractor with the Azure Document Intelligence prebuilt layout model on 3 documents (free tier), or speak the extractor's summary with a text-to-speech API.
