# makefun-news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/shusay12/makefun-news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/shusay12/makefun-news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

<sub>Entered on [make.fun](https://make.fun/?ref=susay21&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>

---

# 21 November 2026 in one image

Entry for make.fun's **news-image-20261121** bounty: one image that sums up
the world news of Saturday 21 November 2026.

The image is a dated front page: a header naming the day over four labelled
panels, one per top story. Built at ~03:40 UTC, only ~3.5 hours into the UTC
day, so the day's news was still thin — every story below is anchored to
something that genuinely happened or was reported on 21 November itself
(see the caveat):

1. **COP31 runs into overtime** — the Antalya climate talks spill into
   Saturday with no deal; a third draft is due this morning and the text
   still makes no mention of fossil fuels.
2. **Cyclone Akvan's rain soaks Bengal** — the storm's remnants bring heavy
   rain into Saturday morning; 300,000 people were evacuated and no major
   damage has been reported.
3. **NATO chief heads to Warsaw** — Mark Rutte visits Poland today after
   Russian missiles crashed there on Friday; Warsaw calls it a deliberate
   provocation.
4. **Rahul completes the SENA set** — KL Rahul's century in Wellington
   makes him the first Indian opener with Test hundreds in South Africa,
   England, New Zealand and Australia.

## Early-day caveat

This entry was built early in the UTC day (03:40 UTC / 10:40 WIB), so it
covers the stories that were already reported by then. Two of the four
panels lean on Friday events whose consequences land today (Akvan's
Saturday rain; Rutte's Saturday visit to Warsaw after Friday's missile
incidents), and the wording says so — nothing is presented as happening
on 21 November that actually happened earlier. The ICJ's Myanmar genocide
ruling (Thursday 19 November) was deliberately left out for that reason.

## Layout

- `entry.png` — the image the judge sees (1024x1024, under 1 MiB).
- `main.py` — the entry program: copies `entry.png` to `/output/entry.png`
  (or `$MAKEFUN_OUTPUT_DIR/entry.png` outside the grader), byte for byte.
- `build_image.py` — composites `entry.png` from the four illustrations in
  `panels/` with Pillow: centre-crops each panel, draws the date header and
  the headline strips.
- `panels/` — the four generated editorial illustrations, one per story.

Run the entry the way the grader does:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
