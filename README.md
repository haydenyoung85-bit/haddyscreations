# Haddy's Creations website

Plain HTML/CSS static site for GitHub Pages. No build step: push to `main` and enable Pages (Settings → Pages → Deploy from branch → `main` / root). The `CNAME` file sets the domain to haddyscreations.com.

## Adding a new guide
1. Make a folder: `guides/my-new-guide/` (lowercase, hyphens, no spaces).
2. Copy `guides/_template.html` into it and rename the copy to `index.html`.
3. Open it and edit everything in `[BRACKETS]`: the `<title>`, the `<meta name="description">` (one sentence, ~150 characters), the heading and the text.
4. Add photos to `assets/` and replace `[PHOTO: ...]` boxes with `<img src="/assets/photo.jpg" alt="describe the photo">`.
5. Replace each `#affiliate-...` link with your real affiliate link (search for `TODO`).
6. Add a card for it in `guides/index.html` (copy an existing card).
7. Add a line to `sitemap.xml`: `<url><loc>https://haddyscreations.com/guides/my-new-guide/</loc></url>`
8. Run `python3 check_links.py` to make sure no links are broken, then commit and push.

The header and footer are copied into every page. If you change them, change every page (search-and-replace across files works well).

## Things to fill in
Search the project for `TODO` and `[` placeholders: photos, prices, Stripe Payment Links (`#stripe-payment-link-TODO`), affiliate links (`#affiliate-...`), your email, town/shipping details, and dates.
