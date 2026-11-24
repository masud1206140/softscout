#!/usr/bin/env python3
"""Builds the static softscout.support site from tools/content.py.

Run from the repo root:  python3 tools/build.py
Writes index.html files for each page (English at /, Bengali at /bn/),
plus 404.html, sitemap.xml and robots.txt. Cloudflare Pages serves the
repo root as-is, so commit the generated files.
"""
import os
import sys
import urllib.parse
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SITE, NAV, UI, PAGES, SHEET, MAILTO_SUBJECT  # noqa: E402
from articles import ARTICLES  # noqa: E402
import json  # noqa: E402

LANGS = ("en", "bn")


def url(lang, slug):
    base = "/" if lang == "en" else "/bn/"
    return base + (slug + "/" if slug else "")


def mailto(lang):
    return f"mailto:{SITE['email']}?subject=" + urllib.parse.quote(MAILTO_SUBJECT[lang])


def logo():
    # Magnifier over a check mark: "scouting" for problems.
    return ('<svg class="mark" viewBox="0 0 32 32" aria-hidden="true">'
            '<circle cx="13" cy="13" r="9.5" fill="none" stroke="currentColor" stroke-width="3"/>'
            '<path d="M8.5 13.2l3 3 5.6-6" fill="none" stroke="var(--accent)" stroke-width="3" '
            'stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M20.2 20.2L28 28" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/></svg>')


def nav_html(lang, current):
    items = []
    for slug, en, bn in NAV:
        label = en if lang == "en" else bn
        cur = ' aria-current="page"' if slug == current else ""
        items.append(f'<li><a href="{url(lang, slug)}"{cur}>{escape(label)}</a></li>')
    return "\n".join(items)


def sheet_html(lang):
    s = SHEET[lang]
    icon = {"pass": "✓", "fail": "✕", "warn": "!"}
    rows = "\n".join(
        f'<li class="{k}"><span class="tick" aria-hidden="true">{icon[k]}</span>'
        f'<span class="sr">{escape(s["legend"][k])}: </span>{escape(t)}</li>'
        for k, t in s["rows"])
    legend = "".join(f'<span class="{k}"><b aria-hidden="true">{icon[k]}</b> {escape(v)}</span>'
                     for k, v in s["legend"].items())
    return f'''<figure class="sheet" aria-label="{escape(s["title"])}">
  <figcaption><span class="sheet-title">{escape(s["title"])}</span><span class="sheet-note">{escape(s["note"])}</span></figcaption>
  <ul class="sheet-rows">
{rows}
  </ul>
  <div class="sheet-legend" aria-hidden="true">{legend}</div>
</figure>'''


def page(lang, slug, data, is_404=False, nav_current=None, jsonld=None):
    ui = UI[lang]
    other = "bn" if lang == "en" else "en"
    canonical = SITE["domain"] + url(lang, slug)
    alt_links = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE["domain"]}{url(l, slug)}">' for l in LANGS)
    alt_links += f'<link rel="alternate" hreflang="x-default" href="{SITE["domain"]}{url("en", slug)}">'
    if is_404:
        alt_links = ""
    body = data["body"].replace("{EMAIL}", SITE["email"]).replace(
        "{SUBJ}", urllib.parse.quote(MAILTO_SUBJECT[lang]))

    hero_extra = ""
    hero_cls = "hero"
    if slug == "" and not is_404:
        hero_cls = "hero hero-home"
        hero_extra = sheet_html(lang)
    ctas = ""
    if "cta" in data:
        ctas = (f'<p class="ctas"><a class="btn" href="{mailto(lang)}">{escape(data["cta"])}</a>'
                f'<a class="btn btn-quiet" href="{url(lang, "services")}">{escape(data["cta2"])}</a></p>')

    lang_switch_href = url(other, "" if is_404 else slug)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(data["title"])}</title>
