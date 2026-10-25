"""Build read-only PDF copies of the plan (Markdown stays the source of truth).

Usage (from anywhere):  python "C:\\Users\\rkumar48\\Personal_Learning\\00_Progress_Tracker\\tools\\build_pdfs.py"
Dependency-free: a small Markdown->HTML converter (stdlib only) + Microsoft Edge headless "print to PDF".
Re-run after editing any Markdown plan file.
"""
import glob, html, os, re, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
JAVA = "Java + Spring + Microservices + Kafka + Docker + Kubernetes"
EDGE_CANDIDATES = [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
                   r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"]

BUNDLES = [
    ("00_Master_Plan.pdf", "Master Plan", "", ["00_START_HERE.md", "03_SETUP_YOUR_LAPTOP.md", "01_MASTER_CALENDAR.md", "02_GAP_ANALYSIS_What_You_Were_Missing.md"], []),
    ("01_Daily_Planner/Daily_Planner_All_30_Weeks.pdf", "Daily Planner — all 30 weeks", "01_Daily_Planner", [], ["Week-*.md"]),
    (f"{JAVA}/Java_Track_Complete_Plan.pdf", "Java Backend Track", JAVA,
     ["README.md", "ROADMAP.md", "Project_TicketVerse/PROJECT_SPEC.md"], ["Weeks/Week-*.md", "INTERVIEW_QUESTION_BANK.md", "*.md", "RESOURCES.md"]),
    ("DSA/DSA_Track_Complete_Plan.pdf", "DSA Track", "DSA",
     ["README.md", "ROADMAP.md", "PATTERNS_CHEATSHEET.md"], ["Weeks/Week-*.md", "*.md", "RESOURCES.md"]),
    ("System Design/System_Design_Track_Complete_Plan.pdf", "System Design Track", "System Design",
     ["README.md", "ROADMAP.md", "HLD_INTERVIEW_FRAMEWORK.md", "LLD_MACHINE_CODING_FRAMEWORK.md"], ["Weeks/Week-*.md", "*.md", "RESOURCES.md"]),
    ("Azure Cloud/Azure_Track_Complete_Plan.pdf", "Azure Cloud Track", "Azure Cloud",
     ["README.md", "ROADMAP.md", "CERTIFICATION_GUIDE.md", "COST_SAFETY_AND_ACCOUNT_SETUP.md"], ["Weeks/Week-*.md", "*.md", "RESOURCES.md"]),
    ("AI Engineering/AI_Engineering_Track_Complete_Plan.pdf", "AI Engineering Track", "AI Engineering",
     ["README.md", "ROADMAP.md", "PROJECTS.md"], ["Weeks/Week-*.md", "AI_INTERVIEW_QUESTION_BANK.md", "*.md", "RESOURCES.md"]),
    ("Career & Interview Prep/Career_and_Interview_Prep.pdf", "Career & Interview Prep", "Career & Interview Prep", ["README.md", "STAR_STORY_BANK.md"], []),
]
EXCLUDE = {"REVISION_TRACKER.md"}  # living logs are not printed

CSS = """
@page { size: A4; margin: 14mm 13mm 16mm 13mm; }
body { font-family: 'Segoe UI', 'Segoe UI Emoji', Arial, sans-serif; font-size: 10.2pt; line-height: 1.45; color: #1f2328; }
h1 { font-size: 19pt; border-bottom: 3px solid #0969da; padding-bottom: 4px; margin-top: 0; color: #0b3d91; }
h2 { font-size: 14pt; border-bottom: 1px solid #d0d7de; padding-bottom: 2px; margin-top: 18px; color: #0b3d91; }
h3 { font-size: 11.5pt; margin-top: 14px; color: #24292f; } h4 { font-size: 10.5pt; }
.doc { page-break-before: always; } .doc.first { page-break-before: avoid; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; } th, td { border: 1px solid #d0d7de; padding: 4px 6px; vertical-align: top; text-align: left; }
th { background: #eef4ff; } tr:nth-child(even) td { background: #f8fafc; }
code { font-family: Consolas, 'Cascadia Mono', monospace; font-size: 8.8pt; background: #f2f4f7; padding: 1px 4px; border-radius: 3px; }
pre { background: #f6f8fa; border: 1px solid #d0d7de; border-radius: 6px; padding: 8px 10px; font-size: 8.4pt; white-space: pre-wrap; word-break: break-word; page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: 8.4pt; }
pre.mermaid { background: #fffbea; border-color: #f2d675; }
blockquote { margin: 8px 0; padding: 6px 12px; background: #f1f8ff; border-left: 4px solid #0969da; color: #24292f; }
blockquote p { margin: 3px 0; }
a { color: #0969da; text-decoration: none; } .rel { color: #57606a; border-bottom: 1px dotted #8c959f; }
ul, ol { margin: 4px 0 6px 0; padding-left: 22px; } li { margin: 2px 0; }
li.task { list-style: none; margin-left: -18px; }
hr { border: 0; border-top: 1px solid #d0d7de; margin: 14px 0; }
.cover { text-align: center; padding-top: 70mm; } .cover h1 { border: 0; font-size: 28pt; }
.cover p { color: #57606a; font-size: 11pt; } .toc { text-align: left; margin: 20mm auto 0; width: 70%; font-size: 10.5pt; }
"""


# ------------------------------------------------------------------ inline
def inline(text):
    codes = []

    def keep_code(m):
        codes.append("<code>" + html.escape(m.group(1)) + "</code>")
        return f"\x00{len(codes) - 1}\x00"

    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = re.sub(r"<!--.*?-->", "", text)
    text = html.escape(text, quote=False)
    text = re.sub(r"&lt;br\s*/?&gt;", "<br>", text)
    text = re.sub(r"&lt;(https?://[^\s&]+)&gt;", r'<a href="\1">\1</a>', text)

    def link(m):
        label, url = m.group(1), m.group(2).strip()
        if url.startswith(("http://", "https://", "mailto:")):
            return f'<a href="{html.escape(url)}">{label}</a>'
        return f'<span class="rel">{label}</span>'  # relative .md links are meaningless inside a PDF

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"[\1]", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", text)
    text = re.sub(r"(?<![\w])_(?!\s)(.+?)(?<!\s)_(?![\w])", r"<em>\1</em>", text)
    text = re.sub(r"~~(.+?)~~", r"<del>\1</del>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
    return text


# ------------------------------------------------------------------- blocks
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


def split_row(line):
    line = line.strip()
    if line.startswith("|"): line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"): line = line[:-1]
    cells, cur, i = [], "", 0
    in_code = False
    while i < len(line):
        ch = line[i]
        if ch == "`": in_code = not in_code
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur += "|"; i += 2; continue
        if ch == "|" and not in_code:
            cells.append(cur.strip()); cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def render_list(items):
    """items: list of (indent, ordered, text, extra_html). Builds nested lists by indentation."""
    out, stack = [], []
    for indent, ordered, text, extra in items:
        while stack and indent < stack[-1][0]:
            out.append("</li></%s>" % ("ol" if stack.pop()[1] else "ul"))
        if not stack or indent > stack[-1][0]:
            stack.append((indent, ordered))
            out.append("<ol>" if ordered else "<ul>")
        else:
            out.append("</li>")
        cls = ""
        m = re.match(r"^\[( |x|X)\]\s+(.*)$", text)
        if m:
            text = ("☑ " if m.group(1).lower() == "x" else "☐ ") + m.group(2)
            cls = ' class="task"'
        out.append(f"<li{cls}>" + inline(text) + extra)
    while stack:
        out.append("</li></%s>" % ("ol" if stack.pop()[1] else "ul"))
    return "".join(out)


def md_to_html(md):
    lines = md.replace("\r\n", "\n").split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1; continue
        if s.startswith("<!--"):
            while i < n and "-->" not in lines[i]: i += 1
            i += 1; continue
        if s.startswith("```"):
            lang = s[3:].strip().lower()
            i += 1; buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            cls = ' class="mermaid"' if lang == "mermaid" else ""
            label = "<em>(diagram source — renders as a picture in a Markdown viewer)</em><br>" if lang == "mermaid" else ""
            out.append(f"<pre{cls}>{label}<code>{html.escape(chr(10).join(buf))}</code></pre>")
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            lvl = len(m.group(1)); out.append(f"<h{lvl}>{inline(m.group(2).strip())}</h{lvl}>"); i += 1; continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            out.append("<hr>"); i += 1; continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            head = split_row(s); i += 2; rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i])); i += 1
            t = "<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            for r in rows:
                r = r + [""] * (len(head) - len(r))
                t += "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r[:len(head)]) + "</tr>"
            out.append(t + "</tbody></table>"); continue
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i])); i += 1
            out.append("<blockquote>" + md_to_html("\n".join(buf)) + "</blockquote>"); continue
        if LIST_RE.match(line):
            items = []
            while i < n:
                lm = LIST_RE.match(lines[i])
                if lm:
                    items.append([len(lm.group(1).expandtabs(4)), lm.group(2)[0].isdigit(), lm.group(3), ""]); i += 1
                elif items and lines[i].strip().startswith("```"):
                    lang = lines[i].strip()[3:].strip().lower(); i += 1; buf = []
                    while i < n and not lines[i].strip().startswith("```"):
                        buf.append(lines[i].strip()); i += 1
                    i += 1
                    items[-1][3] += f"<pre><code>{html.escape(chr(10).join(buf))}</code></pre>"
                elif lines[i].strip() and lines[i].startswith((" ", "\t")) and items:
                    items[-1][2] += " " + lines[i].strip(); i += 1
                else:
                    break
            out.append(render_list([tuple(x) for x in items])); continue
        buf = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,6}\s|```|>|\|)", lines[i].strip()) and not LIST_RE.match(lines[i]):
            buf.append(lines[i]); i += 1
        para_src = "\n".join(b.rstrip("\n") for b in buf)
        para_src = re.sub(r" {2,}\n", "\x01", para_src).replace("\n", " ")
        out.append("<p>" + inline(para_src.strip()).replace("\x01", "<br>") + "</p>")
    return "\n".join(out)


# -------------------------------------------------------------------- build
def collect(folder, first, patterns):
    base = os.path.join(ROOT, folder)
    files, seen = [], set()

    def add(p):
        p = os.path.normpath(p)
        if os.path.exists(p) and p not in seen and os.path.basename(p) not in EXCLUDE:
            seen.add(p); files.append(p)

    for f in first: add(os.path.join(base, f))
    for pat in patterns:
        for p in sorted(glob.glob(os.path.join(base, pat))):
            if pat == "*.md" and os.path.basename(p) == "RESOURCES.md":
                continue  # RESOURCES goes last when explicitly listed
            add(p)
    return files


def build(edge, out_rel, title, folder, first, patterns):
    files = collect(folder, first, patterns)
    if not files:
        print(f"skip (no files): {out_rel}"); return False
    toc = "".join(f"<li>{html.escape(os.path.relpath(f, os.path.join(ROOT, folder)).replace(os.sep, ' / '))}</li>" for f in files)
    body = (f'<div class="cover"><h1>{html.escape(title)}</h1><p>30-Week Career Plan · 26 Oct 2026 → 23 May 2027</p>'
            f'<p>Read-only copy — the Markdown files are the source of truth.</p><ol class="toc">{toc}</ol></div>')
    for f in files:
        with open(f, encoding="utf-8") as fh:
            body += f'<div class="doc">{md_to_html(fh.read())}</div>'
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{body}</body></html>'
    tmp = os.path.join(tempfile.gettempdir(), "plan_pdf_build.html")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(doc)
    out = os.path.join(ROOT, out_rel)
    if os.path.exists(out):
        os.remove(out)
    profile = os.path.join(tempfile.gettempdir(), "edge_pdf_profile")  # isolated profile: never attaches to your open Edge
    cmd = [edge, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check", "--disable-extensions",
           f"--user-data-dir={profile}", "--no-pdf-header-footer", f"--print-to-pdf={out}", "file:///" + tmp.replace("\\", "/")]
    p = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        p.wait(timeout=300)
    except subprocess.TimeoutExpired:
        p.kill()
    ok = os.path.exists(out) and os.path.getsize(out) > 1000
    print(("OK   " if ok else "FAIL ") + f"{out_rel}  ({len(files)} docs, {os.path.getsize(out) // 1024 if ok else 0} KB)")
    return ok


def main():
    edge = next((p for p in EDGE_CANDIDATES if os.path.exists(p)), None)
    if not edge:
        sys.exit("Microsoft Edge not found — cannot print PDFs.")
    only = sys.argv[1:]  # optional filter, e.g. "DSA"
    results = [build(edge, *b) for b in BUNDLES if not only or any(o.lower() in b[0].lower() for o in only)]
    print(f"Done: {sum(results)}/{len(results)} PDFs")


if __name__ == "__main__":
    main()
