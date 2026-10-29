# STATUS — Personal Privacy Basics guide

## What was built

A beginner manual on personal privacy, published by Asdale Dynamics, LLC:

- `docs/` — Markdown manual, one chapter per topic:
  - `01-accounts.md` — locking down accounts (password manager, unique passwords, 2FA, email lock-down, connected apps, social media privacy, breach checks, security questions)
  - `02-browsers.md` — locking down browsers (privacy-friendly browser, tracking protection, uBlock Origin, private browsing, cookies/history, browser sync, link checking, updates)
  - `03-phones.md` — locking down phones (screen lock, find-my-phone, app permissions, updates, public Wi-Fi/VPN, location and ad tracking, SIM PIN, remote erase)
  - `04-ai-training.md` — opting out of AI training (ChatGPT, Claude, Gemini, Copilot, Meta AI, other tools, local AI)
  - `05-data-brokers.md` — opting out of data brokers (search, list, opt-out per site, state rights, paid services, re-checking, reducing future collection)
  - `06-scams.md` — spotting scams (phishing/smishing/vishing/tech support/romance/too-good-to-be-true, red flags, link checking, what to do, recovery steps)
  - `checklist.md` — printable one-page checklist with sign/date line
- `static/` — self-contained HTML version of the manual (one file per chapter + overview), shared `style.css`, print styles for the checklist. No build step; open any `.html` file directly in a browser.
- `README.md` — project overview, chapter index, credits Asdale Dynamics, LLC
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `.gitignore` — OS, editor, build, and log ignores
- `STATUS.md` — this file

All examples use made-up personal information (example.com domains, fictional phone numbers/addresses). No real personal data, secrets, or API keys anywhere.

## How to run it

- Markdown: open any `docs/*.md` file in a text editor or Markdown reader.
- HTML: open any `static/*.html` file directly in a web browser. No server, no install, no internet needed after the files are on disk.
- Print: open `static/checklist.html` and use your browser's Print command for a checkable paper checklist.

## Verification results

- Python HTML-parser check on all 8 static HTML files: valid structure, no unclosed tags, all internal hrefs resolve to existing files — PASS
- `LICENSE` contains exact line `Copyright (c) 2026 Asdale Dynamics, LLC` — PASS
- `README.md` credits Asdale Dynamics, LLC — PASS
- Naive secret scan (OpenAI-style keys, AWS keys, phone-number patterns) across all `.html` and `.md` files: clean — PASS
- Git: initialized locally, one commit `4632275`, identity Dylan Asdale <dylanasdale@users.noreply.github.com>, plain commit message, no Co-authored-by trailers — PASS
- Not pushed, no remote created, no `.github/workflows` files added — PASS

## Known gaps

- No automated test suite or CI (by design: static docs site; no `.github/workflows` per instructions).
- HTML validation was a custom parser check plus link resolution, not a full DTD/schema validation.
- Chapter content names specific AI tools and settings menus; UI locations may change over time and should be re-checked periodically.
- Data-broker opt-out coverage is U.S.-centric (CCPA/CPA/VCDPA mentioned); non-U.S. readers may have different rights.
- SIM PIN section warns about PUK codes; feature is optional and marked as such.
