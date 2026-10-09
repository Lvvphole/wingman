PLAN_READY

# Plan: Wingman ICM governance bootstrap v0.1

## Frozen contract

Goal: Establish the first repository control plane for Wingman so coding agents use one canonical `AGENTS.md`, Claude Code reads it through a pointer-only `CLAUDE.md`, `CONTEXT.md` routes each task to one exact contract, ICM stage context is explicit, and application-code mutation remains fail-closed until all eleven Pre-Code Readiness Gate invariants pass.

Definition of Done:

1. The repository contains the governance tree required by governance-skill v2.2.
2. `CLAUDE.md` contains exactly `@AGENTS.md` plus an optional final newline.
3. `AGENTS.md` has the frozen six-section order and remains a compact repository map.
4. `CONTEXT.md` contains the frozen Code-Capable Tasks entry and maps every route to one existing task contract.
5. The sealed design root, PRD identity, and candidate-readiness identity are bound in `.governance/authority.md`.
6. Unresolved toolchain and Engineering Rules binding values remain explicit and make code-capable work `BLOCKED`.
7. Testing, verification, evidence, completion, and promotion authority remain separate.
8. Seven numbered ICM lifecycle stages define input, process, output, and review boundaries without granting authority.
9. The governance-tree evaluator returns exit 0 twice against one unchanged final candidate.
10. `.harness/pre-code-readiness.md` defines `G_PC_01` through `G_PC_11` as mandatory predicates. A missing, false, unresolved, stale, or unverifiable predicate returns `BLOCKED`.

Pre-Code Readiness Gate invariants:

| Gate | Required invariant |
| --- | --- |
| `G_PC_01` | Current `AGENTS.md` read |
| `G_PC_02` | Current `CONTEXT.md` read |
| `G_PC_03` | Exactly one route selected |
| `G_PC_04` | Canonical Engineering Rules read |
| `G_PC_05` | Required routed sources read |
| `G_PC_06` | Observable defect or gap verified |
| `G_PC_07` | Exact authorized scope established |
| `G_PC_08` | Deterministic verifier or `BLOCKED` condition defined |
| `G_PC_09` | Stop condition defined |
| `G_PC_10` | No unresolved authority conflict |
| `G_PC_11` | 500-LOC change-size rule satisfied for the active increment |

Scout-selected path: Create the governed ICM bootstrap at the repository root before application code.

Authorized scope: Root agent instruction and routing files; `.governance/`; `.harness/`; the executable Pre-Code Readiness Gate contract; numbered ICM stage context; the bootstrap task list.

Non-goals: Application code, schemas, migrations, dependencies, runtime selection, package-manager selection, deployment, candidate parameter selection, private-beta admission, commit, push, pull request, merge, or release.

## Planning mode and repository evidence

Mode: GREENFIELD

Source revision: `c92e695344f00fb30698cd494be4b8abf907e6ee`

Relevant evidence:

- `README.md:1` contains only `# wingman`.
- `git ls-files` returns only `README.md`.
- `git status --short --branch` reports clean `main` tracking `origin/main`.
- The baseline governance evaluator returns exit 1 with 43 failed assertions and 5 passing assertions.
- No package manifest, CI workflow, agent instruction, task router, governance file, contract, test command, or build command exists.

Corrected Scout beliefs: None.

## Authority and protected actions

Governing sources:

- Human approval in this session on 2026-10-08.
- Design Authority Record v0.3, authority root `b4a1a02fc333b7c212186d7b07fb9d2b5536afaf2ae7434c20371ce097c3d10f`.
- Wingman / Black Book PRD v0.2, SHA-256 `a0283859f2b128c9ef0adcb25922901e135e0aeed64ba42900d8b83701f48be1`.
- Candidate-Readiness Register v0.1, SHA-256 `b2a97363962c7745e45e46c7e519b403d347a61f0cb55a6ed65aeba4cf9656b8`.
- Governance skill v2.2 and its frozen file contracts.
- ICM five-layer context hierarchy and stage-contract model.

