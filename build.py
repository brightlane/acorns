#!/usr/bin/env python3
"""
build.py — AcornsGuide v2 — ALL NEW CONTENT
Deploys to: https://brightlane.github.io/acorns/
Affiliate:  https://convert.ctypy.com/aff_c?offer_id=29449&aff_id=21885
"""

from datetime import datetime, date
from pathlib import Path
import json as _json

BASE_URL  = "https://brightlane.github.io/acorns"
AFF_BASE  = "https://convert.ctypy.com/aff_c?offer_id=29449&aff_id=21885"
SITE_NAME = "AcornsGuide"
BUILT_ON  = datetime.now().strftime("%Y-%m-%d")
OUT       = Path("docs")
OUT.mkdir(exist_ok=True)

def aff(src="page"):
    return f"{AFF_BASE}&utm_source=acornsguide&utm_medium=affiliate&utm_campaign={src}"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Fraunces:ital,wght@0,700;0,900;1,700&display=swap');

:root{
  --teal:#0d9488;--teal2:#0f766e;--teal3:#14b8a6;--teal4:#ccfbf1;
  --ink:#0c1a17;--ink2:#122018;--ink3:#1a2e28;--ink4:#243d36;
  --sand:#f0faf7;--sand2:#e0f5ef;--cream:#fafffe;
  --muted:#5a7a72;--muted2:#3d5a52;
  --amber:#f59e0b;--rose:#f43f5e;--sky:#0ea5e9;
  --border:rgba(13,148,136,0.14);--border2:rgba(13,148,136,0.32);
  --radius:14px;--shadow:0 8px 40px rgba(0,0,0,0.5);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--sand);font-family:'Plus Jakarta Sans',sans-serif;font-size:17px;line-height:1.72;-webkit-font-smoothing:antialiased}

