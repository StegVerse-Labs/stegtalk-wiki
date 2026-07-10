# StegTalk Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-Labs/stegtalk-wiki`.

## Current Priority

StegTalk-owned runtime documentation is installed, indexed, receipted, and wired for autonomous GitHub Pages publishing.

The public wiki mesh is now self-describing through a canonical four-node endpoint registry, StegTalk cross-wiki health status, and a machine-readable completion/status receipt.

Next priority: expand structural pages into substantive prose and add page-level evidence/provenance notes.

## Source

Source package: `StegVerse-Labs/StegTalk/wiki-staging`

## Public URL

- `https://stegverse-labs.github.io/stegtalk-wiki/`

## Install Complete

- `README.md`
- `pages/message-lifecycle.md`
- `pages/contact-routing.md`
- `pages/local-inbox-and-store.md`
- `pages/public-discovery.md`
- `pages/shell-runtime.md`
- `pages/account-runtime.md`
- `pages/wiki-overlap-map.md`
- `data/page-index.json`
- `data/ecosystem-documentation-endpoints.json`
- `data/cross-wiki-health-status.json`
- `data/wiki-completion-status.json`
- `scripts/check_documentation_mesh.py`
- `receipts/wiki-migration-receipt.json`

## Publishing Automation Complete

- `.github/workflows/pages.yml`
- validates `scripts/check_documentation_mesh.py`
- publishes endpoint registry, cross-wiki health status, completion status, page index, pages, and migration receipt
- writes `_site/.nojekyll`

## Documentation Mesh

Canonical endpoints:

- `https://stegverse-labs.github.io/Site/`
- `https://stegverse-labs.github.io/admissibility-wiki/`
- `https://stegverse-002.github.io/stegguardian-wiki/`
- `https://stegverse-labs.github.io/stegtalk-wiki/`

Machine-readable records:

- `data/ecosystem-documentation-endpoints.json`
- `data/cross-wiki-health-status.json`
- `data/wiki-completion-status.json`

Current cross-wiki health state remains `pending_live_peer_checks` until peer machine-readable records and schema consistency are externally verified.

## Linked Wikis

- `https://stegverse-002.github.io/stegguardian-wiki/`
- `https://stegverse-labs.github.io/admissibility-wiki/`
- `https://stegverse-labs.github.io/Site/`

## Org Boundary Rule

StegTalk wiki remains under `StegVerse-Labs` because it documents product and runtime behavior. Guardian wiki remains under `StegVerse-002` because Guardian documentation belongs to the governed-entity org boundary. The split is deliberate and should be explained wherever linked wiki origins are shown.

## Decision Enum Rule

StegTalk wiki pages must not introduce a new local decision-result enum. Any decision/status values must identify their surface, such as runtime execution, wiki governance, interop failure posture, or downstream Guardian status.

## Boundary

StegTalk remains a non-production local prototype candidate unless a later source artifact explicitly changes that status.

Public page visibility, endpoint registration, cross-wiki health records, and completion percentages do not create production status, receipt-chain standing, admissibility, cross-repo authority, or execution authority.

## Verification

```text
python scripts/check_documentation_mesh.py
```

## Remaining Open Check

```text
StegVerse-Labs/stegtalk-wiki:
  - expand structural pages into substantive prose
  - add page-level evidence/provenance notes
  - verify linked-wiki origin explanations render publicly
  - confirm peer machine-readable records

StegVerse-Labs/admissibility-wiki:
  - install shared documentation endpoint registry and cross-wiki health record
  - continue canonical enum registry work after public decision-record boundary clarification

StegVerse-Labs/Site:
  - install shared documentation endpoint registry and cross-wiki health record after checking SITE_MIRROR_HANDOFF.md

StegVerse-002/stegguardian-wiki:
  - keep org-boundary note and canonical endpoint registry aligned
```

## Build Rule

Before continuing any StegTalk wiki task, check this file first and treat it as the current handoff and task source of truth.

## Archive Posture

This handoff exists so the complete thread can be archived without losing the current repo state or next task source of truth.
