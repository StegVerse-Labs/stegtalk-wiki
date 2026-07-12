# StegTalk Wiki Mirror Handoff

## Status

This file is the current handoff and task source of truth for `StegVerse-Labs/stegtalk-wiki`.

## Current Priority

StegTalk-owned runtime documentation is installed, indexed, receipted, and wired for autonomous GitHub Pages publishing.

Current integration goal: prove the shared cross-wiki health contract with StegGuardian, then expand structural pages into substantive prose and page-level evidence notes.

## Shared Cross-Wiki Health Contract

Installed:

```text
data/cross-wiki-health-status.schema.json
data/cross-wiki-health-status.json schema_version: 1.0.0
data/cross-wiki-health-status.json schema_ref: data/cross-wiki-health-status.schema.json
scripts/check_documentation_mesh.py schema enforcement
.github/workflows/pages.yml schema publication and public index link
```

The shared schema requires:

```text
schema_version
schema_ref
record_type
repo
observed_at
status
origin_public_url
peer_registry
checks
next_actions
non_claims
```

StegTalk and StegGuardian now use the same schema identifier and common field contract. `cross_wiki_schema_consistency_confirmed` remains false until successful public workflow evidence confirms both published schema and record URLs.

Latest installation commits:

```text
fd18595f90508426949a153b16830034dcdf62bd
43ec4cfb01e412dbf0dcc735e2d6531012236db0
da3b79b4bf378d7ca261df61bf8b9258cec75a94
a6afeadc2e9c7f735a076576077659e83cfd77d0
```

## Session Coordination

No open issue or pull request claims this StegTalk health-schema task.

Site has concurrent active work and must not be modified from this workstream.
Admissibility-wiki has a separately active Goal 5 workstream and must not be modified from this workstream.

## Public URL

```text
https://stegverse-labs.github.io/stegtalk-wiki/
```

## Installed Documentation Mesh

```text
README.md
pages/message-lifecycle.md
pages/contact-routing.md
pages/local-inbox-and-store.md
pages/public-discovery.md
pages/shell-runtime.md
pages/account-runtime.md
pages/wiki-overlap-map.md
data/page-index.json
data/ecosystem-documentation-endpoints.json
data/cross-wiki-health-status.json
data/cross-wiki-health-status.schema.json
data/wiki-completion-status.json
scripts/check_documentation_mesh.py
receipts/wiki-migration-receipt.json
.github/workflows/pages.yml
```

## Canonical Endpoints

```text
https://stegverse-labs.github.io/Site/
https://stegverse-labs.github.io/admissibility-wiki/
https://stegverse-002.github.io/stegguardian-wiki/
https://stegverse-labs.github.io/stegtalk-wiki/
```

## Verification

```text
python scripts/check_documentation_mesh.py
```

## Boundary

StegTalk remains a non-production local prototype candidate unless a later governed source artifact changes that status.

Public visibility, endpoint registration, shared schemas, health records, and completion percentages do not create production status, receipt-chain standing, admissibility, cross-repo authority, Guardian authority, or execution authority.

## Remaining Open Check

```text
confirm StegTalk Pages publishes the shared health schema
confirm StegGuardian Pages publishes the identical shared health schema
inspect public schema and health-record evidence before changing consistency flags
expand structural pages into substantive prose
add page-level evidence and provenance notes
roll the shared schema into Site and admissibility-wiki only through their active handoff owners
promote the reusable schema/checker to repo-standards after multi-repo live proof
```

## Archive Posture

This handoff contains the current documentation mesh, shared health schema, workflow, boundary, coordination, and continuation state. Earlier conversation context is not required.
