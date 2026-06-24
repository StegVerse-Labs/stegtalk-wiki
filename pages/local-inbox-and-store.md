# Local Inbox and Store

The local inbox and store describe how StegTalk projects received envelopes into readable local state and preserves local runtime records.

Runtime fields:

- owner entity
- received envelope
- inbox item
- item hash
- receipt output
- local store or shell state update

StegTalk owns local inbox projection, local item shape, local persistence behavior, and prototype receipt structure.

Overlap:

- Admissibility may evaluate whether an inbox transition should be accepted.
- StegGuardian may evaluate whether account, device, recovery, or guardian boundaries affect local state access.

Boundary: local inbox and store readiness does not imply cloud sync, cross-device persistence, production retention guarantees, or external account recovery.
