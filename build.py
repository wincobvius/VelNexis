# ╔══════════════════════════════════════════════════════════════════╗
# ║  VELNEXIS SITE BUILDER — NON-CODER FRIENDLY                      ║
# ║  Sab content `content/` folder ke TEXT files mein hai.            ║
# ║  Edit karo → `python3 build.py` chalao → site update.             ║
# ║  Yeh file (build.py) sirf design/engine hai — isay chhue bina    ║
# ║  bhi sab kuch edit ho sakta hai.                                 ║
# ╚══════════════════════════════════════════════════════════════════╝
import os, re, base64, time, json

ROOT = os.path.dirname(os.path.abspath(__file__))
C = lambda *p: os.path.join(ROOT, "content", *p)

# ---------------- fonts (assets/fonts se) ----------------
def write_fonts_css():
    """external fonts.css — browser in fonts ko cache karta hai, har page pe dobara load nahi hote"""
    css = ""
    inter = os.path.join(ROOT, "assets/fonts/inter.woff2")
    news = os.path.join(ROOT, "assets/fonts/newsreader-italic.woff2")
    if os.path.exists(inter):
        css += ("@font-face{font-family:'Inter';font-style:normal;font-weight:100 900;font-display:swap;"
                "src:url(inter.woff2) format('woff2-variations')}")
    if os.path.exists(news):
        css += ("@font-face{font-family:'Newsreader';font-style:italic;font-weight:200 800;font-display:swap;"
                "src:url(newsreader-italic.woff2) format('woff2-variations')}")
    open(os.path.join(ROOT, "assets/fonts/fonts.css"), "w", encoding="utf-8").write(css)

# ---------------- parsers ----------------
def yaml_mini(fm):
    """chhota YAML parser: flat keys + string lists (admin panel compatible)"""
    data, pend = {}, None
    for ln in fm.splitlines():
        st = ln.strip()
        if not st or st.startswith("#"): continue
        if st.startswith("- "):
            item = st[2:].strip().strip('"').strip("'")
            if pend: data.setdefault(pend, []).append(item)
            continue
        m = re.match(r"([\w-]+):\s*(.*)", st)
        if not m: continue
        k, v = m.group(1), m.group(2).strip()
        if v == "":
            pend = k; data.setdefault(k, [])
        elif v.startswith("[") and v.endswith("]"):
            pend = None
            data[k] = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
        else:
            pend = None
            data[k] = v.strip('"').strip("'")
    return data

def split_fm(raw):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, re.S)
    if m: return yaml_mini(m.group(1)), m.group(2)
    return {}, raw

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def pretty_date(d):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", d or "")
    if m: return f"{MONTHS[int(m.group(2))-1]} {int(m.group(3))}, {m.group(1)}"
    return d or ""

def parse_settings():
    return yaml_mini(open(C("settings.yml"), encoding="utf-8").read())

def parse_categories():
    cats = {}
    d = C("categories")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"): continue
        meta, _ = split_fm(open(os.path.join(d, fn), encoding="utf-8").read())
        meta.setdefault("pros", []); meta.setdefault("cons", [])
        cats[fn[:-3]] = meta
    return cats

def parse_articles():
    arts = []
    d = C("articles")
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".md"): continue
        meta, body = split_fm(open(os.path.join(d, fn), encoding="utf-8").read())
        meta["id"] = fn[:-3]
        meta["date"] = pretty_date(meta.get("date", ""))
        meta["body"] = body.strip()
        arts.append(meta)
    MON = {m: i+1 for i, m in enumerate(MONTHS)}
    def key(a):
        mm = re.match(r"(\w{3}) (\d+), (\d+)", a.get("date",""))
        return (int(mm.group(3)), MON.get(mm.group(1),0), int(mm.group(2))) if mm else (0,0,0)
    arts.sort(key=key, reverse=True)
    return arts

def inline(t):
    t = re.sub(r"\]\(([\w\-/\.]+?)\.(md|txt)\)", r"](\1.html)", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"\[(.+?)\]\((https?://[^\s)]+)\)", r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', t)
    return t

def md(text):
    """simple text → HTML (markdown-lite)"""
    out, lines, i = [], text.split("\n"), 0
    while i < len(lines):
        ln = lines[i].rstrip()
        st = ln.strip()
        if not st: i += 1; continue
        if st == "((ad))":
            i += 1  # ad slot marker — ads sirf AdSense approval ke BAAD lagenge
        elif st.startswith("%% "):
            out.append('<p class="defline">' + inline(st[3:]) + "</p>"); i += 1
        elif st.startswith("## "):
            out.append("<h2>" + inline(st[3:]) + "</h2>"); i += 1
        elif st.startswith("### "):
            out.append("<h3>" + inline(st[4:]) + "</h3>"); i += 1
        elif st.startswith("- "):
            items = []
            while i < len(lines) and lines[i].strip().startswith("- "):
                items.append(inline(lines[i].strip()[2:])); i += 1
            out.append("<ul>" + "".join("<li>%s</li>" % t for t in items) + "</ul>")
        elif re.match(r"^\d+\. ", st):
            items = []
            while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
                items.append(inline(re.sub(r"^\d+\. ", "", lines[i].strip()))); i += 1
            out.append("<ol>" + "".join("<li>%s</li>" % t for t in items) + "</ol>")
        elif st.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")]); i += 1
            t = "<table><tr>" + "".join("<th>%s</th>" % c for c in rows[0]) + "</tr>"
            for r in rows[1:]:
                t += "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>"
            out.append(t + "</table>")
        elif st.startswith("Q: "):
            q = st[3:]; i += 1; a = ""
            if i < len(lines) and lines[i].strip().startswith("A: "):
                a = lines[i].strip()[3:]; i += 1
            out.append('<details class="faq"><summary>%s</summary><p>%s</p></details>' % (inline(q), inline(a)))
        elif st.startswith("> "):
            out.append('<div class="note">' + inline(st[2:]) + "</div>"); i += 1
        else:
            buf = [st]; i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r"^(## |### |- |\||Q: |A: |> |%% |\(\(ad\)\)|\d+\. )", lines[i].strip()):
                buf.append(lines[i].strip()); i += 1
            out.append("<p>" + " ".join(inline(b) for b in buf) + "</p>")
    return "\n".join(out)

# ---------------- data ----------------
SET = parse_settings()
CATS = parse_categories()
ORDER = list(CATS.keys())
ARTS = parse_articles()
def cat_of(a): return CATS.get(a.get("cat"), {"name": "General", "icon": "📄", "color": "#A78BFA"})
def n_of(k): return len([a for a in ARTS if a.get("cat") == k])