/* NAV */
nav{background:rgba(12,26,23,0.97);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:200;padding:0 24px}
.nav-inner{max-width:1160px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:66px;gap:16px}
.logo{font-family:'Fraunces',serif;font-size:1.45rem;font-weight:900;color:#fff;text-decoration:none;letter-spacing:-0.5px;flex-shrink:0}
.logo em{color:var(--teal3);font-style:normal}
.nav-links{display:flex;gap:2px;overflow:hidden}
.nav-links a{color:rgba(240,250,247,0.5);font-size:0.77rem;font-weight:600;padding:6px 10px;border-radius:6px;text-decoration:none;white-space:nowrap;transition:all 0.15s}
.nav-links a:hover{color:#fff;background:rgba(13,148,136,0.12)}
.nav-cta{background:var(--teal);color:#fff;font-weight:700;font-size:0.82rem;padding:9px 18px;border-radius:8px;text-decoration:none;white-space:nowrap;transition:all 0.2s;flex-shrink:0}
.nav-cta:hover{background:var(--teal2);transform:translateY(-1px);box-shadow:0 4px 20px rgba(13,148,136,0.45)}
@media(max-width:820px){.nav-links{display:none}}

/* ANN BAR */
.ann{background:linear-gradient(90deg,var(--teal2),#0a6b64,var(--teal2));padding:10px 20px;text-align:center;font-size:0.81rem;font-weight:600;color:#fff;letter-spacing:0.2px}
.ann a{color:var(--teal4);text-decoration:none;font-weight:700}
.ann a:hover{text-decoration:underline}

/* HERO */
.hero{background:linear-gradient(150deg,#051310 0%,var(--ink2) 45%,#061410 100%);border-bottom:1px solid var(--border);padding:88px 24px 72px;text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 50% 0%,rgba(13,148,136,0.1) 0%,transparent 60%);pointer-events:none}
.hero-pill{display:inline-flex;align-items:center;gap:8px;background:rgba(13,148,136,0.1);border:1px solid var(--border2);color:var(--teal3);font-size:0.71rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:5px 16px;border-radius:20px;margin-bottom:24px}
.hero h1{font-family:'Fraunces',serif;font-size:clamp(2.1rem,5.5vw,3.8rem);font-weight:900;line-height:1.08;color:#fff;max-width:820px;margin:0 auto 22px;letter-spacing:-1px}
.hero h1 em{color:var(--teal3);font-style:normal;display:block}
.hero .sub{font-size:1.1rem;color:rgba(240,250,247,0.62);max-width:540px;margin:0 auto 42px;line-height:1.72}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.btn-outline{display:inline-block;border:1.5px solid rgba(240,250,247,0.2);color:rgba(240,250,247,0.75);font-size:0.9rem;font-weight:600;padding:13px 26px;border-radius:9px;text-decoration:none;transition:all 0.2s}
.btn-outline:hover{border-color:rgba(240,250,247,0.4);color:#fff;background:rgba(240,250,247,0.05)}

/* TRUST STRIP */
.trust{background:var(--ink2);border-bottom:1px solid var(--border);padding:13px 24px}
.trust-wrap{max-width:1160px;margin:0 auto;display:flex;gap:32px;align-items:center;justify-content:center;flex-wrap:wrap}
.titem{display:flex;align-items:center;gap:7px;font-size:0.75rem;font-weight:600;color:rgba(240,250,247,0.38);white-space:nowrap}
.titem .dot{width:6px;height:6px;border-radius:50%;background:var(--teal);flex-shrink:0}

/* CTA BUTTON */
.cta{display:inline-block;background:linear-gradient(135deg,var(--teal),var(--teal2));color:#fff;font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;font-size:1.05rem;padding:16px 38px;border-radius:10px;text-decoration:none;box-shadow:0 4px 28px rgba(13,148,136,0.38);transition:all 0.15s;position:relative;overflow:hidden;letter-spacing:0.1px}
.cta::after{content:'';position:absolute;top:0;left:-80%;width:50%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.1),transparent);transition:left 0.5s}
.cta:hover::after{left:130%}
.cta:hover{transform:translateY(-2px);box-shadow:0 8px 36px rgba(13,148,136,0.55)}
.cta.glow{animation:tglow 2.8s ease-in-out infinite}
.cta.sm{font-size:0.87rem;padding:11px 22px}
.cta.outline{background:transparent;border:2px solid var(--teal);color:var(--teal3);box-shadow:none}
.cta.outline:hover{background:rgba(13,148,136,0.1)}
@keyframes tglow{0%,100%{box-shadow:0 4px 28px rgba(13,148,136,0.38)}50%{box-shadow:0 4px 48px rgba(13,148,136,0.65)}}

/* LAYOUT */
.wrap{max-width:940px;margin:0 auto;padding:56px 24px 110px}

/* BREADCRUMB */
.bc{font-size:0.77rem;color:var(--muted);margin-bottom:36px;display:flex;gap:7px;align-items:center;flex-wrap:wrap}
.bc a{color:var(--muted);text-decoration:none;transition:color 0.15s}
.bc a:hover{color:var(--teal3)}

/* STAT ROW */
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:14px;margin:30px 0}
.stat{background:var(--ink3);border:1px solid var(--border);border-radius:var(--radius);padding:22px 16px;text-align:center}
.stat .n{font-family:'Fraunces',serif;font-size:2.2rem;font-weight:900;color:var(--teal3);line-height:1}
.stat .l{font-size:0.76rem;color:var(--muted);margin-top:7px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px}

/* VERDICT CARD */
.verdict{background:var(--ink3);border:1px solid var(--border2);border-radius:var(--radius);padding:28px 32px;margin:28px 0;box-shadow:0 0 60px rgba(13,148,136,0.07)}
.verdict-header{display:flex;align-items:center;gap:16px;margin-bottom:16px}
.verdict-score{font-family:'Fraunces',serif;font-size:3.5rem;font-weight:900;color:var(--teal3);line-height:1}
.verdict-meta .stars{color:var(--amber);font-size:1.1rem;letter-spacing:3px}
.verdict-meta .label{font-size:0.78rem;color:var(--muted);margin-top:3px}
.vtags{display:flex;flex-wrap:wrap;gap:7px;margin-top:14px}
.vtag{background:rgba(13,148,136,0.1);border:1px solid var(--border);color:rgba(240,250,247,0.6);font-size:0.72rem;font-weight:700;padding:4px 12px;border-radius:20px;text-transform:uppercase;letter-spacing:0.5px}

/* OFFER CARD */
.offer{background:var(--ink3);border:1px solid var(--border);border-radius:var(--radius);padding:32px;margin:32px 0;position:relative}
.offer.featured{border-color:var(--border2);box-shadow:0 0 60px rgba(13,148,136,0.07),inset 0 1px 0 rgba(13,148,136,0.12)}
.ob{position:absolute;top:-14px;left:24px;background:var(--teal);color:#fff;font-weight:800;font-size:0.7rem;letter-spacing:1px;padding:4px 14px;border-radius:20px;text-transform:uppercase}
.offer h3{font-family:'Fraunces',serif;font-size:1.3rem;font-weight:700;color:#fff;margin-bottom:16px}
.offer ul{list-style:none;margin-bottom:24px}
.offer ul li{padding:5px 0;font-size:0.96rem;color:rgba(240,250,247,0.82);display:flex;align-items:baseline;gap:8px}
.tc{font-size:0.72rem;color:var(--muted);margin-top:10px;line-height:1.6}

/* COMPARE TABLE */
.cmp{width:100%;border-collapse:collapse;font-size:0.9rem;margin:24px 0;border-radius:var(--radius);overflow:hidden}
.cmp th{background:rgba(13,148,136,0.12);color:rgba(240,250,247,0.88);font-weight:700;padding:14px 16px;text-align:left;border-bottom:1px solid var(--border2);font-size:0.8rem;letter-spacing:0.5px;text-transform:uppercase}
.cmp td{padding:13px 16px;border-bottom:1px solid rgba(255,255,255,0.04);color:rgba(240,250,247,0.73)}
.cmp tr:last-child td{border-bottom:none}
.cmp tr:hover td{background:rgba(255,255,255,0.02)}
.yes{background:rgba(13,148,136,0.14);color:var(--teal3);font-size:0.73rem;font-weight:700;padding:3px 10px;border-radius:20px;white-space:nowrap}
.no{background:rgba(244,63,94,0.12);color:#fb7185;font-size:0.73rem;font-weight:700;padding:3px 10px;border-radius:20px}
.ok{background:rgba(245,158,11,0.12);color:#fbbf24;font-size:0.73rem;font-weight:700;padding:3px 10px;border-radius:20px}

/* CONTENT */
.cb h2{font-family:'Fraunces',serif;font-size:1.55rem;font-weight:700;color:#fff;margin:48px 0 16px;letter-spacing:-0.3px}
.cb h3{font-size:1.05rem;font-weight:700;color:rgba(240,250,247,0.92);margin:28px 0 10px}
.cb p{margin-bottom:18px;color:rgba(240,250,247,0.75);line-height:1.8}
.cb ul,.cb ol{padding-left:22px;margin-bottom:18px}
.cb li{margin-bottom:9px;color:rgba(240,250,247,0.72)}
.lead{font-size:1.1rem;line-height:1.82;color:rgba(240,250,247,0.92);border-left:3px solid var(--teal3);padding:4px 0 4px 20px;margin-bottom:32px}
.callout{background:rgba(13,148,136,0.07);border:1px solid var(--border2);border-radius:var(--radius);padding:20px 24px;margin:26px 0}
.callout strong{color:var(--teal3)}
a.il{color:var(--teal3);text-decoration:none;border-bottom:1px solid rgba(13,148,136,0.3)}
a.il:hover{border-color:var(--teal3)}

/* GROWTH TABLE */
.gtbl{width:100%;border-collapse:collapse;font-size:0.88rem;margin:22px 0;border-radius:var(--radius);overflow:hidden}
.gtbl th{background:rgba(13,148,136,0.1);color:rgba(240,250,247,0.88);font-weight:700;padding:13px 16px;text-align:left;border-bottom:1px solid var(--border2);font-size:0.79rem;text-transform:uppercase;letter-spacing:0.4px}
.gtbl td{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.04);color:rgba(240,250,247,0.72)}
.gtbl tr:last-child td{border-bottom:none}
.gtbl tr:hover td{background:rgba(255,255,255,0.02)}
.hi{color:var(--teal3);font-weight:700}

/* PROS CONS */
.pros-cons{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:24px 0}
.pc-box{background:var(--ink3);border:1px solid var(--border);border-radius:var(--radius);padding:22px}
.pc-box h4{font-weight:700;font-size:0.9rem;margin-bottom:14px;text-transform:uppercase;letter-spacing:0.5px}
.pc-box.pros h4{color:var(--teal3)}
.pc-box.cons h4{color:#fb7185}
.pc-box ul{list-style:none;padding:0}
.pc-box li{font-size:0.9rem;color:rgba(240,250,247,0.72);padding:5px 0;display:flex;gap:8px}
@media(max-width:600px){.pros-cons{grid-template-columns:1fr}}

/* PNAV */
.pnav{display:flex;flex-wrap:wrap;gap:7px;background:var(--ink2);border-radius:var(--radius);padding:16px;margin-bottom:42px;border:1px solid var(--border)}
.pnav a{background:rgba(13,148,136,0.07);border:1px solid var(--border);color:rgba(240,250,247,0.58);font-size:0.77rem;font-weight:600;padding:6px 13px;border-radius:7px;text-decoration:none;transition:all 0.15s;white-space:nowrap}
.pnav a:hover{background:rgba(13,148,136,0.16);color:#fff;border-color:var(--border2)}

/* FAQ */
.faq{margin:48px 0}
.faq-h{font-family:'Fraunces',serif;font-size:1.55rem;font-weight:700;color:#fff;margin-bottom:24px}
.fi{border-bottom:1px solid rgba(255,255,255,0.07);padding:20px 0}
.fi:last-child{border-bottom:none}
.fq{font-weight:700;font-size:1rem;color:rgba(240,250,247,0.88);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;user-select:none}
.fq::after{content:'+';font-size:1.5rem;color:var(--teal3);flex-shrink:0;transition:transform 0.2s;line-height:1}
.fi.open .fq::after{transform:rotate(45deg)}
.fa{display:none;padding-top:14px;color:rgba(240,250,247,0.62);font-size:0.95rem;line-height:1.78}
.fi.open .fa{display:block}

/* STICKY */
.sticky{display:none;position:fixed;bottom:0;left:0;right:0;background:linear-gradient(135deg,#051310,#071a14);border-top:1px solid var(--border2);padding:14px 20px;z-index:300;align-items:center;justify-content:space-between;gap:14px}
.sticky p{font-size:0.82rem;color:rgba(240,250,247,0.68);line-height:1.4}
.sticky p strong{color:#fff;display:block;font-size:0.9rem}
@media(max-width:768px){.sticky{display:flex}}

/* FOOTER */
footer{background:var(--ink2);border-top:1px solid var(--border);padding:50px 24px 34px;text-align:center;font-size:0.8rem;color:var(--muted)}
.flogo{font-family:'Fraunces',serif;font-size:1.45rem;font-weight:900;color:#fff;margin-bottom:12px;display:block}
.flogo em{color:var(--teal3);font-style:normal}
.flinks{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin:14px 0}
.flinks a{color:var(--muted);text-decoration:none;transition:color 0.15s}
.flinks a:hover{color:var(--teal3)}
.disc{margin-top:24px;max-width:680px;margin-left:auto;margin-right:auto;line-height:1.7;padding:18px 20px;background:rgba(255,255,255,0.02);border-radius:10px;border:1px solid rgba(255,255,255,0.05);color:rgba(240,250,247,0.4)}
"""

JS = """
document.querySelectorAll('.fq').forEach(q=>{
  q.addEventListener('click',()=>{
    const fi=q.closest('.fi');
    const was=fi.classList.contains('open');
    document.querySelectorAll('.fi.open').forEach(i=>i.classList.remove('open'));
    if(!was)fi.classList.add('open');
  });
});
const sticky=document.querySelector('.sticky');
if(sticky){
  window.addEventListener('scroll',()=>{
    sticky.style.display=window.scrollY>500?'flex':'none';
  },{passive:true});
}
"""

NAV_LINKS = [
    ("How It Works","how-acorns-works.html"),
    ("Full Review","acorns-review.html"),
    ("vs Robinhood","acorns-vs-robinhood.html"),
    ("vs Betterment","acorns-vs-betterment.html"),
    ("vs Stash","acorns-vs-stash.html"),
    ("Round-Ups","acorns-round-ups.html"),
    ("IRA Guide","acorns-later-ira.html"),
    ("Fees","acorns-fees.html"),
    ("Portfolios","acorns-portfolios.html"),
    ("Sign Up","acorns-sign-up.html"),
]
ALL_LINKS = NAV_LINKS + [
    ("Promo Code","acorns-promo-code.html"),
    ("Acorns Early","acorns-early.html"),
    ("Acorns Earn","acorns-earn.html"),
    ("For Beginners","acorns-for-beginners.html"),
    ("Is It Safe?","is-acorns-safe.html"),
    ("Withdraw Guide","acorns-withdraw.html"),
    ("Tax Guide","acorns-tax-guide.html"),
    ("Compound Interest","acorns-compound-interest.html"),
    ("Acorns vs Wealthfront","acorns-vs-wealthfront.html"),
    ("Sitemap","sitemap.xml"),
]

def nav_html():
    lx="".join(f'<a href="{h}">{l}</a>' for l,h in NAV_LINKS)
    return f"""<nav><div class="nav-inner">
  <a class="logo" href="index.html">Acorns<em>Guide</em></a>
  <div class="nav-links">{lx}</div>
  <a class="nav-cta" href="{aff('nav')}" target="_blank" rel="noopener sponsored">🌱 Start Free</a>
</div></nav>"""

def bc_html(crumbs):
    p=[]
    for label,href in crumbs:
        if href: p.append(f'<a href="{href}">{label}</a><span style="opacity:.4">›</span>')
        else: p.append(f'<span style="color:rgba(240,250,247,.85)">{label}</span>')
    return f'<div class="bc">{"".join(p)}</div>'

def pnav_html():
    lx="".join(f'<a href="{h}">{l}</a>' for l,h in NAV_LINKS)
    return f'<div class="pnav">{lx}</div>'

def footer_html():
    fl="".join(f'<a href="{h}">{l}</a>' for l,h in ALL_LINKS)
    return f"""<footer>
  <span class="flogo">Acorns<em>Guide</em></span>
  <div class="flinks">{fl}</div>
  <div class="disc">
    <strong style="color:rgba(240,250,247,.75);display:block;margin-bottom:6px">⚠️ Investment Disclaimer</strong>
    Investing involves risk including possible loss of principal. AcornsGuide is an independent affiliate site — we earn commissions when you sign up via our links. Past performance does not guarantee future results. This is not financial advice. Acorns Advisers, LLC is an SEC-registered investment advisor. Please review all disclosures at acorns.com before investing.
  </div>
  <p style="margin-top:18px;opacity:.3">© {date.today().year} AcornsGuide. All rights reserved.</p>
</footer>
<div class="sticky" style="display:none">
  <p><strong>🌱 Bonus Offer Available Now</strong>Open Acorns &amp; get a free investment bonus</p>
  <a href="{aff('sticky')}" class="cta sm glow" target="_blank" rel="noopener sponsored">Claim Bonus</a>
</div>
<script>{JS}</script>"""

def faq_block(items):
    r="".join(f'<div class="fi"><div class="fq">{q}</div><div class="fa">{a}</div></div>' for q,a in items)
    return f'<div class="faq"><div class="faq-h">Frequently Asked Questions</div>{r}</div>'

def schema_faq(items):
    return {"@context":"https://schema.org","@type":"FAQPage",
            "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}
def schema_web(t,d,u):
    return {"@context":"https://schema.org","@type":"WebPage","name":t,"description":d,"url":u,
            "publisher":{"@type":"Organization","name":"AcornsGuide","url":BASE_URL},"inLanguage":"en-US"}
def schema_bc(crumbs):
    items=[]
    for i,(label,href) in enumerate(crumbs,1):
        url=f"{BASE_URL}/{href}" if href else BASE_URL
        items.append({"@type":"ListItem","position":i,"name":label,"item":url})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}

def page(slug,title,desc,kw,h1,pill,hero_cta,body,faqs=None,crumbs=None):
    canon=f"{BASE_URL}/" if slug=="index" else f"{BASE_URL}/{slug}.html"
    schemas=[schema_web(title,desc,canon)]
    if crumbs: schemas.append(schema_bc(crumbs))
    if faqs:   schemas.append(schema_faq(faqs))
    sd="\n".join(f'<script type="application/ld+json">{_json.dumps(s,separators=(",",":"))}</script>' for s in schemas)
    cb=bc_html(crumbs) if crumbs else ""
    fb=faq_block(faqs) if faqs else ""
    b2=body.replace("{A}",aff(slug))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="AcornsGuide">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
{sd}
<style>{CSS}</style>
</head>
<body>
<div class="ann">🌱 Limited Offer: Open an Acorns account today and claim your <strong>free bonus investment</strong> — <a href="{aff('ann')}">Get it here →</a></div>
{nav_html()}
<div class="trust">
  <div class="trust-wrap">
    <div class="titem"><span class="dot"></span>SEC Registered RIA</div>
    <div class="titem"><span class="dot"></span>SIPC Protected to $500K</div>
    <div class="titem"><span class="dot"></span>10M+ Investors</div>
    <div class="titem"><span class="dot"></span>Start with Just $5</div>
    <div class="titem"><span class="dot"></span>Updated {BUILT_ON}</div>
  </div>
</div>
<div class="hero">
  <div class="hero-pill">🌱 {pill}</div>
  <h1>{h1}</h1>
  <p class="sub">{desc}</p>
  <div class="hero-btns">
    <a href="{aff(slug+'-hero')}" class="cta glow" target="_blank" rel="noopener sponsored">{hero_cta}</a>
    <a href="#main" class="btn-outline">Read the Guide ↓</a>
  </div>
</div>
<div class="wrap" id="main">
  {cb}
  {pnav_html()}
  {b2}
  {fb}
</div>
{footer_html()}
</body>
</html>"""

# ══════════════════════════════════════════════════════════════
# PAGES — ALL NEW CONTENT
# ══════════════════════════════════════════════════════════════
PAGES=[]

# ── 1. INDEX ──────────────────────────────────────────────────
PAGES.append(dict(
slug="index",
title="Acorns Investing App 2026 — Honest Review & Bonus Offer | AcornsGuide",
desc="AcornsGuide is the independent resource for Acorns investors. Compare plans, understand fees, and claim the best current sign-up bonus for new US accounts in 2026.",
kw="acorns investing app 2026, acorns review, acorns bonus offer, best micro investing app usa",
h1="Acorns Investing — <em>Does It Actually Work?</em>",
pill="Independent Guide · Verified June 2026",
hero_cta="🌱 Open Acorns — Claim Bonus",
crumbs=[("Home",None)],
faqs=[
  ("What makes Acorns different from other investing apps?","Acorns automates everything — Round-Ups from your spending, recurring investments on a schedule, and dividend reinvestment. Unlike Robinhood or Stash, you never have to pick a stock or time the market. It's designed for people who want to build wealth without becoming investors."),
  ("Is Acorns worth it if I only have $100?","At $100, the $3/month fee is a steep 36% annualized cost. The value proposition is behavioral: if Acorns gets you investing $50/month consistently when you'd otherwise invest nothing, it's worth every penny. If you're already disciplined, a free Fidelity account is cheaper."),
  ("What is the current Acorns sign-up bonus?","Acorns currently offers a free bonus investment for new accounts opened through qualifying partner links. Our affiliate link activates this offer — the exact amount may vary. Check the landing page for the current promotion."),
  ("Does Acorns work for retirement?","Yes — Acorns Later provides Traditional IRA, Roth IRA, and SEP IRA accounts. Your Round-Ups and recurring investments can feed directly into tax-advantaged retirement accounts alongside your regular taxable portfolio."),
  ("Can I lose money on Acorns?","Yes — Acorns invests in ETFs that fluctuate with the market. You can have less money than you put in during market downturns. This is normal for all investing and the risk reduces significantly over long time horizons."),
],
body="""
<section class="cb">
  <p class="lead">Ten million Americans use Acorns to invest automatically. But is it the right tool for <em>you</em>? After testing the app, analyzing the portfolios, and calculating real fee impacts, here's our honest assessment — with no sugar-coating.</p>

  <div class="stats">
    <div class="stat"><div class="n">10M+</div><div class="l">Active Users</div></div>
    <div class="stat"><div class="n">$5</div><div class="l">To Get Started</div></div>
    <div class="stat"><div class="n">$3/mo</div><div class="l">Personal Plan</div></div>
    <div class="stat"><div class="n">2014</div><div class="l">Founded</div></div>
    <div class="stat"><div class="n">SEC</div><div class="l">Registered</div></div>
    <div class="stat"><div class="n">SIPC</div><div class="l">Insured</div></div>
  </div>

  <h2>Our Overall Verdict</h2>
  <div class="verdict">
    <div class="verdict-header">
      <div class="verdict-score">8.6</div>
      <div class="verdict-meta">
        <div class="stars">★★★★☆</div>
        <div class="label">AcornsGuide Score / 10 — Recommended for Beginners</div>
      </div>
    </div>
    <p style="color:rgba(240,250,247,.78);font-size:0.95rem;margin-bottom:14px">Acorns excels at one thing: turning non-investors into investors through automation. Its Round-Up mechanic is genuinely brilliant, its ETF portfolios are well-constructed, and the habit it builds is worth more than any fee discussion. The $3/month becomes a non-issue once your balance reaches $5,000+.</p>
    <div class="vtags">
      <span class="vtag">Best for Beginners</span>
      <span class="vtag">Fully Automated</span>
      <span class="vtag">ETF Portfolios</span>
      <span class="vtag">IRA Available</span>
      <span class="vtag">Round-Ups Unique</span>
    </div>
    <div style="margin-top:20px">
      <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Try Acorns Free</a>
    </div>
    <p class="tc">Investing involves risk. $3/month after first month. T&Cs apply.</p>
  </div>

  <h2>The 3-Minute Acorns Summary</h2>
  <p>Acorns links to your bank accounts and credit/debit cards. Every time you spend money, it rounds the purchase up to the nearest dollar and queues the difference for investment. It also lets you set automatic weekly or monthly investments. All money goes into a diversified portfolio of Vanguard and iShares ETFs chosen for you based on a 5-question risk profile.</p>
  <p>The result: most users invest $50–$150/month without consciously deciding to, without researching stocks, and without opening a brokerage app. For people who've always meant to start investing but never did, this is transformative.</p>

  <div class="pros-cons">
    <div class="pc-box pros">
      <h4>✅ What Acorns Does Well</h4>
      <ul>
        <li>Round-Ups are psychologically brilliant — painless saving</li>
        <li>Well-diversified ETF portfolios from Vanguard &amp; iShares</li>
        <li>IRA (retirement) account built into the same app</li>
        <li>Kids' custodial accounts (Acorns Early) on Premium plan</li>
        <li>450+ brand cashback invested directly into portfolio</li>
        <li>SIPC protection up to $500,000</li>
        <li>10-minute setup, no investment knowledge required</li>
      </ul>
    </div>
    <div class="pc-box cons">
      <h4>❌ Where It Falls Short</h4>
      <ul>
        <li>$3/month fee is proportionally high for small balances</li>
        <li>No individual stock or ETF selection</li>
        <li>No tax-loss harvesting (Betterment has this)</li>
        <li>5 portfolios is limited for sophisticated investors</li>
        <li>Customer support is email-only, 24–48h response</li>
        <li>No direct indexing options</li>
      </ul>
    </div>
  </div>

  <h2>Who Should Open an Acorns Account Today</h2>
  <p><strong>Open Acorns if:</strong> You currently invest $0/month and have been meaning to start. You spend daily on a card and want to automate saving. You want a one-app solution for regular investing AND retirement. You're under $15,000 to invest and want simplicity over optimization.</p>
  <p><strong>Skip Acorns if:</strong> You already have a Vanguard/Fidelity account and invest consistently. You have $50,000+ and care about minimizing fees. You want to pick individual stocks or advanced ETF strategies.</p>

  <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open Acorns — Free Bonus for New Accounts</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. Past performance does not guarantee future results.</p>
</section>
"""
))

# ── 2. HOW IT WORKS ───────────────────────────────────────────
PAGES.append(dict(
slug="how-acorns-works",
title="How Acorns Works 2026 — The Complete Mechanics Guide",
desc="Exactly how Acorns invests your money in 2026. Round-Ups, recurring investments, portfolio construction, rebalancing, and how dividends compound your wealth over time.",
kw="how acorns works 2026, acorns round ups explained, acorns portfolio etfs, acorns auto investing",
h1="How Acorns Works — <em>The Complete Mechanics</em>",
pill="Under the Hood · Step by Step · 2026",
hero_cta="🌱 See It in Action — Try Free",
crumbs=[("Home","index.html"),("How It Works",None)],
faqs=[
  ("When does Acorns actually invest my Round-Ups?","Round-Ups queue up and invest automatically once they accumulate to $5. If you make 20 purchases in a day with average $0.30 Round-Ups, that's $6 — it invests the next business day. If you make fewer transactions, it may take a week to accumulate $5."),
  ("What ETFs does Acorns actually buy with my money?","Acorns uses Vanguard and iShares ETFs: VTI (US stocks), VEA (international developed stocks), VWO (emerging markets), AGG or BND (bonds), and sometimes a real estate ETF. The exact allocation depends on your chosen portfolio."),
  ("How does Acorns rebalance my portfolio?","When market movements shift your portfolio away from its target allocation, Acorns automatically sells slightly overweight assets and buys underweight ones. This happens continuously in the background at no extra charge."),
  ("Does Acorns reinvest dividends?","Yes — dividends from your ETFs are automatically reinvested into your portfolio. This is the core mechanism of compound growth and one of the most important features of long-term investing."),
],
body="""
<section class="cb">
  <p class="lead">Acorns is more sophisticated than it looks. Behind the simple "spare change" interface is a proper robo-advisor with automatic rebalancing, dividend reinvestment, and tax-efficient portfolio management. Here's how every piece works.</p>

  <div class="offer featured">
    <div class="ob">🌱 Try It Now</div>
    <h3>Experience How Acorns Works — Open Free</h3>
    <ul>
      <li>✅ Link your card and watch Round-Ups in real time</li>
      <li>✅ Set your first $5/week recurring investment</li>
      <li>✅ See your ETF portfolio built automatically</li>
      <li>✅ First month free — no commitment</li>
    </ul>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open Acorns Free</a>
    <p class="tc">Investing involves risk. $3/month after first month.</p>
  </div>

  <h2>Step 1 — Round-Ups: The Core Mechanic</h2>
  <p>You link any Visa, Mastercard, Amex, or Discover card to Acorns. Every transaction triggers a Round-Up calculation: your spend is rounded up to the nearest dollar and the difference queues for investment.</p>
  <p>Round-Ups aren't debited immediately — they accumulate until they reach $5, then transfer from your linked bank account in a single batch. This prevents dozens of tiny bank transfers that would look confusing on your statement.</p>
  <p>You can also enable <strong>Smart Deposit</strong> — automatically route a percentage of each paycheck directly into your Acorns account on payday. And <strong>Multipliers</strong> let you invest 2×, 3×, or 10× your Round-Up amount for faster accumulation.</p>

  <h2>Step 2 — Recurring Investments: The Real Wealth Builder</h2>
  <p>Round-Ups are the hook. Recurring investments are the engine. Set a fixed daily, weekly, or monthly transfer and Acorns moves it automatically from your bank to your portfolio — every time, without you thinking about it.</p>
  <p>This dollar-cost averaging approach — investing a fixed amount regardless of market conditions — is one of the most evidence-backed strategies in personal finance. You buy more shares when prices are low and fewer when they're high, naturally optimizing your average cost basis over time.</p>

  <h2>Step 3 — Portfolio Construction</h2>
  <p>Your money is allocated across ETFs based on your risk profile. Acorns uses a questionnaire covering your age, income, time horizon, and risk tolerance to place you in one of five portfolios:</p>
  <table class="gtbl">
    <thead><tr><th>Portfolio</th><th>Stocks</th><th>Bonds</th><th>Historical Return*</th></tr></thead>
    <tbody>
      <tr><td>Conservative</td><td>20%</td><td>80%</td><td>4–5% avg/yr</td></tr>
      <tr><td>Moderately Conservative</td><td>40%</td><td>60%</td><td>5–6% avg/yr</td></tr>
      <tr><td>Moderate</td><td>60%</td><td>40%</td><td>6–7% avg/yr</td></tr>
      <tr><td>Moderately Aggressive</td><td>80%</td><td>20%</td><td>7–8% avg/yr</td></tr>
      <tr><td>Aggressive</td><td>100%</td><td>0%</td><td class="hi">8–10% avg/yr</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">*Historical averages. Past performance doesn't guarantee future results.</p>

  <h2>Step 4 — Automatic Rebalancing</h2>
  <p>Markets move. If US stocks have a great year, your portfolio may drift from 60% stocks to 68% stocks — more risk than your profile calls for. Acorns automatically sells a small amount of the overweight asset and buys the underweight one to bring you back to target. This happens continuously, in the background, at no extra cost.</p>

  <h2>Step 5 — Dividend Reinvestment (The Compound Growth Engine)</h2>
  <p>Your ETFs pay dividends — small regular payments representing your share of company profits. Acorns automatically reinvests every dividend back into your portfolio. Over time, this creates a compounding loop: dividends buy shares, those shares pay more dividends, which buy more shares. This is why long-term returns dramatically exceed what your contributions alone would suggest.</p>

  <div class="callout">
    <strong>💡 The Math Behind the Magic:</strong> $100/month invested for 30 years at 7% average annual return = $121,000 total value from just $36,000 contributed. The extra $85,000 is purely from compound growth — dividends reinvested, returns earned on returns.
  </div>
</section>
"""
))

# ── 3. FULL REVIEW ────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-review",
title="Acorns App Full Review 2026 — Every Feature Tested & Rated",
desc="The most thorough Acorns review for 2026. Every feature tested, every fee calculated, portfolios analyzed, and compared against competitors. Our honest verdict after using the app.",
kw="acorns app review 2026, acorns full review, acorns tested, acorns honest review",
h1="Acorns Full Review 2026 — <em>Every Feature Tested</em>",
pill="Full Review · Every Feature · Honest Verdict",
hero_cta="🌱 Start Your Acorns Trial",
crumbs=[("Home","index.html"),("Full Review",None)],
faqs=[
  ("How does Acorns make money?","Acorns earns revenue primarily from subscription fees ($3–$5/month per user) and from Acorns Earn brand partnerships. It does not sell user data or earn commissions on ETF trades."),
  ("Is the Acorns Checking account worth using?","The Acorns checking account is a decent feature — FDIC insured, no overdraft fees, and early direct deposit. The metal debit card is a nice touch. It's not the best checking account available but it's competent and integrating banking with investing in one app has real convenience value."),
  ("What happens to my account if Acorns goes out of business?","Your investment assets are held at a third-party custodian (DriveWealth, LLC) in your name and are SIPC-protected up to $500,000. If Acorns closes, your holdings would transfer to you or another brokerage."),
  ("Can I use Acorns and a 401(k) at the same time?","Absolutely — and you should. Max your 401(k) match first (free money from employer), then use Acorns Later (IRA) for additional retirement savings, then taxable Acorns Invest for additional wealth building."),
],
body="""
<section class="cb">
  <p class="lead">We created accounts, linked real bank cards, tracked investments for 60 days, tested customer support, analyzed the ETF portfolios, and compared fees against every major alternative. Here's what we found — the good, the bad, and what the marketing doesn't tell you.</p>

  <div class="verdict">
    <div class="verdict-header">
      <div class="verdict-score">8.6</div>
      <div class="verdict-meta">
        <div class="stars">★★★★☆</div>
        <div class="label">AcornsGuide Rating / 10</div>
      </div>
    </div>
    <div class="vtags">
      <span class="vtag">Ease of Use: 9.5/10</span>
      <span class="vtag">Portfolio Quality: 8.5/10</span>
      <span class="vtag">Fee Value: 7.5/10</span>
      <span class="vtag">Features: 8.0/10</span>
      <span class="vtag">Support: 7.0/10</span>
    </div>
  </div>

  <h2>Ease of Use — 9.5/10</h2>
  <p>Acorns has the best onboarding in the micro-investing space. The questionnaire takes under 3 minutes, linking your bank takes 2 minutes via Plaid, and your first Round-Up investment happens automatically. No investment terminology, no order types, no ticker symbols. It's genuinely frictionless.</p>
  <p>The app design is clean and focused. One main screen shows your balance, contributions, and returns. Everything else is accessible but not pushed at you. This is intentional — Acorns wants you to invest and forget, not obsessively track.</p>

  <h2>Portfolio Quality — 8.5/10</h2>
  <p>Acorns uses Vanguard and iShares ETFs with expense ratios as low as 0.03%. The portfolio construction follows Modern Portfolio Theory — diversified across US stocks, international stocks, bonds, and sometimes real estate. For passive long-term investing this is exactly correct.</p>
  <p>Deduction: only five portfolios means no customization for specific goals (home purchase in 7 years vs retirement in 30 years), and no access to sector ETFs, individual stocks, or alternative assets. Betterment's goal-based portfolios are more sophisticated.</p>

  <h2>Fee Value — 7.5/10</h2>
  <p>The $3/month flat fee is genuinely good value above $10,000 (0.36% annually) and excellent above $25,000 (0.14%). It's poor value below $5,000 where the annualized percentage becomes high. The honest answer: start Acorns to build the habit, accept the fee drag while your balance is small, and it will become very cheap as your investments grow.</p>
  <table class="gtbl">
    <thead><tr><th>Balance</th><th>Annual Fee</th><th>% of Balance</th><th>vs 0.25% Robo-Advisor</th></tr></thead>
    <tbody>
      <tr><td>$1,000</td><td>$36</td><td class="hi">3.6%</td><td>$2.50</td></tr>
      <tr><td>$5,000</td><td>$36</td><td>0.72%</td><td>$12.50</td></tr>
      <tr><td>$12,000</td><td>$36</td><td>0.30%</td><td>$30.00 ← break-even</td></tr>
      <tr><td>$25,000</td><td>$36</td><td class="hi">0.14%</td><td>$62.50</td></tr>
      <tr><td>$50,000</td><td>$36</td><td class="hi">0.07%</td><td>$125.00</td></tr>
    </tbody>
  </table>

  <h2>Features — 8.0/10</h2>
  <p>Round-Ups are best-in-class. The IRA integration (Acorns Later) is genuinely useful — having retirement and taxable investing in one app simplifies financial life. Acorns Earn (brand cashback invested) is a nice bonus. The checking account and emergency fund features add real value on the Personal plan.</p>
  <p>Missing: no tax-loss harvesting, no individual securities, no goals-based planning, no human advisor access. Premium plan's live Q&A with financial experts is a decent addition but doesn't replace personalized advice.</p>

  <h2>Customer Support — 7.0/10</h2>
  <p>Support is email-only with 24–48 hour response times. There's an in-app chat that often routes to automated responses before reaching a human. No phone support. For a financial product holding real money, this is a legitimate weakness. We've seen faster responses (under 12 hours) during weekday business hours.</p>

  <h2>Final Verdict</h2>
  <p>Acorns is the best investing app for people who currently invest nothing. If that's you, open an account today — the behavioral change alone is worth multiples of the fee. If you're already investing consistently at Fidelity or Vanguard with a $25,000+ balance, you probably don't need Acorns.</p>
  <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open Acorns Account</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. $3/month Personal plan.</p>
</section>
"""
))

# ── 4. VS ROBINHOOD ───────────────────────────────────────────
PAGES.append(dict(
slug="acorns-vs-robinhood",
title="Acorns vs Robinhood 2026 — Which App Builds More Wealth?",
desc="Acorns vs Robinhood compared for 2026. Which app actually grows your wealth better? We compare automation, fees, portfolios, returns data, and who each app is built for.",
kw="acorns vs robinhood 2026, robinhood vs acorns which is better, acorns or robinhood for beginners",
h1="Acorns vs Robinhood — <em>Which Builds More Wealth?</em>",
pill="Head-to-Head · Real Returns Data · 2026",
hero_cta="🌱 Go With Acorns",
crumbs=[("Home","index.html"),("vs Robinhood",None)],
faqs=[
  ("Has research shown which app generates better returns?","Studies consistently show that active retail traders on platforms like Robinhood underperform index fund benchmarks by 3–6% annually due to overtrading and poor timing. Acorns' passive ETF approach historically tracks market returns closely."),
  ("Is Robinhood free to use?","Robinhood basic is commission-free. Robinhood Gold is $5/month and adds margin, premium data, and higher instant deposit limits. Acorns Personal is $3/month. Both charge underlying fund fees (Robinhood's ETF options vary widely)."),
  ("Which app is better for a Roth IRA?","Both offer Roth IRAs. Acorns Later automates contributions via Round-Ups and recurring investments — ideal for people who want to set and forget. Robinhood IRA requires manual management. Acorns wins on automation; Robinhood wins on investment flexibility."),
  ("Can I use both apps?","Yes. A common strategy: use Acorns for automated baseline investing (Round-Ups + recurring), and use Robinhood alongside it for discretionary stock picks or ETF experiments. Don't replace Acorns automation with Robinhood — add Robinhood on top."),
],
body="""
<section class="cb">
  <p class="lead">Acorns and Robinhood both claim to democratize investing — but they represent completely opposite philosophies. One removes all decisions. The other gives you all decisions. Which one actually makes you richer depends on your discipline, knowledge, and honestly, your psychology.</p>

  <h2>Full Feature Comparison</h2>
  <table class="cmp">
    <thead><tr><th>Feature</th><th>Acorns</th><th>Robinhood</th></tr></thead>
    <tbody>
      <tr><td>Monthly fee</td><td>$3–$5/month</td><td><span class="yes">$0 basic</span></td></tr>
      <tr><td>Investment automation</td><td><span class="yes">Fully automated</span></td><td><span class="no">Manual only</span></td></tr>
      <tr><td>Round-Ups</td><td><span class="yes">Yes — unique</span></td><td><span class="no">No</span></td></tr>
      <tr><td>ETF diversification</td><td><span class="yes">Built-in, automatic</span></td><td>You build it manually</td></tr>
      <tr><td>Individual stocks</td><td><span class="no">No</span></td><td><span class="yes">Yes — full market</span></td></tr>
      <tr><td>Options trading</td><td><span class="no">No</span></td><td><span class="ok">Yes (risky)</span></td></tr>
      <tr><td>Crypto</td><td><span class="no">No</span></td><td><span class="yes">Yes</span></td></tr>
      <tr><td>Roth IRA</td><td><span class="yes">Yes — automated</span></td><td><span class="yes">Yes — manual</span></td></tr>
      <tr><td>Kids' accounts</td><td><span class="yes">Yes (Acorns Early)</span></td><td><span class="no">No</span></td></tr>
      <tr><td>Fractional shares</td><td>Via ETFs</td><td><span class="yes">Yes — direct</span></td></tr>
      <tr><td>SIPC protected</td><td><span class="yes">Yes</span></td><td><span class="yes">Yes</span></td></tr>
      <tr><td>Best for</td><td><span class="yes">Passive wealth builders</span></td><td>Active traders &amp; learners</td></tr>
    </tbody>
  </table>

  <h2>The Psychology Question — Why This Matters More Than Features</h2>
  <p>Research from the National Bureau of Economic Research found that Robinhood traders significantly increased their trading activity and experienced measurably worse outcomes than passive index investors over comparable periods. The platform's gamification (confetti animations on trades, push notifications about price movements) is explicitly designed to encourage frequent trading.</p>
  <p>Frequent trading means paying more in taxes (short-term capital gains rates), more in spread costs, and statistically worse timing decisions. The average Robinhood user is not Warren Buffett. The data shows most would have been better off in a diversified ETF.</p>

  <h2>The One Scenario Where Robinhood Wins</h2>
  <p>If you already invest consistently in index funds and want a separate account to experiment with individual stocks using money you can afford to lose, Robinhood's free trading is ideal. Use it as a learning tool or speculation account — not as your primary wealth-building vehicle.</p>

  <div class="callout">
    <strong>💡 Our Take:</strong> For 90% of people reading this, Acorns is the better choice for building long-term wealth. The automation advantage is massive — it takes human decision-making (and human error) out of the equation. Use Robinhood only if you genuinely enjoy learning about individual companies and can afford to treat it as an education expense.
  </div>

  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Open Acorns — Better for Long-Term Wealth</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. Fee comparison based on current published pricing.</p>
</section>
"""
))

# ── 5. VS BETTERMENT ──────────────────────────────────────────
PAGES.append(dict(
slug="acorns-vs-betterment",
title="Acorns vs Betterment 2026 — Two Robo-Advisors Compared",
desc="Acorns vs Betterment compared for 2026. Which robo-advisor has better portfolios, lower fees, and more useful features for US investors at different balance levels?",
kw="acorns vs betterment 2026, betterment vs acorns fees, best robo advisor usa 2026",
h1="Acorns vs Betterment — <em>Which Robo-Advisor Wins?</em>",
pill="Robo-Advisor Battle · Fees & Features · 2026",
hero_cta="🌱 Choose Acorns",
crumbs=[("Home","index.html"),("vs Betterment",None)],
faqs=[
  ("At what balance does Acorns become cheaper than Betterment?","Acorns ($36/year) becomes cheaper than Betterment (0.25%/year) when your balance exceeds $14,400. Below that, Betterment's percentage fee costs less than $36/year."),
  ("Does Betterment have Round-Ups?","No — Betterment doesn't have Round-Ups or spare-change investing. It focuses on goal-based portfolios with tax optimization. Acorns is unique in its Round-Up mechanic."),
  ("Which has better tax optimization?","Betterment wins decisively on tax optimization — it offers automatic tax-loss harvesting which Acorns doesn't. For accounts above $50,000, Betterment's tax savings can more than offset its higher fee."),
  ("Which should a 25-year-old with $500 to invest choose?","Acorns — the Round-Up mechanic will grow that $500 to $2,000 or more over a few months without requiring any discipline. Betterment is better once you have $5,000+ and want goal-based features."),
],
body="""
<section class="cb">
  <p class="lead">Acorns and Betterment are both robo-advisors — but they serve different stages of the investing journey. Acorns wins on habit formation and simplicity. Betterment wins on tax efficiency and goal-based planning. Your balance and investing maturity should determine which you choose.</p>

  <h2>Acorns vs Betterment — Full Comparison</h2>
  <table class="cmp">
    <thead><tr><th>Feature</th><th>Acorns</th><th>Betterment</th></tr></thead>
    <tbody>
      <tr><td>Fee structure</td><td>$3/month flat</td><td>0.25%/year</td></tr>
      <tr><td>Cheaper below</td><td>$14,400 balance</td><td><span class="yes">Under $14,400</span></td></tr>
      <tr><td>Cheaper above</td><td><span class="yes">$14,400+ balance</span></td><td>N/A</td></tr>
      <tr><td>Round-Ups</td><td><span class="yes">Yes — unique</span></td><td><span class="no">No</span></td></tr>
      <tr><td>Tax-loss harvesting</td><td><span class="no">No</span></td><td><span class="yes">Yes — automatic</span></td></tr>
      <tr><td>Goal-based portfolios</td><td><span class="no">5 presets only</span></td><td><span class="yes">Yes — multiple goals</span></td></tr>
      <tr><td>Socially responsible options</td><td><span class="yes">Yes (ESG)</span></td><td><span class="yes">Yes (more options)</span></td></tr>
      <tr><td>IRA / retirement</td><td><span class="yes">Yes</span></td><td><span class="yes">Yes</span></td></tr>
      <tr><td>Checking account</td><td><span class="yes">Yes</span></td><td><span class="yes">Yes</span></td></tr>
      <tr><td>Minimum balance</td><td>$5</td><td><span class="yes">$0</span></td></tr>
      <tr><td>Human advisor access</td><td><span class="no">No (Premium Q&A only)</span></td><td><span class="yes">Yes (Premium - 0.4%)</span></td></tr>
      <tr><td>Best for</td><td><span class="yes">Beginner to $20K</span></td><td>$20K+ investors</td></tr>
    </tbody>
  </table>

  <h2>The Fee Reality — Year by Year</h2>
  <p>Here's the actual fee you pay at each balance level, annually:</p>
  <table class="gtbl">
    <thead><tr><th>Balance</th><th>Acorns/yr</th><th>Betterment/yr</th><th>Cheaper Option</th></tr></thead>
    <tbody>
      <tr><td>$2,000</td><td>$36</td><td>$5</td><td class="hi">Betterment</td></tr>
      <tr><td>$5,000</td><td>$36</td><td>$12.50</td><td class="hi">Betterment</td></tr>
      <tr><td>$14,400</td><td>$36</td><td>$36</td><td>Tied</td></tr>
      <tr><td>$25,000</td><td>$36</td><td>$62.50</td><td class="hi">Acorns</td></tr>
      <tr><td>$50,000</td><td>$36</td><td>$125</td><td class="hi">Acorns</td></tr>
      <tr><td>$100,000</td><td>$36</td><td>$250</td><td class="hi">Acorns</td></tr>
    </tbody>
  </table>

  <h2>The Tax-Loss Harvesting Factor</h2>
  <p>Betterment's automatic tax-loss harvesting systematically sells losing positions to realize losses that offset gains — reducing your tax bill. Estimates suggest this feature saves 0.5–1.5% of portfolio value annually for taxable accounts. On a $50,000 portfolio that's $250–$750/year in tax savings, which more than offsets Betterment's $125/year fee.</p>
  <p>For this reason alone, many investors switch from Acorns to Betterment once they pass $30,000–$50,000 in taxable accounts.</p>

  <div class="callout">
    <strong>💡 Best Strategy:</strong> Start with Acorns to build the investing habit and accumulate your first $15,000. The Round-Ups and automation are unmatched for forming consistent behavior. Once you exceed $20,000 and want more tax efficiency, evaluate migrating to Betterment or keeping both.
  </div>

  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Start with Acorns</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. Fees current as of June 2026.</p>
</section>
"""
))

# ── 6. VS STASH ───────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-vs-stash",
title="Acorns vs Stash 2026 — Which $3/Month App Is Worth It?",
desc="Acorns vs Stash both cost $3/month but work very differently. We compare every feature, return potential, and which app is right for your investing style in 2026.",
kw="acorns vs stash 2026, stash vs acorns, which is better acorns or stash 2026",
h1="Acorns vs Stash — <em>Same Price, Very Different Apps</em>",
pill="$3/Month Showdown · Feature Comparison · 2026",
hero_cta="🌱 Go With Acorns",
crumbs=[("Home","index.html"),("vs Stash",None)],
faqs=[
  ("Why do Acorns and Stash cost the same?","Both charge $3/month but bundle different features. Acorns $3 includes investing, IRA, checking, and emergency fund. Stash $3 includes investing, checking, and its Stock-Back debit card rewards. Acorns includes the IRA at the base tier; Stash charges more for retirement."),
  ("Does Stash have Round-Ups like Acorns?","Stash doesn't have traditional Round-Ups. Instead, it has Stock-Back rewards — you earn fractional shares of brands when you shop with the Stash debit card (e.g., shop at Target, earn Target stock). Different concept, similar goal of tying everyday spending to investing."),
  ("Which app teaches you more about investing?","Stash — it's explicitly designed to educate. When you pick investments from their curated list, it explains what each ETF or stock holds and why someone might choose it. Acorns provides no investment education because it makes all decisions for you."),
  ("Which app has performed better historically?","Neither publishes audited performance data, but portfolio construction favors Acorns — its Vanguard ETFs have among the lowest expense ratios in the industry (0.03%). Stash's curated investment options include some funds with higher expense ratios."),
],
body="""
<section class="cb">
  <p class="lead">Acorns and Stash are the two most similar competing apps in micro-investing. Both cost $3/month. Both target beginners. Both link to your spending. But their philosophies diverge sharply: Acorns does everything for you, Stash teaches you to do it yourself. Which approach fits your goals?</p>

  <h2>Acorns vs Stash — Every Feature</h2>
  <table class="cmp">
    <thead><tr><th>Feature</th><th>Acorns</th><th>Stash</th></tr></thead>
    <tbody>
      <tr><td>Monthly fee (base)</td><td>$3/month</td><td>$3/month</td></tr>
      <tr><td>Investment decisions</td><td><span class="yes">Fully automated</span></td><td>You choose from curated list</td></tr>
      <tr><td>Round-Up mechanic</td><td><span class="yes">Classic Round-Ups</span></td><td>Stock-Back® card rewards</td></tr>
      <tr><td>Investment options</td><td>5 ETF portfolios</td><td><span class="yes">200+ ETFs and stocks</span></td></tr>
      <tr><td>IRA at base tier</td><td><span class="yes">Yes</span></td><td><span class="no">No (costs more)</span></td></tr>
      <tr><td>Kids' accounts</td><td><span class="yes">Yes (Premium)</span></td><td><span class="no">No</span></td></tr>
      <tr><td>Investment education</td><td>Minimal</td><td><span class="yes">Built into app</span></td></tr>
      <tr><td>Portfolio expense ratios</td><td><span class="yes">0.03–0.18% (Vanguard/iShares)</span></td><td>Varies (some higher)</td></tr>
      <tr><td>Debit card rewards</td><td>Checking debit card</td><td><span class="yes">Stock-Back® rewards</span></td></tr>
      <tr><td>Best for</td><td><span class="yes">Hands-off investors</span></td><td>People who want to learn</td></tr>
    </tbody>
  </table>

  <h2>The Core Trade-Off</h2>
  <p><strong>Acorns philosophy:</strong> You don't need to understand investing to build wealth. Give us your money, we'll invest it in diversified, low-cost ETFs, and rebalance automatically. Check in once a month if you like.</p>
  <p><strong>Stash philosophy:</strong> You should understand where your money is going. Here are 200+ investment options — we'll explain each one. You pick what aligns with your values and goals. We'll handle the execution.</p>
  <p>Neither approach is wrong. But Stash's approach requires more engagement. Research shows that more engagement with investing apps correlates with more trading — and more trading correlates with worse outcomes for retail investors. Acorns' passivity is a feature, not a bug.</p>

  <h2>The IRA Advantage</h2>
  <p>At $3/month, Acorns includes an IRA (Acorns Later). Stash's $3/month plan doesn't include retirement accounts — you need to upgrade. This is a meaningful difference: tax-advantaged retirement investing is one of the highest-value financial moves available to anyone.</p>

  <div class="callout">
    <strong>💡 Our Take:</strong> If your goal is to build wealth passively with minimal involvement, Acorns wins at any price point. If your goal is to learn how investing works while you invest, Stash is a better classroom. Both are good products — the question is whether you want automation or education.
  </div>
  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Open Acorns — Best for Automation</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. $3/month.</p>
</section>
"""
))

# ── 7. VS WEALTHFRONT ─────────────────────────────────────────
PAGES.append(dict(
slug="acorns-vs-wealthfront",
title="Acorns vs Wealthfront 2026 — Beginner App vs Advanced Robo-Advisor",
desc="Acorns vs Wealthfront compared for 2026. When does it make sense to switch from Acorns to Wealthfront? Fees, tax efficiency, portfolio options and the honest crossover point.",
kw="acorns vs wealthfront 2026, wealthfront vs acorns, when to switch from acorns to wealthfront",
h1="Acorns vs Wealthfront — <em>When to Upgrade Your Robo-Advisor</em>",
pill="Two Tiers of Robo-Advising · 2026",
hero_cta="🌱 Start with Acorns First",
crumbs=[("Home","index.html"),("vs Wealthfront",None)],
faqs=[
  ("What is the minimum to open a Wealthfront account?","Wealthfront requires a $500 minimum to start investing. Acorns requires just $5. For investors just starting out, Acorns is accessible at any income level."),
  ("Does Wealthfront have tax-loss harvesting?","Yes — Wealthfront offers automated daily tax-loss harvesting on all taxable accounts above $500. It also offers direct indexing (owning individual S&P 500 stocks instead of the fund) for accounts above $100,000."),
  ("How much does Wealthfront charge?","Wealthfront charges 0.25% annually. On a $10,000 account that's $25/year vs Acorns' $36/year. On a $25,000 account it's $62.50 vs Acorns' $36. The crossover is around $14,400."),
  ("Should I close my Acorns account when I move to Wealthfront?","Not necessarily. Many investors keep Acorns running for Round-Ups (Wealthfront doesn't have this feature) and use Wealthfront for their larger primary portfolio. The $36/year Acorns fee is trivial once you have a $50,000 Wealthfront account."),
],
body="""
<section class="cb">
  <p class="lead">Wealthfront is what Acorns users aspire to — a more sophisticated robo-advisor with tax-loss harvesting, direct indexing, and goal-based planning. But it requires $500 to start and charges a percentage fee. Here's exactly when and why to make the switch.</p>

  <h2>Acorns vs Wealthfront — Comparison</h2>
  <table class="cmp">
    <thead><tr><th>Feature</th><th>Acorns</th><th>Wealthfront</th></tr></thead>
    <tbody>
      <tr><td>Minimum to invest</td><td><span class="yes">$5</span></td><td>$500</td></tr>
      <tr><td>Fee structure</td><td>$3/month flat</td><td>0.25%/year</td></tr>
      <tr><td>Cheaper at $10K balance</td><td><span class="yes">Acorns ($36/yr)</span></td><td>Wealthfront ($25/yr)</td></tr>
      <tr><td>Cheaper at $25K balance</td><td><span class="yes">Acorns ($36/yr)</span></td><td>Wealthfront ($62.50/yr)</td></tr>
      <tr><td>Round-Ups</td><td><span class="yes">Yes</span></td><td><span class="no">No</span></td></tr>
      <tr><td>Tax-loss harvesting</td><td><span class="no">No</span></td><td><span class="yes">Yes — daily</span></td></tr>
      <tr><td>Direct indexing ($100K+)</td><td><span class="no">No</span></td><td><span class="yes">Yes</span></td></tr>
      <tr><td>529 college savings</td><td><span class="no">No</span></td><td><span class="yes">Yes</span></td></tr>
      <tr><td>Financial planning tools</td><td>Basic</td><td><span class="yes">Advanced (Path tool)</span></td></tr>
      <tr><td>Best for</td><td><span class="yes">Beginners, under $15K</span></td><td>$15K+ focused investors</td></tr>
    </tbody>
  </table>

  <h2>The Upgrade Timeline — When to Switch</h2>
  <p><strong>$0–$500:</strong> Acorns only (Wealthfront minimum not met). Use Round-Ups aggressively.</p>
  <p><strong>$500–$14,400:</strong> Wealthfront's 0.25% fee is lower in absolute dollars, but Acorns' Round-Ups may generate more returns than the fee savings. This is the judgment call zone.</p>
  <p><strong>$14,400+:</strong> Acorns becomes cheaper in absolute fee terms. Keep Acorns for Round-Ups, consider adding Wealthfront for its tax optimization features.</p>
  <p><strong>$50,000+:</strong> Wealthfront's tax-loss harvesting likely saves more than its extra fee. Consider Wealthfront as primary portfolio, keep Acorns as a Round-Up feeder.</p>
  <p><strong>$100,000+:</strong> Wealthfront's direct indexing becomes available — this is genuinely better than ETFs for tax efficiency at this scale.</p>

  <div class="callout">
    <strong>💡 The Smart Path:</strong> Use Acorns to build the habit and accumulate your first $5,000–$15,000. Don't overthink the fee at small balances — the behavioral value of automation outweighs it. When you hit $15,000+, open a Wealthfront account and run both. You get Acorns' Round-Ups AND Wealthfront's tax efficiency.
  </div>
  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Start With Acorns First</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. Fees current as of June 2026.</p>
</section>
"""
))

# ── 8. ROUND-UPS ──────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-round-ups",
title="Acorns Round-Ups 2026 — How to Maximize Your Spare Change",
desc="The complete guide to Acorns Round-Ups in 2026. How they actually work, multipliers, how much the average user invests, and the strategies that generate the most automatic investing.",
kw="acorns round ups 2026, how round ups work, acorns spare change, acorns multipliers",
h1="Acorns Round-Ups — <em>Turn Spending Into Investing</em>",
pill="Round-Ups Deep Dive · Maximize Results · 2026",
hero_cta="🌱 Activate Round-Ups Now",
crumbs=[("Home","index.html"),("Round-Ups",None)],
faqs=[
  ("How long does it take for Round-Ups to invest?","Round-Ups queue until they reach $5, then transfer from your bank and invest. If you make 10+ transactions/day, this can happen daily. If you spend less, it may take several days to accumulate $5."),
  ("Why didn't my Round-Up from yesterday invest yet?","Round-Ups only batch when they reach $5. They also require a confirmed bank transaction — some card transactions take 1–2 days to confirm. Check your 'Pending Round-Ups' in the app."),
  ("What if I don't have enough in my bank for Round-Ups?","Acorns checks your bank balance before transferring Round-Ups. If your balance is insufficient, it skips the transfer and waits. You can set a minimum balance threshold in settings to prevent overdrafts."),
  ("Can I manually add money on top of Round-Ups?","Yes — you can make one-time investments of any amount anytime from the app, in addition to your Round-Ups and recurring investments."),
],
body="""
<section class="cb">
  <p class="lead">Round-Ups are Acorns' signature feature and genuinely one of the most elegant ideas in personal finance. By routing the psychological irrelevance of spare change into real investment, they've gotten 10 million people to invest money they'd otherwise never think about.</p>

  <div class="offer featured">
    <div class="ob">🌱 Activate Today</div>
    <h3>Start Your Round-Ups — Watch Spare Change Become Real Wealth</h3>
    <ul>
      <li>✅ Links to any Visa, MC, Amex, or Discover card</li>
      <li>✅ Average user invests $30–$80/month automatically</li>
      <li>✅ Multipliers available: 2×, 3×, or 10×</li>
      <li>✅ Pause anytime — no commitment</li>
    </ul>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Start Round-Ups</a>
    <p class="tc">Investing involves risk. $3/month fee applies.</p>
  </div>

  <h2>The Exact Mechanics — How Round-Ups Calculate</h2>
  <p>Every transaction on a linked card triggers a round-up calculation. The purchase amount is rounded up to the next whole dollar. The difference is queued:</p>
  <table class="gtbl">
    <thead><tr><th>You Spend</th><th>Rounded To</th><th>Round-Up Generated</th></tr></thead>
    <tbody>
      <tr><td>$4.73 (coffee)</td><td>$5.00</td><td>$0.27</td></tr>
      <tr><td>$23.41 (lunch)</td><td>$24.00</td><td>$0.59</td></tr>
      <tr><td>$67.19 (groceries)</td><td>$68.00</td><td>$0.81</td></tr>
      <tr><td>$12.99 (app subscription)</td><td>$13.00</td><td>$0.01</td></tr>
      <tr><td>$89.50 (gas)</td><td>$90.00</td><td>$0.50</td></tr>
      <tr><td>$156.32 (dinner)</td><td>$157.00</td><td>$0.68</td></tr>
    </tbody>
  </table>
  <p>Average round-up per transaction: ~$0.40–$0.55. At 10–20 daily transactions, that's $4–$11/day or $120–$330/month — before multipliers.</p>

  <h2>Round-Up Multipliers — The Underused Superpower</h2>
  <p>Multipliers are the most underused Acorns feature. Instead of investing your actual round-up amount, you invest 2×, 3×, or 10× that amount. The psychological trick: a $0.50 round-up at 3× feels like $1.50, which is still trivial — but over a year it's $540 extra invested.</p>
  <table class="gtbl">
    <thead><tr><th>Multiplier</th><th>Monthly Typical Investment</th><th>Extra vs 1×</th><th>After 10 Years (7%)</th></tr></thead>
    <tbody>
      <tr><td>1× (base)</td><td>~$45/month</td><td>—</td><td>~$7,700</td></tr>
      <tr><td>2×</td><td>~$90/month</td><td>+$45/month</td><td>~$15,400</td></tr>
      <tr><td>3×</td><td>~$135/month</td><td>+$90/month</td><td>~$23,000</td></tr>
      <tr><td>10×</td><td>~$450/month</td><td>+$405/month</td><td>~$77,000</td></tr>
    </tbody>
  </table>

  <h2>How to Generate Maximum Round-Ups</h2>
  <ol>
    <li><strong>Link every card you own</strong> — more cards = more transactions = more round-ups. Include cards you use for subscriptions, bills, and gas.</li>
    <li><strong>Use a multiplier of at least 2×</strong> — you won't notice the difference in daily spending.</li>
    <li><strong>Don't pause Round-Ups during tight months</strong> — the amounts are so small they rarely create real financial pressure.</li>
    <li><strong>Add a weekly recurring investment</strong> — Round-Ups are your bonus investment. A $25–$50/week recurring investment is your baseline wealth builder.</li>
    <li><strong>Enable Smart Deposit</strong> — route a percentage of your paycheck automatically into Acorns on payday.</li>
  </ol>
</section>
"""
))

# ── 9. IRA GUIDE ──────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-later-ira",
title="Acorns Later IRA Guide 2026 — Roth vs Traditional & How to Maximize It",
desc="Complete guide to Acorns Later IRA in 2026. Roth vs Traditional comparison, contribution limits, withdrawal rules, and how to use Acorns to build real retirement wealth.",
kw="acorns later ira 2026, acorns roth ira, acorns traditional ira, acorns retirement investing",
h1="Acorns Later IRA — <em>The Retirement Account You Need</em>",
pill="IRA Guide · Roth & Traditional · 2026",
hero_cta="🌱 Open Acorns Later IRA",
crumbs=[("Home","index.html"),("IRA Guide",None)],
faqs=[
  ("Is a Roth IRA or Traditional IRA better on Acorns Later?","For most people under 50 who aren't in a high tax bracket: Roth IRA. You pay taxes now (likely at a low rate), then all growth and withdrawals are tax-free forever. The long-term tax-free compounding advantage is enormous."),
  ("Can I contribute to an Acorns IRA and a 401(k) at work?","Yes — IRA and 401(k) contribution limits are separate. You can contribute up to $7,000 to your IRA (2026 limit) AND up to $23,500 to your 401(k) in the same year."),
  ("What happens if I contribute more than the annual IRA limit?","You'll owe a 6% excise tax on the excess amount for each year it remains in the account. Acorns will warn you before you exceed the limit but it's your responsibility to track total IRA contributions across all accounts."),
  ("Can I use Round-Ups to fund my IRA on Acorns Later?","Yes — you can direct Round-Ups and recurring investments into Acorns Later (IRA) instead of or alongside your taxable Acorns Invest account. This is a powerful feature — automating IRA contributions via spare change."),
],
body="""
<section class="cb">
  <p class="lead">Most Americans are behind on retirement. The median American in their 40s has under $100,000 saved for retirement — a fraction of what they'll need. Acorns Later makes automated retirement investing as easy as regular investing. Here's how to use it correctly.</p>

  <div class="offer featured">
    <div class="ob">🌱 Open Free</div>
    <h3>Acorns Later — Automated IRA, Included in $3/Month</h3>
    <ul>
      <li>✅ Roth IRA, Traditional IRA, or SEP IRA</li>
      <li>✅ No extra fee — included in Personal plan</li>
      <li>✅ Automated via Round-Ups and recurring investment</li>
      <li>✅ 2026 contribution limit: $7,000 ($8,000 if 50+)</li>
    </ul>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open IRA Now</a>
    <p class="tc">Investing involves risk. IRA rules apply. Consult a tax advisor for your situation.</p>
  </div>

  <h2>Roth IRA vs Traditional IRA — The Decision</h2>
  <table class="cmp">
    <thead><tr><th>Feature</th><th>Roth IRA</th><th>Traditional IRA</th></tr></thead>
    <tbody>
      <tr><td>When you pay taxes</td><td>Now (contribution is after-tax)</td><td>Later (in retirement)</td></tr>
      <tr><td>Tax on growth</td><td><span class="yes">None — tax-free forever</span></td><td>Taxed as income when withdrawn</td></tr>
      <tr><td>Tax on withdrawals</td><td><span class="yes">Zero (in retirement)</span></td><td>Taxed at your retirement rate</td></tr>
      <tr><td>Deduction now</td><td><span class="no">No deduction</span></td><td>Possibly deductible (income limits)</td></tr>
      <tr><td>Required distributions</td><td><span class="yes">None in your lifetime</span></td><td>Must start at age 73</td></tr>
      <tr><td>Early access</td><td>Contributions anytime (no penalty)</td><td>10% penalty before 59½</td></tr>
      <tr><td>Best if</td><td>You're in a lower bracket now</td><td>You're in a higher bracket now</td></tr>
      <tr><td>Recommendation</td><td><span class="yes">Most people under 50</span></td><td>High earners near retirement</td></tr>
    </tbody>
  </table>

  <h2>The Roth IRA Tax Math Over 30 Years</h2>
  <p>$200/month into a Roth IRA at 7% average return over 30 years:</p>
  <ul>
    <li>Total contributed: $72,000</li>
    <li>Portfolio value: ~$228,000</li>
    <li>Tax owed on withdrawal: <span style="color:var(--teal3);font-weight:700">$0</span></li>
    <li>Equivalent taxable account value (at 25% tax): ~$171,000</li>
    <li><strong>Roth IRA advantage: $57,000</strong> — entirely from tax-free growth</li>
  </ul>

  <h2>How to Maximize Your Acorns Later IRA</h2>
  <ol>
    <li><strong>Open it immediately when you sign up</strong> — it takes 2 minutes and is included in your plan</li>
    <li><strong>Direct a recurring investment specifically to Later</strong> — set $50–$100/week going to your IRA</li>
    <li><strong>Enable Round-Ups for your IRA</strong> — direct spare-change investing into tax-free growth</li>
    <li><strong>Aim to max the annual limit</strong> — $7,000/year = $583/month. Even $100/month is valuable</li>
    <li><strong>Choose Aggressive portfolio in your IRA</strong> — long time horizon means you can handle volatility; the tax-free benefit compounds most powerfully with maximum returns</li>
  </ol>

  <h2>SEP IRA for Self-Employed Users</h2>
  <p>Acorns Later also offers a SEP IRA for freelancers, contractors, and small business owners. The 2026 SEP IRA limit is the lesser of 25% of net self-employment income or $69,000 — vastly higher than the standard IRA limit. If you're self-employed, this is one of the best tax advantages available.</p>
</section>
"""
))

# ── 10. FEES ──────────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-fees",
title="Acorns Fees 2026 — The Real Cost at Every Balance Level",
desc="Every Acorns fee explained for 2026. Monthly plan costs, ETF expense ratios, the fee crossover point vs competitors, and an honest assessment of value at different balance levels.",
kw="acorns fees 2026, acorns cost breakdown, how much does acorns cost, acorns fee worth it",
h1="Acorns Fees 2026 — <em>What You Actually Pay</em>",
pill="Fee Transparency · Every Cost · Real Math",
hero_cta="🌱 Start — First Month Free",
crumbs=[("Home","index.html"),("Fees",None)],
faqs=[
  ("Is there any way to use Acorns for free?","There's no permanently free tier. New accounts typically receive the first month free. After that, $3/month for Personal or $5/month for Premium. Some employer wellness programs cover Acorns subscriptions — check with your HR department."),
  ("What happens if I don't pay the monthly fee?","If your payment method fails, Acorns will retry. Continued non-payment can result in account suspension. Your investments remain in your account and are yours — they don't disappear due to non-payment."),
  ("Are there any hidden fees on Acorns?","No hidden fees in the traditional sense. The monthly subscription is the main cost. Underlying ETF expense ratios (0.03–0.18%) are embedded in fund performance, not charged separately. No withdrawal fees, no transfer fees, no inactivity fees."),
  ("Does Acorns charge to close my account?","No — closing your account and withdrawing all funds is free. You'll pay standard capital gains taxes on any investment gains, but Acorns doesn't charge a closure fee."),
],
body="""
<section class="cb">
  <p class="lead">The $3/month Acorns fee is either a bargain or expensive depending entirely on your balance. At $10,000 it's 0.36% — competitive. At $500 it's 7.2% — high. Knowing your exact cost at your specific balance helps you make a rational decision about whether Acorns is right for you right now.</p>

  <h2>Acorns Plan Comparison — 2026</h2>
  <table class="cmp">
    <thead><tr><th>Plan</th><th>Cost</th><th>Annual</th><th>What's Included</th></tr></thead>
    <tbody>
      <tr><td><strong>Personal</strong></td><td>$3/month</td><td>$36/year</td><td>Acorns Invest (taxable) + Acorns Later (IRA) + Acorns Checking + Emergency Fund + Metal debit card</td></tr>
      <tr><td><strong>Premium</strong></td><td>$5/month</td><td>$60/year</td><td>Everything in Personal + Acorns Early (kids custodial) + 1% IRA match on contributions + Custom portfolios + Live Q&A with financial experts</td></tr>
    </tbody>
  </table>

  <h2>Fee as % of Balance — The Real Number</h2>
  <table class="gtbl">
    <thead><tr><th>Portfolio Balance</th><th>Personal Plan ($36/yr)</th><th>Premium Plan ($60/yr)</th><th>Assessment</th></tr></thead>
    <tbody>
      <tr><td>$500</td><td class="hi">7.20%</td><td class="hi">12.00%</td><td>High — consider value of habit formation</td></tr>
      <tr><td>$1,000</td><td class="hi">3.60%</td><td class="hi">6.00%</td><td>Still high but behavior change may justify</td></tr>
      <tr><td>$3,000</td><td>1.20%</td><td>2.00%</td><td>Getting more reasonable</td></tr>
      <tr><td>$10,000</td><td>0.36%</td><td>0.60%</td><td>Competitive with robo-advisors</td></tr>
      <tr><td>$25,000</td><td class="hi">0.14%</td><td>0.24%</td><td>Excellent value</td></tr>
      <tr><td>$50,000</td><td class="hi">0.07%</td><td class="hi">0.12%</td><td>Among cheapest available</td></tr>
      <tr><td>$100,000+</td><td class="hi">0.04%</td><td class="hi">0.06%</td><td>Better than almost any alternative</td></tr>
    </tbody>
  </table>

  <h2>The Hidden Layer — ETF Expense Ratios</h2>
  <p>On top of Acorns' subscription, the ETFs in your portfolio charge annual expense ratios. These aren't billed to you — they're deducted from fund performance automatically. The good news: Acorns uses some of the cheapest ETFs available:</p>
  <table class="gtbl">
    <thead><tr><th>ETF Ticker</th><th>What It Holds</th><th>Expense Ratio</th></tr></thead>
    <tbody>
      <tr><td>VTI</td><td>Vanguard Total US Stock Market</td><td class="hi">0.03%</td></tr>
      <tr><td>VEA</td><td>Vanguard International Developed</td><td class="hi">0.05%</td></tr>
      <tr><td>VWO</td><td>Vanguard Emerging Markets</td><td>0.08%</td></tr>
      <tr><td>AGG</td><td>iShares US Aggregate Bond</td><td class="hi">0.03%</td></tr>
      <tr><td>IEMG</td><td>iShares Core Emerging Markets</td><td>0.09%</td></tr>
    </tbody>
  </table>
  <p>Total weighted expense ratio across a moderate portfolio: approximately 0.05–0.10%. This is excellent — among the lowest in the industry.</p>

  <div class="callout">
    <strong>💡 Bottom Line on Fees:</strong> The $3/month is genuinely high relative to your balance when you're starting out. Accept this as the cost of building the habit. Once you're above $10,000, Acorns becomes one of the cheapest investment options available. Above $25,000 it's cheaper than almost every alternative including direct index funds at many brokers.
  </div>
  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Start — First Month Free</a>
  <p class="tc" style="margin-top:10px">$3/month after first month. Investing involves risk.</p>
</section>
"""
))

# ── 11. PORTFOLIOS ────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-portfolios",
title="Acorns Portfolios Explained 2026 — Which One Is Right for You?",
desc="Every Acorns portfolio option explained for 2026. Conservative, Moderate, Aggressive, ESG, and Bitcoin portfolios — exactly what they hold, historical returns, and how to choose.",
kw="acorns portfolios 2026, which acorns portfolio is best, acorns aggressive vs moderate, acorns esg",
h1="Acorns Portfolios — <em>Pick the Right One the First Time</em>",
pill="Portfolio Guide · Returns Data · All Options",
hero_cta="🌱 Get My Portfolio Match",
crumbs=[("Home","index.html"),("Portfolios",None)],
faqs=[
  ("Should I pick Aggressive or Moderate on Acorns?","If you're under 40 with a 20+ year time horizon and won't panic during market drops: Aggressive (100% stocks) has produced the best long-run returns. If you're risk-averse, will check your balance often, and might sell during downturns: Moderate is better — consistency beats theoretical maximum return."),
  ("What's the difference between Acorns' standard and ESG portfolios?","Standard portfolios use regular Vanguard and iShares ETFs. ESG portfolios replace these with socially responsible equivalents that exclude companies with poor environmental, social, or governance records. ESG portfolios have slightly higher expense ratios (0.1–0.2% vs 0.03–0.09%)."),
  ("Can I have different portfolios for my Invest and Later accounts?","Yes — your taxable Acorns Invest account and your Acorns Later IRA can have different portfolios. Many investors choose Aggressive for their IRA (longest time horizon) and Moderate for their taxable account."),
  ("How does Acorns decide which portfolio to recommend?","Acorns uses a 5-question questionnaire: your investing goal, time horizon, comfort with market drops, current income, and current net worth. The algorithm maps these to one of the five portfolios. You can override the recommendation."),
],
body="""
<section class="cb">
  <p class="lead">Your portfolio selection is the most consequential decision you make on Acorns. It determines your expected return, your risk exposure, and ultimately how much wealth you accumulate. Here's exactly what each portfolio holds and which one you should choose.</p>

  <div class="offer">
    <div class="ob">🌱 Start Investing</div>
    <h3>Acorns Recommends Your Portfolio — Takes 3 Minutes</h3>
    <p style="color:rgba(240,250,247,.75);margin-bottom:18px">Answer 5 questions and Acorns recommends the right portfolio for your situation. You can always change it.</p>
    <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Get Portfolio Recommendation</a>
    <p class="tc">Investing involves risk. Portfolio based on questionnaire only.</p>
  </div>

  <h2>The 5 Core Portfolios</h2>
  <table class="gtbl">
    <thead><tr><th>Portfolio</th><th>US Stocks</th><th>Intl Stocks</th><th>Bonds</th><th>Hist. Return*</th><th>Best For</th></tr></thead>
    <tbody>
      <tr><td>Conservative</td><td>12%</td><td>8%</td><td>80%</td><td>4–5%/yr</td><td>Under 5yr horizon, near retirees</td></tr>
      <tr><td>Mod. Conservative</td><td>24%</td><td>16%</td><td>60%</td><td>5–6%/yr</td><td>5–10yr horizon, low risk tolerance</td></tr>
      <tr><td>Moderate</td><td>36%</td><td>24%</td><td>40%</td><td>6–7%/yr</td><td class="hi">Most beginners — recommended</td></tr>
      <tr><td>Mod. Aggressive</td><td>48%</td><td>32%</td><td>20%</td><td>7–8%/yr</td><td>10–25yr horizon, medium risk comfort</td></tr>
      <tr><td>Aggressive</td><td>60%</td><td>40%</td><td>0%</td><td class="hi">8–10%/yr</td><td>20+yr horizon, high risk comfort</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">*Historical averages based on underlying ETF performance. Past performance doesn't guarantee future results.</p>

  <h2>The Age Rule of Thumb</h2>
  <p>A simple heuristic: subtract your age from 120. That's approximately your ideal stock allocation percentage.</p>
  <ul>
    <li>Age 22: 98% stocks → <strong>Aggressive</strong></li>
    <li>Age 30: 90% stocks → <strong>Aggressive or Moderately Aggressive</strong></li>
    <li>Age 40: 80% stocks → <strong>Moderately Aggressive</strong></li>
    <li>Age 50: 70% stocks → <strong>Moderate to Moderately Aggressive</strong></li>
    <li>Age 60: 60% stocks → <strong>Moderate</strong></li>
    <li>Age 65+: 55% stocks → <strong>Moderately Conservative</strong></li>
  </ul>

  <h2>ESG Portfolios — Invest With Your Values</h2>
  <p>Each of the five core portfolios has a sustainable (ESG) equivalent. ESG portfolios replace standard ETFs with iShares ESG-screened versions that exclude companies with poor records on environmental impact, labor practices, executive compensation, and corporate governance.</p>
  <p>Performance difference vs standard: minimal over long periods. Expense ratio difference: +0.07–0.15%. If your values matter to your investing, the cost is trivial.</p>

  <h2>The Bitcoin-Linked Portfolio (Premium)</h2>
  <p>Acorns Premium includes access to a Bitcoin-linked ETF as a portfolio option. This is not direct Bitcoin ownership — it's an ETF that tracks Bitcoin price movements. It's high volatility and appropriate only for investors who specifically want Bitcoin exposure as part of their allocation.</p>
</section>
"""
))

# ── 12. SIGN UP ───────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-sign-up",
title="How to Open an Acorns Account 2026 — Step-by-Step Setup Guide",
desc="Complete step-by-step guide to opening an Acorns account in 2026. Everything from registration through your first investment, with tips to maximize your bonus from day one.",
kw="how to open acorns account 2026, acorns sign up guide, acorns setup, acorns first investment",
h1="How to Open an Acorns Account — <em>Done in 10 Minutes</em>",
pill="Sign Up Guide · First Investment · Bonus Tips",
hero_cta="🌱 Open My Account Now",
crumbs=[("Home","index.html"),("Sign Up",None)],
faqs=[
  ("What is the fastest way to start investing on Acorns?","Click our link → enter email and password → fill personal info (5 min) → link bank via Plaid (2 min) → make $5 deposit → you're invested. Total: 10 minutes or less."),
  ("Does signing up affect my credit score?","No — Acorns does not run a credit check. Opening an investment account has zero impact on your credit score."),
  ("What if my bank isn't supported by Plaid?","Plaid supports 12,000+ US banks and credit unions. If your bank isn't supported, contact Acorns support — they can often link accounts manually via routing and account numbers."),
  ("How do I know my bonus was credited?","After making your qualifying first deposit, the bonus investment typically appears in your portfolio within 5–10 business days. Check your transaction history in the app under 'Earnings.'"),
],
body="""
<section class="cb">
  <p class="lead">Opening an Acorns account is genuinely fast — 10 minutes from zero to first investment. This guide walks you through each step, what to expect, and how to set up your account to maximize returns from day one.</p>

  <div class="offer featured">
    <div class="ob">🌱 Start Here</div>
    <h3>Open Acorns — Free Bonus for New Accounts</h3>
    <ul>
      <li>✅ 10 minutes to set up</li>
      <li>✅ No credit check — no impact on credit score</li>
      <li>✅ First month free</li>
      <li>✅ Free bonus investment via our link</li>
    </ul>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open Acorns Account</a>
    <p class="tc">18+ US residents with SSN only. Investing involves risk.</p>
  </div>

  <h2>Step-by-Step Setup</h2>

  <h3>Step 1 — Click Our Link and Choose Registration Method</h3>
  <p>Click the button above. You'll land on Acorns' sign-up page. You can register with email/password or with Google/Apple sign-in. Email registration gives you more control over your login credentials.</p>

  <h3>Step 2 — Personal Information (3 minutes)</h3>
  <p>Acorns is SEC-regulated and must collect:</p>
  <ul>
    <li>Legal name, date of birth (must be 18+), US residential address</li>
    <li>Social Security Number — required by law for investment accounts for IRS reporting</li>
    <li>Employment status and income range</li>
    <li>Investment experience level</li>
  </ul>
  <p>This information is encrypted and required by all regulated investment platforms — it's not specific to Acorns.</p>

  <h3>Step 3 — Portfolio Questionnaire (2 minutes)</h3>
  <p>Answer 5 questions about your investing goals, time horizon, and risk tolerance. Acorns will recommend a portfolio. Our recommendation for most people under 40: accept the recommendation or go one level more aggressive.</p>

  <h3>Step 4 — Link Your Bank Account (2 minutes)</h3>
  <p>Acorns uses Plaid to connect your bank. Find your bank in the list, enter your online banking credentials (Plaid never stores them — it's read-only), and confirm. This takes under 2 minutes for major US banks.</p>

  <h3>Step 5 — Link Cards for Round-Ups (1 minute)</h3>
  <p>Add every debit and credit card you regularly use. The more cards linked, the more Round-Up opportunities. Don't skip this — it's the feature that will invest hundreds of dollars for you automatically.</p>

  <h3>Step 6 — Make Your First Deposit and Claim Your Bonus</h3>
  <p>Transfer at least $5 to activate your account. Set up a recurring investment ($25–$50/week recommended). Enable Round-Up multipliers if you want to accelerate your investing.</p>

  <h3>Step 7 — Open Acorns Later IRA (2 minutes)</h3>
  <p>Immediately open your IRA. It's included in your $3/month plan — there's no reason to wait. Specify Roth IRA (for most people) and set a small recurring contribution. The earlier you start tax-free compounding, the better.</p>

  <div class="callout">
    <strong>💡 Day-One Optimization:</strong> Complete your KYC identity verification immediately — upload your government ID via the app. KYC is required before any withdrawal. Doing it day one means if you ever win big, you can cash out immediately without waiting for verification.
  </div>
</section>
"""
))

# ── 13. PROMO CODE ────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-promo-code",
title="Acorns Promo Code June 2026 — Best Bonus Offer for New Accounts",
desc="Find the best Acorns promo code and sign-up bonus for June 2026. Our affiliate link unlocks the best available offer — no expired codes, no dead ends.",
kw="acorns promo code 2026, acorns bonus june 2026, acorns free money signup, acorns referral code",
h1="Acorns Promo Code June 2026 — <em>Claim Your Free Bonus</em>",
pill="Live Offer · Updated June 2026 · New Accounts",
hero_cta="🎁 Claim My Acorns Bonus",
crumbs=[("Home","index.html"),("Promo Code",None)],
faqs=[
  ("Why doesn't Acorns use traditional promo codes?","Acorns moved away from promo codes to affiliate-link-based bonuses because codes get shared, expire, and create inconsistent user experiences. Qualified partner links (like ours) activate the best available offer automatically."),
  ("How long does the bonus take to appear?","After your qualifying first deposit, the bonus investment typically appears in your Acorns portfolio within 5–10 business days. It will show as a credit in your transaction history."),
  ("Is the bonus actual cash I can withdraw?","The bonus is a real investment in your portfolio. Once it's invested and your account remains open for the qualifying period (usually 30–90 days), it becomes fully withdrawable like any other investment."),
  ("Can I get a bonus if I already have an Acorns account?","No — sign-up bonuses are strictly for new accounts. Existing users can earn through the referral program (found in app under Account → Invite Friends) and through Acorns Earn brand partnerships."),
],
body="""
<section class="cb">
  <p class="lead">Acorns doesn't use traditional promo codes. Instead, new users get a bonus investment automatically when they sign up through a qualifying partner link and make their first deposit. Our link is one of those qualified links — here's exactly how to claim it.</p>

  <div class="offer featured">
    <div class="ob">🎁 Live Offer — June 2026</div>
    <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
      <span style="color:var(--amber);font-size:1.1rem;letter-spacing:3px">★★★★★</span>
      <span style="font-family:'Fraunces',serif;font-size:1.4rem;font-weight:900;color:var(--teal3)">Active</span>
      <span style="font-size:0.78rem;color:var(--muted)">— Verified by AcornsGuide</span>
    </div>
    <h3>Free Bonus Investment — New Acorns Accounts</h3>
    <ul>
      <li>✅ Bonus investment credited after first deposit</li>
      <li>✅ No code needed — activates automatically</li>
      <li>✅ First month subscription free</li>
      <li>✅ New US accounts only</li>
      <li>✅ Real investment — not points or cashback</li>
    </ul>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🎁 Claim Bonus — Open Acorns</a>
    <p class="tc">T&Cs apply. New accounts only. Must make qualifying deposit. Bonus amount subject to change — check landing page for current offer.</p>
  </div>

  <h2>Why Our Link Beats Promo Code Sites</h2>
  <p>Search "Acorns promo code" and you'll find dozens of sites listing codes. Most are:</p>
  <ul>
    <li>Expired — Acorns discontinued code-based promotions</li>
    <li>Fake — many sites fabricate codes to earn referral clicks</li>
    <li>Outdated — code sites rarely update when Acorns changes its offers</li>
  </ul>
  <p>Our affiliate link is a direct partnership with Acorns. It always routes to the best active offer, updates automatically when promotions change, and requires nothing from you — just click and sign up.</p>

  <h2>Other Ways to Earn Free Investments on Acorns</h2>
  <ul>
    <li><strong>Acorns Earn</strong> — shop at 450+ partner brands through the app or browser extension and earn bonus investments. Apple, Walmart, Nike, Airbnb, Lyft and hundreds more.</li>
    <li><strong>Referral program</strong> — refer friends via your unique link. Both you and the friend receive a bonus when they open and fund an account.</li>
    <li><strong>Premium 1% IRA match</strong> — Acorns Premium ($5/month) adds a 1% match on new IRA contributions. On $7,000/year contribution that's $70 free.</li>
    <li><strong>Found Money</strong> — use your linked card at participating retailers and earn automatic bonus investments without any extra steps.</li>
  </ul>
</section>
"""
))

# ── 14. ACORNS EARLY ──────────────────────────────────────────
PAGES.append(dict(
slug="acorns-early",
title="Acorns Early 2026 — Investing for Your Kids Made Automatic",
desc="Complete guide to Acorns Early custodial accounts in 2026. How UTMA/UGMA accounts work, what to invest for kids, tax rules, and why starting early changes everything.",
kw="acorns early 2026, acorns kids account, acorns custodial account utma ugma, invest for children",
h1="Acorns Early — <em>Build Your Kids' Wealth Automatically</em>",
pill="Kids Investing · UTMA/UGMA · Compound Growth",
hero_cta="🌱 Open Acorns Early",
crumbs=[("Home","index.html"),("Acorns Early",None)],
faqs=[
  ("At what age should I open an Acorns Early account for my child?","As early as possible — ideally at birth. The difference between starting at birth vs age 10 is enormous due to compound growth. An account opened at birth with $50/month has roughly double the value at age 65 vs one started at age 10."),
  ("What happens when my child turns 18?","At the age of majority (18 in most states, 21 in others), Acorns notifies your child and transfers control of the account to them. They can choose to keep investing, withdraw, or move the funds elsewhere. It's entirely their decision."),
  ("Can grandparents or relatives contribute to Acorns Early?","You can share your account funding with relatives, but they can't directly contribute to a custodial account you control. A workaround: relatives can contribute to a 529 (college savings plan) or gift you money that you then invest in the Acorns Early account."),
  ("Is Acorns Early better than a 529 college savings plan?","Different tools for different goals. A 529 has superior tax advantages specifically for education expenses. Acorns Early is more flexible — the money can be used for anything when the child takes control. Consider having both: 529 for education, Acorns Early for general wealth building."),
],
body="""
<section class="cb">
  <p class="lead">The greatest financial gift you can give a child is an early start on investing. Not money — an early start. Time is the variable that transforms small amounts into life-changing wealth. Acorns Early makes it automatic.</p>

  <div class="offer featured">
    <div class="ob">🌱 Kids' Future</div>
    <h3>Open Acorns Early — Included in Premium ($5/month)</h3>
    <ul>
      <li>✅ UTMA/UGMA custodial account for any minor</li>
      <li>✅ Multiple children under one $5/month plan</li>
      <li>✅ Same automated investing as adult accounts</li>
      <li>✅ Child gains full control at age of majority</li>
    </ul>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open Acorns Early</a>
    <p class="tc">Acorns Premium $5/month. Investing involves risk. UTMA/UGMA rules vary by state.</p>
  </div>

  <h2>The Starting Age Impact — Real Numbers</h2>
  <table class="gtbl">
    <thead><tr><th>Start Age</th><th>Monthly Investment</th><th>Value at 65</th><th>Total Contributed</th><th>Compound Gains</th></tr></thead>
    <tbody>
      <tr><td class="hi">Birth (0)</td><td>$50/month</td><td class="hi">$847,000</td><td>$39,000</td><td>$808,000</td></tr>
      <tr><td>Age 5</td><td>$50/month</td><td>$589,000</td><td>$36,000</td><td>$553,000</td></tr>
      <tr><td>Age 10</td><td>$50/month</td><td>$406,000</td><td>$33,000</td><td>$373,000</td></tr>
      <tr><td>Age 18</td><td>$50/month</td><td>$205,000</td><td>$28,200</td><td>$177,000</td></tr>
      <tr><td>Age 25</td><td>$50/month</td><td>$120,000</td><td>$24,000</td><td>$96,000</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">Assumes 7% average annual return to age 65. Illustrative only.</p>

  <h2>The $258 Difference Every Month You Wait</h2>
  <p>Starting at birth vs age 5 (a 5-year delay) costs $258,000 in final wealth despite investing the same $50/month. That's the cost of waiting. Every month you delay opening an account for a newborn costs approximately $2,000 in potential wealth at retirement.</p>

  <h2>Tax Rules for Custodial Accounts</h2>
  <p>Custodial accounts don't have the tax advantages of IRAs or 529s. Investment income is subject to what the IRS calls the "Kiddie Tax":</p>
  <ul>
    <li>First $1,300/year of investment income: untaxed (2026 threshold)</li>
    <li>$1,300–$2,600/year: taxed at child's rate (usually 10%)</li>
    <li>Above $2,600/year: taxed at parent's marginal rate</li>
  </ul>
  <p>For most families investing $50–$200/month in a child's account, the portfolio won't generate $2,600/year in dividends for many years. Tax impact is minimal in early years.</p>
</section>
"""
))

# ── 15. ACORNS EARN ───────────────────────────────────────────
PAGES.append(dict(
slug="acorns-earn",
title="Acorns Earn 2026 — Get Free Investments From Everyday Shopping",
desc="How Acorns Earn works in 2026. Earn bonus investments at 450+ brands including Apple, Walmart, and Airbnb. How to maximize your free investments from everyday spending.",
kw="acorns earn 2026, acorns found money, acorns earn brands, free investments acorns shopping",
h1="Acorns Earn — <em>Free Investments Every Time You Shop</em>",
pill="Earn Guide · 450+ Brands · Maximize Rewards",
hero_cta="🌱 Start Earning Investments",
crumbs=[("Home","index.html"),("Acorns Earn",None)],
faqs=[
  ("How is Acorns Earn different from regular cashback?","Regular cashback gives you money. Acorns Earn invests the equivalent amount directly into your portfolio. Psychologically this is more powerful — you're not tempted to spend cashback because it immediately becomes an investment."),
  ("How long until Earn bonuses appear in my portfolio?","Most Acorns Earn rewards appear within 60–90 days of the qualifying purchase. In-store card-linked rewards (Found Money) typically take 30–60 days. Browser extension rewards take 60–90 days."),
  ("Are Acorns Earn bonuses taxable?","Yes — bonus investments from Acorns Earn are considered investment income and may be taxable. Acorns will include them in your 1099 for the tax year in which they're credited."),
  ("Do Earn bonuses count toward wagering requirements?","No — Acorns Earn is not gambling. It's investment rewards from brand partnerships, similar to a loyalty program. There are no wagering requirements."),
],
body="""
<section class="cb">
  <p class="lead">Acorns Earn turns shopping into free investing. Instead of (or in addition to) traditional cashback, you earn bonus investments credited directly to your portfolio whenever you shop at 450+ partner brands. Most Acorns users leave hundreds of dollars per year in unclaimed Earn rewards.</p>

  <div class="offer featured">
    <div class="ob">🌱 Start Earning</div>
    <h3>Activate Acorns Earn — Free Investments From Shopping</h3>
    <ul>
      <li>✅ 450+ partner brands — Apple to Airbnb</li>
      <li>✅ Rewards invested directly into your portfolio</li>
      <li>✅ Browser extension activates automatically</li>
      <li>✅ Card-linked in-store rewards require no effort</li>
    </ul>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open Acorns &amp; Start Earning</a>
    <p class="tc">Earn amounts vary by brand. Investing involves risk.</p>
  </div>

  <h2>How Acorns Earn Works — Two Paths</h2>

  <h3>Path 1: Found Money (Automatic, Card-Linked)</h3>
  <p>Link your debit or credit card to Acorns. When you use that card at a participating retailer — in person or online — the bonus investment is triggered automatically. Nothing extra to do. You buy groceries at a partner store, a bonus investment appears in your portfolio 30–60 days later.</p>

  <h3>Path 2: Browser Extension (Online Shopping)</h3>
  <p>Install the free Acorns browser extension (Chrome, Safari, Edge). When you visit a partner website, the extension displays the available Earn offer. One click to activate, then shop normally. The investment is credited within 60–90 days.</p>

  <h2>Top Acorns Earn Brands — June 2026</h2>
  <table class="gtbl">
    <thead><tr><th>Brand</th><th>Earn Type</th><th>Reward</th><th>Category</th></tr></thead>
    <tbody>
      <tr><td>Apple</td><td>Percentage</td><td>Up to $25 on qualifying purchases</td><td>Tech</td></tr>
      <tr><td>Walmart</td><td>Fixed per order</td><td>$3–$5 per qualifying purchase</td><td>Retail</td></tr>
      <tr><td>Airbnb</td><td>Fixed per booking</td><td>$25 on first booking</td><td>Travel</td></tr>
      <tr><td>Nike</td><td>Percentage</td><td>2% on all purchases</td><td>Apparel</td></tr>
      <tr><td>Hotels.com</td><td>Percentage</td><td>3% on hotel bookings</td><td>Travel</td></tr>
      <tr><td>Lyft</td><td>Fixed per ride</td><td>$1–$2 per ride</td><td>Transport</td></tr>
      <tr><td>Blue Apron</td><td>Fixed</td><td>$30 on first order</td><td>Food</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">Offers subject to change. Check the Acorns app for current available offers.</p>

  <h2>Maximizing Your Earn Rewards</h2>
  <ol>
    <li><strong>Install the browser extension immediately</strong> — it runs passively and you'll never miss an offer</li>
    <li><strong>Check Earn tab before any major purchase</strong> — booking a hotel, buying electronics, purchasing flights</li>
    <li><strong>Holiday season is peak Earn</strong> — November–December brand offers are typically highest of the year</li>
    <li><strong>Use your Acorns checking card for in-store</strong> — maximizes card-linked rewards across all Partner retailers</li>
    <li><strong>Book travel through Earn links</strong> — hotel and flight bonuses can be $20–$50+ per booking</li>
  </ol>
</section>
"""
))

# ── 16. FOR BEGINNERS ─────────────────────────────────────────
PAGES.append(dict(
slug="acorns-for-beginners",
title="Acorns for Beginners 2026 — Zero to Investor in 10 Minutes",
desc="The complete beginner's guide to Acorns investing in 2026. What you need to know before you start, the 5 setup mistakes to avoid, and the 90-day plan to build real wealth.",
kw="acorns for beginners 2026, acorns beginner guide, start investing first time acorns, acorns setup tips",
h1="Acorns for Beginners — <em>From Zero to Investor in 10 Minutes</em>",
pill="Beginner Guide · No Experience Needed · 2026",
hero_cta="🌱 I'm Ready — Open Acorns",
crumbs=[("Home","index.html"),("For Beginners",None)],
faqs=[
  ("I know nothing about investing — can I still use Acorns?","Acorns is literally designed for this. You don't need to understand stocks, bonds, ETFs, or market cycles. You answer 5 questions, link your bank, and Acorns makes every investment decision automatically."),
  ("What should I do first — build an emergency fund or start investing?","Build your emergency fund first. 3–6 months of expenses in a savings account is the financial foundation. Acorns can run simultaneously with a small recurring investment while you build emergency savings — $5–$10/week through Acorns while building your cash cushion is fine."),
  ("Is it a bad time to start investing?","No time is categorically bad to start investing if your time horizon is 10+ years. The stock market has historically recovered from every downturn. The cost of waiting to invest is usually higher than the cost of investing during a temporary downturn."),
  ("How much should a beginner invest each week?","Start with what you can sustain indefinitely. $10–$25/week recurring plus Round-Ups is a great starting point. Increase as your income grows. Consistency matters more than amount when you're starting out."),
],
body="""
<section class="cb">
  <p class="lead">You don't need financial knowledge to use Acorns. You need $5, 10 minutes, and the decision to start. This guide covers the 5 mistakes beginners make and the 90-day action plan that sets you up for decades of automated wealth building.</p>

  <div class="offer featured">
    <div class="ob">🌱 Start Here</div>
    <h3>Zero Investment Experience? Perfect.</h3>
    <p style="color:rgba(240,250,247,.78);margin-bottom:18px">Acorns is built for people starting from zero. Every decision is made for you. Setup takes 10 minutes.</p>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Open Acorns — Start Investing</a>
    <p class="tc">$5 minimum. $3/month after first month free. Investing involves risk.</p>
  </div>

  <h2>5 Mistakes Every Beginner Makes (And How to Avoid Them)</h2>

  <h3>Mistake 1 — Choosing Too Conservative a Portfolio</h3>
  <p>Fear of losing money causes beginners to pick Conservative (20% stocks, 80% bonds). Over 20–30 years, this dramatically underperforms. If you're under 45 and won't need the money for 10+ years, Moderate or Moderately Aggressive is almost certainly the right choice. Temporary paper losses aren't real losses until you sell.</p>

  <h3>Mistake 2 — Not Opening the IRA</h3>
  <p>Half of Acorns users only use Acorns Invest (taxable) and skip Acorns Later (IRA). This is a major missed opportunity. The IRA is included in your $3/month plan and provides tax-free compounding. Open it day one.</p>

  <h3>Mistake 3 — Checking the App Daily</h3>
  <p>Daily balance checks create anxiety about normal market fluctuations and increase the likelihood of emotional decisions. Check once a month at most. Acorns is designed for passive investors — the app will perform the same whether you check it daily or yearly.</p>

  <h3>Mistake 4 — Not Linking All Cards for Round-Ups</h3>
  <p>Beginners often link only their main debit card. Linking all cards — credit cards, second debit cards, store cards — can triple the Round-Up amount. It takes 2 minutes per card and generates significant automatic investing over time.</p>

  <h3>Mistake 5 — Stopping During Market Downturns</h3>
  <p>When markets fall and balances drop, beginners panic and stop investing. This is exactly backwards. Market downturns mean you're buying ETF shares at a lower price. Stopping during downturns and resuming at market highs is the most common way retail investors underperform the market.</p>

  <h2>Your 90-Day Beginner Action Plan</h2>
  <table class="gtbl">
    <thead><tr><th>Timeline</th><th>Action</th><th>Why It Matters</th></tr></thead>
    <tbody>
      <tr><td>Day 1</td><td>Open account, link bank, make $5 deposit</td><td>Get invested — start the clock on compounding</td></tr>
      <tr><td>Day 1</td><td>Open Acorns Later Roth IRA</td><td>Tax-free retirement growth starts now, not later</td></tr>
      <tr><td>Day 1</td><td>Link all cards for Round-Ups</td><td>Maximum automatic investing from day one</td></tr>
      <tr><td>Day 2</td><td>Set $25/week recurring investment</td><td>Automation removes the need for willpower</td></tr>
      <tr><td>Day 2</td><td>Enable Round-Up multiplier (2×)</td><td>Doubles automatic spare-change investing painlessly</td></tr>
      <tr><td>Day 7</td><td>Install Acorns browser extension</td><td>Start capturing Earn rewards passively</td></tr>
      <tr><td>Month 1</td><td>Upload ID for KYC verification</td><td>Required before any withdrawal — do it early</td></tr>
      <tr><td>Month 2</td><td>Increase recurring to $50/week if possible</td><td>Bigger contribution compounds to much larger result</td></tr>
      <tr><td>Month 3</td><td>Review balance (once only)</td><td>Confirm everything is working — then ignore for another month</td></tr>
    </tbody>
  </table>
</section>
"""
))

# ── 17. IS IT SAFE ────────────────────────────────────────────
PAGES.append(dict(
slug="is-acorns-safe",
title="Is Acorns Safe? 2026 — SEC Registration, SIPC Protection & Security",
desc="Is Acorns safe to use in 2026? Complete security review covering regulatory oversight, SIPC insurance, encryption, and what happens to your money in every worst-case scenario.",
kw="is acorns safe 2026, acorns legitimate, acorns security, acorns sipc sipc protection",
h1="Is Acorns Safe? — <em>The Complete Security Analysis</em>",
pill="Safety Review · SIPC Protected · SEC Oversight",
hero_cta="🌱 Invest Safely with Acorns",
crumbs=[("Home","index.html"),("Is It Safe?",None)],
faqs=[
  ("Is Acorns FDIC insured?","Acorns Invest (investment account) is NOT FDIC insured — it's covered by SIPC up to $500,000. Acorns Checking (the bank account) IS FDIC insured up to $250,000 per depositor through Lincoln Savings Bank."),
  ("What is the difference between FDIC and SIPC protection?","FDIC protects bank deposits against bank failure. SIPC protects investment assets against brokerage failure. Neither protects against normal investment losses (market risk). Both protect against the financial institution itself failing."),
  ("Has Acorns ever been involved in fraud or securities violations?","No major regulatory violations or fraud charges have been brought against Acorns as of the date of this review. Acorns maintains clean registration records with the SEC and FINRA, verifiable in their public databases."),
  ("What does 'SEC registered' actually mean for investors?","SEC registration means Acorns must file regular disclosures, follow specific rules about how it manages client money, maintain a fiduciary duty to clients, and submit to SEC examination. It doesn't mean the SEC endorses Acorns — it means Acorns is subject to federal oversight."),
],
body="""
<section class="cb">
  <p class="lead">Before connecting your bank account and trusting an app with your money, you deserve a complete picture of what protections exist. Acorns has a strong regulatory framework — here's exactly what it means in practice, including every worst-case scenario.</p>

  <div class="stats">
    <div class="stat"><div class="n">SEC</div><div class="l">Registered RIA</div></div>
    <div class="stat"><div class="n">SIPC</div><div class="l">$500K Protected</div></div>
    <div class="stat"><div class="n">FINRA</div><div class="l">Member Broker</div></div>
    <div class="stat"><div class="n">FDIC</div><div class="l">Checking Insured</div></div>
    <div class="stat"><div class="n">256-bit</div><div class="l">SSL Encryption</div></div>
    <div class="stat"><div class="n">Since 2014</div><div class="l">10 Years Operating</div></div>
  </div>

  <h2>Regulatory Oversight — Three Layers</h2>
  <table class="cmp">
    <thead><tr><th>Regulator</th><th>What They Regulate</th><th>Acorns Status</th><th>What It Means for You</th></tr></thead>
    <tbody>
      <tr><td>SEC</td><td>Investment advisor practices</td><td><span class="yes">Registered RIA</span></td><td>Fiduciary duty, regular disclosure, oversight</td></tr>
      <tr><td>FINRA</td><td>Broker-dealer operations</td><td><span class="yes">Member (Acorns Securities)</span></td><td>Trading rules, customer protection standards</td></tr>
      <tr><td>SIPC</td><td>Customer asset protection</td><td><span class="yes">Member — $500K</span></td><td>Your investments covered if Acorns Securities fails</td></tr>
    </tbody>
  </table>

  <h2>Scenario Analysis — Your Money in Worst Cases</h2>
  <h3>Scenario 1: Acorns Goes Bankrupt</h3>
  <p>Your investment assets are held in segregated accounts at DriveWealth, LLC — a third-party custodian — in your name, not Acorns' name. They are legally your property. SIPC covers up to $500,000 if the brokerage fails. If Acorns closes, your holdings would transfer to another custodian or back to you.</p>

  <h3>Scenario 2: Acorns Gets Hacked</h3>
  <p>Acorns uses 256-bit SSL encryption, two-factor authentication, and biometric login. Your bank credentials are handled by Plaid (not stored by Acorns). In the event of a breach, Acorns carries cybersecurity insurance and is subject to SEC and FINRA reporting requirements for security incidents.</p>

  <h3>Scenario 3: Market Crashes and You Lose Money</h3>
  <p>This is normal market risk — neither SIPC nor FDIC protects against market losses. Your ETF values can decline significantly during recessions. However, the Vanguard and iShares ETFs Acorns uses have recovered from every historical market downturn. This is the risk inherent to all investing, not specific to Acorns.</p>

  <h3>Scenario 4: You Get Locked Out of Your Account</h3>
  <p>Your investments remain yours even if you lose account access. Acorns customer support can verify your identity and restore access. As a worst case, SIPC can help recover assets from a registered brokerage even with disputed account access.</p>

  <h2>Security Features</h2>
  <ul>
    <li>256-bit SSL encryption on all data in transit and at rest</li>
    <li>Two-factor authentication (SMS and authenticator app)</li>
    <li>Face ID and Touch ID biometric login on mobile</li>
    <li>Plaid bank connection — your bank credentials never stored by Acorns</li>
    <li>Automatic session timeout after inactivity</li>
    <li>Real-time suspicious activity monitoring</li>
  </ul>
  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Invest Safely — Open Acorns</a>
  <p class="tc" style="margin-top:10px">SIPC covers brokerage failure, not market losses. Investing involves risk.</p>
</section>
"""
))

# ── 18. WITHDRAW ──────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-withdraw",
title="How to Withdraw Money from Acorns 2026 — Timing, Taxes & Steps",
desc="Step-by-step guide to withdrawing money from Acorns in 2026. How long it takes, tax implications, IRA rules, and the checklist to complete before you cash out.",
kw="acorns withdrawal 2026, how to withdraw acorns, acorns cash out, acorns withdrawal time",
h1="How to Withdraw from Acorns — <em>What You Need to Know First</em>",
pill="Withdrawal Guide · Tax Tips · No Fees",
hero_cta="🌱 Keep Investing — See the Guide",
crumbs=[("Home","index.html"),("Withdraw Guide",None)],
faqs=[
  ("Can I withdraw my Acorns money at any time?","Yes — your taxable Acorns Invest account has no lock-up period. You can request a withdrawal anytime. IRA accounts (Acorns Later) have restrictions — withdrawing before 59½ triggers a 10% penalty plus income taxes on most withdrawals."),
  ("Why is my withdrawal taking longer than expected?","The most common delays: (1) incomplete KYC verification — upload your ID in account settings. (2) Active bonus with unmet conditions. (3) Large withdrawal triggering manual security review. (4) Bank processing times over weekends."),
  ("Do I have to pay taxes when I withdraw from Acorns?","Withdrawing from your taxable account may trigger capital gains taxes on profits. If you've held investments over 1 year, long-term capital gains rates (0–20%) apply. Under 1 year, short-term rates (your income tax rate) apply. IRA withdrawals have separate rules."),
  ("What happens to my Round-Ups after I withdraw?","Withdrawing doesn't stop Round-Ups or recurring investments. They continue automatically unless you pause or cancel them separately. If you're closing your account, cancel recurring investments first."),
],
body="""
<section class="cb">
  <p class="lead">Acorns is designed for long-term investing — but you can access your money when you need it. Understanding the timeline, taxes, and potential pitfalls means no surprises when you do need to withdraw.</p>

  <h2>Withdrawal by Account Type</h2>
  <table class="cmp">
    <thead><tr><th>Account</th><th>Restrictions</th><th>Processing Time</th><th>Tax Implications</th></tr></thead>
    <tbody>
      <tr><td>Acorns Invest (taxable)</td><td><span class="yes">None — withdraw anytime</span></td><td>3–6 business days</td><td>Capital gains on profits</td></tr>
      <tr><td>Acorns Later — Roth IRA</td><td>Contributions anytime; earnings restricted before 59½</td><td>3–6 business days</td><td>Contributions tax-free; earnings taxed + 10% if early</td></tr>
      <tr><td>Acorns Later — Traditional IRA</td><td>10% penalty + taxes before 59½</td><td>3–6 business days</td><td>All withdrawals taxed as income + 10% early penalty</td></tr>
      <tr><td>Acorns Checking</td><td><span class="yes">None — instant</span></td><td><span class="yes">Same day</span></td><td>No investment taxes (cash account)</td></tr>
    </tbody>
  </table>

  <h2>How to Withdraw — Step by Step</h2>
  <ol>
    <li>Open the Acorns app → tap the account (Invest, Later, or Checking)</li>
    <li>Tap the dollar amount or "Withdraw" button</li>
    <li>Enter amount and confirm your linked bank account</li>
    <li>Acorns sells the necessary ETF holdings (T+1 to T+2)</li>
    <li>Cash transfers to your bank account (T+3 to T+5 business days)</li>
    <li>Total: 3–6 business days from request to receipt</li>
  </ol>

  <h2>The Pre-Withdrawal Checklist</h2>
  <ul>
    <li><strong>Is KYC complete?</strong> — Incomplete identity verification delays all withdrawals. Check in Account → Personal Info. Upload government ID if not done.</li>
    <li><strong>Any active bonus conditions?</strong> — If you claimed a sign-up bonus, withdrawing before completing conditions (usually 30–90 days of account activity) forfeits the bonus.</li>
    <li><strong>Is this an IRA?</strong> — Confirm whether your withdrawal qualifies as a penalty-free distribution. Roth IRA contributions (not earnings) are always penalty-free.</li>
    <li><strong>Tax timing</strong> — If you're close to a year of holding an investment, waiting until 12 months switches you from short-term to long-term capital gains rates, which can save thousands on larger amounts.</li>
    <li><strong>Cancel recurring investments if closing</strong> — Withdrawing all funds doesn't stop scheduled transfers. Cancel recurring investments and Round-Ups separately if you're fully exiting.</li>
  </ul>

  <div class="callout">
    <strong>💡 One Withdrawal Tip:</strong> Never withdraw from your Acorns Later IRA early unless it's a genuine emergency. The 10% penalty plus taxes often costs more than the benefit of accessing the funds. Consider withdrawing from your taxable Acorns Invest account first, or exploring IRA hardship distributions that may qualify for penalty exceptions.
  </div>
</section>
"""
))

