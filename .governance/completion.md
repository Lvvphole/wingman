# Completion governance

The producer reports observed gates and hands evidence to the named completion authority. It cannot self-accept, adopt the portable contract, declare private-beta readiness, authorize merge, or promote a release.

Engineering completion uses `.governance/states.md`. Product release status remains the sealed Decision-025 field with only `ACCEPTED`, `REJECTED`, or `BLOCKED`. Engineering states cannot populate or redefine product release status.

Missing authority, configuration, evidence, verification, review, branch protection, or privileged-boundary proof returns `BLOCKED`. A false required predicate returns `FAIL` within engineering evaluation and cannot be translated into product acceptance.

A clean producer build record is evidence, not an acceptance verdict. Adoption requires every predicate in `.governance/adoption.md` plus independent verification.

For an `INC-*` or `SPRINT-*`, completion cannot advance beyond produced candidate until the unit has a bound isolated worktree and branch, an open pull request, exact-head `PR Verification` PASS, and a current Codex review disposition. Merge remains a separate owner-authorized transition.
