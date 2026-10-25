"""Literature search for Ch. 2 via official bibliographic APIs.

Keyword search: OpenAlex, PubMed (NCBI E-utilities), arXiv API.
Citation search (works citing VoxTell and SAT): Semantic Scholar Graph API and OpenAlex.
(Semantic Scholar keyword search dropped 2026-10-23: unauthenticated rate limit, HTTP 429.)
Writes raw hits to papers/search/raw_<date>.jsonl and counts to stdout.
Rerun: python papers/search/run_search.py
"""
import json, time, datetime, urllib.parse, urllib.request, xml.etree.ElementTree as ET, pathlib, sys

YEARS = (2018, 2026)
N = 30  # hits per query and source
QUERIES = {
    "Q1": "continual learning medical image segmentation text prompt",
    "Q2": "continual learning vision-language model medical image segmentation",
    "Q3": "continual learning foundation model 3D medical image segmentation",
    "Q4": "few-shot continual learning medical image segmentation",
    "Q5": "incremental learning language-driven universal medical image segmentation",
    "Q6": "parameter-efficient fine-tuning few-shot 3D medical image segmentation",
}
PUBMED = {
    "Q1": '("continual learning" OR "incremental learning" OR "lifelong learning") AND segmentation AND ("text prompt" OR "language" OR "vision-language")',
    "Q2": '("continual learning" OR "incremental learning") AND segmentation AND "foundation model"',
    "Q3": '"few-shot" AND ("continual learning" OR "incremental learning") AND segmentation',
}
ARXIV = {
    "Q1": "abs:continual AND abs:segmentation AND abs:medical AND (abs:text OR abs:language OR abs:prompt)",
    "Q2": "abs:continual AND abs:segmentation AND abs:medical AND abs:foundation",
    "Q3": "abs:few-shot AND (abs:continual OR abs:incremental) AND abs:segmentation AND abs:medical",
    "Q4": "abs:incremental AND abs:segmentation AND abs:medical AND (abs:text OR abs:language OR abs:CLIP)",
}
CITING = {"VoxTell": "arXiv:2511.11450", "SAT": "arXiv:2312.17183"}
CITING_TITLES = {"VoxTell": "VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation",
                 "SAT": "Large-vocabulary segmentation for medical images with text prompts"}
UA = {"User-Agent": "MT-thesis-literature-search (mailto:shashank2531998@gmail.com)"}

def get(url, tries=6):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except Exception as e:
            if i == tries - 1:
                print("FAIL", url[:120], e, file=sys.stderr); return None
            time.sleep(20 * (i + 1))

def s2(q):
    f = "title,year,venue,externalIds,citationCount,abstract"
    u = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(
        {"query": q, "limit": N, "fields": f, "year": f"{YEARS[0]}-{YEARS[1]}"})
    d = get(u); time.sleep(5)
    return [dict(title=p["title"], year=p.get("year"), venue=p.get("venue"), ids=p.get("externalIds") or {},
                 cites=p.get("citationCount"), abstract=(p.get("abstract") or "")[:600])
            for p in (json.loads(d).get("data") or [])] if d else []

def s2_citing(pid):
    u = f"https://api.semanticscholar.org/graph/v1/paper/{pid}/citations?" + urllib.parse.urlencode(
        {"fields": "title,year,venue,externalIds,abstract", "limit": 1000})
    d = get(u); time.sleep(5)
    return [dict(title=c["citingPaper"]["title"], year=c["citingPaper"].get("year"), venue=c["citingPaper"].get("venue"),
                 ids=c["citingPaper"].get("externalIds") or {}, abstract=(c["citingPaper"].get("abstract") or "")[:600])
            for c in (json.loads(d).get("data") or []) if c.get("citingPaper", {}).get("title")] if d else []

def openalex_citing(title):
    d = get("https://api.openalex.org/works?" + urllib.parse.urlencode({"search": title, "per-page": 1}))
    if not d or not json.loads(d)["results"]: return []
    wid = json.loads(d)["results"][0]["id"].rsplit("/", 1)[-1]
    out, cursor = [], "*"
    while cursor:
        d = get("https://api.openalex.org/works?" + urllib.parse.urlencode(
            {"filter": f"cites:{wid}", "per-page": 200, "cursor": cursor, "mailto": "shashank2531998@gmail.com"}))
        if not d: break
        j = json.loads(d)
        for w in j["results"]:
            src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name")
            out.append(dict(title=w.get("title"), year=w.get("publication_year"), venue=src, ids={"DOI": w.get("doi"), "OpenAlex": w.get("id")}))
        cursor = j["meta"].get("next_cursor") if j["results"] else None
    return out

def openalex(q):
    u = "https://api.openalex.org/works?" + urllib.parse.urlencode(
        {"search": q, "per-page": N, "filter": f"publication_year:{YEARS[0]}-{YEARS[1]}", "mailto": "shashank2531998@gmail.com"})
    d = get(u)
    out = []
    for w in (json.loads(d).get("results") or []) if d else []:
        src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name")
        out.append(dict(title=w.get("title"), year=w.get("publication_year"), venue=src,
                        ids={"DOI": w.get("doi"), "OpenAlex": w.get("id")}, cites=w.get("cited_by_count")))
    return out

def pubmed(q):
    u = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": q, "retmax": N, "retmode": "json", "mindate": YEARS[0], "maxdate": YEARS[1], "datetype": "pdat"})
    d = get(u); time.sleep(0.5)
    if not d: return [], 0
    r = json.loads(d)["esearchresult"]; ids = r.get("idlist", [])
    if not ids: return [], int(r.get("count", 0))
    s = json.loads(get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids)))["result"]
    time.sleep(0.5)
    return [dict(title=s[i]["title"], year=s[i].get("pubdate", "")[:4], venue=s[i].get("fulljournalname"), ids={"PMID": i})
            for i in ids], int(r.get("count", 0))

def arxiv(q):
    u = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": q, "max_results": 60, "sortBy": "relevance"})
    d = get(u); time.sleep(3)
    if not d: return [], 0
    ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
    root = ET.fromstring(d)
    total = int(root.find("o:totalResults", ns).text)
    out = []
    for e in root.findall("a:entry", ns):
        out.append(dict(title=" ".join(e.find("a:title", ns).text.split()), year=e.find("a:published", ns).text[:4],
                        venue="arXiv", ids={"ArXiv": e.find("a:id", ns).text.rsplit("/", 1)[-1]},
                        abstract=" ".join(e.find("a:summary", ns).text.split())[:600]))
    return out, total

if __name__ == "__main__":
    date = datetime.date.today().isoformat()
    out = pathlib.Path(__file__).with_name(f"raw_{date}.jsonl")
    rows = []
    def add(source, qid, query, hits, total=None):
        print(f"{source:16} {qid:8} hits={len(hits):4} total={total}")
        for h in hits: rows.append(dict(source=source, qid=qid, query=query, date=date, **h))
    for qid, q in QUERIES.items():
        add("OpenAlex", qid, q, openalex(q))
    for qid, q in PUBMED.items():
        h, t = pubmed(q); add("PubMed", qid, q, h, t)
    for qid, q in ARXIV.items():
        h, t = arxiv(q); add("arXiv", qid, q, h, t)
    for name, pid in CITING.items():
        add("SemanticScholar", "cites_" + name, pid, s2_citing(pid))
        add("OpenAlex", "cites_" + name, CITING_TITLES[name], openalex_citing(CITING_TITLES[name]))
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows), encoding="utf-8")
    print("written", out, len(rows))
