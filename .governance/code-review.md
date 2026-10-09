# Independent code review

## Adoption boundary

`CR-01..CR-14` remain subject to repository adoption, except the authenticated owner's current requirements in `CR-06` and `CR-13`, which govern review repair immediately. Google sources guide the response format but do not override repository authority.

## Required review

Codex is the required independent reviewer for each `INC-*` or `SPRINT-*`. Initiate Codex review only after the exact pull-request head has a green `PR Verification` status. The reviewer evaluates the entire applicable authored change and relevant context. The implementing agent cannot review or accept its own candidate. A substantive implementation, verifier, or governance-semantics change invalidates prior review and requires a new exact-head CI PASS before Codex re-review.

The proposed maximum is three cycles. It is not enforced until the destination owner approves it. Each later cycle requires evidence-backed repair and refreshed exact-head CI. A review-repair patch must not increase total code lines: `post_patch_code_lines - pre_patch_code_lines <= 0`. A fourth cycle requires new explicit owner authorization. Renaming a cycle, changing reviewers, or regenerating a report does not reset the limit.

For every finding, reply in its thread with the disposition, exact fix or authority evidence, verification result, and candidate SHA; then resolve that thread. An unaddressed, uncommented, or unresolved actionable thread blocks review acceptance. A pure base-branch refresh requires fresh exact-head CI; review carries forward only when the effective reviewed diff is proven unchanged.

## Finding classes

| Classification | Effect |
| --- | --- |
| Material defect | Blocks review acceptance |
| Governing-rule violation | Blocks review acceptance |
| Security or privacy issue | Blocks review acceptance |
| Missing required verification | Blocks review acceptance |
| Required adopted-style violation | Correct or obtain an authorized exception |
| Optional improvement or Nit | Advisory; does not independently block |
| Unsupported or inaccurate finding | Correct or withdraw using evidence |

Technical facts and evidence take precedence over preference. Reviewers do not demand unrelated perfection when the candidate satisfies governance and improves overall code health.

## Mechanical and judgment separation

Mechanical: description fields, formatter/linter, change size, test execution, assigned files, exact candidate identity, and attestation currentness.

Independent judgment: architecture, assertion quality, justified complexity, conceptual cohesion, user and edge-case correctness, code-health improvement, and whether a finding is actionable. Agent assertion cannot satisfy a judgment requirement.

Review acceptance has no merge effect.
