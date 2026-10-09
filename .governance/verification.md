# Verification governance

## Obligation coverage

Every required obligation has a deterministic verifier or explicit `BLOCKED` condition. Verification covers every applicable changed surface and preserves accepted regression requirements.

## Exact-head CI

Each required check record contains: registered check ID, applicability predicate, expected runner/verifier identity, command or externally enforced operation, candidate commit SHA, completion state, result, and evidence reference.

PASS requires every applicable mandatory check to succeed for the exact final candidate head. A skip is acceptable only under an approved deterministic non-applicability rule. Missing, cancelled, inconclusive, stale, mismatched, or failing checks cannot establish PASS.

For every `INC-*` or `SPRINT-*`, the mandatory pull-request status context is exactly `PR Verification`. It must report `PASS` for the exact pull-request head SHA. A local command, check with another name, result from another head, or successful prior run cannot substitute for this status context. If the repository has no active `PR Verification` check, the unit is `BLOCKED/PR_VERIFICATION_UNAVAILABLE`.

Codex review admission requires the work-unit record, unique worktree and branch binding, pull-request identity, exact pull-request head SHA, `PR Verification` result, and CI evidence reference. Review cannot start while CI is pending, missing, failed, cancelled, inconclusive, or stale.

## Independent review

Required independent review begins only after exact-head CI succeeds. Acceptance requires current review identity, zero unresolved actionable findings, and an approved cycle limit. The producer cannot supply the independent review disposition.

## Currentness

Verification belongs to exact candidate bytes and configuration. Mutation invalidates prior verification. A pure base refresh can preserve review only with proof that the effective implementation diff is unchanged; exact-head CI must still run again.

Any mutation after a green CI result returns the work unit to mutation state. The updated branch must be pushed and `PR Verification` must pass on the new head before Codex review or re-review starts.

## Separation

Producer checks produce evidence only. `VERIFIED`, `REVIEW_ACCEPTED`, and `MERGE_ELIGIBLE` are distinct. None authorizes merge, deployment, release, or promotion.