Protected actions:

- Create or modify the declared local governance files -> AUTHORIZED.
  - owner: user
  - gate boundary: exact files declared by one active increment
  - evidence: user message `Approved`
- Run the read-only governance evaluator -> AUTHORIZED.
  - owner: user
  - gate boundary: repository-local candidate only
  - evidence: approved bootstrap Definition of Done
- Install dependencies -> UNAUTHORIZED.
- Create a branch -> UNAUTHORIZED.
- Commit -> UNAUTHORIZED.
- Push -> UNAUTHORIZED.
- Create or merge a pull request -> UNAUTHORIZED.
- Deploy, migrate, release, or promote -> UNAUTHORIZED.

## Obligations and evaluation

| DoD | Obligation | Behavior | Verification | Acceptance criterion | Oracle | Increment |
| --- | --- | --- | --- | --- | --- | --- |
| D1-D4 | `OBL-001` Root discovery and routing | GAP | GAP | Canonical files exist; pointer and routes are exact | Root predicate check | `INC-1` |
| D5-D7 | `OBL-002` Stable lifecycle ownership | GAP | GAP | Authority, execution, security, testing, verification, evidence, and completion owners are separate and fail closed | Governance predicate checks | `INC-2`, `INC-3` |
| D1, D6 | `OBL-003` Harness gates | GAP | GAP | Evals, inference loop, runtime loop, and run directory exist with bounded stop and provenance semantics | Harness predicate checks | `INC-3`, `INC-4`, `INC-8` |
| D4, D6 | `OBL-004` Exact task contracts | GAP | GAP | Every declared route resolves to one contract with the correct Engineering Rules binding | Route/contract evaluator | `INC-4` through `INC-6` |
| D8 | `OBL-005` ICM lifecycle stages | GAP | GAP | Seven numbered stage contracts define inputs, process, outputs, and review gate without authority grant | Stage predicate checks | `INC-6`, `INC-7` |
| D9 | `OBL-006` Deterministic whole-tree evidence | GAP | GAP | Governance evaluator exits 0 twice on unchanged bytes | Same-state double run | `INC-8` |
| D10 | `OBL-007` Pre-Code Readiness Gate | GAP | GAP | All `G_PC_01` through `G_PC_11` predicates are present, mandatory, and fail closed | Gate-contract predicate check | `INC-4`, `INC-8` |

## Dependency graph

`INC-1 -> INC-2 -> INC-3 -> INC-4 -> INC-5 -> INC-6 -> INC-7 -> INC-8`

Execution order: `INC-1`, `INC-2`, `INC-3`, `INC-4`, `INC-5`, `INC-6`, `INC-7`, `INC-8`.

The first seven increments are bounded structural prerequisites. Each has a deterministic local predicate. `INC-8` closes the end-to-end governance behavior.

## Selected design

Selected: Use the governance skill's semantic ICM adaptation.

- Layer 0: root `AGENTS.md`.
- Claude compatibility: exact pointer-only `CLAUDE.md`.
- Layer 1: root `CONTEXT.md` task router.
- Layer 2: `.harness/contracts/<task>.md` authorization envelopes.
- Pre-code admission: `.harness/pre-code-readiness.md` owns `G_PC_01` through `G_PC_11` and returns only `PASS` or `BLOCKED`.
- Layer 3: `.governance/` stable authority and control references.
- Layer 4: `.harness/runs/` mutable run evidence.
- Lifecycle navigation: seven numbered `.harness/stages/*/CONTEXT.md` files.

Rejected material alternatives:

- Independent policy in `CLAUDE.md`: rejected because it creates a second authority source.
- Full PRD content in `AGENTS.md`: rejected because it creates duplication, drift, and excess context.
- Application scaffold before governance: rejected because no admitted code-capable route or Engineering Rules binding exists.
- Invented toolchain defaults: rejected because the repository and sealed authority do not select them.