# ---------------- CSS ----------------
CSS = """
:root{--bg:#101014;--card:rgba(255,255,255,.04);--card2:rgba(255,255,255,.07);--line:rgba(255,255,255,.08);
--txt:#ECEAE6;--mut:#A3A09A;--gold:#8B5CF6;--gold2:#C4B5FD;--r:16px;--max:1180px}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;color-scheme:dark;-webkit-tap-highlight-color:transparent;scrollbar-color:#2A2438 transparent}
::-webkit-scrollbar{width:11px;height:11px}
::-webkit-scrollbar-thumb{background:#2A2438;border-radius:8px}
::-webkit-scrollbar-thumb:hover{background:#3D3552}
::-webkit-scrollbar-track{background:transparent}
::selection{background:rgba(139,92,246,.5);color:#fff}
::placeholder{color:#7B786F;opacity:1}
a:focus-visible,button:focus-visible{outline:2px solid #A78BFA;outline-offset:3px;border-radius:4px}
body{background:linear-gradient(180deg,#100C1A,#090810 52%,#0C0A15);color:var(--txt);
font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
line-height:1.65;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;opacity:.05;
background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.5'/%3E%3C/svg%3E")}
body::after{content:"";position:fixed;inset:0;z-index:-2;pointer-events:none;
background:radial-gradient(900px 480px at 50% -12%,rgba(139,92,246,.10),transparent 60%)}
a{color:inherit;text-decoration:none}
.wrap{max-width:var(--max);margin:0 auto;padding:0 22px}
.gt{background:linear-gradient(135deg,#A5B4FC,#7C3AED);-webkit-background-clip:text;background-clip:text;color:transparent}
.mut{color:var(--mut)}
.nav{position:sticky;top:0;z-index:50;background:rgba(10,9,14,.85);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:64px;gap:14px}
.logo{font-weight:800;font-size:1.3rem;letter-spacing:-.3px}
.nav-links{display:flex;align-items:center;gap:4px;list-style:none}
.nav-links a{padding:8px 13px;border-radius:10px;font-size:.92rem;color:var(--mut);transition:color .25s,background .25s,transform .15s,box-shadow .25s}
.nav-links a:hover{color:var(--txt);background:var(--card2)}
.nav-links a.on{color:var(--gold2);background:rgba(139,92,246,.10);border:1px solid rgba(139,92,246,.28)}
.nav-links a:active{transform:scale(.92)}
.nav-links a.snav{color:var(--gold2)}
.nav-links a.snav:hover{color:var(--txt);background:rgba(167,139,250,.14);box-shadow:0 0 16px rgba(167,139,250,.38)}
.nav-links a.snav:active{transform:scale(.90);animation:sflash .35s ease}
@keyframes sflash{from{box-shadow:0 0 0 0 rgba(167,139,250,.60)}to{box-shadow:0 0 0 14px rgba(167,139,250,0)}}
.burger{display:none;background:var(--card2);border:1px solid var(--line);color:var(--txt);width:42px;height:42px;border-radius:10px;font-size:1.15rem;cursor:pointer}
.js [data-rev]{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease}
.js [data-rev].in{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){.js [data-rev]{opacity:1;transform:none;transition:none}}
.hero{padding:84px 0 60px;position:relative}
.hero .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:44px;align-items:center}
.hero h1{font-size:clamp(2.1rem,4.6vw,3.4rem);line-height:1.14;font-weight:800;margin:0 0 18px;letter-spacing:-.6px}
.hero p.sub{font-family:'Newsreader',Georgia,'Times New Roman',serif;font-style:italic;font-weight:500;color:#E4DEF5;font-size:1.26rem;line-height:1.85;max-width:620px;letter-spacing:.2px}
.btn{display:inline-flex;align-items:center;gap:8px;border:none;cursor:pointer;font-weight:700;font-size:.92rem;border-radius:11px;padding:12px 20px;transition:transform .25s,box-shadow .25s,border-color .25s;font-family:inherit}
.btn.p{background:linear-gradient(135deg,var(--gold2),var(--gold));color:#fff;box-shadow:0 6px 22px rgba(139,92,246,.28)}
.btn.p:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(139,92,246,.4)}
.btn.g{background:transparent;color:var(--txt);border:1px solid var(--line)}
.btn.g:hover{border-color:rgba(139,92,246,.5)}
.hero-cta{display:flex;gap:12px;margin-top:24px;flex-wrap:wrap}
.hcards{position:relative;height:380px}
.hglow{position:absolute;will-change:transform;width:240px;height:240px;border-radius:50%;filter:blur(70px);opacity:.35;background:rgba(139,92,246,.45);top:14%;left:16%;animation:float 9s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-20px)}}
.fcard{position:absolute;will-change:transform;background:rgba(20,17,28,.92);border:1px solid var(--line);border-radius:16px;padding:16px 18px;box-shadow:0 14px 40px rgba(0,0,0,.45);animation:float 7s ease-in-out infinite}
.fcard.f1{top:6%;left:4%;width:76%;animation-delay:-1s}
.fcard.f2{top:38%;right:0;width:70%;animation-delay:-3.4s}
.fcard.f3{bottom:3%;left:10%;width:72%;animation-delay:-5.6s}
.fcard h4{font-size:.95rem;margin-bottom:4px}
.fcard .yes{color:#6EE7A0;font-weight:700;font-size:.82rem}
.fcard .no{color:#F08A8A;font-weight:700;font-size:.82rem}
section.block{padding:64px 0}
.shead{display:flex;align-items:end;justify-content:space-between;gap:18px;margin-bottom:30px;flex-wrap:wrap}
.shead h2{font-size:clamp(1.5rem,3vw,2.05rem);font-weight:800;letter-spacing:-.4px}
.kicker{font-size:.82rem;font-weight:800;letter-spacing:2.2px;color:var(--gold2);text-transform:uppercase;margin-bottom:8px}
.cgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.ccard{position:relative;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:22px;transition:transform .3s,border-color .3s,box-shadow .3s;overflow:hidden}
.ccard::before{content:"";position:absolute;inset:0;background:radial-gradient(180px 120px at 85% -10%,var(--t),transparent 70%);opacity:0;transition:opacity .3s}
.ccard:hover{transform:translateY(-5px);border-color:var(--line2);box-shadow:0 14px 34px rgba(0,0,0,.4)}
.ccard:hover::before{opacity:1}
.ccard .ic{width:46px;height:46px;border-radius:13px;display:grid;place-items:center;font-size:1.35rem;background:rgba(255,255,255,.05);border:1px solid var(--line);margin-bottom:14px}
.ccard h3{font-size:1.05rem;margin-bottom:6px}
.ccard p{font-size:.84rem;color:var(--mut)}
.ccard .cnt{margin-top:14px;font-size:.75rem;font-weight:700;color:var(--gold2);letter-spacing:.6px;text-transform:uppercase}
.agrid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.acard{background:var(--card);border:1px solid var(--line);border-radius:var(--r);overflow:hidden;transition:transform .3s,border-color .3s,box-shadow .3s;display:flex;flex-direction:column}
.acard:hover{transform:translateY(-5px);box-shadow:0 14px 36px rgba(0,0,0,.42);border-color:rgba(139,92,246,.35)}
.thumb{height:150px;background:linear-gradient(135deg,var(--t1),transparent 70%),#14101D;display:grid;place-items:center;font-size:46px}
.thumb.hasimg{background-size:cover;background-position:center;position:relative}
.thumb.hasimg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 45%,rgba(8,6,14,.78))}
.ahero{width:100%;aspect-ratio:2/1;object-fit:cover;border-radius:18px;border:1px solid var(--line);margin-top:26px;display:block;background:#14101D}
.abody{padding:18px;display:flex;flex-direction:column;gap:9px;flex:1}
.tag{align-self:flex-start;font-size:.7rem;font-weight:800;letter-spacing:1px;text-transform:uppercase;padding:4px 10px;border-radius:999px;border:1px solid;color:var(--tc);border-color:var(--tcb);background:var(--tcbg)}
.acard h3{font-size:1.02rem;line-height:1.4}
.acard p{font-size:.86rem;color:var(--mut)}
.meta{margin-top:auto;display:flex;gap:14px;font-size:.76rem;color:#7B786F}
.authcard{display:flex;align-items:center;gap:18px;background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:24px;text-decoration:none;transition:border-color .3s,box-shadow .3s,transform .3s}
.authcard:hover{border-color:rgba(139,92,246,.45);box-shadow:0 14px 36px rgba(0,0,0,.42);transform:translateY(-3px)}
.authcard .avatar{width:64px;height:64px;display:grid;place-items:center;border-radius:50%;background:linear-gradient(135deg,#C4B5FD,#8B5CF6);color:#fff;font-weight:800;font-size:1.3rem;flex-shrink:0}
.authcard .ainfo{display:flex;flex-direction:column;gap:5px;min-width:0}
.authcard .ainfo b{font-size:1.08rem;color:var(--txt);-webkit-text-fill-color:var(--txt)}
.authcard .arole{font-size:.74rem;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:#A78BFA}
.authcard .abio{font-size:.88rem;color:var(--mut);line-height:1.6}
.authcard .amore{font-size:.8rem;font-weight:700;color:#A78BFA;margin-top:4px}
.apage-head{display:flex;flex-direction:column;align-items:center;text-align:center;gap:14px;margin:8px 0 10px}
.apage-head .avatar{width:104px;height:104px;display:grid;place-items:center;border-radius:50%;background:linear-gradient(135deg,#C4B5FD,#8B5CF6);color:#fff;font-weight:800;font-size:2.1rem}
.apage-head .arole{font-size:.78rem;font-weight:800;letter-spacing:1.6px;text-transform:uppercase;color:#A78BFA}
.apage-head h1{margin:0;font-size:clamp(1.8rem,4vw,2.6rem)}
.ctabtn{display:inline-flex;align-items:center;gap:8px;margin-top:26px;padding:13px 26px;border-radius:999px;background:linear-gradient(135deg,#8B5CF6,#7C3AED);color:#fff;font-weight:700;font-size:.9rem;text-decoration:none;transition:transform .25s,box-shadow .25s}
.ctabtn:hover{transform:translateY(-2px);box-shadow:0 10px 30px rgba(139,92,246,.35)}
.plist{list-style:none;max-width:780px}
/* Phase 3: extracted inline styles */
.wrap860{max-width:860px}.wrap760{max-width:760px}.prose-c{max-width:860px;margin:0 auto 10px}
.pt10{padding-top:10px}.pt0{padding-top:0}.center{text-align:center}
.gold{color:var(--gold2)}.byb{color:var(--txt)}
.aul{color:inherit;text-decoration:underline;text-decoration-color:rgba(139,92,246,.55);text-underline-offset:3px}
.flogo{margin-bottom:12px;display:inline-block}.ftag{font-size:.88rem;max-width:280px}.fcontact{font-size:.85rem;margin-top:14px}
.g3{grid-template-columns:repeat(3,1fr)}.g1{grid-template-columns:1fr}
.arth1{font-size:clamp(1.6rem,3.6vw,2.3rem);margin:14px 0 4px}.cath1{margin:0}.catp{margin:6px 0 0}
.btnw{width:100%;justify-content:center}.hp{display:none}
.nfhero{text-align:center;padding:80px 0}.nf404{font-size:5rem;font-weight:800;line-height:1;background:linear-gradient(135deg,#C4B5FD,#8B5CF6);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.nfh1{margin:14px 0 8px}.nfh2{font-size:1.05rem;margin:0 0 14px}.nfp{max-width:440px;margin:0 auto 28px}
.nfbtns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.ccard .ic{border-color:var(--tcb2)}
.acard{position:relative}
.str{color:inherit}
.str::after{content:"";position:absolute;inset:0}
.fgrid h3.fh,.fgrid h4{font-size:.76rem;font-weight:800;letter-spacing:1.4px;text-transform:uppercase;color:#A78BFA;margin:0 0 12px}
.ich{font-size:.98rem;margin:0 0 6px}
.fcard h2.fch{font-size:.95rem;margin:0 0 8px;font-weight:800}
.plist li{display:flex;gap:16px;padding:18px 6px;border-bottom:1px solid var(--line);align-items:flex-start;transition:transform .25s}
.plist li:last-child{border-bottom:none}
.plist li:hover{transform:translateX(6px)}
.plist .pk{width:42px;height:42px;border-radius:12px;display:grid;place-items:center;font-size:1.15rem;background:rgba(139,92,246,.12);border:1px solid rgba(139,92,246,.35);flex-shrink:0}
.plist h3{font-size:1.04rem;margin-bottom:4px;letter-spacing:-.2px}
.plist p{font-size:.92rem;color:var(--mut);line-height:1.7}
footer{border-top:1px solid var(--line);background:#08070C;padding:54px 0 26px;margin-top:40px}
.fgrid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:34px;margin-bottom:36px}
.fgrid h4{font-size:.82rem;letter-spacing:1.4px;text-transform:uppercase;color:#fff;margin-bottom:14px}
.fgrid ul{list-style:none}.fgrid li{margin-bottom:9px}
.fgrid a{color:var(--mut);font-size:.9rem;transition:color .25s}
.fgrid a:hover{color:var(--gold2)}
.fbot{border-top:1px solid var(--line);padding-top:20px;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:.82rem;color:#7B786F}
.phero{padding:56px 0 34px;border-bottom:1px solid var(--line);background:linear-gradient(180deg,rgba(139,92,246,.05),transparent)}
.phero h1{font-size:clamp(1.9rem,4vw,2.6rem);font-weight:800;margin:0 0 10px;letter-spacing:-.5px}
.phero p{color:var(--mut);max-width:720px}
.defline{font-family:'Newsreader',Georgia,'Times New Roman',serif;font-style:italic;font-weight:500;color:#DCC9FF;font-size:1.22rem;line-height:1.85;max-width:780px;text-shadow:0 0 26px rgba(167,139,250,.25)}
.defline b{color:#EFE8FF;font-weight:600}
.prose{max-width:820px;margin:0 auto;padding:46px 22px 70px}
.prose h2{font-size:1.35rem;margin:34px 0 12px;padding-left:14px;border-left:3px solid var(--gold)}
.prose h2.first{margin-top:0}
.prose h3{font-size:1.08rem;margin:24px 0 10px}
.prose p{color:#C9C6BF;margin-bottom:14px}
.prose ul{margin:0 0 16px 20px;color:#C9C6BF}.prose li{margin-bottom:8px}
.prose table{width:100%;border-collapse:collapse;margin:18px 0;font-size:.9rem}
.prose th{background:rgba(139,92,246,.12);text-align:left;padding:10px 12px;border:1px solid var(--line)}
.prose td{padding:10px 12px;border:1px solid var(--line);color:#C9C6BF}
details.faq{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-bottom:10px}
details.faq summary{cursor:pointer;font-weight:700;font-size:.95rem}
details.faq p{margin:10px 0 0;color:var(--mut);font-size:.9rem}
.crumb{font-size:.82rem;color:#7B786F;margin-bottom:10px}.crumb a{color:var(--gold2)}
.note{border:1px solid rgba(139,92,246,.3);background:rgba(139,92,246,.06);border-radius:12px;padding:14px 18px;font-size:.88rem;color:#D6CFF2;margin:18px 0}
.vchip{display:inline-flex;align-items:center;gap:6px;font-size:.75rem;font-weight:700;padding:5px 12px;border-radius:999px;border:1px solid rgba(85,199,149,.4);background:rgba(85,199,149,.08);color:#6EE7A0}
.vchip.o{border-color:rgba(139,92,246,.4);background:rgba(139,92,246,.08);color:var(--gold2)}
.ameta{display:flex;gap:14px;align-items:center;font-size:.84rem;color:#7B786F;margin:16px 0 6px;flex-wrap:wrap}
.ameta .av{width:38px;height:38px;border-radius:50%;background:linear-gradient(135deg,var(--gold2),var(--gold));display:grid;place-items:center;font-weight:800;color:#fff}
.cgrid2{display:grid;grid-template-columns:.9fr 1.1fr;gap:26px;align-items:start}
.info-card{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:20px;margin-bottom:14px;display:flex;gap:14px;align-items:flex-start}
.info-card .ic{width:44px;height:44px;border-radius:12px;background:rgba(139,92,246,.12);border:1px solid rgba(139,92,246,.3);display:grid;place-items:center;font-size:1.15rem;flex-shrink:0}
.info-card h4{font-size:.95rem;margin-bottom:3px}.info-card p{font-size:.85rem;color:var(--mut)}
form.cf{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:26px}
.frow{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.fld{margin-bottom:14px}
.fld label{display:block;font-size:.8rem;font-weight:700;letter-spacing:.5px;color:var(--mut);margin-bottom:6px}
.fld input,.fld select,.fld textarea{width:100%;background:rgba(255,255,255,.04);border:1px solid var(--line);border-radius:11px;padding:11px 14px;color:var(--txt);font-size:.92rem;outline:none;transition:border-color .25s;font-family:inherit}
.fld input:focus,.fld select:focus,.fld textarea:focus{border-color:rgba(139,92,246,.55)}
.fld textarea{min-height:130px;resize:vertical}
.fld select{background-color:#14101D;cursor:pointer}
.fld input.srch{transition:border-color .25s,box-shadow .25s;animation:vpulse 1.4s ease 1}
@keyframes vpulse{0%{box-shadow:0 0 0 0 rgba(167,139,250,.45)}70%{box-shadow:0 0 0 10px rgba(167,139,250,0)}100%{box-shadow:0 0 0 0 rgba(167,139,250,0)}}
.fld input.srch:focus{border-color:#A78BFA;box-shadow:0 0 0 4px rgba(167,139,250,.15)}
#sres li{animation:vfade .25s ease both}
@keyframes vfade{from{opacity:0;transform:translateY(5px)}to{opacity:1;transform:none}}
.fld select option{background-color:#14101D;color:#fff}
.fld input:-webkit-autofill,.fld textarea:-webkit-autofill,.fld select:-webkit-autofill{-webkit-box-shadow:0 0 0 1000px #14101D inset;-webkit-text-fill-color:var(--txt);caret-color:var(--txt)}
#toast{position:fixed;bottom:26px;left:50%;transform:translateX(-50%) translateY(80px);background:#1B1B22;border:1px solid rgba(139,92,246,.5);color:var(--txt);padding:13px 22px;border-radius:12px;font-size:.9rem;box-shadow:0 14px 40px rgba(0,0,0,.5);opacity:0;transition:all .4s;z-index:99;max-width:90vw;display:flex;align-items:center;gap:11px}
#toast.show{transform:translateX(-50%) translateY(0);opacity:1}
.toastdot{width:9px;height:9px;border-radius:50%;flex-shrink:0}
.toastdot.ok{background:#34D399;box-shadow:0 0 9px rgba(52,211,153,.9)}
.toastdot.err{background:#F87171;box-shadow:0 0 9px rgba(248,113,113,.9)}
.pop{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:22px;margin-top:26px}
.pop h3{font-size:1rem;margin-bottom:14px}
.pop ol{margin-left:20px;color:#C9C6BF}.pop li{margin-bottom:10px;font-size:.92rem}
.pop a:hover{color:var(--gold2)}
.cathead{display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.cathead .big{width:64px;height:64px;border-radius:18px;display:grid;place-items:center;font-size:1.9rem;background:rgba(255,255,255,.05);border:1px solid var(--line)}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:30px 0}
.stat{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px;text-align:center}
.stat b{display:block;font-size:1.5rem;background:linear-gradient(135deg,#A5B4FC,#7C3AED);-webkit-background-clip:text;background-clip:text;color:transparent}
.stat span{font-size:.78rem;color:var(--mut);letter-spacing:.4px}
/* review box */
.revbox{background:var(--card);border:1px solid rgba(139,92,246,.35);border-radius:var(--r);padding:26px;margin-top:34px}
.revbox .revhead{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:12px}
.revbox .revhead h3{font-size:1.15rem}
.stars{color:#C4B5FD;font-size:1.1rem;letter-spacing:2px}
.stars b{color:#fff;font-size:.85rem;letter-spacing:.5px;margin-left:8px}
.revbox .verdict{font-family:'Newsreader',Georgia,serif;font-style:italic;font-weight:500;color:#DCC9FF;font-size:1.05rem;line-height:1.8;margin-bottom:16px}
.pc{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pc>div{border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:.88rem;color:var(--mut)}
.pc .pros{border-color:rgba(85,199,149,.3)}.pc .cons{border-color:rgba(248,113,113,.3)}
.pc h4{font-size:.72rem;letter-spacing:1.4px;text-transform:uppercase;margin-bottom:8px}
.pc .pros h4{color:#6EE7A0}.pc .cons h4{color:#F08A8A}
.pc ul{list-style:none}.pc li{margin-bottom:6px;padding-left:18px;position:relative}
.pc .pros li::before{content:"✔";position:absolute;left:0;color:#6EE7A0}
.pc .cons li::before{content:"✖";position:absolute;left:0;color:#F08A8A}
.urate{margin-top:20px;padding-top:18px;border-top:1px solid var(--line);display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.ulab{font-size:.72rem;font-weight:800;letter-spacing:1.2px;text-transform:uppercase;color:var(--mut)}
.ustars{font-size:1.6rem;letter-spacing:6px;cursor:pointer;user-select:none;display:inline-flex;gap:2px}
.ustars i,.ustars button{font-style:normal;color:#57546E;transition:transform .15s,color .15s;pointer-events:auto;background:none;border:none;font-size:inherit;padding:0;cursor:pointer;line-height:1}
.ustars i.on,.ustars button.on,.ustars button:hover{color:#C4B5FD}
.ustars button:focus-visible{outline:2px solid #A78BFA;outline-offset:3px;border-radius:4px}
.ustars button:hover{transform:scale(1.22)}
.utext{font-size:.84rem;color:var(--mut)}
.utext b{color:var(--txt)}
.rnote{margin:12px 0 0;font-size:.74rem;color:#7B786F;line-height:1.5}
.revmeta{margin:2px 0 10px;font-size:.78rem;color:#7B786F;letter-spacing:.3px}
@media(max-width:640px){.pc{grid-template-columns:1fr}}
.cimg{height:112px;background-size:cover;background-position:center;position:relative;border-bottom:1px solid var(--line)}
.cimg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,12,26,.08),rgba(16,12,26,.78))}
.ccard{overflow:hidden}
.ccard.hasimg .ic{margin-top:-26px;position:relative;z-index:2}
.catbanner{height:180px;border-radius:18px;background-size:cover;background-position:center;position:relative;overflow:hidden;border:1px solid var(--line);margin-bottom:20px}
.catbanner::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,12,26,.12),rgba(16,12,26,.82))}
@media(max-width:1020px){.cgrid{grid-template-columns:repeat(2,1fr)}.agrid{grid-template-columns:repeat(2,1fr)}
.hero .wrap{grid-template-columns:1fr}.hcards{display:none}.fgrid{grid-template-columns:1fr 1fr}}
@media(max-width:760px){.burger{display:block}
.nav-links{position:absolute;top:64px;left:0;right:0;background:rgba(10,9,14,.97);border-bottom:1px solid var(--line);flex-direction:column;align-items:stretch;padding:12px 18px 18px;gap:4px;max-height:0;overflow:hidden;transition:max-height .4s ease}
.nav-links.open{max-height:400px}
.agrid,.cgrid,.frow,.cgrid2{grid-template-columns:1fr}.fgrid{gap:22px}
section.block{padding:44px 0}.hero{padding:52px 0 40px}.stats{grid-template-columns:repeat(2,1fr)}}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

# ---------------- layout helpers ----------------
SITE = SET.get("site_name", "VelNexis")
SITE_URL = SET.get("site_url", "https://velnexis.netlify.app").rstrip("/")

def nav(active=""):
    def cls(k): return ' class="on"' if k == active else ""
    return f'''<nav class="nav"><div class="wrap">
<a href="index.html" class="logo">{SITE}</a>
<ul class="nav-links" id="navLinks">
<li><a href="index.html"{cls("home")}>Home</a></li>
<li><a href="categories.html"{cls("categories")}>Categories</a></li>
<li><a href="search.html" class="snav{' on' if active == 'search' else ''}">&#128269; Search</a></li>
<li><a href="about.html"{cls("about")}>About</a></li>
<li><a href="privacy.html"{cls("privacy")}>Privacy Policy</a></li>
<li><a href="contact.html"{cls("contact")}>Contact</a></li>
</ul>
<button class="burger" id="burger" aria-label="Menu">☰</button>
</div></nav>'''

def footer():
    cats = "".join(f'<li><a href="category-{k}.html">{CATS[k]["name"]}</a></li>' for k in ORDER[:6])
    return f'''<footer><div class="wrap"><div class="fgrid">
<div>
<a href="index.html" class="logo flogo">{SITE}</a>
<p class="mut ftag">{SET.get("footer_tagline","")}</p>
<p class="mut fcontact">📧 <a class="gold" data-em="{base64.b64encode(SET.get("contact_email","").encode()).decode()}" href="contact.html">Email us</a><br>📍 {SET.get("postal_address","Rawalpindi, Punjab, Pakistan")}</p>
</div>
<div><h3 class="fh">Categories</h3><ul>{cats}<li><a href="categories.html">All categories →</a></li></ul></div>
<div><h3 class="fh">Pages</h3><ul>
<li><a href="index.html">Home</a></li>
<li><a href="about.html">About Us</a></li>
<li><a href="contact.html">Contact Us</a></li>
<li><a href="categories.html">Categories</a></li>
<li><a href="search.html">Search</a></li>
</ul></div>
<div><h3 class="fh">Legal</h3><ul>
<li><a href="privacy.html">Privacy Policy</a></li>
<li><a href="terms.html">Terms &amp; Conditions</a></li>
<li><a href="disclaimer.html">Disclaimer</a></li><li><a href="editorial-policy.html">Editorial Policy</a></li>
</ul></div>
</div>
<div class="fbot"><span>© <span id="yr"></span> {SITE}. All rights reserved · Content updated {time.strftime("%B %Y")}</span><span>Made with care for tech lovers</span></div>
</div></footer>'''

BASE_JS = '''<script>
var b=document.getElementById("burger"),n=document.getElementById("navLinks");
b&&b.addEventListener("click",()=>n.classList.toggle("open"));
var y=document.getElementById("yr");if(y)y.textContent=new Date().getFullYear();
document.querySelectorAll("[data-em]").forEach(function(el){try{var e=atob(el.getAttribute("data-em"));el.textContent=e;el.setAttribute("href","mailto:"+e)}catch(err){}});
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.1});
document.querySelectorAll("[data-rev]").forEach(function(el){io.observe(el)});
function toast(m,ok){var t=document.getElementById("toast");t.innerHTML='<span class="toastdot '+(ok!==false?"ok":"err")+'"></span>'+m;t.classList.add("show");clearTimeout(t._x);t._x=setTimeout(function(){t.classList.remove("show")},3400)}
</script>'''

RATE_JS = '''<script>
document.querySelectorAll(".ustars").forEach(function(el){
  var cat=el.dataset.cat,items=[],cur=null;
  var box=el.closest(".revbox");
  var ut=box?box.querySelector("[data-utext]"):null;
  var form=box?box.querySelector('form[name="reader-rating"]'):null;
  function paint(n){items.forEach(function(x){x.className=(x.dataset.v<=n)?"on":""})}
  function savedText(v){if(ut)ut.innerHTML="Your rating: <b>"+v+"/5</b> — saved on this device ✓"}
  for(var i=1;i<=5;i++){
    var s=document.createElement("button");s.type="button";s.textContent="★";s.dataset.v=i;
    s.setAttribute("aria-label","Rate "+i+" out of 5 stars");
    s.addEventListener("mouseenter",function(){paint(this.dataset.v)});
    el.appendChild(s);items.push(s);
  }
  el.addEventListener("mouseleave",function(){paint(cur)});
  try{cur=localStorage.getItem("vn-rate-"+cat)}catch(e){}
  if(cur){paint(cur);savedText(cur)}
  items.forEach(function(x){x.addEventListener("click",function(){
    cur=x.dataset.v;
    try{localStorage.setItem("vn-rate-"+cat,cur)}catch(e){}
    paint(cur);savedText(cur);toast("Thanks! Your rating has been saved.");
    if(form){
      try{
        var fd=new URLSearchParams();fd.set("form-name","reader-rating");
        fd.set("category",cat);fd.set("rating",cur);fd.set("bot-field","");
        fetch("/",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:fd.toString()}).catch(function(){});
      }catch(e){}
    }
  })});
});
</script>'''

_AID = SET.get("analytics_id", "")
ANA_HOOK = f'\n<meta name="analytics-id" content="{_AID}">\n<!-- Analytics hook: ID set hai par koi SDK bundled nahi. Activation = build.py mein ANA_HOOK ke neeche gtag/pixel snippet add karna. -->' if _AID else ""

def shell(title, desc, body, active="", extra_js="", image="", schema=""):
    image = image or "assets/uploads/og-default.png"  # og:image fallback site-wide
    og_img = (f'\n<meta property="og:image" content="{SITE_URL}/{image}">'
              f'\n<meta name="twitter:card" content="summary_large_image">') if image else '\n<meta name="twitter:card" content="summary">'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preload" href="assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/newsreader-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<meta name="google-site-verification" content="2Uxh3ESC40aQh-Os3qW8hIhYUzSby7SwYoAixbw9bbo">
<link rel="stylesheet" href="assets/fonts/fonts.css">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:type" content="website">{og_img}
{schema}
<link rel="stylesheet" href="assets/site.css">
<script>document.documentElement.classList.add("js")</script>{ANA_HOOK}
</head>
<body>
{nav(active)}
{body}
{footer()}
<div id="toast" role="status"></div>
{BASE_JS}{extra_js}
</body>
</html>'''

def cat_card(k):
    c = CATS[k]
    _img = f"assets/uploads/cats/{k}.jpg"
    _imh = f'<div class="cimg bi-{k}" aria-hidden="true"></div>' if os.path.exists(_img) else ""
    _cls = ("ccard hasimg" if _imh else "ccard") + f" cv-{k}"
    return f'''<article class="{_cls} cv-{k}">
{_imh}<div class="ic">{c["icon"]}</div>
<h3><a class="str" href="category-{k}.html">{c["name"]}</a></h3><p>{c["desc"]}</p>
<div class="cnt">{n_of(k)} guide{"s" if n_of(k)!=1 else ""} →</div></article>'''

def a_card(a):
    c = cat_of(a)
    img = a.get("image", "")
    if img and os.path.exists(os.path.join(ROOT, img)):
        _stem = re.sub(r"[^a-z0-9]+", "-", os.path.basename(img)[:-4])
        thumb = f'<div class="thumb hasimg bi-{_stem}"></div>'
    else:
        thumb = f'<div class="thumb">{a.get("icon","📄")}</div>'
    return f'''<article class="acard cv-{a.get("cat","")}">
{thumb}
<div class="abody"><span class="tag">{c["name"]}</span>
<h3><a class="str" href="articles/{a["id"]}.html">{a.get("title","Untitled")}</a></h3><p>{a.get("excerpt","")}</p>
<div class="meta"><span>📅 {a.get("date","")}</span><span>⏱️ {a.get("mins","5")} min read</span></div></div></article>'''

def review_box(k):
    c = CATS[k]
    r = float(c.get("rating", "4"))
    full = int(r)
    starstr = "★" * full + "☆" * (5 - full)
    pros = "".join(f"<li>{p}</li>" for p in c.get("pros", []))
    cons = "".join(f"<li>{x}</li>" for x in c.get("cons", []))
    n = n_of(k)
    upd = time.strftime("%b %Y")
    return f'''<div class="revbox" data-rev>
<div class="revhead"><h3>Editor's Review — {c["name"]}</h3>
<div class="stars">{starstr}<b>{r}/5</b></div></div>
<div class="revmeta">📚 {n} in-depth guide{"s" if n!=1 else ""} · 🔄 Updated {upd}</div>
<p class="verdict">{c.get("verdict","")}</p>
<div class="pc">
<div class="pros"><h4>What works</h4><ul>{pros}</ul></div>
<div class="cons"><h4>What could improve</h4><ul>{cons}</ul></div>
</div>
<div class="urate">
<span class="ulab">Reader rating</span>
<span class="ustars" data-cat="{k}" aria-label="Rate this category"></span>
<span class="utext" data-utext>Tap a star to rate</span>
</div>
<p class="rnote">The rating above is our editorial opinion. Your rating is saved privately on your device — no account, no tracking.</p>
<form name="reader-rating" data-netlify="true" data-netlify-honeypot="bot-field" hidden aria-hidden="true">
<input type="text" name="bot-field" tabindex="-1" autocomplete="off">
<input type="hidden" name="category" value="{k}">
<input type="hidden" name="rating" value="">
</form>
</div>'''

def write(name, html):
    p = os.path.join(ROOT, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    cu = SITE_URL + "/" if name == "index.html" else SITE_URL + "/" + name
    html = html.replace("</title>", f'</title>\n<link rel="canonical" href="{cu}">', 1)
    open(p, "w", encoding="utf-8").write(html)

# ---------------- GENERATED CSS (category colors + images) ----------------
CATC = "".join(f".cv-{k}{{--t:{c['color']}14;--t1:{c['color']}22;--tc:{c['color']};--tcb:{c['color']}55;--tcbg:{c['color']}14;--tcb2:{c['color']}44;--line2:{c['color']}55}}" for k, c in CATS.items())
_imgs_seen = set()
for _a in ARTS:
    _p = _a.get("image", "")
    if _p: _imgs_seen.add(_p)
for _k in ORDER:
    _imgs_seen.add(f"assets/uploads/cats/{_k}.jpg")
_IMGC = "".join(f".bi-{re.sub(r'[^a-z0-9]+', '-', os.path.basename(_p)[:-4])}{{background-image:url('/{_p}')}}" for _p in sorted(_imgs_seen) if os.path.exists(_p))
CSS = CSS + CATC + _IMGC
os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
_css_min = re.sub(r"/\*.*?\*/", "", CSS, flags=re.S)
_css_min = re.sub(r"\s+", " ", _css_min).replace(" {", "{").replace("{ ", "{").replace(" }", "}").replace("} ", "}")
_css_min = _css_min.replace(";}", "}")
open(os.path.join(ROOT, "assets/site.css"), "w").write(_css_min)

# ---------------- HOME ----------------
trust = "".join(
    f'<li><span class="pk">{SET.get(f"trust{i}_icon","✅")}</span><div><h3>{SET.get(f"trust{i}_title","")}</h3>'
    f'<p>{SET.get(f"trust{i}_text","")}</p></div></li>' for i in range(1, 5))

home_body = f'''<header class="hero"><div class="wrap">
<div>
<h1>{SET.get("hero_heading","")} <span class="gt">{SET.get("hero_accent","")}</span></h1>
<p class="sub">{SET.get("hero_paragraph","")}</p>
<div class="hero-cta">
<a class="btn p" href="categories.html">Explore Categories</a>
<a class="btn g" href="about.html">Why Trust Us →</a>
</div>
</div>
<div class="hcards" aria-hidden="true">
<div class="hglow"></div>
<div class="fcard f1"><h2 class="fch">🧠 Rumor: “AI reads your mind”</h2><span class="no">FALSE — it predicts text patterns, not thoughts</span></div>
<div class="fcard f2"><h2 class="fch">🛡️ Incognito = invisible?</h2><span class="no">NO — your ISP &amp; sites still see you</span></div>
<div class="fcard f3"><h2 class="fch">📱 Battery myth: close all apps</h2><span class="yes">REALITY — it actually drains more battery</span></div>
</div>
</div></header>
<section class="block"><div class="wrap">
<div class="shead" data-rev><div><div class="kicker">Browse</div><h2>All <span class="gt">Categories</span></h2></div></div>
<div class="cgrid" data-rev>{"".join(cat_card(k) for k in ORDER)}</div>
</div></section>
<section class="block pt10"><div class="wrap">
<div class="shead" data-rev><div><div class="kicker">Fresh</div><h2>Latest <span class="gt">Articles</span></h2></div></div>
<div class="agrid" data-rev>{"".join(a_card(a) for a in ARTS[:6])}</div>
</div></section>
<section class="block pt10"><div class="wrap">
<div class="prose prose-c">
<h2>Tech problems, fixed step by step</h2>
<p>Every guide on VelNexis starts the same way: with a real problem someone actually has. The printer that prints blank pages at midnight. The phone that dies by 3pm. The WiFi that works in one room and dies in the next. We take those problems apart, explain what is actually going wrong, and then walk through the fix one step at a time — no guessing, no “restart and pray” unless restarting is genuinely the fix.</p>
<p>The site covers 20 categories, from Windows and Android problems to printers, cameras, payments and AI rumors. Each category is kept small on purpose — it is easier to stay honest and current in a section you can actually keep up with. New articles land every week, and older guides get revisited when menus and app versions change.</p>
<h2>What the articles are like</h2>
<p>Articles here follow a simple pattern. First the quick answer, for people in a hurry. Then the full step by step walkthrough, with settings menus named exactly as you will see them on your screen. Then the “if that didn’t work” section — because the first fix is not always the one that works. Many guides end with a quick recap you can screenshot and keep.</p>
<p>The apps coverage is practical too — Play Store errors, WhatsApp backup failures, notification problems and the rest of the daily grind. No filler anywhere: no ten-paragraph history of the smartphone before the actual fix, no pages built to farm clicks. If a fix takes three lines, the article takes three lines.</p>
<h2>How the guides are written</h2>
<p>VelNexis is written and maintained by Abdul Rafay, a computer science student who has spent years around tech websites — long enough to know what useful writing looks like, and what lazy content looks like. Every article is checked for the things that matter: do the steps match current menus, does the advice hold up, is the warning there when a step carries risk.</p>
<p>When a rumor spreads — “this setting destroys your battery”, “AI reads your WhatsApp” — it gets traced back to where it started and weighed against how the technology actually works. That is the part of this site we care about most: replacing loud claims with boring, useful truth.</p>
<p>Have a problem the site hasn’t covered yet? <a href="contact.html">Send it in</a> — real reader questions shape what gets written next.</p>
</div>
<div class="shead" data-rev><div><div class="kicker">Our Promise</div><h2>Why Readers <span class="gt">Trust {SITE}</span></h2></div></div>
<ul class="plist" data-rev>{trust}</ul>
</div></section>'''

_postal = SET.get("postal_address", "Rawalpindi, Punjab, Pakistan")
_site_schema = '<script type="application/ld+json">' + json.dumps({
    "@context": "https://schema.org",
    "@graph": [
        {"@type": "Organization", "@id": SITE_URL + "/#organization",
         "name": SITE, "url": SITE_URL + "/", "alternateName": "velnexis.netlify.app",
         "publishingPrinciples": SITE_URL + "/editorial-policy.html",
         "logo": {"@type": "ImageObject", "url": SITE_URL + "/assets/uploads/logo.png", "width": 512, "height": 512},
         "contactPoint": {"@type": "ContactPoint", "contactType": "customer support",
                          "url": SITE_URL + "/contact.html", "availableLanguage": ["English"]},
         "founder": {"@type": "Person", "name": "Abdul Rafay", "url": SITE_URL + "/author.html", "jobTitle": "Founder and Tech Writer", "knowsAbout": ["Windows troubleshooting", "Android", "consumer tech", "AI tools", "web publishing"], "sameAs": ["https://github.com/wincobvius"], "worksFor": {"@type": "Organization", "name": SITE, "url": SITE_URL + "/"}},
         "address": {"@type": "PostalAddress", "addressLocality": "Rawalpindi",
                     "addressRegion": "Punjab", "addressCountry": "PK"}},
        {"@type": "WebSite", "@id": SITE_URL + "/#website",
         "name": SITE, "url": SITE_URL + "/",
         "alternateName": "velnexis.netlify.app",
         "potentialAction": {"@type": "SearchAction",
                             "target": {"@type": "EntryPoint", "urlTemplate": SITE_URL + "/search.html?q={search_term_string}"},
                             "query-input": "required name=search_term_string"},
         "publisher": {"@id": SITE_URL + "/#organization"},
         "inLanguage": "en"}
    ]}, ensure_ascii=False) + '</script>'
write("index.html", shell(f"{SITE} — Tech Problems, Apps & Step by Step Guides",
    "Step by step fixes for real tech problems — Windows, Android, iPhone, apps, WiFi, printers and more. 330+ honest articles, zero fluff.",
    home_body, "home", schema=_site_schema))

# ---------------- CATEGORIES PAGE ----------------
cats_body = f'''<div class="phero"><div class="wrap">
<h1>All <span class="gt">Categories</span></h1>
<p>{len(ORDER)} focused sections — each one built around real questions people search for every day.</p>
</div></div>
<section class="block"><div class="wrap wrap860">
<div class="prose">
<h2>Find your fix faster</h2>
<p>Search boxes are great when you know the right words. Categories are better when you just know what is broken. That is the idea behind this page: 20 sections, each built around a specific kind of tech issue, so you can jump straight to the guide that matches yours.</p>
<p>Fixing a Windows PC? The Windows section covers slow boots, blue screens, update failures and the rest. Phone playing up? Android, iPhone and the apps sections handle battery drain, storage trouble, Play Store errors, WhatsApp backups and notification issues. Trying to buy something? The buying guides section has checklists for phones and laptops — what to check, what to ignore, and where cheap usually costs more.</p>
<p>Every category page opens with a short description of what that section covers, then lists its guides. Each section also carries an editor’s review — an honest take on how useful that area of the site currently is, including what could be better. No section is padded to look bigger than it is.</p>
</div>
</div></section>
<section class="block pt0"><div class="wrap">
<div class="shead" data-rev><div><div class="kicker">Browse</div><h2>All <span class="gt">20 categories</span></h2></div></div>
<div class="cgrid g3" data-rev>{"".join(cat_card(k) for k in ORDER)}</div>
</div></section>'''
_cats_schema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "CollectionPage", "name": "All Categories", "url": SITE_URL + "/categories.html", "inLanguage": "en",
     "isPartOf": {"@type": "WebSite", "@id": SITE_URL + "/#website"}},
    {"@type": "ItemList", "name": "VelNexis categories",
     "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": CATS[k]["name"], "url": SITE_URL + "/category-" + k + ".html"} for i, k in enumerate(ORDER)]},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "Categories", "item": SITE_URL + "/categories.html"}]}]}, ensure_ascii=False) + '</script>'
write("categories.html", shell(f"Categories — {SITE}", "Browse all categories.", cats_body, "categories", schema=_cats_schema))

# ---------------- CATEGORY PAGES ----------------
for k in ORDER:
    c = CATS[k]
    lst = [a for a in ARTS if a.get("cat") == k]
    pop = [a for a in ARTS if a.get("cat") != k][:5]
    _img = f"assets/uploads/cats/{k}.jpg"
    _ban = f'<div class="catbanner bi-{k}" aria-hidden="true"></div>' if os.path.exists(_img) else ""
    _intro = c.get("intro", "")
    _intro_sec = ('<section class="block"><div class="wrap wrap860"><div class="prose">' + md(_intro) + '</div></div></section>') if _intro else ""
    _close = c.get("closing", "")
    _close_sec = ('<section class="block pt0"><div class="wrap wrap860"><div class="prose">' + md(_close) + '</div></div></section>') if _close else ""
    body = f'''<div class="phero"><div class="wrap">
{_ban}<div class="crumb"><a href="index.html">Home</a> › <a href="categories.html">Categories</a> › {c["name"]}</div>
<div class="cathead"><div class="big">{c["icon"]}</div>
<div><h1 class="cath1">{c["name"]}</h1><p class="catp">{c["desc"]}</p></div></div>
</div></div>
{_intro_sec}
<section class="block pt0"><div class="wrap">
<div class="shead" data-rev><div><div class="kicker">Guides</div><h2>{len(lst)} fix-it guide{"s" if len(lst)!=1 else ""} in this section</h2></div></div>
<div class="agrid">{"".join(a_card(a) for a in lst)}</div>
{review_box(k)}
</div></section>
{_close_sec}'''
    _cschema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": SITE_URL + f"/category-{k}.html#page", "name": c["name"],
         "description": c.get("desc", ""), "url": SITE_URL + f"/category-{k}.html", "inLanguage": "en",
         "isPartOf": {"@type": "WebSite", "@id": SITE_URL + "/#website"}},
        {"@type": "ItemList", "name": c["name"] + " guides",
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": x.get("title", ""),
                              "url": SITE_URL + "/articles/" + x["id"] + ".html"} for i, x in enumerate(lst)]},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": "Categories", "item": SITE_URL + "/categories.html"},
            {"@type": "ListItem", "position": 3, "name": c["name"]}]}]}, ensure_ascii=False) + '</script>'
    write(f"category-{k}.html", shell(f'{c["name"]} — {SITE}', c.get("desc", ""), body, "categories", RATE_JS, schema=_cschema))

# ---------------- ARTICLE PAGES ----------------
def rebase(html):
    # articles/ subfolder mein pages hain — relative paths ko ../ se root par wapas lao
    html = re.sub(r'(href|src)="(?!https?:|#|mailto:|data:|//)([^"]+)"', r'\1="../\2"', html)
    html = re.sub(r"url[(]'(?!https?:|/|data:|#)([^']+)'[)]", r"url('../\1')", html)
    return html

for a in ARTS:
    c = cat_of(a)
    rel = [x for x in ARTS if x.get("cat") == a.get("cat") and x["id"] != a["id"]] + \
          [x for x in ARTS if x.get("cat") != a.get("cat")]
    rel = rel[:3]
    _img = a.get("image", "")
    if _img and not os.path.exists(os.path.join(ROOT, _img)): _img = ""
    _ahero = f'<img class="ahero" src="{_img}" alt="{a.get("title","").replace(chr(34),"&quot;")}" width="900" height="450" decoding="async">' if _img else ""
    body = f'''<div class="phero"><div class="wrap wrap860">
<div class="crumb"><a href="index.html">Home</a> › <a href="category-{a.get("cat","")}.html">{c["name"]}</a> › {a.get("title","")}</div>
<span class="tag cv-{a.get("cat","")}">{c["name"]}</span>
<h1 class="arth1">{a.get("title","")}</h1>
<div class="ameta"><span class="av">V</span><span><b class="byb"><a class="aul" href="author.html">Abdul Rafay</a></b><br>CS student &amp; tech writer · {a.get("date","")} · {a.get("mins","5")} min read</span>
<span class="vchip">✅ Editor-reviewed</span><span class="vchip o">📅 Published {a.get("date","")}</span></div>
{_ahero}
</div></div>
<div class="prose">{md(a.get("body",""))}
<h2>Related Reads</h2>
<div class="agrid g1">{"".join(a_card(r) for r in rel)}</div>
</div>'''
    _dp = ""
    try:
        _dp = time.strftime("%Y-%m-%d", time.strptime(a.get("date", ""), "%b %d, %Y"))
    except Exception:
        pass
    _graphs = [{"@type": "Article",
           "@id": SITE_URL + "/articles/" + a["id"] + ".html#article",
           "headline": a.get("title", ""),
           "image": [SITE_URL + "/" + _img] if _img else [SITE_URL + "/assets/uploads/og-default.png"],
           "author": {"@type": "Person", "name": "Abdul Rafay", "url": SITE_URL + "/author.html", "jobTitle": "Founder and Tech Writer", "knowsAbout": ["Windows troubleshooting", "Android", "consumer tech", "AI tools", "web publishing"], "sameAs": ["https://github.com/wincobvius"], "worksFor": {"@type": "Organization", "name": SITE, "url": SITE_URL + "/"}},
           "publisher": {"@type": "Organization", "name": SITE, "logo": {"@type": "ImageObject", "url": SITE_URL + "/assets/uploads/logo.png"}},
           "mainEntityOfPage": SITE_URL + "/articles/" + a["id"] + ".html",
           "inLanguage": "en",
           "publishingPrinciples": SITE_URL + "/editorial-policy.html",
           "articleSection": c["name"],
           "wordCount": len(re.sub(r"[#*>\-\[\]()`]", " ", a.get("body", "")).split())}]
    if _dp:
        _graphs[0]["datePublished"] = _dp
        _graphs[0]["dateModified"] = _dp
    _graphs.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": c["name"], "item": SITE_URL + "/category-" + a.get("cat", "") + ".html"},
        {"@type": "ListItem", "position": 3, "name": a.get("title", "")}]})
    _steps = re.findall(r"^\d+\. (.+)$", a.get("body", ""), re.M)
    if len(_steps) >= 3:
        _graphs.append({"@type": "HowTo", "name": a.get("title", ""),
                        "totalTime": "PT" + str(int(a.get("mins", 5)) * 60) + "S",
                        "step": [{"@type": "HowToStep", "position": i + 1, "text": t} for i, t in enumerate(_steps[:12])]})
    _faqs = re.findall(r"^Q: (.+)$\n^A: (.+)$", a.get("body", ""), re.M)
    if _faqs:
        _graphs.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}}
            for q, ans in _faqs]})
    _schema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": _graphs}, ensure_ascii=False) + '</script>'
    write(f'articles/{a["id"]}.html', rebase(shell(f'{a.get("title","")} — {SITE}', a.get("excerpt", a.get("title", "")), body, "categories", image=_img, schema=_schema)))

# ---------------- ABOUT (pages/about.txt) ----------------
def render_page(name):
    _, raw = split_fm(open(C("pages", name + ".md"), encoding="utf-8").read())
    n_cats = sum(1 for k in ORDER if n_of(k) > 0)
    stats_html = f'''<div class="stats">
<div class="stat"><b>{len(ARTS)}+</b><span>In-depth guides</span></div>
<div class="stat"><b>{n_cats}</b><span>Focused categories</span></div>
<div class="stat"><b>100%</b><span>Independent</span></div>
<div class="stat"><b>0</b><span>Sponsored verdicts</span></div>
</div>'''
    team_html = '''<a class="authcard" href="author.html">
<span class="avatar">AR</span>
<span class="ainfo"><b>Abdul Rafay</b>
<span class="arole">Founder &amp; Author — VelNexis</span>
<span class="abio">CS student, tech writer, and the person behind every guide on this site.</span>
<span class="amore">Read more about me →</span></span></a>'''
    html = md(raw).replace("<p>((stats))</p>", stats_html).replace("<p>((team))</p>", team_html)
    # pehla h2 .first class
    html = html.replace("<h2>", '<h2 class="first">', 1)
    return html

about_body = f'''<div class="phero"><div class="wrap">
<h1>About <span class="gt">{SITE}</span></h1>
</div></div>
<div class="prose">{render_page("about")}</div>'''
_about_schema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "AboutPage", "url": SITE_URL + "/about.html", "name": "About " + SITE, "inLanguage": "en",
     "mainEntity": {"@id": SITE_URL + "/#organization"},
     "isPartOf": {"@type": "WebSite", "@id": SITE_URL + "/#website"}},
    {"@type": "Person", "name": "Abdul Rafay", "url": SITE_URL + "/author.html",
     "jobTitle": "Founder and Tech Writer",
     "knowsAbout": ["Windows troubleshooting", "Android", "consumer tech", "AI tools", "web publishing"], "sameAs": ["https://github.com/wincobvius"],
     "worksFor": {"@id": SITE_URL + "/#organization"}},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "About Us", "item": SITE_URL + "/about.html"}]}]}, ensure_ascii=False) + '</script>'
write("about.html", shell(f"About Us — {SITE}", "About " + SITE + ": mission, standards and the author behind it.", about_body, "about", schema=_about_schema))

# ---------------- AUTHOR PAGE (pages/author.md) ----------------
_ap = split_fm(open(C("pages", "author.md"), encoding="utf-8").read())
_author_facts = f'''<div class="stats">
<div class="stat"><b>{len(ARTS)}+</b><span>Guides written</span></div>
<div class="stat"><b>{len(ORDER)}</b><span>Categories covered</span></div>
<div class="stat"><b>🎓</b><span>BS Computer Science (in progress)</span></div>
<div class="stat"><b>💻</b><span>Multiple tech sites built</span></div>
</div>'''
_author_body = f'''<div class="phero"><div class="wrap wrap760">
<div class="crumb"><a href="index.html">Home</a> › <a href="about.html">About</a> › Author</div>
<div class="apage-head">
<div class="avatar">AR</div>
<h1>Abdul <span class="gt">Rafay</span></h1>
<span class="arole">Founder &amp; Author — VelNexis</span>
</div>
</div></div>
<div class="prose">{md(_ap[1])}
{_author_facts}
<div class="center"><a class="ctabtn" href="contact.html">Get in touch ✉</a></div>
</div>'''
_person_schema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "Person", "name": "Abdul Rafay", "url": SITE_URL + "/author.html",
     "jobTitle": "Founder & Author", "worksFor": {"@type": "Organization", "name": SITE},
     "knowsAbout": ["Windows troubleshooting", "Android", "consumer tech", "AI tools", "web publishing"], "sameAs": ["https://github.com/wincobvius"]},
    {"@type": "AboutPage", "url": SITE_URL + "/author.html", "mainEntity": {"@type": "Person", "name": "Abdul Rafay"}},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "Abdul Rafay", "item": SITE_URL + "/author.html"}]}]},
    ensure_ascii=False) + '</script>'
write("author.html", shell(f"Abdul Rafay — Founder & Author, {SITE}", "Meet Abdul Rafay — the founder and author behind " + SITE + ".", _author_body, "about", schema=_person_schema))

# ---------------- CONTACT ----------------
contact_body = f'''<div class="phero"><div class="wrap">
<h1>Get in <span class="gt">Touch</span></h1>
<p>Questions, tips, rumor reports, or corrections — we usually reply within 48 hours.</p>
</div></div>
<section class="block pt0"><div class="wrap wrap860"><div class="prose">
<h2>Before you write — it makes replies faster</h2>
<p>A good message gets a good answer, usually the same day. A vague one goes back and forth for a week. If you are reporting a tech problem, include four things: the device (phone model or PC specs), the operating system and its version, the exact error message if there is one, and what you already tried. With those four lines, most problems get a real diagnosis in the first reply instead of questions.</p>
<p>Reporting a viral rumor? Paste the message or screenshot text you received, and mention where it reached you — a WhatsApp group, a YouTube video, a forwarded SMS. Origin matters: half of every rumor check is tracing where the claim started, and your first-hand source is often the missing piece.</p>
<p>Found an error in a guide? Say which article and which step, and what happened when you followed it. Corrections get priority treatment — wrong steps on a site people use for fixes are the one thing we take more seriously than rumors.</p>
<p>One honest note: there is no phone line and no live chat. This is a one-author publication, and written replies are how it stays accurate — every answer can be checked, linked and corrected later. Advertising and partnership queries are welcome too; pick the matching subject below so nothing lands in the wrong pile.</p>
</div></div></section>
<section class="block pt0"><div class="wrap">
<div class="cgrid2" data-rev>
<div>
<div class="info-card"><div class="ic">📧</div><div><h2 class="ich">Email</h2><p><a class="gold" data-em="{base64.b64encode(SET.get("contact_email","").encode()).decode()}" href="contact.html">Email us</a></p></div></div>
<div class="info-card"><div class="ic">⏱️</div><div><h2 class="ich">Response Time</h2><p>{SET.get("contact_response","48 hours")}</p></div></div>
<div class="info-card"><div class="ic">🔥</div><div><h2 class="ich">Rumor Reports</h2><p>Seen a viral tech claim? Send it — we’ll investigate &amp; publish the verdict.</p></div></div>
</div>
<form class="cf" id="ctForm" name="contact" method="POST" data-netlify="true" netlify-honeypot="bot-field">
<input type="hidden" name="form-name" value="contact">
<p class="hp" aria-hidden="true"><label>Leave empty: <input name="bot-field" tabindex="-1"></label></p>
<div class="frow">
<div class="fld"><label>Your Name</label><input type="text" name="name" placeholder="Ali Khan" required></div>
<div class="fld"><label>Your Email</label><input type="email" name="email" placeholder="you@email.com" required></div>
</div>
<div class="fld"><label>Subject</label>
<select name="subject"><option>General question</option><option>Rumor check request</option><option>Correction / feedback</option><option>Advertising</option><option>Other</option></select>
</div>
<div class="fld"><label>Message</label><textarea name="message" rows="6" placeholder="Write your message…" required></textarea></div>
<button class="btn p btnw" type="submit">Send Message</button>
</form>
</div>
</div></section>'''
contact_js = '''<script>
var cf=document.getElementById("ctForm");
cf&&cf.addEventListener("submit",function(e){
  e.preventDefault();
  var btn=cf.querySelector("button[type=submit]");btn.disabled=true;btn.textContent="Sending…";
  fetch("/",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:new URLSearchParams(new FormData(cf)).toString()})
  .then(function(){cf.reset();toast("Message sent! We usually reply within 48 hours.");btn.disabled=false;btn.textContent="Send Message";})
  .catch(function(){toast("Could not send — please email us directly at "+cf.dataset.email,false);btn.disabled=false;btn.textContent="Send Message";});
});
</script>'''
_contact_schema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "ContactPage", "url": SITE_URL + "/contact.html", "name": "Contact " + SITE, "inLanguage": "en",
     "mainEntity": {"@type": "Organization", "name": SITE, "url": SITE_URL + "/",
                    "contactPoint": {"@type": "ContactPoint", "contactType": "customer support",
                                     "url": SITE_URL + "/contact.html", "availableLanguage": "English"}},
     "isPartOf": {"@type": "WebSite", "@id": SITE_URL + "/#website"}},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "Contact Us", "item": SITE_URL + "/contact.html"}]}]}, ensure_ascii=False) + '</script>'
write("contact.html", shell(f"Contact Us — {SITE}", "Contact " + SITE + " — questions, rumor reports and corrections, answered within 48 hours.", contact_body, "contact", contact_js, schema=_contact_schema))

# ---------------- LEGAL PAGES ----------------
for pg, title, desc in [("privacy", "Privacy Policy", "Privacy Policy: cookies, analytics, AdSense, GDPR."),
                        ("terms", "Terms & Conditions", "Terms and Conditions of use."),
                        ("disclaimer", "Disclaimer", "Disclaimer: general information and advice notice."),
                        ("editorial-policy", "Editorial Policy", "Editorial Policy: how VelNexis researches, writes and corrects its guides.")]:
    body = f'''<div class="phero"><div class="wrap"><h1>{title.replace("Privacy Policy", "<span class=\\'gt\\'>Privacy Policy</span>").replace("Terms & Conditions","Terms &amp; <span class=\\'gt\\'>Conditions</span>").replace("Disclaimer","<span class=\\'gt\\'>Disclaimer</span>")}</h1><p>Last updated: September 2026</p></div></div>
<div class="prose">{render_page(pg)}</div>'''
    _bschema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": title}]}]}, ensure_ascii=False) + '</script>'
    write(f"{pg}.html", shell(f"{title} — {SITE}", desc, body, "privacy", schema=_bschema))

# ---------------- 404 ----------------
nf_body = '''<div class="phero"><div class="wrap nfhero">
<div class="nf404">404</div>
<h1 class="nfh1">This page took a wrong <span class="gt">turn</span></h1>
<p class="mut nfp">The link is broken or the page moved. The fix is one click away — that's what we do here.</p>
<h2 class="nfh2">Popular ways back</h2>
<div class="nfbtns">
<a class="btn p" href="index.html">Back to Home</a>
<a class="btn g" href="categories.html">Browse Categories</a>
</div>
</div></div>'''
write("404.html", shell(f"Page not found — {SITE}", "Page not found.", nf_body))

# ---------------- SEARCH ----------------
open(os.path.join(ROOT, "assets/search-index.js"), "w").write(
    "window.VN_INDEX=" + json.dumps([{"t": a.get("title", ""), "u": "articles/" + a["id"] + ".html", "c": cat_of(a)["name"]} for a in ARTS], ensure_ascii=False) + ";")
_pop_slugs = ["my-printer-is-printing-blank-pages", "wifi-connected-no-internet", "overnight-charging",
               "my-phone-battery-drains-very-fast", "win-slow-update", "blue-screen-error-keeps-coming-again-and-again",
               "can-ai-read-my-whatsapp-chats", "my-email-shows-a-login-from-another-country"]
_pop = [_a for _s in _pop_slugs for _a in ARTS if _a["id"] == _s]
_search_body = '''<div class="phero"><div class="wrap">
<h1>Search <span class="gt">VelNexis</span></h1>
<p>330 fix-it guides and rumor checks — type what is broken.</p>
</div></div>
<section class="block pt0"><div class="wrap wrap860">
<div class="fld"><label for="sq">Search guides</label><input type="search" id="sq" class="srch" placeholder="printer blank pages, wifi connected no internet, overnight charging..." autocomplete="off"></div>
<div class="prose"><h2>Results</h2><p class="mut" id="scount">Type at least two letters.</p><ul id="sres"></ul></div>
<div id="spop">
<div class="prose"><h2>Popular searches</h2><p class="mut">The guides people open most — start here, or type your own problem above.</p></div>
<div class="agrid g1">''' + "".join(a_card(x) for x in _pop) + '''</div>
</div>
</div></section>'''
_search_js = '''<script src="assets/search-index.js" defer></script>
<script>
(function(){
var el=document.getElementById("sq"),res=document.getElementById("sres"),cnt=document.getElementById("scount"),pop=document.getElementById("spop");
function esc(s){return s.replace(/[&<>'"']/g,function(c){return c==="&"?"&amp;":c==="<"?"&lt;":c===">"?"&gt;":c==="'"?"&#39;":"&quot;"})}
function run(){
var v=el.value.trim().toLowerCase();
if(v.length<2){cnt.textContent="Type at least two letters.";res.innerHTML="";if(pop){pop.style.display=""}return}
var idx=window.VN_INDEX||[];
var hits=idx.filter(function(x){return x.t.toLowerCase().indexOf(v)>-1}).slice(0,50);
cnt.textContent=hits.length+" guide"+(hits.length===1?"":"s")+" found"+(hits.length===50?" - showing first 50":"")+".";
if(pop){pop.style.display=hits.length?"none":""}
res.innerHTML=hits.map(function(x){return "<li><a class='gold' href='"+x.u+"'>"+esc(x.t)+"</a> <span class='mut'>"+esc(x.c)+"</span></li>"}).join("");
}
el.addEventListener("input",run);
var q=new URLSearchParams(location.search).get("q")||"";
if(q){el.value=q}
if(window.matchMedia&&matchMedia("(pointer:fine)").matches){setTimeout(function(){el.focus()},400)}
window.addEventListener("load",run);
})();
</script>'''
_search_schema = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": [
    {"@type": "WebPage", "url": SITE_URL + "/search.html", "name": "Search — " + SITE, "inLanguage": "en",
     "isPartOf": {"@type": "WebSite", "@id": SITE_URL + "/#website"}},
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"},
        {"@type": "ListItem", "position": 2, "name": "Search", "item": SITE_URL + "/search.html"}]}]}, ensure_ascii=False) + '</script>'
write("search.html", shell(f"Search — {SITE}", "Search all VelNexis tech fix guides and rumor checks.", _search_body, "search", _search_js, schema=_search_schema))

# ---------------- SITEMAP / ROBOTS ----------------
urls = ["", "search.html", "categories.html", "about.html", "author.html", "contact.html", "privacy.html", "terms.html", "disclaimer.html", "editorial-policy.html"] \
     + [f"category-{k}.html" for k in ORDER] + [f"articles/{a['id']}.html" for a in ARTS]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     "".join(f"<url><loc>{SITE_URL}/{u}</loc></url>\n" for u in urls) + "</urlset>"
open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
_robots = ["User-agent: *", "Allow: /", "",
 "# Explicitly welcome AI/answer engines:", "User-agent: GPTBot", "Allow: /", "",
 "User-agent: ClaudeBot", "Allow: /", "", "User-agent: PerplexityBot", "Allow: /", "",
 "User-agent: Google-Extended", "Allow: /", "", "User-agent: Applebot-Extended", "Allow: /", "",
 "Sitemap: " + SITE_URL + "/sitemap.xml", ""]
open(os.path.join(ROOT, "robots.txt"), "w").write("\n".join(_robots))

# ---------------- LLMOS.TXT (AI crawlers ke liye) ----------------
_llmd = f"""# {SITE}

