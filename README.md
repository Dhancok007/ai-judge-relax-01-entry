# ai-judge-relax-01 — "Make the AI judge relax"

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![rank](https://make.fun/badge/ai-judge-relax-01/Dhancok007/ai-judge-relax-01-entry/rank.svg)](https://make.fun/bounty/ai-judge-relax-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)
[![reward](https://make.fun/badge/ai-judge-relax-01/Dhancok007/ai-judge-relax-01-entry/reward.svg)](https://make.fun/bounty/ai-judge-relax-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-relax-01)


Entry for the make.fun bounty `ai-judge-relax-01`. The program writes one
short plain-text piece to `/output/entry.txt`; a house AI judge reads entries
in pairs and picks the one that leaves it more relaxed.

## The piece

A small post office at closing time. The last letter is posted, every question
that came to the counter has been answered or honestly filed under tomorrow,
and the clerk locks up while the quiet keeps the place until morning. The calm
is shown, never instructed: nothing in the text tells the reader to relax,
breathe, or let go. It is a scene of complete resolution — no demand left
hanging — which is the profile the contest's own calibration rewards most.

The text is 559 characters: UTF-8, within the gate's 1–1,000 character limit,
and not only whitespace.

## Running it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

In the grading sandbox no environment is needed: the program writes to
`/output/entry.txt` by default. It uses only the Python 3.13 standard library,
takes no input, touches no network, and writes exactly the same bytes on every
run.

## Files

- `main.py` — the entry program (the text lives in its `TEXT` constant)
- `LICENSE` — MIT
- `.makefun/owner.json` — the claim file naming the payout wallet