Decision basis: This design is the smallest structure that meets the user-approved ICM model and the governance evaluator while preserving fail-closed authority.

## Contracts

Preserved:

- `README.md` remains byte-for-byte unchanged.
- Design Authority Record v0.3 and PRD v0.2 remain higher authority than repository implementation artifacts.
- Candidate status remains `NOT_READY`; private-beta status remains `BLOCKED`.

Changed:

- The repository gains an explicit instruction-discovery, routing, authorization, execution, evidence, and completion control plane.
- Coding-agent tasks gain exact route and stage contracts.

Failure behavior:

- Missing, ambiguous, stale, mismatched, false, or unavailable required authority or evidence returns `BLOCKED`.
- An unresolved Engineering Rules location, identity, or SHA-256 blocks code-capable mutation.
- Any false, missing, unresolved, stale, or unverifiable `G_PC_01` through `G_PC_11` predicate blocks code-capable mutation.
- `G_PC_11` applies to each active implementation increment. An increment with more than 500 added plus deleted lines is `BLOCKED` before mutation.
- A route without exactly one existing contract is invalid.
- Testing cannot establish acceptance.
- The producer cannot self-accept or promote a candidate.

## Task-list handoff

Target: `.harness/tasks.md`

Preservation evidence: The target does not exist at source revision `c92e695344f00fb30698cd494be4b8abf907e6ee`; therefore, no prior task-list content can be overwritten.

Entries Build must record before implementation:

- [ ] `INC-1` Create root discovery, routing, authority binding, and bootstrap task list.
- [ ] `INC-2` Create execution, security, testing, verification, and evidence owners.
- [ ] `INC-3` Create completion, style, review-repair, risk, and eval owners.
- [ ] `INC-4` Create the Pre-Code Readiness Gate, harness loops, and initial contracts.
- [ ] `INC-5` Create governance-change and central code-capable engineering contracts.
- [ ] `INC-6` Create remaining contracts and intake stage.
- [ ] `INC-7` Create scout through verify ICM stages.
- [ ] `INC-8` Create candidate stage and mutable run directory marker, then run final deterministic verification.

## Increments

### INC-1

Objective: Establish canonical repository discovery, routing, authority binding, and the preserved task-list state.

Obligations: `OBL-001`, part of `OBL-002`.

Dependencies: none.

Files:

- `.harness/tasks.md`
- `AGENTS.md`
- `CLAUDE.md`
- `CONTEXT.md`
- `.governance/authority.md`

Actions and postconditions: Create the five files from frozen templates; preserve exact `CLAUDE.md` body; record unresolved toolchain and Engineering Rules identity as fail-closed values; bind the three product-authority identities.

Acceptance criteria: All five files exist; `CLAUDE.md` is exact; `AGENTS.md` has the exact six-section order; route names and contract paths are unique; authority binding contains the sealed root and required pre-code gate.

Verifier and oracle: `python3` read-only predicates over the five declared files; exit 0 only when every acceptance criterion is true.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 30 seconds; increment timeout 300 seconds.

Checkpoint: Root routing and authority files exist; later route targets may remain absent until their declared increments.

Stateful: false.

Protected actions: Local writes to the five declared files only.

Recovery: Not applicable.

Stop condition: Any need to choose a runtime, package manager, candidate value, or Engineering Rules identity.

### INC-2

Objective: Separate lifecycle governance for execution, security, testing, verification, and evidence.

Obligations: part of `OBL-002`.

Dependencies: `INC-1`.

Files: `.governance/execution.md`, `.governance/security.md`, `.governance/testing.md`, `.governance/verification.md`, `.governance/evidence.md`.

Actions and postconditions: Create the five stable policy owners with explicit stop, canonical-path, test/proof separation, exact-candidate, and evidence-class rules.

Acceptance criteria: Each file exists and contains its declared lifecycle predicates; verification invalidates after mutation; evidence cannot self-promote.

Verifier and oracle: `python3` read-only predicate check; exit 0 only when all five owners and predicates exist.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 30 seconds; increment timeout 300 seconds.