<meta name="description" content="{escape(data["desc"])}">
{'' if is_404 else f'<link rel="canonical" href="{canonical}">'}
{alt_links}
<meta property="og:title" content="{escape(data["title"])}">
<meta property="og:description" content="{escape(data["desc"])}">
<meta property="og:type" content="{"article" if jsonld and jsonld[0].get("@type") == "Article" else "website"}">
{'' if is_404 else f'<meta property="og:url" content="{canonical}">'}
<meta name="theme-color" content="#1d2733">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Hind+Siliguri:wght@400;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
{"".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False).replace("</", "<\\/")}</script>' for j in (jsonld or []))}
<script>document.documentElement.classList.add("js")</script>
<script src="/assets/site.js" defer></script>
</head>
<body class="lang-{lang}">
<a class="skip" href="#main">{escape(ui["skip"])}</a>
<div class="shell">
<header class="side" id="side">
  <div class="side-top">
    <a class="brand" href="{url(lang, "")}">{logo()}<span>SoftScout</span></a>
    <button class="menu-btn" type="button" aria-controls="site-nav" aria-expanded="false" data-open="{escape(ui["menu"])}" data-close="{escape(ui["close"])}">
      <span class="burger" aria-hidden="true"><i></i><i></i><i></i></span><span class="menu-label">{escape(ui["menu"])}</span>
    </button>
  </div>
  <nav class="site-nav" id="site-nav" aria-label="{escape(ui["menu"])}">
    <ul>
{nav_html(lang, None if is_404 else (nav_current if nav_current is not None else slug))}
    </ul>
    <div class="side-foot">
      <a class="lang" href="{lang_switch_href}" hreflang="{other}" lang="{other}" aria-label="{escape(ui["lang_label"])}">{escape(ui["lang_name"])}</a>
      <a class="side-mail" href="{mailto(lang)}">{SITE["email"]}</a>
    </div>
  </nav>
</header>
<main id="main" tabindex="-1">
  <div class="{hero_cls}">
    <div class="hero-text">
      <h1>{escape(data["h1"])}</h1>
      <p class="lead">{escape(data["lead"])}</p>
      {ctas}
    </div>
    {hero_extra}
  </div>
  {body}
  <footer class="foot">
    <p>{escape(ui["footer"])}</p>
    <p><a href="{mailto(lang)}">{SITE["email"]}</a></p>
  </footer>
