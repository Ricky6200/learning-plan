# ☁️ Azure Cloud · Week 16 — AZ-104 exam and AI-200 kickoff

> 📅 **Mon 08 Feb 2027 → Sun 14 Feb 2027** · Season 4 — Distributed Kingdom  
> ⏱️ Slots: Tue, Wed, Fri · 45 min + Sat 60 min LAB · Sunday test: 20 min

[← Week 15](Week-15.md) · [Roadmap](../ROADMAP.md) · [Today's planner](../../01_Daily_Planner/Week-16.md) · [Week 17 →](Week-17.md)

**Why this week:** Earning Azure Administrator Associate validates your admin foundation; pivoting straight to AI-200 (the AZ-204 replacement) connects Azure to the Python and AI skills you're building in the AI track - exactly the Java + Azure + AI profile you are targeting.

## 🗓️ Sessions

### Tuesday 09 Feb · 45 min — Final AZ-104 revision: traps sprint and exam-day setup
- 📚 **Learn:** Your `w15/gaps.csv`, cram chapters for anything still red, and the online-exam rules in [About online exams with Pearson VUE](https://learn.microsoft.com/en-us/credentials/certifications/online-exams). Optional: how score reports work in [Exam scoring and score reports](https://learn.microsoft.com/en-us/credentials/certifications/exam-scoring-reports).
- 🛠️ **Do:** Run a 30-card flashcard sprint across all 5 domains (target 26/30); re-read your traps list; rerun the Pearson VUE system test; prepare ID and a clean desk. Update `w16/exam-day.md` with your plan: first pass answers what you know, flag long case studies, use Learn only for precise lookups. Done when: the sprint score is logged and the checklist is ticked.

### Wednesday 10 Feb · 45 min — Practice run 3 and weakest-domain repair
- 📚 **Learn:** Final calibration with the [AZ-104 practice assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/az-104/practice/assessment?assessment-type=practice&assessmentId=21). Optional: Microsoft Learn's [AZ-104 course videos](https://www.youtube.com/playlist?list=PLahhVEj9XNTcj4dwEwRHozO3xcxI_UHYG) for your weakest domain.
- 🛠️ **Do:** Practice run 3 (target 85%+). For each remaining miss, write the correct answer and its doc link in `gaps.csv`. Watch one 10-15 minute course video on your weakest domain. Stop studying by 10 pm. Done when: the run-3 score is logged and no objective in `gaps.csv` lacks a fix note.

### Friday 12 Feb · 45 min — EXAM: Sit AZ-104 (swap with Saturday if you booked Sat)
- 📚 **Learn:** No new content - 10 minutes on your traps list. Facts: 100 minutes, 700/1000 to pass, Microsoft Learn available in-exam but the timer keeps running, and after a break you can't return to earlier questions ([exam experience](https://learn.microsoft.com/en-us/credentials/support/exam-duration-exam-experience)). Retakes: 24 hours after the first attempt, then 14 days (Optional: [retake policy](https://learn.microsoft.com/en-us/credentials/support/retake-policy)).
- 🛠️ **Do:** Sit the exam: answer what you know first, flag long case studies, use Learn only for exact facts (CLI parameter names, SKU limits). Save the score report. If you don't pass: note the per-domain bars, book the retake and schedule two 45-minute fix sessions next to the AI-200 work. Done when: the score report is saved in `w16/` (and the badge is on LinkedIn if you passed).

### Saturday 13 Feb · 60 min — LAB: AI-200 kickoff - study guide map + keyless Python SDK
- 📚 **Learn:** AI-200 domains and audience (Python, SDKs, vector databases, containers); DefaultAzureCredential's chain (environment, workload identity, managed identity, Azure CLI and more); system- vs user-assigned managed identities. Read the [AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200). Optional: [Authenticate Python apps to Azure](https://learn.microsoft.com/en-us/azure/developer/python/sdk/authentication/overview).
- 🛠️ **Do:** 10 min: map every AI-200 bullet to W17-W25 in `w16/ai200-map.md`. Then, on the personal laptop, create a Python 3.12 venv with uv in `azure-labs/py` (`uv venv --python 3.12`, as in the AI track), `uv pip install azure-identity azure-mgmt-resource azure-storage-blob`, `az login`, and write `whoami.py` that uses DefaultAzureCredential to list your resource groups and upload a blob (after granting yourself Storage Blob Data Contributor). Done when: the map is committed and `whoami.py` runs with zero secrets in code.

## 📦 Deliverable (by Saturday night)
AZ-104 passed (score report + badge) or retake booked with a fix plan; `w16/ai200-map.md`; `py/whoami.py` (Python 3.12) using DefaultAzureCredential with no secrets.

## ✅ Self-check (Sunday test preview)
- What are AI-200's four skill areas and their weights?
- What is DefaultAzureCredential's credential chain, and why is it convenient both locally and in Azure?
- System-assigned vs user-assigned managed identity: which is deleted with its resource, and which can be shared?
- Why are keyless (Entra ID + RBAC) connections preferred over connection strings and keys?
- Control plane vs data plane RBAC: give a Storage example of each.
- How do Azure SDK for Python clients handle retries and long-running operations (pollers)?

## 🚀 Stretch (optional)
Watch the official [AI-200 exam prep 1 of 4 (containers)](https://www.youtube.com/watch?v=XHOBLJQZBCU) and the first 25 minutes of Savill's [Managed Identity Deep Dive](https://www.youtube.com/watch?v=rC1TV0_sIrM).
