# StegTalk Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-Labs/stegtalk-wiki`.

## Current Priority

StegTalk-owned runtime documentation has been installed, indexed, receipted, and wired for autonomous GitHub Pages publishing.

Next priority: make the public wiki mesh self-explaining before expanding page content.

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
- `receipts/wiki-migration-receipt.json`

## Publishing Automation Complete

- `.github/workflows/pages.yml`

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

Public page visibility does not create production status, receipt-chain standing, or admissibility.

## Remaining Open Check

```text
StegVerse-Labs/stegtalk-wiki:
  - expand structural pages into substantive prose
  - add page-level evidence/provenance notes
  - add a machine-readable completion/status receipt
  - verify linked-wiki origin explanations render publicly

StegVerse-002/stegguardian-wiki:
  - keep org-boundary note aligned with StegTalk and Admissibility wiki references

StegVerse-Labs/admissibility-wiki:
  - continue canonical enum registry work after the public decision-record boundary clarification
```

## Build Rule

Before continuing any StegTalk wiki task, check this file first and treat it as the current handoff and task source of truth.

## Archive Posture

This handoff exists so the complete thread can be archived without losing the current repo state or next task source of truth.
