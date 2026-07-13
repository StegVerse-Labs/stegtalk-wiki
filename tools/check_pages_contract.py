#!/usr/bin/env python3
"""Validate the StegTalk Pages workflow without external dependencies."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "pages.yml"

REQUIRED = [
    "pull_request:",
    "name: Validate sandbox-first readiness",
    "python tools/run_sandbox_validation.py",
    "reports/sandbox-first-validation.report.json",
    "actions/upload-artifact@v4",
    "if: github.event_name == 'push' && github.ref == 'refs/heads/main'",
    "needs: validate",
    "cp data/cross-wiki-health-status.schema.json _site/data/cross-wiki-health-status.schema.json",
    "actions/deploy-pages@v4",
]


def main() -> int:
    text = WORKFLOW.read_text(encoding="utf-8") if WORKFLOW.exists() else ""
    missing = [marker for marker in REQUIRED if marker not in text]
    if missing:
        print("PAGES CONTRACT: FAIL - " + ", ".join(missing))
        return 1
    if text.count("actions/deploy-pages@v4") != 1:
        print("PAGES CONTRACT: FAIL - deployment action count mismatch")
        return 1
    print("PAGES CONTRACT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
