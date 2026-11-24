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


def page(lang, slug, data, is_404=False):
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
<meta property="og:type" content="website">
{'' if is_404 else f'<meta property="og:url" content="{canonical}">'}
<meta name="theme-color" content="#1d2733">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=Hind+Siliguri:wght@400;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
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
{nav_html(lang, None if is_404 else slug)}
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


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", path)


def main():
    urls = []
    for lang in LANGS:
        for slug, _, _ in NAV:
            data = PAGES[slug][lang]
            rel = url(lang, slug).lstrip("/") + "index.html"
            write(rel, page(lang, slug, data))
            urls.append(SITE["domain"] + url(lang, slug))
    nf = {"title": UI["en"]["nf_title"] + " — SoftScout", "desc": UI["en"]["nf_body"],
          "h1": UI["en"]["nf_title"], "lead": UI["en"]["nf_body"],
          "body": f'<section class="block"><p><a class="btn" href="/">{UI["en"]["nf_cta"]}</a> '
                  f'<a class="btn btn-quiet" href="/bn/" lang="bn">{UI["bn"]["nf_cta"]}</a></p></section>'}
    write("404.html", page("en", "", nf, is_404=True))
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += [f"  <url><loc>{u}</loc></url>" for u in urls]
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /tools/\n\nSitemap: {SITE['domain']}/sitemap.xml\n")


if __name__ == "__main__":
    main()
