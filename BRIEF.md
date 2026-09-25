# Brief for Claude Code — six new photos, plus file moves

Drop `build.py` and `style.css` over the repo. Then make these file moves in `images/`
(the plan changed; some places came off, new ones went on):

- `images/day3/5.jpg` (Sammy's Fish Box) → move to `images/day5/6.jpg` (a copy is in this zip too).
- Delete `images/day3/2.jpg` (Red Rooster) and `images/day3/4.jpg` (City Island).
- Delete `images/day10/2.jpg` (Tenement Museum), `images/day10/3.jpg` (Katz's), `images/day10/4.jpg` (Yonah Schimmel's).
- Delete `images/day13/4.jpg` (Joe's Pizza) and `images/day14/2.jpg` (Brooklyn Bridge).
Update each folder's CREDITS.txt to match (drop the removed lines; add Sammy's line to day5).

## Six new slots (same rules and sources as before; ~1.9:1 crops; credits lines)
1. `images/day3/2.jpg` — **Melba's**, 300 W 114th St at Frederick Douglass Blvd: storefront/awning, or chicken and waffles.
2. `images/day3/4.jpg` — **The Schomburg Center**, 515 Malcolm X Blvd at 135th: the building exterior or the lobby.
3. `images/day10/2.jpg` — **The Museum at Eldridge Street**, 12 Eldridge St: the sanctuary interior (Commons has good ones) or the facade.
4. `images/day10/3.jpg` — **Essex Market**, 88 Essex St: the new hall interior (2019) with stalls.
5. `images/day10/4.jpg` — **Economy Candy**, 108 Rivington St: the storefront or the packed interior.
6. `images/day13/4.jpg` — **Prince Street Pizza**, 27 Prince St: the pepperoni square, or the storefront with the line.
7. `images/day14/2.jpg` — **The Manhattan Bridge** walkway with the Brooklyn Bridge visible, or the Manhattan-side arch and colonnade at Canal and Bowery.

## Build
`python render.py`. The "up close" page now comes BEFORE each day's plan page; that's intended.
Check the new slots, then zip `images/` and hand it back.