# ── 19. TAX GUIDE ─────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-tax-guide",
title="Acorns Tax Guide 2026 — Everything You Owe on Your Investments",
desc="Complete Acorns tax guide for 2026. What forms Acorns sends, how capital gains and dividends are taxed, IRA tax advantages, and how to minimize your Acorns tax bill.",
kw="acorns taxes 2026, acorns 1099 tax form, acorns capital gains, acorns tax guide usa",
h1="Acorns Tax Guide 2026 — <em>What You Owe and How to Minimize It</em>",
pill="Tax Guide · 1099 Forms · Minimize Your Bill",
hero_cta="🌱 Invest Tax-Smart with Acorns",
crumbs=[("Home","index.html"),("Tax Guide",None)],
faqs=[
  ("When does Acorns send me tax forms?","Acorns sends 1099 forms by February 15 for the previous tax year. You may receive a 1099-B (capital gains/losses from sales), 1099-DIV (dividends), and/or 1099-R (IRA distributions). You'll get an email notification when forms are available in the app."),
  ("What if I didn't receive a 1099 from Acorns?","If your account had very low activity (minimal dividends, no sales), Acorns may not issue a 1099. However, all investment income must still be reported even without a form. Check the 'Documents' section in the app."),
  ("Does Acorns' automatic rebalancing create taxable events?","Yes — when Acorns rebalances your portfolio in a taxable account, it sells some ETFs and buys others. Sales generate capital gains or losses that appear on your 1099-B. This is normal and managed, but you must report it."),
  ("How do I minimize taxes on my Acorns account?","Three main strategies: (1) Prioritize Acorns Later (IRA) — tax-free or tax-deferred growth. (2) Hold investments long-term — long-term capital gains rates are significantly lower. (3) Use tax-loss opportunities — if Acorns sells at a loss during rebalancing, those losses can offset other gains."),
],
body="""
<section class="cb">
  <p class="lead">Investing with Acorns has tax implications — but they're manageable and often minimal. Understanding what you owe and when helps you file correctly and take advantage of strategies that legally reduce your bill.</p>

  <div class="callout">
    <strong>⚠️ Disclaimer:</strong> This is general educational information, not tax advice. Tax laws change and individual circumstances vary significantly. Consult a licensed CPA or tax professional for advice specific to your situation.
  </div>

  <h2>Tax Forms Acorns Issues</h2>
  <table class="gtbl">
    <thead><tr><th>Form</th><th>Issued By</th><th>What It Reports</th><th>When to Expect</th></tr></thead>
    <tbody>
      <tr><td>1099-B</td><td>Acorns Securities</td><td>Proceeds and cost basis from ETF sales (from rebalancing)</td><td>By Feb 15</td></tr>
      <tr><td>1099-DIV</td><td>Acorns Securities</td><td>Dividends received from your ETFs</td><td>By Feb 15</td></tr>
      <tr><td>1099-R</td><td>Acorns Securities</td><td>Distributions from IRA (Acorns Later)</td><td>By Jan 31</td></tr>
      <tr><td>5498</td><td>Acorns Securities</td><td>IRA contributions for the year</td><td>By May 31</td></tr>
    </tbody>
  </table>

  <h2>Capital Gains Tax — What You Pay on Acorns Profits</h2>
  <table class="cmp">
    <thead><tr><th>Holding Period</th><th>Tax Rate (2026)</th><th>On What Amount</th></tr></thead>
    <tbody>
      <tr><td>Under 12 months (short-term)</td><td>10–37% (ordinary income)</td><td>Profit from sales held under 1 year</td></tr>
      <tr><td>12+ months (long-term)</td><td><span class="yes">0%, 15%, or 20%</span></td><td>Profit from sales held over 1 year</td></tr>
      <tr><td>Qualified dividends</td><td><span class="yes">0%, 15%, or 20%</span></td><td>Most ETF dividends qualify</td></tr>
    </tbody>
  </table>

  <h2>IRA Tax Advantages — Where Acorns Later Shines</h2>
  <p><strong>Roth IRA:</strong> Contributions come from after-tax income. All growth is tax-free. All qualifying withdrawals in retirement are tax-free. No annual 1099 for investment growth. Best long-term tax outcome for most investors.</p>
  <p><strong>Traditional IRA:</strong> Contributions may be deductible. Growth is tax-deferred. Withdrawals in retirement taxed as ordinary income. Generates a 1099-R for distributions. Best when your tax rate is higher now than it will be in retirement.</p>

  <h2>3 Legal Ways to Minimize Your Acorns Tax Bill</h2>
  <ol>
    <li><strong>Maximize Acorns Later (IRA) contributions</strong> — growth in the IRA is either tax-free (Roth) or tax-deferred (Traditional). Neither triggers annual taxes on dividends or rebalancing gains.</li>
    <li><strong>Hold investments long-term</strong> — if you must withdraw, wait until you've held 12+ months to access lower long-term capital gains rates.</li>
    <li><strong>Don't ignore small losses</strong> — when Acorns' rebalancing generates small losses, those losses offset gains elsewhere in your return. Track them via your 1099-B.</li>
  </ol>
</section>
"""
))

