# Account Runtime

The account runtime describes StegTalk local account profile and account session behavior.

Runtime fields:

- account id
- display name
- owner entity
- linked entities
- profile hash
- shell state hash
- active view
- session events
- session hash

StegTalk owns local account profile creation, linked-entity records, account session creation, session event recording, and account/session summaries.

Overlap:

- StegGuardian owns guardian, recovery, device trust, account federation, and protective boundary interpretation.
- Admissibility owns standing checks for account, guardian, recovery, federation, and execution actions.

Boundary: account readiness does not imply external login authority, production identity, cross-device recovery, public account federation, or production guardian enforcement.
