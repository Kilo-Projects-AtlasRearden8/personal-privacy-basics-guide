#!/usr/bin/env python3
"""Verify the Personal Privacy Basics static site.

Checks:
- every HTML file in static/ is well-formed (no unclosed tags)
- every internal href resolves to an existing file
- LICENSE contains the exact copyright line
- README credits Asdale Dynamics, LLC
- no real-looking secrets (API keys) or phone numbers in examples

Exit code 0 if all checks pass, 1 otherwise.
"""

import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(ROOT, "static")
LICENSE = os.path.join(ROOT, "LICENSE")
README = os.path.join(ROOT, "README.md")

EXPECTED_LICENSE_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"

failures = []
passes = []


def note(name, ok, detail=""):
    if ok:
        passes.append(name)
    else:
        failures.append((name, detail))


class HTMLChecker(html.parser.HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.stack = []
        self.void = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr",
        }
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.void:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void:
            return
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors.append(
                f"unexpected close </{tag}> (open: {self.stack[-5:]})"
            )

    def finish(self):
        for tag in reversed(self.stack):
            self.errors.append(f"unclosed <{tag}>")


def check_html():
    html_files = sorted(f for f in os.listdir(STATIC) if f.endswith(".html"))
    note("html files found", len(html_files) > 0, f"found {len(html_files)}")

    for f in html_files:
        path = os.path.join(STATIC, f)
        checker = HTMLChecker(f)
        with open(path, encoding="utf-8") as fh:
            checker.feed(fh.read())
        checker.finish()

        # internal links
        text = open(path, encoding="utf-8").read()
        links = re.findall(r'href="([^"]+)"', text)
        for link in links:
            if link.startswith(("#", "http://", "https://", "mailto:", "android:", "data:")):
                continue
            target = os.path.join(STATIC, link)
            if not os.path.isfile(target):
                checker.errors.append(f"broken link {link!r}")

        if checker.errors:
            note(f"html valid: {f}", False, "; ".join(checker.errors))
        else:
            note(f"html valid: {f}", True)


def check_license():
    text = open(LICENSE, encoding="utf-8").read()
    note("license exact copyright line", EXPECTED_LICENSE_LINE in text)


def check_readme_credit():
    text = open(README, encoding="utf-8").read()
    note("readme credits Asdale Dynamics, LLC", "Asdale Dynamics, LLC" in text)


def check_no_secrets():
    patterns = {
        "openai-style key": r"sk-[A-Za-z0-9]{20,}",
        "aws key id": r"AKIA[0-9A-Z]{16}",
        "phone number": r"\b\d{3}[-.]\d{3}[-.]\d{4}\b",
    }
    secret_found = False
    for root, _, files in os.walk(ROOT):
        if os.path.join(ROOT, ".git") in root or root == os.path.join(ROOT, ".git"):
            continue
        for fn in files:
            if not fn.endswith((".html", ".md", ".py")):
                continue
            path = os.path.join(root, fn)
            try:
                text = open(path, encoding="utf-8").read()
            except OSError:
                continue
            for name, pat in patterns.items():
                if re.search(pat, text):
                    note(f"no secrets ({name} in {path})", False)
                    secret_found = True
    if not secret_found:
        note("no secrets or phone patterns in docs", True)


def main():
    print("Verifying Personal Privacy Basics static site\n")
    check_html()
    check_license()
    check_readme_credit()
    check_no_secrets()

    print(f"Passed: {len(passes)}")
    for p in passes:
        print(f"  - {p}")
    if failures:
        print(f"\nFailed: {len(failures)}")
        for name, detail in failures:
            print(f"  - {name}: {detail}")
        print("\nVERIFICATION FAILED")
        return 1
    print("\nVERIFICATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
