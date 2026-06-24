# Contact Routing

Contact routing resolves a receiver hint into a local contact or entity target before a message envelope is created.

Runtime fields:

- sender entity
- receiver hint
- message body
- contact index
- scope
- route decision
- envelope result
- receipt result

StegTalk owns local routing behavior, contact index interpretation, route decision output, and message-envelope handoff.

Overlap:

- StegGuardian may govern sender, receiver, account, device, or guardian boundary effects.
- Admissibility may govern whether the requested route has current standing.

Boundary: contact routing readiness does not imply external messaging federation, production delivery, or guardian-approved communication.
