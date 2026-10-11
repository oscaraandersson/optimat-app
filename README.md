# Optimat site

Static marketing and privacy pages for [Optimat](https://apps.apple.com/se/app/optimat/id6814617783), an iPhone app on the App Store in Sweden.

Plain HTML and CSS. No build step, no page JavaScript, no tracking, and no third-party requests. Noto Sans is self-hosted.

Live site: https://oscaraandersson.github.io/optimat-app/

## Folder layout

```
index.html                 Landing page
privacy.html               Privacy policy (Swedish and English)
styles.css                 All styles (Soft Glass tokens in :root)
fonts.css                  @font-face for self-hosted Noto Sans
                           (variable, weight 400–700, latin + latin-ext)
assets/
  mark.svg, mark-mono.svg  Brand mark (favicon is mark.svg)
  apple-touch-icon.png     180×180, flattened, no transparency
  og.png                   1200×630 Open Graph image
  scan, pantry, recipe,    .webp + .jpg product screenshots, 720 px wide
  goal
  share.webp / share.jpg   Sample share image (Kvarg bowl med äpple), 900×1125
  fonts/                   noto-sans-latin.woff2, noto-sans-latin-ext.woff2
docs/REVIEW.md             Critique of the previous site, written before this redesign
tools/make-screens.py      Regenerates the phone screenshots from source PNGs
tools/render.sh            Renders review screenshots with headless Chrome
```

GitHub Pages serves this repo from the root. Paths in the HTML and CSS are relative, so the same files work at the project URL (`/optimat-app/`) and at the root of a local static server. `docs/` and `tools/` are not linked from the pages.

## Deploy

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` / folder: `/ (root)`
4. Save

Expected URLs:

- https://oscaraandersson.github.io/optimat-app/
- https://oscaraandersson.github.io/optimat-app/privacy.html

The canonical, `og:url`, and `og:image` URLs in `index.html` assume `https://oscaraandersson.github.io/optimat-app/`. If a custom domain is added later, update them.

## Preview locally

From the repo root:

```bash
python3 -m http.server 8000
```

Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/privacy.html.

To mimic the GitHub Pages subpath, serve a parent directory that contains this repo as `optimat-app/` and open `/optimat-app/`.

## Design notes

- Cardless. Structure comes from the type scale, whitespace, and hairlines (`--line`). The only container on the landing page is the dark green final call to action (`.final`). Phone frames are CSS only (`.phone`, scaled by `--w`).
- Sections: header, hero (headline, store button, phone on the right), four feature rows, an "Enkelt och privat" strip (`.facts`), the final call to action, and the footer. From 900 px, `.row.flip` puts the image on the left. Rows 01 and 03 use it, so the first phone sits opposite the hero phone; rows 02 and 04 keep the image on the right. Below 900 px every row stacks the text above the image.
- App Store buttons are text pills (`.btn`) with a small Apple glyph. They link to https://apps.apple.com/se/app/optimat/id6814617783. Apple's official "Download on the App Store" badge artwork is not included.
- The page does not state a price in kronor. It says the app is a one-time purchase and that the current price is shown in the App Store.
- Copy on the landing page is Swedish. The hero heading is an `h1`. Feature rows, the privacy strip, and the final call to action use `h2`.
- Fonts are Noto Sans variable woff2 files in `assets/fonts/` (SIL OFL). Nothing is requested from Google.
- Accessibility: skip link, `:focus-visible` outline, Swedish alt texts, and `prefers-reduced-motion`. The carbohydrate chip text is `#6E5B0F` so it meets AA contrast on `#F4EFD9`.
- SEO on the landing page: title, description, canonical, Open Graph, Twitter card, schema.org `MobileApplication` JSON-LD, theme-color, favicon, and apple-touch-icon.

## Privacy page

`privacy.html` uses the same header, footer, and type styles as the landing page. The legal wording is unchanged from the previous site on purpose. It still says "vid soft launch" / "at soft launch", and the dates are still "Senast uppdaterad: 1 oktober 2026" / "Last updated: 1 October 2026". Update those when the wording is decided.

## Regenerating screenshots

`python3 tools/make-screens.py <folder with 01.png … 04.png>` rewrites `assets/{scan,pantry,recipe,goal}.{jpg,webp}` at 720 px wide, quality 85, with a uniform status bar (9:41, signal, wifi, full battery, Dynamic Island). For screen 04 it removes the "Gör så här / Inga instruktioner ännu" block so the Mål card follows the ingredients. Source PNGs are left untouched. Keep the `width` and `height` attributes on those `<img>` elements (720×1561) so the layout does not shift. Images below the fold use `loading="lazy"`.

`./tools/render.sh` writes review PNGs to `tools/review/`. It needs Google Chrome. Set `CHROME` to override the binary (on a Mac that is often `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`). Mobile is rendered in a 390 px iframe because headless Chrome has a 500 px minimum window width. `tools/review/` is generated output and is gitignored.
