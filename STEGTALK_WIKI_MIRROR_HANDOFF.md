# StegTalk Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-Labs/stegtalk-wiki`.

## Current Priority

StegTalk-owned runtime documentation is installed, indexed, receipted, and wired for autonomous GitHub Pages publishing.

Current integration goal: adopt and prove `ST-017 Sandbox-First Validation` without adding another workflow, then continue shared cross-wiki health verification and substantive documentation expansion.

## ST-017 Sandbox-First Validation

Installed on validation branch `validation/st017-sandbox-adoption`:

```text
templates/sandbox-first/stegtalk-wiki.sandbox-profile.json
tools/run_sandbox_validation.py
tools/check_pages_contract.py
tools/validate_st017_adoption.py
reports/sandbox-first-validation.report.json (generated evidence)
.github/workflows/pages.yml validation integration
```

Required sequence:

```text
change installed
-> clean temporary repository copy
-> bounded repository-specific commands
-> reports/sandbox-first-validation.report.json
-> SANDBOX PASS
-> GitHub Actions observation
-> merge
-> main-only Pages deployment
-> public-output verification
```

Required status dimensions:

```text
SANDBOX: PASS | FAIL | NOT_RUN
GITHUB_ACTIONS: PASS | FAIL | NOT_OBSERVED
PUBLIC_OUTPUT: VERIFIED | NOT_VERIFIED | NOT_APPLICABLE
```

A red sandbox requires immediate repair and rerun. It is not an `awaiting workflow` state.

The existing single Pages workflow is preserved. Pull requests execute only the validation job. Deployment remains restricted to pushes on `main` after successful sandbox validation.

## Repository-Specific Sandbox Profile

The canonical profile runs:

```text
python -m compileall scripts tools
python scripts/check_documentation_mesh.py
python tools/check_pages_contract.py
python tools/validate_st017_adoption.py --structural-only
```

The sandbox excludes `.git`, caches, prior reports, and prior `_site` output, then recreates an empty reports directory in isolation.

## Shared Cross-Wiki Health Contract

Installed:

```text
data/cross-wiki-health-status.schema.json
data/cross-wiki-health-status.json schema_version: 1.0.0
data/cross-wiki-health-status.json schema_ref: data/cross-wiki-health-status.schema.json
scripts/check_documentation_mesh.py schema enforcement
.github/workflows/pages.yml schema publication and public index link
```

StegTalk and StegGuardian use the same schema identifier and common field contract. `cross_wiki_schema_consistency_confirmed` remains false until successful public evidence confirms both published schema and record URLs.

## Session Coordination

No open issue or pull request claimed this StegTalk ST-017 work before branch creation.

Site has concurrent active work and must not be modified from this workstream.

Admissibility-wiki has a separately active Goal 5 workstream and must not be modified from this workstream.

## Public URL

```text
https://stegverse-labs.github.io/stegtalk-wiki/
```

## Verification

```text
python tools/validate_st017_adoption.py
python scripts/check_documentation_mesh.py
```

## Current Evidence Posture

Until the validation pull request executes and its artifact is inspected:

```text
SANDBOX: NOT_RUN
GITHUB_ACTIONS: NOT_OBSERVED
PUBLIC_OUTPUT: NOT_VERIFIED
```

Installation alone is not adoption proof.

## Boundary

StegTalk remains a non-production local prototype candidate unless a later governed source artifact changes that status.

Sandbox success, workflow success, public visibility, endpoint registration, shared schemas, health records, and completion percentages do not create production status, receipt-chain standing, admissibility, cross-repo authority, Guardian authority, deployment authority, or execution authority.

## Remaining Work

- open the ST-017 validation pull request;
- execute and inspect the sandbox artifact immediately;
- repair any red command before merge;
- merge only after sandbox and PR workflow PASS;
- observe the main deployment separately;
- verify public schema and health-record output before changing consistency flags;
- expand structural pages into substantive prose and page-level evidence notes.

## Archive Posture

This handoff contains the current ST-017 adoption, documentation mesh, shared health schema, workflow boundary, evidence posture, and continuation state. Earlier conversation context is not required.