Checkpoint: Stable lifecycle policy exists through evidence classification.

Stateful: false.

Protected actions: Local writes to the five declared files only.

Recovery: Not applicable.

Stop condition: Any weakening of authority, verifier independence, or exact-candidate binding.

### INC-3

Objective: Complete stable governance and define deterministic oracle ownership.

Obligations: remainder of `OBL-002`; part of `OBL-003`.

Dependencies: `INC-2`.

Files: `.governance/completion.md`, `.governance/style.md`, `.governance/review-repair-invariants.md`, `.governance/risk-register.md`, `.harness/evals.md`.

Actions and postconditions: Create completion rules, unresolved-style policy, verbatim review-repair invariants, required risk seeds, and named evaluator contract.

Acceptance criteria: Completion states are exact; all INV-1 through INV-8 exist; two-attempt/no-third rule exists; risk register contains all required agent risks; eval contract names command, expected result, failure meaning, and consumers.

Verifier and oracle: `python3` read-only predicate check; exit 0 only when all declared content is present.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 30 seconds; increment timeout 300 seconds.

Checkpoint: Stable governance and oracle policy are structurally complete.

Stateful: false.

Protected actions: Local writes to the five declared files only.

Recovery: Not applicable.

Stop condition: Any shortened, renumbered, or weakened review-repair invariant.

### INC-4

Objective: Establish the eleven-predicate Pre-Code Readiness Gate, inference/runtime gates, and initial read-only/bootstrap contracts.

Obligations: part of `OBL-003` and `OBL-004`; `OBL-007`.

Dependencies: `INC-3`.

Files: `.harness/pre-code-readiness.md`, `.harness/inference-loop.md`, `.harness/runtime-loop.md`, `.harness/contracts/read-only.md`, `.harness/contracts/governance-bootstrap.md`.

Actions and postconditions: Create the fail-closed gate contract, bounded loops, and two task contracts with exact authority, path, action, evidence, and completion fields.

Acceptance criteria: `G_PC_01` through `G_PC_11` exist exactly once and are mandatory; gate result is only `PASS` or `BLOCKED`; the 500-LOC rule applies per active increment; contract admission, canonical scope, proposal-before-execution, result binding, budget, and stop semantics exist; both contracts have the correct Engineering Rules disposition.

Verifier and oracle: `python3` read-only predicate check; exit 0 only when all loop and contract predicates pass.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 30 seconds; increment timeout 300 seconds.

Checkpoint: Pre-code admission, harness loops, and initial exact contracts exist.

Stateful: false.

Protected actions: Local writes to the five declared files only.

Recovery: Not applicable.

Stop condition: A gate predicate is omitted or weakened, the LOC unit is changed without authority, or a contract grants authority merely because routing selected it.

### INC-5

Objective: Establish governance-change and the central code-capable engineering task contracts.

Obligations: part of `OBL-004`.

Dependencies: `INC-4`.

Files: `.harness/contracts/governance-change.md`, `.harness/contracts/mutation.md`, `.harness/contracts/feature-architecture.md`, `.harness/contracts/bug-fix.md`, `.harness/contracts/review-repair.md`.

Actions and postconditions: Create five exact contracts; bind every code-capable contract through `.governance/authority.md` and `.harness/pre-code-readiness.md`; include complete AHE records where required.

Acceptance criteria: All five contracts contain required fields; code-capable contracts require all eleven Pre-Code Readiness Gate predicates; governance-change, bug-fix, and review-repair contain complete AHE records; review-repair binds INV-1 through INV-8.

Verifier and oracle: `python3` read-only predicate check; exit 0 only when all contract predicates pass.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 30 seconds; increment timeout 300 seconds.

Checkpoint: Core engineering work has exact fail-closed task envelopes.

Stateful: false.

Protected actions: Local writes to the five declared files only.

Recovery: Not applicable.

Stop condition: Any code-capable route that bypasses Engineering Rules admission.

