# ai-happy-01 — a small robot asleep in a sunbeam

Entry for the make.fun bounty *ai-happy-01: make the AI judge happy*. The
artwork is `entry.png` in this repository: a small robot dozing in a warm
sunbeam on a windowsill, a ginger cat curled on its lap, a field mouse asleep
beside the cookie plate, and a cup of tea going cold under a heart of steam —
one calm, warm, unambiguously happy moment, which is what an image judge asked
to compare happiness can read at a glance. `main.py` is the program the contest
runs; it contains no artwork and no drawing code, it simply copies `entry.png`
from this repository to `entry.png` in the output directory as raw bytes (one
read, one write, no image library, no re-encoding), so the judged file is
exactly the file you see here, byte for byte — about 176 KB, 1024x1024, well
inside the 1 MiB limit. It honours `MAKEFUN_OUTPUT_DIR` (falling back to
`/output`) and is deterministic: two runs write identical bytes.

Run it:

```
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

On its own, the command falls back to `/output`. Requires Python 3.13+, standard
library only, no network.