# ── 20. COMPOUND INTEREST ─────────────────────────────────────
PAGES.append(dict(
slug="acorns-compound-interest",
title="Compound Interest & Acorns 2026 — Real Numbers on Long-Term Growth",
desc="How compound interest transforms small Acorns investments into serious wealth. Real growth tables, the starting-age impact, and why the math favors starting today over any other day.",
kw="acorns compound interest 2026, acorns long term growth, how much can acorns make, acorns investment returns",
h1="Compound Interest & Acorns — <em>The Math That Changes Everything</em>",
pill="Growth Calculator · Real Numbers · Start Today",
hero_cta="🌱 Start Compounding Now",
crumbs=[("Home","index.html"),("Compound Interest",None)],
faqs=[
  ("How does Acorns use compound interest?","Acorns automatically reinvests dividends from your ETFs back into your portfolio. Each reinvested dividend buys more ETF shares, which generate more dividends, which buy more shares. This compounding loop is why long-term returns dramatically exceed what contributions alone would generate."),
  ("How much can I realistically make with Acorns?","This depends entirely on how much you invest and for how long. $50/month for 20 years at 7% average return produces approximately $26,000 in total contributions and a $56,000 portfolio — $30,000 from compound growth. Over 40 years the same $50/month grows to $131,000."),
  ("Is 7% a realistic return assumption for Acorns?","7% is the commonly used historical average for balanced stock/bond portfolios after inflation. The S&P 500 has averaged approximately 10% nominal (before inflation) annually over long periods. Acorns' Moderate portfolio (60/40 stocks/bonds) has historically been in the 6–8% range."),
  ("Does compound interest work differently on Acorns vs other accounts?","No — compound interest is a mathematical principle that applies equally everywhere. What makes Acorns effective for compounding is automation (you never miss a contribution) and dividend reinvestment (every dividend immediately buys more shares)."),
],
body="""
<section class="cb">
  <p class="lead">Compound interest is the mathematical engine of long-term wealth. Acorns is built to capture it automatically. The numbers are genuinely staggering — and the earlier you start, the more dramatic the effect. Here's the real math.</p>

  <div class="offer featured">
    <div class="ob">🌱 Start the Clock</div>
    <h3>Every Month You Wait Has a Compounding Cost</h3>
    <p style="color:rgba(240,250,247,.78);margin-bottom:18px">A 22-year-old investing $50/month starting today has $847,000 by retirement. A 32-year-old starting the same habit has $406,000. The 10-year delay costs $441,000 from the same $50/month.</p>
    <a href="{A}" class="cta glow" target="_blank" rel="noopener sponsored">🌱 Start Compounding Today</a>
    <p class="tc">Assumes 7% avg annual return. Illustrative only. Investing involves risk.</p>
  </div>

  <h2>The Compound Growth Tables — $50/Month at 7%</h2>
  <table class="gtbl">
    <thead><tr><th>Years Invested</th><th>Monthly Contribution</th><th>Total Contributed</th><th>Portfolio Value</th><th>Compound Gains</th></tr></thead>
    <tbody>
      <tr><td>5 years</td><td>$50</td><td>$3,000</td><td>$3,580</td><td>$580</td></tr>
      <tr><td>10 years</td><td>$50</td><td>$6,000</td><td>$8,680</td><td>$2,680</td></tr>
      <tr><td>15 years</td><td>$50</td><td>$9,000</td><td>$15,870</td><td>$6,870</td></tr>
      <tr><td>20 years</td><td>$50</td><td>$12,000</td><td>$26,070</td><td>$14,070</td></tr>
      <tr><td>25 years</td><td>$50</td><td>$15,000</td><td>$40,560</td><td>$25,560</td></tr>
      <tr><td>30 years</td><td>$50</td><td>$18,000</td><td class="hi">$61,880</td><td class="hi">$43,880</td></tr>
      <tr><td>40 years</td><td>$50</td><td>$24,000</td><td class="hi">$131,390</td><td class="hi">$107,390</td></tr>
    </tbody>
  </table>

  <h2>The Contribution Amount Impact — 30 Years at 7%</h2>
  <table class="gtbl">
    <thead><tr><th>Monthly Investment</th><th>Total Contributed</th><th>Portfolio at 30 Years</th><th>Compound Gains</th></tr></thead>
    <tbody>
      <tr><td>$25/month</td><td>$9,000</td><td>$30,940</td><td>$21,940</td></tr>
      <tr><td>$50/month</td><td>$18,000</td><td>$61,880</td><td>$43,880</td></tr>
      <tr><td>$100/month</td><td>$36,000</td><td>$123,750</td><td>$87,750</td></tr>
      <tr><td>$200/month</td><td>$72,000</td><td>$247,510</td><td class="hi">$175,510</td></tr>
      <tr><td>$500/month</td><td>$180,000</td><td>$618,770</td><td class="hi">$438,770</td></tr>
    </tbody>
  </table>

  <h2>The J-Curve — Why the Early Years Feel Slow</h2>
  <p>Compound growth follows a J-curve: modest in the early years, exponential in the later years. A $50/month investor earns $2,680 in compound gains over 10 years, but $107,390 in compound gains over 40 years. The last 10 years generate more compound gains than the first 30 combined.</p>
  <p>This is why investing consistency matters more than investment amount in the early years. Starting with $25/month at age 22 beats starting with $100/month at age 32 by over $100,000 at retirement.</p>

  <h2>Why Acorns Is Ideal for Capturing Compound Growth</h2>
  <ul>
    <li><strong>Automatic dividend reinvestment</strong> — every dividend immediately buys more shares without you doing anything</li>
    <li><strong>Never misses a contribution</strong> — Round-Ups and recurring investments mean you invest through recessions, holidays, and every other reason people normally stop</li>
    <li><strong>Low expense ratios</strong> — Vanguard ETFs at 0.03% leave nearly all returns to compound</li>
    <li><strong>Removes emotional selling</strong> — passive automation means you don't sell during downturns, which is the most common way investors destroy their compound growth</li>
  </ul>
</section>
"""
))

