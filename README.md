# AcornsGuide v2 🌱

> Independent Acorns investing reviews, comparisons, and guides for US investors.

**Live site:** https://brightlane.github.io/acorns/

---

## What This Is

AcornsGuide is an affiliate marketing site targeting people researching the Acorns micro-investing app. It covers in-depth reviews, competitor comparisons (Robinhood, Betterment, Stash, Wealthfront), fee analysis, and practical how-to guides — linking readers to Acorns via an affiliate partner link.

Built entirely from a single Python script. No frameworks, no database, no server. Deploys automatically to GitHub Pages via GitHub Actions.

---

## How It Works

```
build.py  →  docs/  →  GitHub Pages  →  live site
```

1. `build.py` generates 20 HTML pages + support files into `docs/`
2. GitHub Actions commits `docs/` back to the repo and deploys to GitHub Pages
3. The site rebuilds automatically every day at 6 AM UTC

---

## Pages (20 total)

| Page | URL |
|---|---|
| Homepage — Honest Review & Verdict | `/` |
| How Acorns Works | `/how-acorns-works.html` |
| Full App Review | `/acorns-review.html` |
| Acorns vs Robinhood | `/acorns-vs-robinhood.html` |
| Acorns vs Betterment | `/acorns-vs-betterment.html` |
| Acorns vs Stash | `/acorns-vs-stash.html` |
| Acorns vs Wealthfront | `/acorns-vs-wealthfront.html` |
| Round-Ups Guide | `/acorns-round-ups.html` |
| Acorns Later IRA | `/acorns-later-ira.html` |
| Fees Breakdown | `/acorns-fees.html` |
| Portfolios Guide | `/acorns-portfolios.html` |
| Sign Up Guide | `/acorns-sign-up.html` |
| Promo Code | `/acorns-promo-code.html` |
| Acorns Early (Kids) | `/acorns-early.html` |
| Acorns Earn | `/acorns-earn.html` |
| For Beginners | `/acorns-for-beginners.html` |
| Is Acorns Safe? | `/is-acorns-safe.html` |
| Withdraw Guide | `/acorns-withdraw.html` |
| Tax Guide | `/acorns-tax-guide.html` |
| Compound Interest | `/acorns-compound-interest.html` |

---

## Adding or Editing Content

All content lives in `build.py` inside the `PAGES` list. Each page is a Python dict:

```python
PAGES.append(dict(
    slug="page-slug",
    title="Page Title | AcornsGuide",
    desc="Meta description for Google.",
    kw="keyword one, keyword two",
    h1="H1 Heading — <em>Styled Part</em>",
    pill="Eyebrow Label · Subtitle Text",
    hero_cta="🌱 Button Text",
    crumbs=[("Home","index.html"),("Page Name",None)],
    faqs=[
        ("Question?", "Answer."),
    ],
    body="""
    <section class="cb">
      <p class="lead">Opening paragraph...</p>
      <h2>Section Heading</h2>
      <p>Body content. Use {A} for the affiliate link.</p>
      <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">Button</a>
    </section>
    """
))
```

Use `{A}` anywhere in the body to insert the affiliate link with UTM tracking automatically appended.

### Available CSS Classes

| Class | Use |
|---|---|
| `.cb` | Main content wrapper |
| `.lead` | Large intro paragraph with green left border |
| `.offer` | Offer/bonus card box |
| `.offer.featured` | Offer card with glowing green border |
| `.cta` | Green CTA button |
| `.cta.glow` | Animated pulsing CTA button |
| `.cta.sm` | Small CTA button |
| `.cta.outline` | Outlined CTA button |
| `.cmp` | Comparison table |
| `.gtbl` | Growth/data table |
| `.stats` | Stat cards grid |
| `.pros-cons` | Pros and cons two-column grid |
| `.verdict` | Score/verdict card |
| `.callout` | Highlighted callout box |
| `.yes` / `.no` / `.ok` | Table cell badges (green/red/amber) |
| `.hi` | Highlighted table cell text (teal) |

---

## Running Locally

```bash
python build.py
```

Creates a `docs/` folder with all HTML files. Open `docs/index.html` in a browser to preview.

**Requirements:** Python 3.7+ — standard library only, no pip installs needed.

---

## Deploying

Push any change to `main` — GitHub Actions builds and deploys automatically.

To trigger manually: **Actions → Build & Deploy AcornsGuide → Run workflow**

---

## Affiliate Link

All CTAs use:

```
https://convert.ctypy.com/aff_c?offer_id=29449&aff_id=21885
```

With UTM params automatically appended per page:

```
&utm_source=acornsguide&utm_medium=affiliate&utm_campaign={slug}
```

Track conversions by page in the affiliate dashboard using the `utm_campaign` value.

---

## File Structure

```
acorns/
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions — builds & deploys on push
├── build.py              # Generates entire site — edit content here
├── README.md             # This file
└── docs/                 # Auto-generated — do not edit manually
    ├── index.html
    ├── acorns-review.html
    ├── acorns-vs-robinhood.html
    ├── acorns-vs-betterment.html
    ├── acorns-vs-wealthfront.html
    ├── ... (20 pages total)
    ├── sitemap.xml
    ├── robots.txt
    ├── llms.txt
    └── 404.html
```

---

## SEO Features

- JSON-LD structured data on every page (WebPage, BreadcrumbList, FAQPage)
- Canonical URLs, Open Graph, Twitter Card meta tags
- XML sitemap with all 20 URLs, auto-updated on every build
- `robots.txt` pointing crawlers to the sitemap
- `llms.txt` for AI crawler discovery
- Custom 404 page with CTA
- Breadcrumb navigation on every page

---

## Design System

- **Fonts:** Plus Jakarta Sans (body) + Fraunces serif (headings/logo)
- **Colors:** Teal (#0d9488) on dark ink (#0c1a17) background
- **Accent:** Amber stars, rose badges for negatives
- **Components:** Verdict card, stat grid, pros/cons grid, comparison tables, offer cards, sticky mobile CTA

---

*Investing involves risk including possible loss of principal. Not financial advice. AcornsGuide earns affiliate commissions when users sign up via our links. Review all disclosures at acorns.com.*
