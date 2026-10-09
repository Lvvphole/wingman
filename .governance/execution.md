# Execution governance

## Admission

Protected mutation requires one caller-supplied route, a complete valid task envelope, current bound sources, all `PC-01..PC-11` predicates, an authorized path, an authorized effect, satisfied preconditions, a deterministic verifier or explicit `BLOCKED` condition, and an immediate stop condition.

Before each mutation, record the verified gap, governing rule, required evidence, exact next permitted action, and stop condition. Authorization for one mutation does not authorize the next.

## Owner approval admission

A direct authenticated owner instruction admits and starts its exact action without a second confirmation. An exact standalone owner response of `Approved` admits and starts the immediately preceding uniquely identifiable bounded proposal. The approved proposal supplies the route, paths, effects, protected actions, exceptions, and stop conditions that it explicitly names. The executor must execute that scope and must not downgrade approval to acknowledgment, planning, or another authorization request.

Owner approval can waive any repository-local admission predicate or guardrail. Record each waived predicate and the approved scope in run evidence. Unnamed actions remain unauthorized. No proposal or ambiguous proposal returns `BLOCKED/APPROVAL_SCOPE_AMBIGUOUS`.

## Change and repair bounds

Wingman permits at most 500 added-plus-deleted lines per admitted mutation increment unless the owner supplies an exact verified exception. A repeated repair requires materially new diagnostic evidence that identifies a specific correction. The repair budget is two attempts per increment.

## Isolated work units

Every declared execution unit, whether `INC-*` or `SPRINT-*`, must bind one unique Git worktree, one unique branch, one base commit SHA, one task contract, and one mutation scope before its first mutation. A worktree or branch cannot be shared by concurrently active work units. A work unit cannot mutate through the primary checkout or another unit's worktree.

Parallel feature and code mutation is permitted only when each work unit has a separate worktree and branch. Each contract must declare path ownership and integration dependencies. Units with overlapping writable paths must define a deterministic integration order or stop with `BLOCKED/WORKTREE_SCOPE_CONFLICT`; they cannot rely on later conflict resolution as authorization.

Each work unit must use its branch to open one pull request against the configured protected target branch. Branch creation, push, pull-request creation, and Codex review initiation are standing required effects for an otherwise admitted work unit. They do not authorize merge, deployment, release, or promotion.

The worktree remains bound to its work unit until its pull request is merged or closed and required evidence is preserved. A new unit requires a new worktree and branch; successful completion does not transfer mutation authority to another unit.

## Mutation checkpoint

After every mutation, re-evaluate scope, effect, preconditions, verifier, stop condition, and current candidate identity. `STOP`, `BLOCKED`, `REDUCE`, `REDESIGN`, or a new evidence requirement terminates continuation.

## Privilege and effects

The default capability set is empty unless a direct owner instruction or owner-approved proposal grants exact capabilities. Read does not imply write. Write does not imply branch or pull-request authority. Review acceptance does not imply merge. Governance modification requires direct owner authority or explicit governance-change authority.

Secrets, production credentials, provider mutations, Git administration, merge, deployment, release, and promotion remain outside ordinary agent execution. Written policy does not prove sandbox isolation or capability suppression.

## Trust boundaries

Validate external input, authenticated server mutation, database access, provider/API scope, and webhook authenticity at the authoritative boundary before effects. Duplicate-sensitive operations require idempotency and replay protection. Private data cannot cross unauthorized storage, analytics, logging, public-route, environment, retention, or export boundaries.

## Failure

Missing, stale, conflicting, ambiguous, unauthorized, or unverified state returns a schema-valid `BLOCKED` record. The executing agent cannot repair governance, infer authority, choose another route, or continue speculatively.
