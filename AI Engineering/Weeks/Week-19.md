# 🤖 AI Engineering · Week 19 — Multimodal and Document AI

> 📅 **Mon 01 Mar 2027 → Sun 07 Mar 2027** · Season 4 — Distributed Kingdom · ⚔️ **BOSS WEEK**  
> ⏱️ Slots: Mon, Tue, Thu, Fri · 45 min + Sat 45 min BUILD · Sunday test: 25 min

[← Week 18](Week-18.md) · [Roadmap](../ROADMAP_26_WEEKS.md) · [Today's planner](../../01_Daily_Planner/Week-19.md) · [Week 20 →](Week-20.md)

**Why this week:** Enterprise data lives in PDFs, scans, images and audio. Extracting reliable JSON from them (KYC, invoices, resumes, claims) is high-demand work in Indian companies.

## 🗓️ Sessions

### Monday 01 Mar · 45 min — Vision-language models: image question answering
- 📚 **Learn:** VLMs encode images into tokens the LLM attends to; images go in chat messages (base64 or URL); resolution drives token cost; OCR-free extraction and its limits (tiny text, dense tables, invented fields). Read: [Ollama vision models](https://ollama.com/blog/vision-models) and the [Gemini PDF/files notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/PDF_Files.ipynb); model: [qwen3-vl](https://ollama.com/library/qwen3-vl).
- 🛠️ **Do:** Send 5 images (screenshot, receipt, chart, handwritten note, resume photo) to one local Ollama VLM and one API model, asking the same 3 questions each, and score correctness. Done when: `10-resume-jd-extractor/vlm_tests.md` has a comparison table and 2 failure examples.

### Tuesday 02 Mar · 45 min — PDF and OCR to structured JSON
- 📚 **Learn:** Three paths: text-layer extraction (PyMuPDF, Docling, MarkItDown), OCR for scans, or a VLM directly; layout and tables; schema-first extraction with pydantic; confidence and human review queues. Read: [Docling](https://github.com/docling-project/docling) and [MarkItDown](https://github.com/microsoft/markitdown); awareness: [Azure Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/overview).
- 🛠️ **Do:** Build `extract_resume(pdf) -> Resume` (name, contact redacted in logs, skills, experience, education): text layer + structured output first, VLM fallback for scanned pages. Test on 5 resumes (yours plus public samples). Done when: all 5 give schema-valid JSON and you note which path each took.

### Thursday 04 Mar · 45 min — Speech: Whisper speech-to-text and text-to-speech
- 📚 **Learn:** Speech-to-text with Whisper or faster-whisper locally vs API transcription; timestamps, language detection and Hindi-English code-mixing; text-to-speech for voice output; latency for voice agents. Read: [faster-whisper](https://github.com/SYSTRAN/faster-whisper), [Gemini transcription notebook](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Get_started_transcribe.ipynb); TTS awareness: [Azure AI Speech](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/overview).
- 🛠️ **Do:** Record a 1-minute Hinglish voice note describing your target job. Transcribe it with faster-whisper (small model, CPU) and with an API, compare errors, then feed the transcript to your extractor to produce a `TargetJob` JSON; optionally speak the summary with TTS. Done when: both transcripts are compared and the JSON validates.

### Friday 05 Mar · 45 min — Image generation awareness and boss-battle skeleton
- 📚 **Learn:** Diffusion models generate images by iterative denoising guided by text; API vs open models; safety and watermarking; rarely core for backend roles but common interview trivia. Skim: [Diffusers docs](https://huggingface.co/docs/diffusers/index). Awareness: [Azure Content Understanding](https://learn.microsoft.com/en-us/azure/ai-services/content-understanding/overview) for multimodal extraction.
- 🛠️ **Do:** Prepare the battle skeleton: `extract(path, kind)` router (text PDF vs scanned PDF vs image), pydantic `Resume` and `JobDescription` schemas, a validator with one repair retry, and 6 test files with expected JSON. Done when: the skeleton runs with TODO stubs and tests fail for the right reasons.

### Saturday 06 Mar · 45 min — BOSS BATTLE: Resume/JD multimodal extractor in 45 minutes
- 📚 **Learn:** Rules: 45 minutes from your skeleton; inputs: 3 PDFs (text and scanned) and 3 images; output: validated JSON plus a resume-JD match score. Rubric /100: schema validity 30, field accuracy 30, routing/fallback 15, match score 15, README/demo 10. Recap: [Ollama structured outputs](https://ollama.com/blog/structured-outputs) (works with vision models too).
- 🛠️ **Do:** Implement routing (text -> LLM structured output; image or scan -> VLM), validation with one repair retry, `match(resume, jd)` skill-overlap score and CLI `extract file.pdf --type resume`. Run the 6 test files. Done when: 100% of outputs are schema-valid, field accuracy is 85%+ on labelled fields, rubric is 80+, and tag `v1.0-resume-jd-extractor` is pushed.

## 📦 Deliverable (by Saturday night)
`10-resume-jd-extractor/` v1.0: VLM comparison, text/OCR/VLM routing, pydantic schemas with repair retry, Whisper transcription demo, resume-JD match scoring and battle results.

## ✅ Self-check (Sunday test preview)
- How do vision-language models consume images, and what drives their token cost?
- Text-layer extraction vs OCR vs VLM: when do you use each?
- How do you make extraction reliable (schemas, retries, confidence, human review)?
- Where does Whisper struggle with Indian English or Hinglish audio?
- Design a pipeline that processes 1M invoices per month.
- What do Azure Document Intelligence or Content Understanding give you over a DIY pipeline?

## 🚀 Stretch (optional)
Compare your extractor with the Azure Document Intelligence prebuilt layout model on 3 documents (free tier) and note accuracy differences.