> {SET.get("footer_tagline", "")}

{SITE} publishes step by step tech guides and honest rumor checks: Windows, Android, iPhone, apps, WiFi, printers, cameras, payments, AI and more. {len(ARTS)} articles across {len(ORDER)} categories, written by Abdul Rafay.

## Key pages

- [Home]({SITE_URL}/): latest articles and all categories
- [All Categories]({SITE_URL}/categories.html): every section in one place
- [Search]({SITE_URL}/search.html): search all {len(ARTS)} guides by keyword
- [About]({SITE_URL}/about.html): how the site works and its editorial standards
- [Author]({SITE_URL}/author.html): Abdul Rafay, founder and author
- [Contact]({SITE_URL}/contact.html): questions, corrections and rumor reports
- [Privacy Policy]({SITE_URL}/privacy.html): data and cookie policy
- [Sitemap]({SITE_URL}/sitemap.xml): full URL list

## Categories

"""
for _k in ORDER:
    _c = CATS[_k]
    _llmd += f"- [{_c['name']}]({SITE_URL}/category-{_k}.html): {_c.get('desc','')}\n"
    for _a2 in ARTS:
        if _a2.get("cat") == _k:
            _llmd += f"  - [{_a2.get('title','')}]({SITE_URL}/articles/{_a2['id']}.html)\n"
_llmd += f"""
## Content notes

- Guides are practical: quick answer first, then full step by step instructions.
- Rumor articles trace claims to their source and give a plain verdict.
- Updated {time.strftime("%B %Y")}. Contact: {SITE_URL}/contact.html
"""
open(os.path.join(ROOT, "llms.txt"), "w").write(_llmd)

write_fonts_css()
print(f"DONE — {len(ARTS)} articles, {len(ORDER)} categories, {len(urls)+2} files")
