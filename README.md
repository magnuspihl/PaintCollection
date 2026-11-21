# Paint Collection

Track which Army Painter **Warpaints Fanatic** paints you own, see coverage per Flexible Triad family, and get suggestions for what to buy next.

- 216 paints, grouped into the 27 six-step Flexible Triad families (dark → light) plus effects, fluorescents, metallics, gemstones, washes and auxiliaries.
- Click a paint to mark it owned. Collection is stored in the browser (localStorage); "Share link" encodes it in the URL to move it between devices.
- Boxed sets (Starter, Most Wanted, Mega, Wargamers, Washes, Metallics, Combat Se7ens, …) can be marked owned in one click, and show new paints, triads completed and price vs. singles.

## Editing

`index.html` is generated — edit `src/template.html` (page) or `data/paints.json` (paints, families, sets, prices), then run:

```sh
python3 build.py
```

## Data sources

- Colours sampled from Army Painter's full-range Fanatic chart; families from the official Flexible Triad System poster.
- Set contents read from the product images on thearmypainter.com; prices from the EU webshop (EUR) as of 2026-11-21.
