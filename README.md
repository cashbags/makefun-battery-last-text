# The Battery's Last Text to Its Charger — Cancellation Notice

[![make.fun](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?ref=qrg7fvky)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/cashbags/makefun-battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?ref=qrg7fvky)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/cashbags/makefun-battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?ref=qrg7fvky)

A one-line comedy text for [The Battery's Last Text to Its Charger](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?ref=qrg7fvky) on make.fun.

## The entry

> This is your cancellation notice: my free trial ends at 0%. You had all day to plug me in. Your card will not be charged. Neither will I.

`main.py` writes exactly that line to `/output/entry.txt` — 137 characters, one
line, byte-identical on every run. No network, no clock, no randomness.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else. See `DESIGN.md` for why this
line was chosen: the lane check against the field, the 12-candidate pairwise
tournament, and the judge-criteria reasoning.
