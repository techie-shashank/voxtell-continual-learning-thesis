"""Download PDFs of all works in thesis/literature.bib and papers/index.csv.

Order per work: arXiv ID from the bib (eprint) or index -> arXiv title search -> OpenAlex open-access PDF.
Saves papers/<theme>/<key>.pdf (theme from index.csv, else 'other'); report in papers/download_report.csv.
PDFs already in the repo (voxtell_paper/, datasets/) are not downloaded again.
Rerun: python papers/download_papers.py   (skips files that already exist)
"""
import re, csv, json, time, difflib, unicodedata, urllib.parse, urllib.request, xml.etree.ElementTree as ET, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
P = ROOT / "papers"
UA = {"User-Agent": "MT-thesis-paper-download (mailto:shashank2531998@gmail.com)"}
LOCAL = {  # already in the repo
    "rokuss2025voxtellfreetextpromptableuniversal": "voxtell_paper/voxtell.pdf",
    "zheng2023preventingzeroshottransferdegradation": "voxtell_paper/zscl.pdf",
    "D_Alessandro_2023": "voxtell_paper/cpe_clip.pdf",
    "delange2022": "voxtell_paper/delange.pdf",
    "Chaudhry_2018": "voxtell_paper/chaudhary_riemann.pdf",
    "Zhang_2024_CVPR": "voxtell_paper/spu.pdf",
    "hu2022lora": "voxtell_paper/lora_hu.pdf",
    "kalajdzievski2023rankstabilizationscalingfactor": "voxtell_paper/rslora.pdf",
    "zhou2022cocoop": "voxtell_paper/Zhou_Conditional_Prompt_Learning_for_Vision-Language_Models_CVPR_2022_paper.pdf",
    "desai2021skmtea": "datasets/skm_tea_paper.pdf",
}
EXTRA_ARXIV = {  # works without a bib entry yet
    "NEW_wang2024sammed3dmoe": "2407.04938", "NEW_wang2026casam": "2511.17201",
    "NEW_ye2025medseqft": "2509.06096", "wu2024gift": "2503.04229",
}
SKIP = {"skmtea_tutorial"}

def get(url, tries=3, wait=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                return r.read()
        except Exception as e:
            err = e; time.sleep(wait * (i + 1))
    print("  fail", url[:100], err, file=sys.stderr); return None

def norm(t): return re.sub(r"[^a-z0-9 ]", "", unicodedata.normalize("NFKD", t.lower())).strip()

def bib():
    txt = (ROOT / "thesis/literature.bib").read_text(encoding="utf-8")
    out = {}
    for e in re.split(r"\n(?=@)", txt):
        m = re.match(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", e)
        if not m: continue
        def f(n):
            mm = re.search(r"\b" + n + r"\s*=\s*[{\"](.*?)[}\"]\s*,?\s*\n", e, re.S | re.I)
            return re.sub(r"[{}\s]+", " ", mm.group(1)).strip() if mm else ""
        out[m.group(2)] = dict(type=m.group(1).lower(), title=f("title"), eprint=f("eprint"), doi=f("doi"))
    return out

def is_pdf(b): return b is not None and b[:5] == b"%PDF-" and len(b) > 30000

def arxiv_by_title(title):
    q = "ti:" + " AND ti:".join([w for w in norm(title).split() if len(w) > 3][:8])
    d = get("http://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": q, "max_results": 5})); time.sleep(3)
    if not d: return None
    ns = {"a": "http://www.w3.org/2005/Atom"}
    for e in ET.fromstring(d).findall("a:entry", ns):
        t = " ".join(e.find("a:title", ns).text.split())
        if difflib.SequenceMatcher(None, norm(t), norm(title)).ratio() > 0.9:
            return re.sub(r"v\d+$", "", e.find("a:id", ns).text.rsplit("abs/", 1)[-1])
    return None

def openalex_pdf(title, doi):
    if doi:
        u = "https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi.replace("https://doi.org/", ""))
        d = get(u); ws = [json.loads(d)] if d else []
    else:
        d = get("https://api.openalex.org/works?" + urllib.parse.urlencode({"search": title, "per-page": 3}))
        ws = [w for w in (json.loads(d).get("results", []) if d else [])
              if difflib.SequenceMatcher(None, norm(w.get("title") or ""), norm(title)).ratio() > 0.9]
    for w in ws:
        locs = [w.get("best_oa_location")] + (w.get("locations") or [])
        for l in locs:
            if l and l.get("pdf_url"): yield l["pdf_url"]
        ids = w.get("ids") or {}
        if (w.get("doi") or "").lower().find("arxiv") >= 0: yield w["doi"]

def main():
    b = bib()
    idx = {r["key"]: r for r in csv.DictReader(open(P / "index.csv", encoding="utf-8"))}
    keys = [k for k in list(b) + [k for k in idx if k not in b] if k not in SKIP]
    rep = P / "download_report.csv"
    done = {r["key"]: r for r in csv.DictReader(open(rep, encoding="utf-8"))} if rep.exists() else {}
    rows = []
    for k in keys:
        theme = idx.get(k, {}).get("theme") or "other"
        safe = unicodedata.normalize("NFKD", k).encode("ascii", "ignore").decode()
        dest = P / theme / f"{safe}.pdf"
        info = b.get(k, dict(title=idx.get(k, {}).get("short_name", ""), eprint="", doi=""))
        if k in LOCAL:
            rows.append(dict(key=k, theme=theme, status="local", source="", path=LOCAL[k])); continue
        if dest.exists():
            rows.append(done.get(k) or dict(key=k, theme=theme, status="ok", source="existing file", path=str(dest.relative_to(ROOT)))); continue
        print(k, flush=True)
        cands = []
        aid = info.get("eprint") or EXTRA_ARXIV.get(k)
        if not aid and info.get("title"): aid = arxiv_by_title(info["title"])
        if aid: cands.append(("arXiv " + aid, f"https://arxiv.org/pdf/{aid}"))
        if info.get("title"): cands += [("OpenAlex OA", u) for u in openalex_pdf(info["title"], info.get("doi"))]
        status, src = "manual", ""
        for name, u in cands:
            data = get(u); time.sleep(3 if "arxiv" in u else 1)
            if is_pdf(data):
                dest.parent.mkdir(parents=True, exist_ok=True); dest.write_bytes(data)
                status, src = "ok", f"{name} | {u}"; break
        rows.append(dict(key=k, theme=theme, status=status, source=src,
                         path=str(dest.relative_to(ROOT)) if status == "ok" else ""))
        with open(rep, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["key", "theme", "status", "source", "path"]); w.writeheader(); w.writerows(rows)
        print("  ->", status, src[:80], flush=True)
    with open(rep, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["key", "theme", "status", "source", "path"]); w.writeheader(); w.writerows(rows)
    print("DONE", {s: sum(r["status"] == s for r in rows) for s in ("ok", "local", "manual")})

if __name__ == "__main__":
    main()
