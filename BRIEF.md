# Brief for Claude Code — page 6 photos

This folder builds a 29-page landscape PDF, "Sarah in New York — Part Seven".
The design and all copy are done. The only job right now is **photos for page 6**
(the "Day 2, up close" page). Nothing else in the deck should change.

## How it works
- `build.py` holds all content and generates `book.html`. `style.css` is the design.
- `render.py` runs the build and prints the PDF with Playwright/Chromium.
- Page 6 has five blocks. If an image exists at `images/day2/<n>.jpg` (or .png/.webp),
  the build uses it automatically in place of the colored plate. No code changes needed.

## The five images to find
Save each as `images/day2/<n>.jpg`, landscape orientation, at least 1200px wide,
under 400 KB each (resize/compress if needed).

1. `1.jpg` — The Chelsea gallery district: a gallery interior or the West 20s
   streetscape (David Zwirner 20th St, Gagosian 24th St, Hauser & Wirth 22nd St).
2. `2.jpg` — Printed Matter, 231 11th Ave: storefront or interior with the book walls.
3. `3.jpg` — Poster House, 119 W 23rd St: facade or gallery interior.
4. `4.jpg` — El Quijote in the Hotel Chelsea, 226 W 23rd St: the dining room with
   the Don Quixote murals, or the Hotel Chelsea facade if the interior isn't available.
5. `5.jpg` — The Surge: An Ode to Sinéad O'Connor at the Joyce Theater (Sept 16–27, 2026,
   choreographer Sonya Tayeh). Try the Joyce's page for the show at joyce.org
   (press/production photos by Tom Visser), then Factory International's page for
   the Manchester premiere. If no production still is usable, the Joyce Theater
   facade on 8th Ave at 19th.

## Sources, in order of preference
1. Wikimedia Commons (commons.wikimedia.org) — CC-licensed; note the author and license.
2. The venue's own website or press page.
3. Flickr, Creative Commons licenses only.
Skip anything watermarked, and skip stock/Google Images results with no clear license.

## Record what you used
Append one line per image to `images/day2/CREDITS.txt`:
`<n>.jpg — <source URL> — <author> — <license>`

## Build and check
```
pip install playwright && playwright install chromium
python render.py
```
Then open the PDF and look at page 6. The photos sit above each block's title, cropped
to a short landscape band. If a photo's subject is cut off badly, pick a different crop
or a different image; do not change `style.css` or the copy.