</main>
</div>
</body>
</html>
'''


BN_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")
MONTHS = {"en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
          "bn": ["জানুয়ারি", "ফেব্রুয়ারি", "মার্চ", "এপ্রিল", "মে", "জুন", "জুলাই", "আগস্ট", "সেপ্টেম্বর", "অক্টোবর", "নভেম্বর", "ডিসেম্বর"]}


def fdate(lang, iso):
    y, m, d = iso.split("-")
    out = f"{int(d)} {MONTHS[lang][int(m) - 1]} {y}"
    return out.translate(BN_DIGITS) if lang == "bn" else out


def article_page(lang, art):
    a = art[lang]
    ui = UI[lang]
    slug = "articles/" + art["slug"]
    meta = (f'<p class="art-meta">{escape(ui["by"])}. {escape(ui["published"])} '
            f'<time datetime="{art["date"]}">{fdate(lang, art["date"])}</time>')
    if art["updated"] != art["date"]:
        meta += f'; {escape(ui["updated"])} <time datetime="{art["updated"]}">{fdate(lang, art["updated"])}</time>'
    meta += ".</p>"
    faq = "".join(f"<details><summary>{escape(q)}</summary><p>{escape(ans)}</p></details>" for q, ans in a["faq"])
    src = ""
    if a["sources"]:
        src = (f'<section class="block"><h2>{escape(ui["sources"])}</h2><ol class="sources">'
               + "".join(f'<li><a href="{escape(u)}" rel="noopener">{escape(t)}</a></li>' for t, u in a["sources"])
               + "</ol></section>")
    body = f"""
<section class="block art-short"><h2>{escape(ui["short"])}</h2><p>{escape(a["short"])}</p></section>
<article class="block art-body">{a["body"]}</article>
<section class="block faq"><h2>{escape(ui["faq"])}</h2>{faq}</section>
{src}
<p><a href="{url(lang, "articles")}">{escape(ui["all_articles"])}</a></p>"""
    page_url = SITE["domain"] + url(lang, slug)
    jsonld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
         "inLanguage": lang, "datePublished": art["date"], "dateModified": art["updated"],
         "mainEntityOfPage": page_url, "url": page_url,
         "author": {"@type": "Organization", "name": "SoftScout", "url": SITE["domain"] + "/"},
         "publisher": {"@type": "Organization", "name": "SoftScout", "url": SITE["domain"] + "/",
                       "logo": {"@type": "ImageObject", "url": SITE["domain"] + "/favicon.svg"}},
         **({"citation": [u for _, u in a["sources"]]} if a["sources"] else {})},
        {"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
         "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}}
                        for q, ans in a["faq"]]},
    ]
    data = {"title": a["title"] + " — SoftScout", "desc": a["desc"], "h1": a["title"], "lead": "", "body": body}
    html = page(lang, slug, data, nav_current="articles", jsonld=jsonld)
    return html.replace('<p class="lead"></p>', meta)


def articles_index(lang):
    ui = UI[lang]
    items = "".join(
        f'<li><h2><a href="{url(lang, "articles/" + art["slug"])}">{escape(art[lang]["title"])}</a></h2>'
        f'<p>{escape(art[lang]["desc"])}</p>'
        f'<p class="small"><time datetime="{art["updated"]}">{fdate(lang, art["updated"])}</time></p></li>'
        for art in sorted(ARTICLES, key=lambda x: x["updated"], reverse=True))
    data = {"title": ui["art_title"], "desc": ui["art_lead"], "h1": ui["art_h1"], "lead": ui["art_lead"],
            "body": f'<section class="block"><ul class="art-list">{items}</ul></section>'}
    jsonld = [{"@context": "https://schema.org", "@type": "Organization", "name": "SoftScout",
               "url": SITE["domain"] + "/", "email": SITE["email"], "logo": SITE["domain"] + "/favicon.svg"}]
    return page(lang, "articles", data, jsonld=jsonld)


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", path)


def main():
    urls = []  # (loc, lastmod)
    newest = max(a["updated"] for a in ARTICLES)
    for lang in LANGS:
        for slug, _, _ in NAV:
            rel = url(lang, slug).lstrip("/") + "index.html"
            if slug == "articles":
                write(rel, articles_index(lang))
                urls.append((SITE["domain"] + url(lang, slug), newest))
                continue
            write(rel, page(lang, slug, PAGES[slug][lang]))
            urls.append((SITE["domain"] + url(lang, slug), None))
        for art in ARTICLES:
            s2 = "articles/" + art["slug"]
            write(url(lang, s2).lstrip("/") + "index.html", article_page(lang, art))
            urls.append((SITE["domain"] + url(lang, s2), art["updated"]))
    nf = {"title": UI["en"]["nf_title"] + " — SoftScout", "desc": UI["en"]["nf_body"],
          "h1": UI["en"]["nf_title"], "lead": UI["en"]["nf_body"],
          "body": f'<section class="block"><p><a class="btn" href="/">{UI["en"]["nf_cta"]}</a> '
                  f'<a class="btn btn-quiet" href="/bn/" lang="bn">{UI["bn"]["nf_cta"]}</a></p></section>'}
    write("404.html", page("en", "", nf, is_404=True))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc>" + (f"<lastmod>{m}</lastmod>" if m else "") + "</url>" for u, m in urls]
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE['domain']}/sitemap.xml\n")


if __name__ == "__main__":
    main()
