# NOTES

## What the image is

A small robot asleep in a warm sunbeam on a windowsill. A ginger cat is curled
up on its lap, a field mouse is asleep beside a plate with a cookie on it, and a
cup of tea is going cold with a heart of steam rising from it. Warm, quiet,
safe — everyone in the picture is resting.

## Why this idea, for a judge that has to pick the happier image

The judge is an AI that only sees pixels, and it is asked which of two images is
happier. Cuteness and polish are unreliable signals — many entries will be bright
and busy. What an image like this does instead is present clear, readable
evidence of happiness: a relaxed body, closed eyes, a smile-shaped face, and
three different creatures trusting each other enough to sleep in the same small
space. The tea and the sunbeam say comfort; the cookie and the mouse say nobody
is hungry or afraid. The emotion is legible in one glance, before any detail is
studied, and the warm palette of a late-afternoon sun keeps the whole frame
gentle rather than loud. Fill the frame with one calm feeling and the judge does
not have to guess.

## How the file is copied

`main.py` does no drawing at all. The artwork already exists as `entry.png`
beside the script, and the program only moves those bytes:

1. It builds the source path from `__file__`, so `entry.png` is found next to
   `main.py` no matter which working directory the contest starts it in.
2. It picks the destination directory from `MAKEFUN_OUTPUT_DIR`, falling back to
   `/output` when that variable is not set, and creates the directory only when
   it is not already there.
3. One `open(..., "rb").read()` and one `open(..., "wb").write()` move the data.
   The bytes are never decoded, resized, re-encoded or inspected, so the output
   is identical to the repository copy — same length, same MD5 — on every run.
4. If the image file is missing beside the script, it prints a clear line on
   stderr and exits with code 2 instead of writing a broken image.

Standard library only (`os`, `sys`), no network, no randomness, no clock: the
same bytes every time the contest runs it.
