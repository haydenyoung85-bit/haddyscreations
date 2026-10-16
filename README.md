# Haddy's Creations website

Plain HTML/CSS static site for GitHub Pages. No build step: push to `main` and enable Pages (Settings → Pages → Deploy from branch → `main` / root). Live (for now) at https://haydenyoung85-bit.github.io/haddyscreations/ . All links are **relative** (e.g. `../shop/`), so the site works both there and on a custom domain. Exception: `404.html` uses full URLs because GitHub serves it at any broken path.

## Adding a new guide
1. Make a folder: `guides/my-new-guide/` (lowercase, hyphens, no spaces).
2. Copy `guides/_template.html` into it and rename the copy to `index.html`.
3. Links: the template sits one folder up from your new guide, so after moving it, change every `../` to `../../` (e.g. `../assets/style.css` → `../../assets/style.css`). Then edit everything in `[BRACKETS]`: the `<title>`, the `<meta name="description">` (one sentence, ~150 characters), the heading and the text.
4. Add photos to `assets/` and replace `[PHOTO: ...]` boxes with `<img src="/assets/photo.jpg" alt="describe the photo">`.
5. Replace each `#affiliate-...` link with your real affiliate link (search for `TODO`).
6. Add a card for it in `guides/index.html` (copy an existing card).
7. Add a line to `sitemap.xml`: `<url><loc>https://haydenyoung85-bit.github.io/haddyscreations/guides/my-new-guide/</loc></url>`
8. Run `python3 check_links.py` to make sure no links are broken, then commit and push.

The header and footer are copied into every page. If you change them, change every page (search-and-replace across files works well).

## Things to fill in
Search the project for `TODO` and `[` placeholders: photos, prices, Stripe Payment Links (`#stripe-payment-link-TODO`), affiliate links (`#affiliate-...`), your email, town/shipping details, and dates.

## Adding the custom domain later (haddyscreations.com)
The CNAME file was removed on purpose: a CNAME without working DNS breaks the github.io address. Once you've bought the domain:
1. At your domain registrar, add DNS records: four `A` records for `@` pointing to 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153, and a `CNAME` record for `www` pointing to `haydenyoung85-bit.github.io`.
2. Create a file named `CNAME` in the repo root containing just `haddyscreations.com`, commit and push (or set it in repo Settings → Pages → Custom domain).
3. When the certificate is ready, tick "Enforce HTTPS" in Settings → Pages.
4. Replace `https://haydenyoung85-bit.github.io/haddyscreations/` with `https://haddyscreations.com/` in `sitemap.xml`, `robots.txt` (also change the Disallow line to `/guides/_template.html`) and `404.html`.
