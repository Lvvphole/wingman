# GOVERNANCE_BOOTSTRAP task contract

Status: authorized for the exact approved plan only.

The authenticated owner's direct instruction dated 2026-10-08, bound by SHA-256 `965d5788362bea1a6d75eb3200db3adcc74938f992d374719e4cf4cb84f0bfc5`, additionally authorizes the bounded owner-authority correction to `AGENTS.md`, `CONTEXT.md`, `.governance/authority.md`, `.governance/execution.md`, this contract, `.harness/runs/`, and `scripts/verify-governance.py`. This current owner instruction overrides the historical plan-only limitation for that correction only.

The authenticated owner's direct instruction dated 2026-10-08, bound by SHA-256 `4fcf6ea70c2648f2f3135b3a50ff81308e24577ef079a4d7272eeeb2de1392f5`, authorizes the compact root map and isolated worktree-to-PR-to-`PR Verification`-to-Codex-review lifecycle in the paths named by construction contract SHA-256 `cac494471e3f337b03783faa19d9705f88e7e6f132b28fa01a99cebe17c4f0fd`.

The authenticated owner's defect report dated 2026-10-08, bound by SHA-256 `c70cfe82f00890c75cfe0ebf618375c887bbe5f0071a667e2ef8599bdf71ed54`, authorizes the bounded compact-root repair in construction contract SHA-256 `d544685b07a49901f7c1fb321e8621f1ef897a1182f07f9c8293d48762371249`.

## Task envelope

```json
{
  "task_domains": ["GOVERNANCE_BOOTSTRAP"],
  "source_sections": [
    "plan-v0.2/Frozen contract",
    "plan-v0.2/Contracts and invariants",
    "plan-v0.2/Canonical invariant inventory",
    "plan-v0.2/Destination configuration contracts",
    "plan-v0.2/Review classifications and judgment boundary",
    "plan-v0.2/Negative controls and portable states",
    "plan-v0.2/Adoption record",
    "design-authority-v0.3/root",
    "prd-v0.2/sections-35-38",
    "engineering-rules/rule-statements"
  ],
  "workpiece_paths": ["README.md", "plans/wingman-governance-router-plan-v0.2.md"],
  "selected_evidence_ids": ["SCOUT-C92E695", "BASELINE-GOV-EVAL-43-FAIL"],
  "authorized_candidate_paths": [".harness/", ".governance/", "AGENTS.md", "CLAUDE.md", "CONTEXT.md", "scripts/verify-governance.py"],
  "approvals": ["USER_DOMAIN_GOVERNANCE_BOOTSTRAP", "USER_LOC_CEILING_500", "USER_APPROVED_PLAN_EB45E338"],
  "source_binding": {
    "commit": "c92e695344f00fb30698cd494be4b8abf907e6ee",
    "staged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "unstaged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "untracked_manifest_sha256": "015ccfdbfa30f551bbae21214e98f85781ca220517569d38739383a2c1be423e",
    "dirty_submodule_manifest_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "excluded_plan_path": "plans/wingman-governance-router-plan-v0.2.md"
  }
}
```

## Scope

Only the envelope candidate paths and the exact effects in the approved seven-increment plan are authorized. Commit, branch, push, pull request, merge, deployment, release, promotion, provider mutation, credential use, and private-beta admission are forbidden.

## Success

All seven increments close within 500 changed lines each. The final deterministic verifier passes twice on one unchanged candidate. Producer evidence does not adopt or accept the candidate.

## Stop

Stop on any identity mismatch, route ambiguity, source failure, envelope failure, Pre-Code failure, scope/effect violation, missing oracle, missing stop condition, exhausted repair budget, external protected action, or candidate mutation between final runs.