### INC-6

Objective: Complete remaining task contracts and establish the intake ICM lifecycle stage.

Obligations: remainder of `OBL-004`; part of `OBL-005`.

Dependencies: `INC-5`.

Files: `.harness/contracts/deterministic-ci-cd.md`, `.harness/contracts/agentic-workflow.md`, `.harness/contracts/release-consumer.md`, `.harness/contracts/complete-failure.md`, `.harness/stages/00-intake/CONTEXT.md`.

Actions and postconditions: Create the final four task contracts and the stage contract for task classification.

Acceptance criteria: The four task contracts satisfy required envelopes and Pre-Code Gate bindings; the intake stage declares exact inputs, process, outputs, review gate, and no authority grant.

Verifier and oracle: `python3` read-only predicate check; exit 0 only when all five declared artifacts satisfy their contracts.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 30 seconds; increment timeout 300 seconds.

Checkpoint: Task routing targets are complete; lifecycle routing reaches intake.

Stateful: false.

Protected actions: Local writes to the five declared files only.

Recovery: Not applicable.

Stop condition: Release-consumer contract grants release, promotion, merge, or deployment authority.

### INC-7

Objective: Establish scout through verify ICM lifecycle stages.

Obligations: remainder of `OBL-005`.

Dependencies: `INC-6`.

Files: `.harness/stages/10-scout/CONTEXT.md`, `.harness/stages/20-plan/CONTEXT.md`, `.harness/stages/30-build/CONTEXT.md`, `.harness/stages/40-test/CONTEXT.md`, `.harness/stages/50-verify/CONTEXT.md`.

Actions and postconditions: Create scout, plan, build, test, and verify stage contracts with explicit handoffs and human review gates.

Acceptance criteria: Each stage contains Inputs, Process, Outputs, Review Gate, and Authority Boundary sections; build requires all eleven Pre-Code Gate predicates; testing does not verify; verification does not promote.

Verifier and oracle: `python3` read-only predicate check; exit 0 only when all five stage contracts satisfy the acceptance criteria.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 30 seconds; increment timeout 300 seconds.

Checkpoint: The lifecycle is inspectable and routed through independent verification.

Stateful: false.

Protected actions: Local writes to the five declared files only.

Recovery: Not applicable.

Stop condition: Any stage claims authority owned by a task contract, verifier, completion authority, or promotion principal.

### INC-8

Objective: Establish candidate packaging and the mutable run-evidence directory, then close deterministic whole-tree verification.

Obligations: remainder of `OBL-003`; `OBL-006`.

Dependencies: `INC-7`.

Files: `.harness/stages/60-candidate/CONTEXT.md`, `.harness/runs/.gitkeep`.

Actions and postconditions: Create the candidate-stage contract and run-directory marker; confirm each increment's added plus deleted lines did not exceed 500; inspect the exact candidate; run the governance-tree evaluator twice without mutation between runs.

Acceptance criteria: Candidate packaging does not release or promote; the mutable run directory exists; `G_PC_01` through `G_PC_11` are present and fail closed; every increment satisfies the per-increment 500-LOC rule; both evaluator runs exit 0 and report zero failed assertions; the candidate identity is unchanged across the two runs.

Verifier and oracle: `bash /root/.codex/skills/remote-skills/skill-6a93bf00369c8191b994ae64fd5e0a7b/scripts/eval-governance-tree.sh /workspace/scratch/99e6ff3f9161/wingman`; oracle is exit 0 with `fail=0`, twice on unchanged state.

Verifier class: `DETERMINISTIC`.

Budgets: two repair attempts; command timeout 60 seconds for each run; increment timeout 300 seconds.

Checkpoint: Governance bootstrap candidate produced with stable deterministic evidence; not independently accepted or promoted.

Stateful: false.

Protected actions: Local writes to the two declared files; read-only LOC and evaluator execution.

Recovery: Not applicable.

