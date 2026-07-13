#!/usr/bin/env python3
"""Validate StegTalk's ST-017 adoption and optionally execute its sandbox."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "templates/sandbox-first/stegtalk-wiki.sandbox-profile.json"
RUNNER = ROOT / "tools/run_sandbox_validation.py"
REPORT = ROOT / "reports/sandbox-first-validation.report.json"
WORKFLOW = ROOT / ".github/workflows/pages.yml"
HANDOFF = ROOT / "STEGTALK_WIKI_MIRROR_HANDOFF.md"
CHECKER = ROOT / "tools/check_pages_contract.py"


def errors() -> list[str]:
    problems: list[str] = []
    for path in (PROFILE, RUNNER, WORKFLOW, HANDOFF, CHECKER):
        if not path.exists():
            problems.append("missing:" + str(path.relative_to(ROOT)))
    if problems:
        return problems
    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    if profile.get("repository") != "StegVerse-Labs/stegtalk-wiki":
        problems.append("profile_repository_mismatch")
    ids = [item.get("id") for item in profile.get("commands", [])]
    for required in {"compile-python", "validate-documentation-mesh", "validate-pages-contract", "validate-st017-adoption"}:
        if required not in ids:
            problems.append("missing_command:" + required)
    workflow = WORKFLOW.read_text(encoding="utf-8")
    for marker in ["pull_request:", "actions/upload-artifact@v4", "reports/sandbox-first-validation.report.json"]:
        if marker not in workflow:
            problems.append("workflow_missing:" + marker)
    handoff = HANDOFF.read_text(encoding="utf-8")
    for marker in ["ST-017 Sandbox-First Validation", "SANDBOX: PASS | FAIL | NOT_RUN", "GITHUB_ACTIONS: PASS | FAIL | NOT_OBSERVED"]:
        if marker not in handoff:
            problems.append("handoff_missing:" + marker)
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--structural-only", action="store_true")
    args = parser.parse_args()
    problems = errors()
    if problems:
        print("ST-017 ADOPTION: FAIL - " + ", ".join(problems))
        return 1
    if args.structural_only:
        print("ST-017 ADOPTION: PASS (STRUCTURAL_ONLY)")
        return 0
    result = subprocess.run([
        sys.executable,
        str(RUNNER.relative_to(ROOT)),
        str(PROFILE.relative_to(ROOT)),
        "--output",
        str(REPORT.relative_to(ROOT)),
    ], cwd=ROOT, check=False)
    if result.returncode != 0:
        return result.returncode
    report = json.loads(REPORT.read_text(encoding="utf-8"))
    if report.get("sandbox_status") != "PASS":
        return 1
    print("ST-017 ADOPTION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
