# StegTalk Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-Labs/stegtalk-wiki`.

## Current Priority

StegTalk-owned runtime documentation is installed, indexed, receipted, and wired for autonomous GitHub Pages publishing.

Current integration goal remains ST-017 Sandbox-First Validation plus shared cross-wiki health verification. A new non-authorizing documentation projection is also installed for the StegVerse system AI entity lifecycle.

## System AI Entity Projection — 2026-08-29

Installed:

`docs/system-ai-entity.md`

StegTalk Wiki is now an explicit post-activation projection target for `StegVerse-002` alongside Site, Publisher, admissibility-wiki, and stegguardian-wiki.

Canonical source authority remains outside this wiki:

```text
StegVerse-Labs/.github/control/system-ai-entity-registry.json
StegVerse-Labs/.github/control/system-ai-goal-registry.json
StegVerse-Labs/.github/docs/SYSTEM_AI_ENTITY_MIRROR_HANDOFF.md
StegVerse-002/micro-node-runtime/docs/SYSTEM_AI_ENTITY_MIRROR_HANDOFF.md
```

Current entity state remains `FEDERATION_REGISTERED`; this wiki must not claim `SYSTEM_AI_ACTIVE` until canonical activation evidence exists. Wiki publication has authority effect NONE.

First assigned entity goal:

```text
STEGVERSE-002-FIRST-GOAL-001
Achieve governed system-AI activation
```

The entity may produce evidence toward the goal but may not self-certify completion.

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

A red sandbox requires immediate repair and rerun. It is not an awaiting-workflow state.

## Shared Cross-Wiki Health Contract

Installed:

```text
data/cross-wiki-health-status.schema.json
data/cross-wiki-health-status.json
scripts/check_documentation_mesh.py
.github/workflows/pages.yml
```

StegTalk and StegGuardian use the same schema identifier and common field contract. `cross_wiki_schema_consistency_confirmed` remains false until successful public evidence confirms both published schema and record URLs.

## Public URL

`https://stegverse-labs.github.io/stegtalk-wiki/`

## Boundary

StegTalk remains a non-production documentation/prototype surface unless a later governed source artifact changes that status. Sandbox success, workflow success, public visibility, system-AI documentation, and completion percentages do not create production status, receipt-chain standing, admissibility, cross-repo authority, Guardian authority, deployment authority, or execution authority.

## Remaining Work

- complete ST-017 validation and public-output verification;
- after authentic `SYSTEM_AI_ACTIVE`, verify the StegVerse-002 system-AI projection against canonical receipts;
- continue substantive documentation expansion.

## Archive Posture

This handoff contains the current ST-017 adoption, system-AI projection, documentation mesh, shared health schema, workflow boundary, evidence posture, and continuation state. Earlier conversation context is not required.
