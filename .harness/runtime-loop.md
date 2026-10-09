# Work-unit runtime loop

This state machine applies to every declared `INC-*` or `SPRINT-*`.

## Identity binding

Before mutation, bind the work-unit ID, task contract, unique worktree path, unique branch, base SHA, authorized paths, effects, verifier, and stop condition. Shared worktree or branch identity returns `BLOCKED/WORKTREE_NOT_ISOLATED`. Overlapping writable paths without a deterministic integration order return `BLOCKED/WORKTREE_SCOPE_CONFLICT`.

## State order

1. `CREATED` — contract admitted; worktree and branch identities reserved.
2. `MUTATING` — mutation occurs only inside the bound worktree on the bound branch.
3. `PR_OPEN` — the branch is pushed and one pull request targets the configured protected branch.
4. `CI_PENDING` — exact status context `PR Verification` runs for the pull-request head SHA.
5. `CI_GREEN` — `PR Verification` reports `PASS` for that exact head.
6. `CODEX_REVIEW` — Codex review is initiated only from `CI_GREEN`.
7. `REVIEW_ACCEPTED` — every finding has an evidence-bound thread response and resolution, no actionable finding remains for the same head, and every review-repair patch has nonpositive net code-line growth.
8. `MERGE_ELIGIBLE` — all technical prerequisites are current; merge still requires separate owner authorization.
9. `CLOSED` — the pull request is merged or closed and evidence is preserved.

No state can skip `PR_OPEN`, `CI_PENDING`, or `CI_GREEN` on the path to `CODEX_REVIEW`. Missing evidence returns `BLOCKED`.

## Mutation after CI or review

Any candidate mutation from `CI_PENDING`, `CI_GREEN`, `CODEX_REVIEW`, `REVIEW_ACCEPTED`, or `MERGE_ELIGIBLE` returns the unit to `MUTATING`. Push the new head, rerun `PR Verification`, and initiate Codex re-review only after the new exact head is green.

## Parallel execution

Independent units may occupy different states concurrently only in separate worktrees and branches. Their accepted proposals and results remain identity-bound. One unit's CI, review, or completion evidence cannot satisfy another unit.