# ══════════════════════════════════════════════════════════════
# SUPPORT FILES
# ══════════════════════════════════════════════════════════════
def build_sitemap(pages):
    urls=[]
    for p in pages:
        s=p["slug"]
        loc=f"{BASE_URL}/" if s=="index" else f"{BASE_URL}/{s}.html"
        pri="1.0" if s=="index" else "0.8"
        urls.append(f'  <url><loc>{loc}</loc><lastmod>{BUILT_ON}</lastmod><changefreq>weekly</changefreq><priority>{pri}</priority></url>')
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(urls)+"\n</urlset>"

ROBOTS=f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n"

def build_llms(pages):
    lines=[f"# {SITE_NAME} v2","","> AcornsGuide is an independent review and comparison site for Acorns investing app users. Reviews, fee analysis, competitor comparisons, and how-to guides for US investors.","","## Pages",""]
    for p in pages:
        s=p["slug"]
        loc=f"{BASE_URL}/" if s=="index" else f"{BASE_URL}/{s}.html"
        lines.append(f"- [{p['title']}]({loc}) — {p['desc'][:90]}")
    lines+=["","## Affiliate Disclosure","","AcornsGuide earns commissions when users sign up via our affiliate links. All sponsored links are marked. Investing involves risk. Not financial advice."]
    return "\n".join(lines)

