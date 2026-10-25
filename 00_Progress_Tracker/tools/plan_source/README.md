# 🛠️ Plan source (for re-planning only)

This folder holds the **data** the 30-week plan was generated from, plus the tools that generate and check it.
**Day-to-day you never need it.** The Markdown files in the track folders and `01_Daily_Planner/` are the source of truth.

| File | Purpose |
|---|---|
| `data/track_dsa.py` | DSA plan: patterns, concepts, daily LeetCode IDs, bonus, self-checks |
| `data/track_java.py` · `track_ai.py` · `track_sd.py` · `track_azure.py` | Session-by-session plans (learn / do / deliverable / self-check / stretch) |
| `lc_index.json` | LeetCode catalog snapshot (24 Oct 2026): id → title, slug, difficulty, premium flag |
| `gen.py` | Regenerates `Weeks/*.md`, `ROADMAP.md`, `01_Daily_Planner/*.md`, `01_MASTER_CALENDAR.md` |
| `validate_track.py` | Checks a track data file: 30 weeks, schema, word limits, "Done when", boss Saturdays, company-neutral wording (employer-specific words come from the git-ignored `forbidden_words.local.md`), DSA problem ids/limits |
| `check_urls.py` · `check_all.py` | Link checker (YouTube titles via oEmbed) for a file or for every Markdown file |

## ⚠️ Rules
1. `gen.py` **overwrites ticked checkboxes**, so it refuses to run without `--force`. Use it only for a re-plan the user has approved, and log that re-plan in Section 10 of `AI_MEMORY.md`.
2. Before regenerating, copy progress somewhere safe: the dashboard, revision tracker and logs are *not* overwritten, but planner checkboxes are.
3. Workflow: edit `data/track_*.py` → `python validate_track.py data/track_<key>.py` → `python gen.py --force` → `python check_all.py` → `python ..\build_pdfs.py`.
4. For a small fix (a typo or a single link), just edit the Markdown file directly.