Stop condition: The two same-state runs disagree, any assertion fails, or the candidate changes between runs.

## Source binding

Canonical command: `python /root/.codex/skills/remote-skills/skill-6a931d92b4488191aa64c7bd84e5736c/scripts/source-binding.py --repo /workspace/scratch/99e6ff3f9161/wingman --exclude-plan-path plans/wingman-icm-governance-bootstrap-plan-v0.1.md`

Artifact path excluded: `plans/wingman-icm-governance-bootstrap-plan-v0.1.md`

commit: `c92e695344f00fb30698cd494be4b8abf907e6ee`

staged diff SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

unstaged diff SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

untracked manifest SHA-256: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

dirty submodule manifest SHA-256: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`

## Build manifest

```json
{
  "schema": "build-agent/v2",
  "completion_authority": "User (Emory Harris) after independent verification evidence",
  "source_binding": {
    "commit": "c92e695344f00fb30698cd494be4b8abf907e6ee",
    "staged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "unstaged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "untracked_manifest_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "dirty_submodule_manifest_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "excluded_plan_path": "plans/wingman-icm-governance-bootstrap-plan-v0.1.md"
  },
  "task_list": {
    "target": ".harness/tasks.md",
    "preservation_evidence": "Target absent at c92e695344f00fb30698cd494be4b8abf907e6ee; no prior content exists.",
    "entries": [
      {"increment": "INC-1", "text": "Create root discovery, routing, authority binding, and bootstrap task list."},
      {"increment": "INC-2", "text": "Create execution, security, testing, verification, and evidence owners."},
      {"increment": "INC-3", "text": "Create completion, style, review-repair, risk, and eval owners."},
      {"increment": "INC-4", "text": "Create the Pre-Code Readiness Gate, harness loops, and initial contracts."},
      {"increment": "INC-5", "text": "Create governance-change and central code-capable engineering contracts."},
      {"increment": "INC-6", "text": "Create remaining contracts and intake stage."},
      {"increment": "INC-7", "text": "Create scout through verify ICM stages."},
      {"increment": "INC-8", "text": "Create candidate stage and run directory, then run final deterministic verification."}
    ]
  },
  "increments": [
    {
      "id": "INC-1",
      "objective": "Establish canonical repository discovery, routing, authority binding, and task-list state.",
      "obligations": ["OBL-001", "OBL-002"],
      "dependencies": [],
      "files": [".harness/tasks.md", "AGENTS.md", "CLAUDE.md", "CONTEXT.md", ".governance/authority.md"],
      "actions": [{"instruction": "Create the five root/bootstrap artifacts from the frozen contracts.", "postcondition": "Root routing and authority predicates pass."}],
      "acceptance_criteria": ["Exact CLAUDE pointer", "Exact AGENTS section order", "Unique exact routes", "Fail-closed authority binding"],
      "verifier": {"reference": "INC-1 Python file predicates", "oracle": "All INC-1 predicates true and process exits 0", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 30, "increment_timeout_seconds": 300},
      "checkpoint": "Root routing and authority files exist.",
      "stateful": false,
      "protected_actions": [{"action": "local governance file mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    },
    {
      "id": "INC-2",
      "objective": "Separate lifecycle governance for execution, security, testing, verification, and evidence.",
      "obligations": ["OBL-002"],
      "dependencies": ["INC-1"],
      "files": [".governance/execution.md", ".governance/security.md", ".governance/testing.md", ".governance/verification.md", ".governance/evidence.md"],
      "actions": [{"instruction": "Create five stable lifecycle owners.", "postcondition": "Lifecycle ownership predicates pass."}],
      "acceptance_criteria": ["Execution stops are bounded", "Canonical path rules exist", "Testing and verification remain separate", "Evidence classes cannot self-promote"],
      "verifier": {"reference": "INC-2 Python file predicates", "oracle": "All INC-2 predicates true and process exits 0", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 30, "increment_timeout_seconds": 300},
      "checkpoint": "Lifecycle policy exists through evidence classification.",
      "stateful": false,
      "protected_actions": [{"action": "local governance file mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    },
    {
      "id": "INC-3",
      "objective": "Complete stable governance and deterministic oracle ownership.",
      "obligations": ["OBL-002", "OBL-003"],
      "dependencies": ["INC-2"],
      "files": [".governance/completion.md", ".governance/style.md", ".governance/review-repair-invariants.md", ".governance/risk-register.md", ".harness/evals.md"],
      "actions": [{"instruction": "Create completion, style, review, risk, and eval owners.", "postcondition": "Completion, invariant, risk, and oracle predicates pass."}],
      "acceptance_criteria": ["Exact completion states", "INV-1 through INV-8", "Required risk seeds", "Named deterministic evaluator"],
      "verifier": {"reference": "INC-3 Python file predicates", "oracle": "All INC-3 predicates true and process exits 0", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 30, "increment_timeout_seconds": 300},
      "checkpoint": "Stable governance and oracle policy are structurally complete.",
      "stateful": false,
      "protected_actions": [{"action": "local governance file mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    },
    {
      "id": "INC-4",
      "objective": "Establish the eleven-predicate Pre-Code Readiness Gate, inference/runtime gates, and initial task contracts.",
      "obligations": ["OBL-003", "OBL-004", "OBL-007"],
      "dependencies": ["INC-3"],
      "files": [".harness/pre-code-readiness.md", ".harness/inference-loop.md", ".harness/runtime-loop.md", ".harness/contracts/read-only.md", ".harness/contracts/governance-bootstrap.md"],
      "actions": [{"instruction": "Create the fail-closed gate contract, bounded loops, and two exact task contracts.", "postcondition": "All eleven gate, loop, and initial contract predicates pass."}],
      "acceptance_criteria": ["G_PC_01 through G_PC_11 mandatory", "Per-increment 500-LOC rule", "Canonical scope", "Proposal/result binding", "Correct Engineering Rules dispositions"],
      "verifier": {"reference": "INC-4 Python file predicates", "oracle": "All INC-4 predicates true and process exits 0", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 30, "increment_timeout_seconds": 300},
      "checkpoint": "Harness loops and initial exact contracts exist.",
      "stateful": false,
      "protected_actions": [{"action": "local harness file mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    },
    {
      "id": "INC-5",
      "objective": "Establish governance-change and central code-capable engineering contracts.",
      "obligations": ["OBL-004"],
      "dependencies": ["INC-4"],
      "files": [".harness/contracts/governance-change.md", ".harness/contracts/mutation.md", ".harness/contracts/feature-architecture.md", ".harness/contracts/bug-fix.md", ".harness/contracts/review-repair.md"],
      "actions": [{"instruction": "Create five fail-closed governance and engineering task contracts.", "postcondition": "All contracts bind the eleven-predicate gate and applicable AHE records."}],
      "acceptance_criteria": ["All eleven Pre-Code Gate predicates required", "Complete AHE records", "Review invariants bound"],
      "verifier": {"reference": "INC-5 Python file predicates", "oracle": "All INC-5 predicates true and process exits 0", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 30, "increment_timeout_seconds": 300},
      "checkpoint": "Core engineering work has exact task envelopes.",
      "stateful": false,
      "protected_actions": [{"action": "local contract mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    },
    {
      "id": "INC-6",
      "objective": "Complete remaining task contracts and intake stage.",
      "obligations": ["OBL-004", "OBL-005"],
      "dependencies": ["INC-5"],
      "files": [".harness/contracts/deterministic-ci-cd.md", ".harness/contracts/agentic-workflow.md", ".harness/contracts/release-consumer.md", ".harness/contracts/complete-failure.md", ".harness/stages/00-intake/CONTEXT.md"],
      "actions": [{"instruction": "Create final task contracts and intake stage.", "postcondition": "Contract and intake-stage predicates pass."}],
      "acceptance_criteria": ["Task envelopes complete", "Gate bindings correct", "Stage IO and review gate explicit", "No release authority"],
      "verifier": {"reference": "INC-6 Python file predicates", "oracle": "All INC-6 predicates true and process exits 0", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 30, "increment_timeout_seconds": 300},
      "checkpoint": "Task routing targets are complete; lifecycle reaches scout.",
      "stateful": false,
      "protected_actions": [{"action": "local contract and stage mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    },
    {
      "id": "INC-7",
      "objective": "Establish scout through verify ICM lifecycle stages.",
      "obligations": ["OBL-005"],
      "dependencies": ["INC-6"],
      "files": [".harness/stages/10-scout/CONTEXT.md", ".harness/stages/20-plan/CONTEXT.md", ".harness/stages/30-build/CONTEXT.md", ".harness/stages/40-test/CONTEXT.md", ".harness/stages/50-verify/CONTEXT.md"],
      "actions": [{"instruction": "Create scout through verify lifecycle stage contracts.", "postcondition": "All stage boundary and gate predicates pass."}],
      "acceptance_criteria": ["Inputs/process/outputs/review/authority sections", "Build requires G_PC_01 through G_PC_11", "Testing does not verify", "Verification does not promote"],
      "verifier": {"reference": "INC-7 Python file predicates", "oracle": "All INC-7 predicates true and process exits 0", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 30, "increment_timeout_seconds": 300},
      "checkpoint": "Seven-stage ICM lifecycle is inspectable and routed.",
      "stateful": false,
      "protected_actions": [{"action": "local stage mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    },
    {
      "id": "INC-8",
      "objective": "Create candidate packaging and the mutable run directory, then close deterministic whole-tree verification.",
      "obligations": ["OBL-003", "OBL-006", "OBL-007"],
      "dependencies": ["INC-7"],
      "files": [".harness/stages/60-candidate/CONTEXT.md", ".harness/runs/.gitkeep"],
      "actions": [{"instruction": "Create the candidate-stage contract and run-directory marker, confirm the per-increment 500-LOC rule, and execute the evaluator twice without mutation.", "postcondition": "All gate predicates hold and both same-state runs exit 0 with fail=0."}],
      "acceptance_criteria": ["Candidate stage cannot release", "Run directory exists", "G_PC_01 through G_PC_11 fail closed", "Every increment is 500 LOC or fewer", "Two unchanged-state evaluator passes", "Candidate identity unchanged"],
      "verifier": {"reference": "bash /root/.codex/skills/remote-skills/skill-6a93bf00369c8191b994ae64fd5e0a7b/scripts/eval-governance-tree.sh /workspace/scratch/99e6ff3f9161/wingman", "oracle": "Exit 0 and fail=0 twice on unchanged state", "class": "DETERMINISTIC"},
      "budgets": {"repair_attempts": 2, "command_timeout_seconds": 60, "increment_timeout_seconds": 300},
      "checkpoint": "Governance bootstrap candidate produced with deterministic evidence; not accepted or promoted.",
      "stateful": false,
      "protected_actions": [{"action": "local run-directory marker mutation", "state": "AUTHORIZED", "owner": "user", "evidence_ref": "Approved"}],
      "recovery": null
    }
  ],
  "publication": {
    "mode": "NONE"
  }
}
```

## Stop conditions

- The plan identity or source binding does not match.
- Current repository governance conflicts with this plan.
- A required file exceeds the five-file increment boundary.
- A task requires an invented runtime, dependency, command, candidate value, or authority owner.
- The exact review-repair invariants cannot be preserved.
- A contract grants authority from routing alone.
- Code-capable work can bypass the unresolved Engineering Rules binding.
- The evaluator or a targeted increment predicate fails after two repair attempts.
- Repository state changes outside the current increment delta.
- Commit, push, pull request, merge, deployment, migration, release, or promotion is requested without separate explicit authority.

## Completion authority

User (Emory Harris), after independent verification evidence for the exact candidate. Build produces evidence only and cannot self-accept.
