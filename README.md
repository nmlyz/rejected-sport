# rejected-sport

[![make.fun · u-motasimfuad-rejected-olympic-sports-9d83e7da](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![rank](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/nmlyz/rejected-sport/rank.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rejected-olympic-sports-9d83e7da)
[![reward](https://make.fun/badge/u-motasimfuad-rejected-olympic-sports-9d83e7da/nmlyz/rejected-sport/reward.svg)](https://make.fun/bounty/u-motasimfuad-rejected-olympic-sports-9d83e7da?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rejected-olympic-sports-9d83e7da)

rejected-sport writes one line to a text file: a sport the Olympics turned down. The line was picked from 38 candidates by pairwise judging against the brief — the event is the 100m dash, the twist is the committee's reason for running it backwards, and it lands on the last word. A commentator would have to read it with a straight face.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`). No network access needed; the same text, byte for byte, on every run. The line is 99 characters, a single line, and ends on its strongest beat. The program holds the line as one constant and checks it against the entry gate (length, single line, no leading or trailing space, exact judged length) before writing it, then reads the file back to confirm the bytes match.

---

<sub>Entered on [make.fun](https://make.fun/?ref=23ae7fx0&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-rejected-olympic-sports-9d83e7da)</sub>
