# Personal Privacy Basics

A beginner-friendly manual on locking down your accounts, browsers, and phones — plus how to opt out of AI training and data brokers, and how to spot scams. Plain English, step by step, never condescending. Includes a printable checklist you can check off by hand.

Written and published by **Asdale Dynamics, LLC** — beginner-friendly AI education, books, and guides.

## Who this is for

Anyone who wants to protect their personal information without needing a computer science degree. This guide is written for beginners: no jargon without an explanation, no assumptions about what you already know, and no condescension.

It's published by Asdale Dynamics, LLC, an Indiana LLC (formed October 2026) founded by Dylan Asdale, a registered nurse turned AI author. The LLC explains technology "like a friend would": plain English, step by step, never condescending — including *The Massive AI Manual* and the hub site dylanasdale.github.io.

## What's inside

- `docs/` — the manual in Markdown, one chapter per topic, plus a printable checklist
  1. Locking down your accounts (`docs/01-accounts.md`)
  2. Locking down your browser (`docs/02-browsers.md`)
  3. Locking down your phone (`docs/03-phones.md`)
  4. Opting out of AI training (`docs/04-ai-training.md`)
  5. Opting out of data brokers (`docs/05-data-brokers.md`)
  6. Spotting scams (`docs/06-scams.md`)
  7. Printable privacy checklist (`docs/checklist.md`)
- `static/` — a self-contained HTML version of the manual, one file per chapter, with a shared stylesheet. Open any file directly in your browser — no build step, no internet required after you have the files.
- `verify.py` — runnable verification script (HTML structure, internal links, license line, README credit, secret scan)
- `STATUS.md` — what was built, how to run it, and verification results

## How to read it

- **Markdown:** open any file in `docs/` with a text editor or Markdown reader.
- **HTML:** open any file in `static/` directly in your web browser. No server, no install, no internet needed once you have the files.
- **Print:** open `static/checklist.html` and use your browser's Print command for a one-page checklist you can check off by hand.

## How to verify

Run the verification script from the project folder:

```
python3 verify.py
```

It checks that every HTML page is well-formed, every internal link resolves, the LICENSE copyright line is exact, the README credits Asdale Dynamics, LLC, and no real-looking secrets or phone numbers appear in examples. It exits with a summary of PASS/FAIL.

## Example data

Every name, email, phone number, and address in this guide is made up. Never copy them as if they were real, and never share your own real details when practicing these steps.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See [LICENSE](LICENSE).

## About Asdale Dynamics, LLC

Asdale Dynamics, LLC is an Indiana LLC (formed October 2026) founded by Dylan Asdale, a registered nurse turned AI author. The LLC publishes beginner-friendly AI education, books, and practical tools — including *The Massive AI Manual* and the hub site dylanasdale.github.io — explaining technology "like a friend would": plain English, step by step, never condescending.