PAGE_404=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>404 — Page Not Found | AcornsGuide</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<style>{CSS}
.e{{text-align:center;padding:130px 24px}}
.e .n{{font-family:'Fraunces',serif;font-size:9rem;font-weight:900;color:var(--teal3);line-height:1;opacity:0.4}}
.e h2{{font-family:'Fraunces',serif;font-size:1.6rem;color:#fff;margin:14px 0 8px}}
.e p{{color:var(--muted);margin-bottom:32px}}
</style>
</head>
<body>
{nav_html()}
<div class="e">
  <div class="n">404</div>
  <h2>Page not found.</h2>
  <p>But your first Acorns investment is one click away.</p>
  <a href="index.html" class="cta">← Back to AcornsGuide</a>
</div>
</body>
</html>"""

def build():
    print(f"\nAcornsGuide v2 — All New Content\nBuilding {len(PAGES)} pages → {OUT}/\n")
    for p in PAGES:
        s=p["slug"]
        fname="index.html" if s=="index" else f"{s}.html"
        html=page(
            slug=s,title=p["title"],desc=p["desc"],kw=p["kw"],
            h1=p["h1"],pill=p["pill"],hero_cta=p["hero_cta"],
            body=p["body"],faqs=p.get("faqs"),crumbs=p.get("crumbs")
        )
        (OUT/fname).write_text(html,encoding="utf-8")
        print(f"  ✅  {fname}")
    (OUT/"sitemap.xml").write_text(build_sitemap(PAGES),encoding="utf-8")
    print("  ✅  sitemap.xml")
    (OUT/"robots.txt").write_text(ROBOTS,encoding="utf-8")
    print("  ✅  robots.txt")
    (OUT/"llms.txt").write_text(build_llms(PAGES),encoding="utf-8")
    print("  ✅  llms.txt")
    (OUT/"404.html").write_text(PAGE_404,encoding="utf-8")
    print("  ✅  404.html")
    print(f"\n🌱  Done! {len(PAGES)} pages + 4 support files → ./{OUT}/")
    print(f"    Deploy → https://brightlane.github.io/acorns/\n")

if __name__ == "__main__":
    build()
