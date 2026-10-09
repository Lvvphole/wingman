# Canonical task-domain router

`CONTEXT.md` routes caller-supplied task domains to exact contracts and sources. It does not grant authority.

## Routing rules

1. Accept `task_domains` only from the caller or an authorized external controller. A task domain stated exactly in a uniquely identifiable proposal becomes caller supplied when the authenticated owner responds with the exact standalone approval token `Approved`.
2. Match the supplied selector against the registered routes below.
3. Require exactly one match.
4. Load only the matched route's declared contract and source sections.
5. Return `BLOCKED/ROUTE_ZERO_MATCH` for zero matches.
6. Return `BLOCKED/ROUTE_MULTI_MATCH` for multiple matches.
7. Do not infer, combine, decompose, or substitute a domain.
8. Do not request the task domain again after owner approval admits a proposal that states it exactly.

Reusing the exact selector from an owner-approved proposal is not agent inference. If the approval cannot bind to exactly one bounded proposal, return `BLOCKED/APPROVAL_SCOPE_AMBIGUOUS`.

## Registered routes

| Task domain | Exact contract | Required source registry |
| --- | --- | --- |
| `GOVERNANCE_BOOTSTRAP` | `.harness/contracts/governance-bootstrap.md` | `.governance/source-registry.md` |

No other route is registered.

## Envelope

Admission requires exactly these fields: `task_domains`, `source_sections`, `workpiece_paths`, `selected_evidence_ids`, `authorized_candidate_paths`, `approvals`, and `source_binding`.

## Code-capable tasks

A route that can mutate code, tests, schemas, migrations, build logic, harness logic, or governance must bind the canonical Engineering Rules and pass the complete Pre-Code Readiness Gate before mutation.
