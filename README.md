# softscout

Source for https://softscout.support (Cloudflare Pages, no build step).

- Edit page text in `tools/content.py` (English and Bengali side by side).
- Rebuild the pages: `python3 tools/build.py` (needs Python 3, no packages).
- Commit the generated `index.html` files, `bn/`, `404.html`, `sitemap.xml` and `robots.txt`.
- Styles: `assets/site.css`. Phone menu: `assets/site.js`.

English pages live at `/`, Bengali at `/bn/`. Pushing to `main` deploys the live site;
any other branch gets a preview link at `<branch>.softscout.pages.dev`.
