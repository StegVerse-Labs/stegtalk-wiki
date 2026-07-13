#!/usr/bin/env python3
"""Run a bounded command profile in a clean temporary copy of the repository."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def copy_repo(destination: Path, excluded: set[str]) -> None:
    def ignore(_directory: str, names: list[str]) -> set[str]:
        return {name for name in names if name in excluded}

    shutil.copytree(ROOT, destination, dirs_exist_ok=True, ignore=ignore)
    (destination / "reports").mkdir(parents=True, exist_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    profile_path = ROOT / args.profile
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    timeout = int(profile.get("timeout_seconds", 180))
    excluded = set(profile.get("exclude", []))
    results: list[dict] = []
    sandbox_status = "PASS"

    with tempfile.TemporaryDirectory(prefix="stegtalk-st017-") as temporary:
        sandbox = Path(temporary) / "repo"
        copy_repo(sandbox, excluded)

        for command in profile.get("commands", []):
            started = time.monotonic()
            timed_out = False
            try:
                completed = subprocess.run(
                    command["argv"],
                    cwd=sandbox,
                    text=True,
                    capture_output=True,
                    timeout=timeout,
                    check=False,
                )
                actual_exit = completed.returncode
                stdout = completed.stdout[-6000:]
                stderr = completed.stderr[-6000:]
            except subprocess.TimeoutExpired as exc:
                timed_out = True
                actual_exit = None
                stdout = (exc.stdout or "")[-6000:] if isinstance(exc.stdout, str) else ""
                stderr = (exc.stderr or "")[-6000:] if isinstance(exc.stderr, str) else ""

            passed = not timed_out and actual_exit == command.get("expected_exit", 0)
            results.append({
                "id": command["id"],
                "argv": command["argv"],
                "expected_exit": command.get("expected_exit", 0),
                "actual_exit": actual_exit,
                "duration_seconds": round(time.monotonic() - started, 3),
                "timed_out": timed_out,
                "status": "PASS" if passed else "FAIL",
                "stdout_tail": stdout,
                "stderr_tail": stderr,
            })
            if not passed:
                sandbox_status = "FAIL"
                break

    report = {
        "schema_version": "1.0.0",
        "record_type": "sandbox_validation_report",
        "repository": profile.get("repository"),
        "profile_id": profile.get("profile_id"),
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "sandbox_status": sandbox_status,
        "github_actions_status": "NOT_OBSERVED",
        "public_output_status": "NOT_VERIFIED",
        "results": results,
        "non_claims": {
            "remote_ci_success": False,
            "deployment_authority": False,
            "production_status": False,
            "public_output_verified": False,
            "cross_repo_authority": False
        }
    }
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"SANDBOX: {sandbox_status}")
    return 0 if sandbox_status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
