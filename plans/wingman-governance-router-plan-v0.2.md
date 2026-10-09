PLAN_READY

# Plan: Wingman portable deterministic engineering governance v0.2

## Frozen contract

Goal: Establish a reusable repository governance baseline that preserves one authority root, one caller-controlled deterministic router, bounded context, no agent-inferred permission, and fail-closed execution.

Definition of Done:

1. `CLAUDE.md` is pointer-only and contains exactly `@AGENTS.md` with an optional final newline.
2. Exactly one root `AGENTS.md` owns repository execution authority and non-negotiable constraints.
3. Root `CONTEXT.md` exclusively owns task-domain routing and the source registry route map.
4. The executing agent cannot select, infer, combine, or decompose `task_domains`.
5. The initial caller-supplied domain is exactly `GOVERNANCE_BOOTSTRAP`.
6. A canonical inventory contains exactly 50 portable invariants: `RT-01` through `RT-15`, `EX-01` through `EX-07`, `VF-01` through `VF-07`, `ZT-01` through `ZT-07`, and `CR-01` through `CR-14`.
7. Every invariant records its source trace, executable predicate, required evidence, negative control, and stop condition.
8. Every task envelope contains exactly the seven required fields: `task_domains`, `source_sections`, `workpiece_paths`, `selected_evidence_ids`, `authorized_candidate_paths`, `approvals`, and `source_binding`.
9. Unique-route, required-input, allowed-input, source-present/current, evidence-nonauthority, bounded-discovery, pre-code-readiness, and mutation gates fail closed.
10. `G_PC_01` through `G_PC_11` are mandatory. Wingman binds `G_PC_11` to at most 500 added-plus-deleted lines per admitted mutation candidate.
11. Standard `BLOCKED` output contains `status`, `reason_code`, `gate_id`, `route_candidates`, `missing_inputs`, `conflicts`, `source_binding`, and `resolution_required`.
12. Skills are optional procedures and confer no route, permission, waiver, or execution authority.
13. Repository routing does not require Scout, Plan, Contract, Build, or another predecessor stage unless a routed governing authority independently requires it.
14. Authorized workpieces and evidence load only after routing and admission pass.
15. After each mutation, the mutation gate and stop condition are evaluated again.
16. Positive and negative controls pass twice on one unchanged final candidate.
17. Destination CI, review, branch-protection, permitted-effect, privileged-boundary, negative-control, state-transition, and adoption configurations are explicit and fail closed.
18. Repository adapters that lack an authorized value remain unresolved and force `BLOCKED`; the bootstrap does not inherit becoming-the-man values.
19. Google review guidance remains non-authoritative until the destination authority adopts its exact bound references.

Scout-selected path: Create the governed ICM-style control plane before application code.

Authorized scope: `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `.governance/`, `.harness/`, the deterministic governance verifier, and the bootstrap task list.

Non-goals: Product-specific task routes; application code; architecture selection; dependencies; schemas; migrations; CI; deployment; release; promotion; commit; push; pull request; merge; private-beta admission; mandatory agent lifecycle; implementation of supervisor-controlled tool admission, disposable sandbox isolation, verifier write protection, cryptographic evidence provenance, or independent evaluation outside the agent environment.

## Planning mode and repository evidence

Mode: GREENFIELD

Source revision: `c92e695344f00fb30698cd494be4b8abf907e6ee`

Evidence:

- `README.md:1` contains only `# wingman`.
- `git ls-files` returns only `README.md`.
- The baseline governance-tree evaluator exits 1 with 43 failures.
- The superseded plan at `plans/wingman-icm-governance-bootstrap-plan-v0.1.md` is untracked and is part of this plan's source binding. It is not governing authority.
- Canonical Engineering Rules source artifact: `/root/.codex/skills/remote-skills/skill-6a7bbe3c89448191900ebcdd6395ac7c/SKILL.md`, SHA-256 `deb95b212e0d3fae948e6cd0b9b932ede58cbaeef0170ccc8257b7a80a117793`.

Corrected prior plan beliefs:

- Agents do not classify their own domains.
- The repository does not mandate a Scout-to-Plan-to-Build lifecycle.
- Skills do not create authority.
- ICM is used for bounded routing and context delivery, not mandatory stages.
- The 500-LOC ceiling is a Wingman-specific caller decision, not a portable default.

## Authority and protected actions

Governing sources:

- User's portable routing invariant specification in this session.
- User's Portable Deterministic Engineering Governance Contract v1.0 in this session, status `NOT ADOPTED`.
- Caller selections: `GOVERNANCE_BOOTSTRAP` and 500 LOC.
- Design Authority Record v0.3 root `b4a1a02fc333b7c212186d7b07fb9d2b5536afaf2ae7434c20371ce097c3d10f`.
- PRD v0.2 SHA-256 `a0283859f2b128c9ef0adcb25922901e135e0aeed64ba42900d8b83701f48be1`.
- Candidate-Readiness Register v0.1 SHA-256 `b2a97363962c7745e45e46c7e519b403d347a61f0cb55a6ed65aeba4cf9656b8`.
- Engineering Rules source SHA-256 `deb95b212e0d3fae948e6cd0b9b932ede58cbaeef0170ccc8257b7a80a117793`; only the 53 rule statements are transferred as repository governing rules. Skill workflow prose is not transferred and creates no repository lifecycle.
- Google review references are source material only until an exact destination adoption record authorizes them.
  - Writing Good CL Descriptions: `https://google.github.io/eng-practices/review/developer/cl-descriptions.html`
  - Small CLs: `https://google.github.io/eng-practices/review/developer/small-cls.html`
  - Google Style Guides: `https://google.github.io/styleguide/`
  - The Standard of Code Review: `https://google.github.io/eng-practices/review/reviewer/standard.html`
  - What to Look For in a Code Review: `https://google.github.io/eng-practices/review/reviewer/looking-for.html`

Protected actions:

- Declared local governance mutations -> AUTHORIZED by user, subject to the exact approved plan, seven-field envelope, all admission gates, and 500-LOC candidate ceiling.
- Read-only deterministic verification -> AUTHORIZED.
- Install, branch, commit, push, PR, merge, deploy, migrate, release, and promote -> UNAUTHORIZED.

## Obligations and evaluation

| Obligation | Current behavior | Current verification | Acceptance criterion | Oracle | Increment |
| --- | --- | --- | --- | --- | --- |
| `OBL-001` Single authority and pointer | GAP | GAP | One root authority; exact Claude pointer; no competing authority | Structural verifier | `INC-1` |
| `OBL-002` Caller-controlled unique router | GAP | GAP | Caller supplies domain; exactly one match; zero/multi match block | Route positive/negative controls | `INC-1`, `INC-5` |
| `OBL-003` Exact source and bounded input admission | GAP | GAP | Required subset loaded; loaded subset allowed; exact current sources | Input/source negative controls | `INC-2`, `INC-5` |
| `OBL-004` Evidence and skills nonauthority | GAP | GAP | Neither can create authority or waive a gate | Policy and negative controls | `INC-2`, `INC-7` |
| `OBL-005` Seven-field envelope | GAP | GAP | All fields present and valid; omission blocks | Schema controls | `INC-5` |
| `OBL-006` Pre-code and mutation admission | GAP | GAP | `G_PC_01`-`G_PC_11` pass; exact path/effect/preconditions; stop rechecked | Gate controls | `INC-5`, `INC-6` |
| `OBL-007` Structured fail-closed result | GAP | GAP | Every terminal failure validates against the `BLOCKED` schema | Schema controls | `INC-5`, `INC-6`, `INC-7` |
| `OBL-008` Deterministic system verification | GAP | GAP | All 50 invariants and 18 negative controls pass twice unchanged | Verifier double run | `INC-7` |
| `OBL-009` Canonical portable inventory | GAP | GAP | Exact closed 50-ID set; one trace, predicate, evidence set, negative control, and stop per invariant | Inventory schema and membership controls | `INC-2`, `INC-7` |
| `OBL-010` Execution, review, and zero-trust boundaries | GAP | GAP | Exact-head evidence, bounded diagnostic repair, privilege/data boundaries, independent review, and separate merge authority fail closed | Policy and adversarial controls | `INC-2`, `INC-3`, `INC-7` |
| `OBL-011` Proof-boundary honesty | GAP | GAP | Written governance never claims host isolation, capability suppression, immutable provenance, or external verification that has not been independently implemented and verified | Prohibited-claim controls | `INC-2`, `INC-7` |
| `OBL-012` Google-aligned review governance | GAP | GAP | `CR-01` through `CR-14`, finding classes, mechanical/judgment separation, and exact reference adoption are explicit | Review-policy and adoption controls | `INC-3`, `INC-7` |
| `OBL-013` Destination configuration schemas | GAP | GAP | CI, review, branch protection, permitted effects, and privileged boundaries reject unresolved required values | Five schema suites | `INC-4`, `INC-7` |
| `OBL-014` Negative controls and state machine | GAP | GAP | `NC-01` through `NC-18` and every proposed state/transition have exact, non-escalating outcomes | Negative-control and transition evaluator | `INC-5`, `INC-6`, `INC-7` |
| `OBL-015` Adoption evidence | GAP | GAP | All 14 adoption predicates are explicit; unresolved items preserve `NOT_ADOPTED` and prohibit implementation authority | Adoption-record schema | `INC-3`, `INC-6`, `INC-7` |

## Dependency graph

`INC-1 -> INC-2 -> INC-3 -> INC-4 -> INC-5 -> INC-6 -> INC-7`

Execution order: `INC-1`, `INC-2`, `INC-3`, `INC-4`, `INC-5`, `INC-6`, `INC-7`.

These increments are build batching only. They do not create a mandatory repository lifecycle.

## Selected design

Selected structure:

```text
AGENTS.md                          canonical execution authority
CLAUDE.md                         exact pointer only
CONTEXT.md                        caller-domain router and route registry
.governance/
  authority.md                    precedence and authority identities
  source-registry.md              exact source locators and bindings
  engineering-rules.md            repository-authorized 53 rule statements
  invariant-inventory.json        closed 50-invariant machine-readable inventory
  execution.md                    fail-closed execution rules
  evidence.md                     evidence and skill nonauthority
  code-review.md                  Google-aligned review and finding classification
  verification.md                 exact-head and exact-candidate proof
  completion.md                   terminal disposition
  states.md                       proposed states and authorized transitions
  adoption.md                     destination adoption requirements and status
  config/
    ci.schema.json                required and conditional CI configuration
    review.schema.json            independent review-cycle configuration
    branch-protection.schema.json provider enforcement and evidence
    permitted-effects.schema.json closed capability/effect grants
    privileged-boundaries.schema.json trust topology and enforcement evidence
.harness/
  route-invariants.md             unique-route predicates
  task-envelope.schema.json       seven-field envelope
  input-gates.md                  required/allowed/source/discovery gates
  pre-code-readiness.md           G_PC_01 through G_PC_11
  mutation-gate.md                path/effect/precondition and stop recheck
  blocked-record.schema.json      standard terminal failure
  contracts/governance-bootstrap.md
  negative-controls.json          NC-01 through NC-18
  adoption-record.schema.json     destination adoption evidence
  evals.md
  tasks.md
  runs/.gitkeep
scripts/verify-governance.py       deterministic positive/negative controls
```

Rejected alternatives:

- Agent-selected routing: violates caller control.
- Numbered mandatory stages: violates lifecycle neutrality.
- Policy in `CLAUDE.md`: creates competing authority.
- Skills as routing sources: violates skills nonauthority.
- Full PRD in `AGENTS.md`: violates bounded context and creates drift.
- Product-domain routes now: would invent repository-specific domains.

## Contracts and invariants

Admission aggregate:

`G_ADMISSION = G_AUTHORITY AND G_ROUTE AND G_INPUTS AND G_SOURCE AND G_SCOPE AND G_READINESS`.

Unique routing: exactly one route predicate matches the caller-supplied domain. Zero match returns `ROUTE_ZERO_MATCH`; multiple matches return `ROUTE_MULTI_MATCH`.

Input authorization: required inputs are a subset of loaded inputs, and loaded inputs are a subset of allowed inputs.

Source authority: every routed source exists and matches its trusted binding.

Evidence separation: evidence cannot create a requirement, permission, waiver, routing choice, merge authorization, or completion authority.

Discovery: discovery is locator-only, uses bounded reads, does not mutate, and does not establish readiness.

Mutation: the path is authorized, the effect is authorized, every precondition passes, and the stop condition is evaluated after each mutation.

Failure behavior: missing, stale, conflicting, unauthorized, ambiguous, or unverified state returns schema-valid `BLOCKED`. The agent cannot repair governance, infer missing values, or choose a different route from that result.

## Canonical invariant inventory

The following closed membership is normative for the bootstrap. Each machine-readable record must also contain `source_trace`, `predicate`, `required_evidence`, `negative_control`, and `stop_condition`.

| ID | Portable invariant | Deterministic requirement |
| --- | --- | --- |
| `RT-01` | Single authority root | Exactly one root `AGENTS.md` governs repository execution. |
| `RT-02` | Single context router | Root `CONTEXT.md` exclusively controls task-domain and source routing. |
| `RT-03` | No competing authority | Subordinate documents cannot override root authority. |
| `RT-04` | Caller-controlled domain | The caller or authorized external controller supplies the domain; the executing agent never infers it. |
| `RT-05` | Unique route | Exactly one canonical route predicate matches. |
| `RT-06` | Complete task envelope | All seven required task-envelope fields are present and valid. |
| `RT-07` | Exact source resolution | Every required governing source resolves exactly once. |
| `RT-08` | Source binding | Required source identities match the trusted execution binding. |
| `RT-09` | Least-context loading | Only route-selected sources, sections, workpieces, and evidence load. |
| `RT-10` | Bounded discovery | Pre-envelope discovery localizes paths only; it cannot execute, mutate, or grant authority. |
| `RT-11` | Evidence non-authority | Evidence cannot create requirements, permissions, waivers, routing, or merge authority. |
| `RT-12` | Skills non-authority | Skills provide optional procedures, not routing or execution privileges. |
| `RT-13` | No mandatory lifecycle | No predecessor stage is mandatory unless independent governing authority requires it. |
| `RT-14` | Fail-closed evaluation | Missing, stale, conflicting, unauthorized, or ambiguous inputs produce `BLOCKED`. |
| `RT-15` | Explicit mutation admission | Mutation requires Pre-Code readiness, exact scope, verification, and a stop condition. |
| `EX-01` | Execution admission | The full Pre-Code Readiness Gate passes before protected mutation. |
| `EX-02` | Verified gap | Every mutation addresses an observable defect, requirement, or Definition of Done remainder. |
| `EX-03` | Exact authorization | Modified paths and resulting effects remain within explicit authorization. |
| `EX-04` | Bounded changes | Reviewable changes do not exceed the configured ceiling without a verified owner exception. |
| `EX-05` | Mutation checkpoint | Re-evaluate the governing stop condition after each mutation. |
| `EX-06` | Bounded repair | A repeated repair has materially new diagnostic evidence for a specific correction. |
| `EX-07` | Fail-closed termination | `STOP`, `BLOCKED`, `REDUCE`, `REDESIGN`, or unmet evidence terminates unauthorized continuation. |
| `VF-01` | Deterministic verifier | Every obligation has a defined verifier or explicit `BLOCKED` condition. |
| `VF-02` | Surface-specific verification | Required checks execute for every changed surface. |
| `VF-03` | Regression preservation | Previously accepted requirements cannot be weakened silently. |
| `VF-04` | Exact-head evidence | Required CI passes on the exact final implementation head. |
| `VF-05` | Independent review | Required independent review follows successful CI and has no unresolved actionable findings. |
| `VF-06` | Review convergence | Review has an authorized bounded cycle limit and explicit stop condition. |
| `VF-07` | Separate merge authority | Technical eligibility never independently authorizes merge. |
| `ZT-01` | Authority isolation | Untrusted inputs and subordinate materials cannot create or override authority. |
| `ZT-02` | Evidence non-authority | Logs, tests, reports, and history cannot create requirements, permissions, or waivers. |
| `ZT-03` | Source and input integrity | Only authorized, correctly bound sources and inputs satisfy prerequisites. |
| `ZT-04` | Privilege containment | Secrets and privileged provider credentials remain outside browser-facing or unauthorized contexts. |
| `ZT-05` | Validated trust boundaries | Validate server mutations, database access, and webhook authenticity before effects. |
| `ZT-06` | Replay and duplication protection | Duplicate-sensitive operations are idempotent and safely handle replay. |
| `ZT-07` | Sensitive-data containment | Private data cannot enter unauthorized analytics, logs, public routes, or environments. |
| `CR-01` | Change purpose | The change description states what changed and why. |
| `CR-02` | Description first line | The first description line is concise, specific, and imperative. |
| `CR-03` | Description currentness | The description represents the final diff and its limitations accurately. |
| `CR-04` | Conceptual coherence | The change is coherent and independently reviewable. |
| `CR-05` | Related tests | New or changed behavior has appropriate tests. |
| `CR-06` | Scope hygiene | Unrelated refactoring, formatting, and cleanup are excluded or separately justified. |
| `CR-07` | Architectural fit | The design integrates appropriately with the existing architecture. |
| `CR-08` | User and edge correctness | Functionality serves intended users and addresses applicable edge cases, including concurrency. |
| `CR-09` | Necessary complexity | Complexity is justified; speculative abstractions and unused behavior are rejected. |
| `CR-10` | Test quality | Tests contain meaningful assertions that detect incorrect behavior. |
| `CR-11` | Intent communication | Names, comments, and documentation communicate intent accurately. |
| `CR-12` | Adopted style | Authored code conforms to adopted language-specific style guides. |
| `CR-13` | Independent line review | Every assigned authored line and relevant surrounding context receives independent review. |
| `CR-14` | Code-health improvement | The change improves overall code health with no unresolved material finding. |

Source traces:

- `RT-01..RT-15` -> `USER-ROUTING-SPEC-2026-10-08`.
- `EX-01..ZT-07` -> `USER-EXECUTION-SPEC-2026-10-08`.
- `CR-01..CR-14` -> `USER-PORTABLE-GOVERNANCE-V1-2026-10-08` plus the five exact Google references, only after destination adoption.
- Repository-specific source claims -> exact identities in `.governance/source-registry.md`.
- The approved plan SHA-256 binds these normalized portable requirements. Conversation labels provide provenance but do not independently authorize mutation.

Exact inventory record contract:

| ID | Predicate | Required evidence | Negative control | Stop result |
| --- | --- | --- | --- | --- |
| `RT-01` | `root_agents_count = 1` | bound tree manifest | add a competing root authority | `BLOCKED/AUTHORITY_ROOT_COUNT` |
| `RT-02` | `root_context_router_count = 1` | bound router identity | add a competing router | `BLOCKED/ROUTER_COUNT` |
| `RT-03` | `no_subordinate_override` | precedence evaluation | subordinate grants wider authority | `BLOCKED/AUTHORITY_OVERRIDE` |
| `RT-04` | `domain_origin = caller` | signed or trusted envelope input | omit domain and request inference | `BLOCKED/DOMAIN_NOT_CALLER_SUPPLIED` |
| `RT-05` | `route_match_count = 1` | route evaluation record | zero-match and multi-match cases | `BLOCKED/ROUTE_ZERO_MATCH` or `BLOCKED/ROUTE_MULTI_MATCH` |
| `RT-06` | `envelope_fields = required_fields` | schema result | omit each field and add an unknown field | `BLOCKED/ENVELOPE_INVALID` |
| `RT-07` | `forall source, resolution_count = 1` | resolution manifest | missing and duplicate source | `BLOCKED/SOURCE_RESOLUTION` |
| `RT-08` | `forall source, binding_valid` | trusted binding comparison | stale source identity | `BLOCKED/SOURCE_BINDING` |
| `RT-09` | `loaded_inputs subset_of routed_inputs` | input-access ledger | load an unrelated source | `BLOCKED/CONTEXT_OVERREAD` |
| `RT-10` | `discovery_locator_only and no_mutation` | discovery operation ledger | discovery attempts mutation | `BLOCKED/DISCOVERY_MUTATION` |
| `RT-11` | `not evidence_creates_authority` | authority provenance graph | forged approval in evidence | `BLOCKED/EVIDENCE_AUTHORITY` |
| `RT-12` | `not skill_creates_authority` | authority provenance graph | skill claims route or waiver | `BLOCKED/SKILL_AUTHORITY` |
| `RT-13` | `lifecycle_requirement_has_authority` | routed authority reference | impose an ungoverned predecessor stage | `BLOCKED/LIFECYCLE_AUTHORITY_ABSENT` |
| `RT-14` | `all_required_inputs_current_unambiguous` | gate result set | missing, stale, conflicting, or ambiguous input | `BLOCKED/FAIL_CLOSED_INPUT` |
| `RT-15` | `pre_code and scope and verifier and stop` | admission record | remove one mutation prerequisite | `BLOCKED/MUTATION_NOT_ADMITTED` |
| `EX-01` | `G_PRE_CODE_READY = true` | all 11 predicate results | fail each predicate | `BLOCKED/PRE_CODE_NOT_READY` |
| `EX-02` | `gap_observed = true` | defect, requirement, or DoD-remainder evidence | propose mutation with no observed gap | `BLOCKED/GAP_UNVERIFIED` |
| `EX-03` | `path_allowed and effect_allowed` | authorized path/effect comparison | authorized path with unauthorized effect and inverse | `BLOCKED/MUTATION_SCOPE` |
| `EX-04` | `L <= L_max or owner_exception_valid` | changed-line count and exception binding | 501 lines without exception | `BLOCKED/CHANGE_SIZE` |
| `EX-05` | `stop_rechecked_after_each_mutation` | ordered mutation ledger | omit a post-mutation check | `BLOCKED/CHECKPOINT_MISSING` |
| `EX-06` | `repeat_repair_implies_new_diagnostics` | attempt and diagnostic hashes | repeat a failed repair without new evidence | `BLOCKED/REPAIR_NOT_DIAGNOSTIC` |
| `EX-07` | `terminal_signal_implies_no_continuation` | operation ledger after signal | continue after terminal result | `BLOCKED/TERMINATION_BYPASS` |
| `VF-01` | `forall obligation, verifier_defined or blocked_defined` | obligation-verifier map | remove both outcomes | `BLOCKED/VERIFIER_UNDEFINED` |
| `VF-02` | `required_surface_checks subset_of executed_checks` | changed-surface and check manifests | omit one applicable check | `BLOCKED/SURFACE_CHECK_MISSING` |
| `VF-03` | `accepted_regressions_preserved` | before/after regression results | weaken or delete an accepted requirement | `BLOCKED/REGRESSION_WEAKENED` |
| `VF-04` | `G_CI(final_head) = true` | check statuses bound to final head | present PASS from an older head | `BLOCKED/CI_NOT_EXACT_HEAD` |
| `VF-05` | `ci_pass and review_current and findings = 0` | independent review bound to candidate | retain an actionable finding | `BLOCKED/REVIEW_FINDINGS` |
| `VF-06` | `N <= N_max and stop_defined` | authorized limit and cycle ledger | exceed limit or omit stop | `BLOCKED/REVIEW_LIMIT` |
| `VF-07` | `merge_requires_separate_user_authority` | explicit user authorization and protection evidence | agent attempts merge from green checks alone | `BLOCKED/MERGE_UNAUTHORIZED`; effect denied |
| `ZT-01` | `authority_sources subset_of trusted_authority` | authority graph and bindings | untrusted input overrides policy | `BLOCKED/UNTRUSTED_AUTHORITY` |
| `ZT-02` | `evidence_changes_authority = false` | evidence classification record | report attempts waiver | `BLOCKED/EVIDENCE_WAIVER` |
| `ZT-03` | `inputs_authorized and bindings_valid` | admitted input manifest | inject unauthorized or stale input | `BLOCKED/INPUT_INTEGRITY` |
| `ZT-04` | `privileged_credentials_outside_untrusted_contexts` | capability and secret-exposure manifest | expose privileged secret to browser or agent sandbox | `BLOCKED/PRIVILEGE_EXPOSURE` |
| `ZT-05` | `all_effect_boundaries_validated` | server, database, and webhook validation evidence | unsigned webhook or unvalidated mutation | `BLOCKED/TRUST_BOUNDARY` |
| `ZT-06` | `duplicate_sensitive_effects_idempotent` | replay test bound to operation | replay identical request | `BLOCKED/REPLAY_UNSAFE` |
| `ZT-07` | `private_data_destinations subset_of authorized_destinations` | data-flow and environment evidence | route private data to logs, analytics, public route, or wrong environment | `BLOCKED/SENSITIVE_DATA_EXPOSURE` |
| `CR-01` | `description_has_what_and_why` | current description bound to candidate | omit what or why | `BLOCKED/REVIEW_DESCRIPTION_INCOMPLETE` |
| `CR-02` | `first_line_concise_specific_imperative` | description parser result | vague or non-imperative first line | `BLOCKED/REVIEW_DESCRIPTION_FIRST_LINE` |
| `CR-03` | `description_matches_final_diff` | reviewer attestation bound to final candidate | mutate diff without refreshing description | `BLOCKED/REVIEW_DESCRIPTION_STALE` |
| `CR-04` | `change_conceptually_coherent` | independent reviewer judgment | combine unrelated concepts | `BLOCKED/REVIEW_NOT_COHERENT` |
| `CR-05` | `behavior_change_implies_related_tests` | changed-behavior/test map | change behavior without applicable test or approved BLOCKED condition | `BLOCKED/REVIEW_TESTS_MISSING` |
| `CR-06` | `unrelated_delta_absent_or_separately_justified` | diff-scope review | add unrelated cleanup | `BLOCKED/REVIEW_SCOPE_CONTAMINATION` |
| `CR-07` | `design_fits_architecture` | independent architectural review | introduce boundary violation | `BLOCKED/REVIEW_ARCHITECTURE` |
| `CR-08` | `users_and_applicable_edges_addressed` | requirement, edge-case, and reviewer record | omit an applicable concurrency or user edge | `BLOCKED/REVIEW_FUNCTIONALITY` |
| `CR-09` | `complexity_justified_and_no_speculation` | design rationale and reviewer judgment | add unused abstraction or behavior | `BLOCKED/REVIEW_COMPLEXITY` |
| `CR-10` | `tests_detect_incorrect_behavior` | mutation/regression evidence and reviewer judgment | replace assertions with non-detecting checks | `BLOCKED/REVIEW_TEST_QUALITY` |
| `CR-11` | `names_comments_docs_accurate` | independent line review | misleading name, comment, or documentation | `BLOCKED/REVIEW_INTENT` |
| `CR-12` | `authored_code_conforms_to_adopted_style` | adopted style identity and formatter/linter evidence | style violation without exception | `BLOCKED/REVIEW_STYLE` |
| `CR-13` | `assigned_authored_lines_and_context_reviewed` | coverage attestation bound to final diff | leave an assigned authored line unreviewed | `BLOCKED/REVIEW_COVERAGE` |
| `CR-14` | `code_health_improves_and_material_findings_zero` | independent final review disposition | unresolved material finding or net health regression | `BLOCKED/REVIEW_NOT_ACCEPTED` |

Executable aggregate predicates:

- `G_ROUTE_UNIQUE(E) := |{r in R : P_r(E) = true}| = 1`.
- `G_REQUIRED_INPUTS := I_required subset_of I_loaded`.
- `G_ALLOWED_INPUTS := I_loaded subset_of I_allowed`.
- `G_SOURCE_PRESENT := AND(s in S_routed, exists(s) AND bindingValid(s))`.
- `G_PRE_CODE_READY := AND(i=1..11, G_PC_i)`.
- `G_MUTATION(m) := path(m) in P AND effect(m) in A AND AND(Preconditions(m))`.
- `G_CHANGE_SIZE := L <= L_max OR G_OWNER_EXCEPTION`.
- `G_REPAIR := G_CONTRACT AND G_REPRODUCTION AND G_SCOPE AND G_VERIFIER`.
- `G_CI(h) := AND(c in C_required, status(c,h) = PASS)`.
- `G_REVIEW := G_CI AND G_REVIEW_CURRENT AND F = 0 AND N <= N_max`.
- `G_MERGE := G_CI AND G_REVIEW AND G_BRANCH_PROTECTION AND G_USER_AUTHORIZATION`.
- `G_EXECUTION_ADMISSION := G_ROUTE AND G_SOURCE AND G_PRE_CODE_READY AND G_MUTATION`.
- `G_ACCEPTANCE := G_VERIFICATION AND G_REVIEW AND G_EVIDENCE_CURRENT`.

`G_ACCEPTANCE` does not imply `G_MERGE`. Missing repository adapter values, including `C_required`, `N_max`, branch-protection evidence, permitted effects, or privileged-boundary configuration, produce `BLOCKED`; the bootstrap does not invent them.

This bootstrap establishes repository governance contracts and mechanical document-level controls. It does not prove container isolation, host-level capability suppression, cryptographic evidence provenance, verifier immutability, or an external trusted verifier. A later zero-trust harness candidate must independently implement and verify supervisor-controlled tool admission, disposable sandbox isolation, agent-inaccessible verifier writes, immutable evidence bindings, and evaluation outside the agent execution environment before any zero-trust-complete claim.

## Destination configuration contracts

All fields below are required schema members. A placeholder, absent approval, stale binding, or unverified value preserves `NOT_ADOPTED` and returns `BLOCKED` when the applicable gate is invoked.

CI configuration fields: repository identifier; protected target branch; trusted CI provider; exact required status contexts; trusted runner or integration IDs; dependency verification; lint and formatting; static/type verification; unit tests; integration/contract tests; build/package verification; security checks; repository regressions; change-size verifier; exact-head verifier; independent verifier identity and authority boundary. Applicability predicates must cover database, API, UI, security-sensitive, agent/harness, and release surfaces. Skips require an approved deterministic non-applicability result.

Review configuration fields: review mechanism; maximum cycles; entire applicable authored-change scope; reviewer independence; exact-head CI prerequisite; evidence-backed repair and refreshed CI; zero unresolved actionable findings; cycle-limit stop; explicit owner authority for an additional cycle; equivalent-effective-diff carry-forward proof; no merge effect. `maximum_cycles = 3` is proposed only and remains unenforced until destination-owner approval.

Branch-protection fields: repository and target branch; exact ruleset identity; active enforcement; pull-request requirement; exact required checks and integration IDs; strict currentness; bypass actors and conditions; force-push restriction; deletion restriction; reviewer policy; current candidate head; exact-head CI records; review disposition; separate merge authorization. A workflow file is not enforcement evidence.

Permitted-effect records use `PE-01` through `PE-10`: exact authorized reads; bounded discovery; exact file create/modify; authorized deletion; approved verification; sanitized non-authoritative evidence; authorized branch/PR creation; review request; separately user-authorized eligible merge; governance modification under governance-change authority. Each record contains effect ID, target scope, principal, route/task binding, preconditions, tool capability, expected evidence, and stop condition. The default capability set is empty.

Privileged-boundary records use `PB-01` through `PB-10`: authority/content separation; caller domain control; sandbox/supervisor separation; verifier/approval write protection; production-secret denial; separate Git administration; independent result preservation; scoped provider mutation; separate merge/deploy/release privilege; approved sensitive-data lifecycle. Required evidence includes supervisor identity, agent identity and sandbox, tool allowlist, filesystem boundaries, protected locations, secret policy, network permissions, Git permissions, evidence immutability/currentness, and promotion enforcement.

## Review classifications and judgment boundary

Blocking classes: material defect, governing-rule violation, security/privacy issue, missing required verification. A required adopted-style violation requires correction or an authorized exception. Optional improvements and nits are advisory. Unsupported or inaccurate findings must be corrected or withdrawn using evidence.

Mechanical checks include description fields, formatter/linter results, size, executed tests, assigned review files, and candidate-bound attestation. Architectural quality, assertion correctness, justified complexity, conceptual cohesion, code-health improvement, and whether a finding is actionable require an independent reviewer judgment. The implementing agent cannot self-attest these judgments.

## Negative controls and portable states

The closed negative-control set is `NC-01` through `NC-18`: missing/forged authorization; ambiguous route; unregistered source/input; stale binding; out-of-scope write; unauthorized external effect; verifier/policy mutation; protected-credential access; stale CI; skipped mandatory CI; unresolved material review finding; unauthorized fourth cycle; forged/agent-authored review acceptance; branch-protection bypass; unauthorized merge; unsafe replay; evidence-created authority; unauthorized sandbox/network privilege. Each control requires independently captured rejection evidence. Missing or unjustifiably skipped controls cannot PASS.

Proposed portable states are `READY`, `BLOCKED`, `FAIL`, `STOP`, `REDUCE`, `REDESIGN`, `VERIFIED`, `REVIEW_ACCEPTED`, and `MERGE_ELIGIBLE`. They belong to a separate `engineering_admission_state` field and cannot populate or redefine the sealed Decision-025 `release_status`, whose only values remain `ACCEPTED`, `REJECTED`, and `BLOCKED`. The destination must approve an exact transition table. `VERIFIED` and `REVIEW_ACCEPTED` never transition automatically to merge. The acceptance sequence is route, authority, readiness, exact scope, bounded execution, independent CI, independent review, merge eligibility, then separately user-authorized merge.

## Adoption record

The destination adoption record has 14 mandatory predicates: current root authority; current router; bound Engineering Rules; valid route/source bindings; approved destination configuration; registered CI identities; approved reviewer and cycle limit; adopted applicable Google style guides; independently verified branch protection; explicit effects/resources; established privileged boundaries/controller; defined negative controls; defined stop/terminal records; zero unresolved authority conflicts.

Until all 14 predicates and their independent evidence pass, the portable contract status remains `NOT_ADOPTED`. Only separately authorized read-only work is eligible. The contract cannot authorize implementation, relax checks, or modify governance by itself.

## Task-envelope handoff

The caller-authorized bootstrap envelope is:

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
  "authorized_candidate_paths": [
    ".harness/", ".governance/", "AGENTS.md", "CLAUDE.md", "CONTEXT.md", "scripts/verify-governance.py"
  ],
  "approvals": ["USER_DOMAIN_GOVERNANCE_BOOTSTRAP", "USER_LOC_CEILING_500", "EXACT_PLAN_SHA_APPROVAL_PENDING"],
  "source_binding": "build-manifest/source_binding"
}
```

The final approval item changes from pending only when the user approves this exact plan SHA-256.

## Task-list handoff

Target: `.harness/tasks.md`.

Preservation evidence: target absent at the bound source state.

Entries:

- [ ] `INC-1` Establish authority root, pointer, caller-domain router, and task list.
- [ ] `INC-2` Establish source registry, 50-invariant inventory, Engineering Rules, execution, and evidence constraints.
- [ ] `INC-3` Establish review, verification, completion, states, and adoption governance.
- [ ] `INC-4` Establish CI, review, branch-protection, permitted-effect, and privileged-boundary schemas.
- [ ] `INC-5` Establish route, envelope, failure, input, and Pre-Code contracts.
- [ ] `INC-6` Establish mutation admission, 18 negative controls, and adoption evidence.
- [ ] `INC-7` Add deterministic whole-system verification and exact-candidate evidence.

## Increments

### INC-1

Objective: Establish the single authority root and caller-controlled router.

Obligations: `OBL-001`, part of `OBL-002`.

Dependencies: none.

Files: `.harness/tasks.md`, `AGENTS.md`, `CLAUDE.md`, `CONTEXT.md`, `.governance/authority.md`.

Actions: Create only these five files. `CONTEXT.md` registers only `GOVERNANCE_BOOTSTRAP`. It accepts caller-supplied domains and never selects one. Record current task entries before other mutation.

Acceptance: exact pointer; one authority root; one router; one bootstrap route; no agent-inference language; added-plus-deleted lines at most 500.

Verifier: deterministic file, route, and line-delta predicates. Timeout 30 seconds. Two repair attempts.

Checkpoint: authority and routing exist; every unresolved downstream dependency remains fail-closed.

### INC-2

Objective: Establish exact source binding, the closed inventory, and execution/evidence controls.

Obligations: `OBL-003`, `OBL-004`, `OBL-009`, `OBL-010`, `OBL-011`.

Dependencies: `INC-1`.

Files: `.governance/source-registry.md`, `.governance/engineering-rules.md`, `.governance/invariant-inventory.json`, `.governance/execution.md`, `.governance/evidence.md`.

Actions: Bind source identities, including the five Google references as non-authoritative pending adoption. Transfer only the 53 Engineering Rules statements. Encode exactly 50 invariant records with the six required fields. Define execution, diagnostic repair, evidence, privilege, replay, sensitive-data, and proof-boundary controls.

Acceptance: exact source records; closed 50-ID inventory; complete record fields; no skill or evidence grants; no false enforcement claim; added-plus-deleted lines at most 500.

Verifier: deterministic JSON, membership, source, prohibited-authority, proof-boundary, and line-delta predicates. Timeout 30 seconds. Two repair attempts.

Checkpoint: portable requirements are machine-readable but the destination remains `NOT_ADOPTED`.

### INC-3

Objective: Establish review, verification, completion, portable states, and adoption governance.

Obligations: `OBL-005`, `OBL-007`, `OBL-010`, `OBL-012`, `OBL-014`, `OBL-015`.

Dependencies: `INC-2`.

Files: `.governance/code-review.md`, `.governance/verification.md`, `.governance/completion.md`, `.governance/states.md`, `.governance/adoption.md`.

Actions: Define CR-01 through CR-14, finding classes, mechanical/judgment separation, exact-head proof, bounded independent review, non-escalating states, separate merge authority, and the 14 adoption predicates. Keep the proposed three-cycle value non-enforcing until owner approval.

Acceptance: Google guidance requires adoption; stale evidence and self-attestation are rejected; states have no automatic merge transition; unresolved adoption stays `NOT_ADOPTED`; added-plus-deleted lines at most 500.

Verifier: deterministic policy, reference, transition, prohibited-escalation, and line-delta predicates. Timeout 30 seconds. Two repair attempts.

Checkpoint: review and adoption policy exists without conferring review, PASS, merge, or implementation authority.

### INC-4

Objective: Establish the five destination configuration schemas.

Obligations: `OBL-013`, parts of `OBL-006`, `OBL-010`, `OBL-012`, `OBL-015`.

Dependencies: `INC-3`.

Files: `.governance/config/ci.schema.json`, `.governance/config/review.schema.json`, `.governance/config/branch-protection.schema.json`, `.governance/config/permitted-effects.schema.json`, `.governance/config/privileged-boundaries.schema.json`.

Actions: Encode every required field, closed ID set, applicability rule, evidence binding, and unresolved-value rejection for CI, review, provider enforcement, effects, and privileged boundaries.

Acceptance: placeholders and omissions reject; review maximum three is proposed, not approved; capability default is empty; workflow files do not prove provider enforcement; added-plus-deleted lines at most 500.

Verifier: deterministic schema positive/negative controls and line-delta predicates. Timeout 30 seconds. Two repair attempts.

Checkpoint: destination adapters are mechanically specifiable and remain unresolved until authorized evidence is supplied.

### INC-5

Objective: Establish route, input, envelope, failure, and Pre-Code contracts.

Obligations: `OBL-002`, `OBL-003`, `OBL-005`, `OBL-006`, `OBL-007`.

Dependencies: `INC-4`.

Files: `.harness/route-invariants.md`, `.harness/task-envelope.schema.json`, `.harness/blocked-record.schema.json`, `.harness/input-gates.md`, `.harness/pre-code-readiness.md`.

Actions: Define zero/multi/one route outcomes, the exact seven-field envelope, the eight-field `BLOCKED` record, required/allowed/source/discovery gates, and PC-01 through PC-11.

Acceptance: omissions and additional fields reject; every route/input ambiguity blocks; Wingman PC-11 is 500 LOC; added-plus-deleted lines at most 500.

Verifier: deterministic schema, route, input, readiness, and line-delta controls. Timeout 30 seconds. Two repair attempts.

Checkpoint: routing and Pre-Code readiness are evaluable without agent inference.

### INC-6

Objective: Establish mutation admission, the 18 negative controls, and the adoption evidence contract.

Obligations: `OBL-006`, `OBL-007`, `OBL-010`, `OBL-013`, `OBL-014`, `OBL-015`.

Dependencies: `INC-5`.

Files: `.harness/mutation-gate.md`, `.harness/contracts/governance-bootstrap.md`, `.harness/negative-controls.json`, `.harness/adoption-record.schema.json`, `.harness/evals.md`.

Actions: Define per-mutation authorization and stop recheck, bind the bootstrap envelope, encode NC-01 through NC-18 with independent rejection evidence, encode the 14 adoption predicates, and name every positive/negative evaluator.

Acceptance: exact NC and adoption memberships; skipped controls require approved deterministic non-applicability; governance/verifier mutation and unauthorized effects reject; added-plus-deleted lines at most 500.

Verifier: deterministic schema, membership, mutation, adoption, and line-delta controls. Timeout 30 seconds. Two repair attempts.

Checkpoint: all contracts and evaluators exist, but none can self-certify adoption.

### INC-7

Objective: Add deterministic whole-system verification and produce exact-candidate evidence.

Obligations: `OBL-001` through `OBL-015`.

Dependencies: `INC-6`.

Files: `scripts/verify-governance.py`, `.harness/runs/.gitkeep`.

Actions: Implement positive and negative controls for all 50 invariants, PC-01 through PC-11, PE-01 through PE-10, PB-01 through PB-10, NC-01 through NC-18, all schemas, all states, all adoption predicates, stale-head evidence, unauthorized fourth review, forged review acceptance, branch-protection bypass, and unauthorized merge. Run twice without mutation.

Acceptance: verifier exits 0 twice; exact closed memberships and every named control pass; candidate identity is unchanged; destination status remains `NOT_ADOPTED` unless separately supplied independent evidence satisfies every adoption predicate; added-plus-deleted lines at most 500.

Verifier: `python3 scripts/verify-governance.py`; exit 0 with every named control passing twice on one unchanged candidate. Timeout 60 seconds per run. Two repair attempts.

Checkpoint: the bootstrap candidate has deterministic producer evidence. It is not adopted, independently accepted, merged, committed, or published.

## Source binding

Canonical command: `python /root/.codex/skills/remote-skills/skill-6a931d92b4488191aa64c7bd84e5736c/scripts/source-binding.py --repo /workspace/scratch/99e6ff3f9161/wingman --exclude-plan-path plans/wingman-governance-router-plan-v0.2.md`

- commit: `c92e695344f00fb30698cd494be4b8abf907e6ee`
- staged diff SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- unstaged diff SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- untracked manifest SHA-256: `015ccfdbfa30f551bbae21214e98f85781ca220517569d38739383a2c1be423e`
- dirty submodule manifest SHA-256: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`
- excluded plan path: `plans/wingman-governance-router-plan-v0.2.md`

## Build manifest

```json
{
  "schema": "build-agent/v2",
  "completion_authority": "User (Emory Harris) after independent verification of the exact candidate",
  "source_binding": {
    "commit": "c92e695344f00fb30698cd494be4b8abf907e6ee",
    "staged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "unstaged_diff_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "untracked_manifest_sha256": "015ccfdbfa30f551bbae21214e98f85781ca220517569d38739383a2c1be423e",
    "dirty_submodule_manifest_sha256": "4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945",
    "excluded_plan_path": "plans/wingman-governance-router-plan-v0.2.md"
  },
  "task_list": {
    "target": ".harness/tasks.md",
    "preservation_evidence": "Target absent at the bound source state.",
    "entries": [
      {
        "increment": "INC-1",
        "text": "Establish authority root, pointer, caller-domain router, and task list."
      },
      {
        "increment": "INC-2",
        "text": "Establish source registry, 50-invariant inventory, Engineering Rules, execution, and evidence constraints."
      },
      {
        "increment": "INC-3",
        "text": "Establish review, verification, completion, states, and adoption governance."
      },
      {
        "increment": "INC-4",
        "text": "Establish CI, review, branch-protection, permitted-effect, and privileged-boundary schemas."
      },
      {
        "increment": "INC-5",
        "text": "Establish route, envelope, failure, input, and Pre-Code contracts."
      },
      {
        "increment": "INC-6",
        "text": "Establish mutation admission, 18 negative controls, and adoption evidence."
      },
      {
        "increment": "INC-7",
        "text": "Add deterministic whole-system verification and exact-candidate evidence."
      }
    ]
  },
  "increments": [
    {
      "id": "INC-1",
      "objective": "Establish the single authority root and caller-controlled router.",
      "obligations": [
        "OBL-001",
        "OBL-002"
      ],
      "dependencies": [],
      "files": [
        ".harness/tasks.md",
        "AGENTS.md",
        "CLAUDE.md",
        "CONTEXT.md",
        ".governance/authority.md"
      ],
      "actions": [
        {
          "instruction": "Create the five declared authority and routing files.",
          "postcondition": "Pointer, root authority, caller-controlled route, and line-delta predicates pass."
        }
      ],
      "acceptance_criteria": [
        "Exact CLAUDE pointer",
        "One authority root",
        "One caller-supplied bootstrap route",
        "No agent-inferred domain",
        "At most 500 changed LOC"
      ],
      "verifier": {
        "reference": "INC-1 deterministic predicates",
        "oracle": "All declared predicates true and exit 0",
        "class": "DETERMINISTIC"
      },
      "budgets": {
        "repair_attempts": 2,
        "command_timeout_seconds": 30,
        "increment_timeout_seconds": 300
      },
      "checkpoint": "Authority and routing exist; downstream dependencies remain blocked.",
      "stateful": false,
      "protected_actions": [
        {
          "action": "declared local governance mutations",
          "state": "AUTHORIZED",
          "owner": "user",
          "evidence_ref": "domain and LOC selections plus exact-plan approval"
        }
      ],
      "recovery": null
    },
    {
      "id": "INC-2",
      "objective": "Establish exact source binding, the closed inventory, and execution/evidence controls.",
      "obligations": [
        "OBL-003",
        "OBL-004",
        "OBL-009",
        "OBL-010",
        "OBL-011"
      ],
      "dependencies": [
        "INC-1"
      ],
      "files": [
        ".governance/source-registry.md",
        ".governance/engineering-rules.md",
        ".governance/invariant-inventory.json",
        ".governance/execution.md",
        ".governance/evidence.md"
      ],
      "actions": [
        {
          "instruction": "Create exact source records, the closed 50-record inventory, rule statements, and execution, evidence, security, and proof-boundary controls.",
          "postcondition": "Inventory, source, nonauthority, trust-boundary, proof-boundary, and line-delta predicates pass."
        }
      ],
      "acceptance_criteria": [
        "Exact source bindings",
        "Exactly 50 invariant IDs with six required fields",
        "Only 53 rule statements transferred",
        "Evidence and skills nonauthority",
        "No false enforcement claim",
        "At most 500 changed LOC"
      ],
      "verifier": {
        "reference": "INC-2 deterministic predicates",
        "oracle": "All declared predicates true and exit 0",
        "class": "DETERMINISTIC"
      },
      "budgets": {
        "repair_attempts": 2,
        "command_timeout_seconds": 30,
        "increment_timeout_seconds": 300
      },
      "checkpoint": "Portable requirements are machine-readable; destination remains NOT_ADOPTED.",
      "stateful": false,
      "protected_actions": [
        {
          "action": "declared local governance mutations",
          "state": "AUTHORIZED",
          "owner": "user",
          "evidence_ref": "exact-plan approval"
        }
      ],
      "recovery": null
    },
    {
      "id": "INC-3",
      "objective": "Establish review, verification, completion, portable states, and adoption governance.",
      "obligations": [
        "OBL-005",
        "OBL-007",
        "OBL-010",
        "OBL-012",
        "OBL-014",
        "OBL-015"
      ],
      "dependencies": [
        "INC-2"
      ],
      "files": [
        ".governance/code-review.md",
        ".governance/verification.md",
        ".governance/completion.md",
        ".governance/states.md",
        ".governance/adoption.md"
      ],
      "actions": [
        {
          "instruction": "Create review, exact-head verification, completion, non-escalating state, and adoption policies.",
          "postcondition": "CR, finding-class, judgment-separation, transition, adoption, and line-delta predicates pass."
        }
      ],
      "acceptance_criteria": [
        "CR-01 through CR-14",
        "Google references nonauthoritative before adoption",
        "No automatic merge transition",
        "14 adoption predicates",
        "At most 500 changed LOC"
      ],
      "verifier": {
        "reference": "INC-3 deterministic predicates",
        "oracle": "All declared predicates true and exit 0",
        "class": "DETERMINISTIC"
      },
      "budgets": {
        "repair_attempts": 2,
        "command_timeout_seconds": 30,
        "increment_timeout_seconds": 300
      },
      "checkpoint": "Review and adoption policy exists without granting review, PASS, merge, or implementation authority.",
      "stateful": false,
      "protected_actions": [
        {
          "action": "declared local governance mutations",
          "state": "AUTHORIZED",
          "owner": "user",
          "evidence_ref": "exact-plan approval"
        }
      ],
      "recovery": null
    },
    {
      "id": "INC-4",
      "objective": "Establish the five destination configuration schemas.",
      "obligations": [
        "OBL-006",
        "OBL-010",
        "OBL-012",
        "OBL-013",
        "OBL-015"
      ],
      "dependencies": [
        "INC-3"
      ],
      "files": [
        ".governance/config/ci.schema.json",
        ".governance/config/review.schema.json",
        ".governance/config/branch-protection.schema.json",
        ".governance/config/permitted-effects.schema.json",
        ".governance/config/privileged-boundaries.schema.json"
      ],
      "actions": [
        {
          "instruction": "Create strict schemas for CI, review, branch protection, effects, and privileged boundaries.",
          "postcondition": "All required field, closed-ID, unresolved-value, and line-delta predicates pass."
        }
      ],
      "acceptance_criteria": [
        "No unresolved required value accepted",
        "Three review cycles proposed only",
        "PE-01 through PE-10",
        "PB-01 through PB-10",
        "Empty default capability set",
        "At most 500 changed LOC"
      ],
      "verifier": {
        "reference": "INC-4 deterministic predicates",
        "oracle": "All declared predicates true and exit 0",
        "class": "DETERMINISTIC"
      },
      "budgets": {
        "repair_attempts": 2,
        "command_timeout_seconds": 30,
        "increment_timeout_seconds": 300
      },
      "checkpoint": "Destination adapters are schema-validatable and remain unresolved.",
      "stateful": false,
      "protected_actions": [
        {
          "action": "declared local governance mutations",
          "state": "AUTHORIZED",
          "owner": "user",
          "evidence_ref": "exact-plan approval"
        }
      ],
      "recovery": null
    },
    {
      "id": "INC-5",
      "objective": "Establish route, input, envelope, failure, and Pre-Code contracts.",
      "obligations": [
        "OBL-002",
        "OBL-003",
        "OBL-005",
        "OBL-006",
        "OBL-007"
      ],
      "dependencies": [
        "INC-4"
      ],
      "files": [
        ".harness/route-invariants.md",
        ".harness/task-envelope.schema.json",
        ".harness/blocked-record.schema.json",
        ".harness/input-gates.md",
        ".harness/pre-code-readiness.md"
      ],
      "actions": [
        {
          "instruction": "Create route, seven-field envelope, eight-field BLOCKED, input, and PC-01 through PC-11 contracts.",
          "postcondition": "Schema, route, input, readiness, and line-delta predicates pass."
        }
      ],
      "acceptance_criteria": [
        "Unique route exact",
        "Seven-field envelope exact",
        "Eight-field BLOCKED record exact",
        "PC-01 through PC-11",
        "Wingman 500-LOC gate",
        "At most 500 changed LOC"
      ],
      "verifier": {
        "reference": "INC-5 deterministic predicates",
        "oracle": "All declared predicates true and exit 0",
        "class": "DETERMINISTIC"
      },
      "budgets": {
        "repair_attempts": 2,
        "command_timeout_seconds": 30,
        "increment_timeout_seconds": 300
      },
      "checkpoint": "Routing and Pre-Code readiness are mechanically evaluable.",
      "stateful": false,
      "protected_actions": [
        {
          "action": "declared local governance mutations",
          "state": "AUTHORIZED",
          "owner": "user",
          "evidence_ref": "exact-plan approval"
        }
      ],
      "recovery": null
    },
    {
      "id": "INC-6",
      "objective": "Establish mutation admission, the 18 negative controls, and adoption evidence.",
      "obligations": [
        "OBL-006",
        "OBL-007",
        "OBL-010",
        "OBL-013",
        "OBL-014",
        "OBL-015"
      ],
      "dependencies": [
        "INC-5"
      ],
      "files": [
        ".harness/mutation-gate.md",
        ".harness/contracts/governance-bootstrap.md",
        ".harness/negative-controls.json",
        ".harness/adoption-record.schema.json",
        ".harness/evals.md"
      ],
      "actions": [
        {
          "instruction": "Create mutation, bootstrap, NC-01 through NC-18, adoption-record, and evaluator contracts.",
          "postcondition": "Mutation, negative-control, adoption, and line-delta predicates pass."
        }
      ],
      "acceptance_criteria": [
        "Per-mutation stop recheck",
        "NC-01 through NC-18",
        "Independent rejection evidence",
        "14 adoption predicates",
        "At most 500 changed LOC"
      ],
      "verifier": {
        "reference": "INC-6 deterministic predicates",
        "oracle": "All declared predicates true and exit 0",
        "class": "DETERMINISTIC"
      },
      "budgets": {
        "repair_attempts": 2,
        "command_timeout_seconds": 30,
        "increment_timeout_seconds": 300
      },
      "checkpoint": "Mutation, negative-control, and adoption contracts exist but cannot self-certify.",
      "stateful": false,
      "protected_actions": [
        {
          "action": "declared local governance mutations",
          "state": "AUTHORIZED",
          "owner": "user",
          "evidence_ref": "exact-plan approval"
        }
      ],
      "recovery": null
    },
    {
      "id": "INC-7",
      "objective": "Add deterministic whole-system verification and produce exact-candidate evidence.",
      "obligations": [
        "OBL-001",
        "OBL-002",
        "OBL-003",
        "OBL-004",
        "OBL-005",
        "OBL-006",
        "OBL-007",
        "OBL-008",
        "OBL-009",
        "OBL-010",
        "OBL-011",
        "OBL-012",
        "OBL-013",
        "OBL-014",
        "OBL-015"
      ],
      "dependencies": [
        "INC-6"
      ],
      "files": [
        "scripts/verify-governance.py",
        ".harness/runs/.gitkeep"
      ],
      "actions": [
        {
          "instruction": "Implement and run every declared positive and negative control twice on one unchanged candidate.",
          "postcondition": "All memberships, schemas, denials, transitions, adoption gates, and unchanged-state replay pass."
        }
      ],
      "acceptance_criteria": [
        "All 50 invariants",
        "All 11 Pre-Code gates",
        "PE-01 through PE-10",
        "PB-01 through PB-10",
        "NC-01 through NC-18",
        "All 14 adoption gates",
        "Two unchanged-state passes",
        "At most 500 changed LOC"
      ],
      "verifier": {
        "reference": "python3 scripts/verify-governance.py",
        "oracle": "Exit 0 with every named control PASS twice on unchanged state",
        "class": "DETERMINISTIC"
      },
      "budgets": {
        "repair_attempts": 2,
        "command_timeout_seconds": 60,
        "increment_timeout_seconds": 300
      },
      "checkpoint": "Candidate has deterministic producer evidence; not adopted, accepted, merged, or published.",
      "stateful": false,
      "protected_actions": [
        {
          "action": "declared local verifier and governance mutations",
          "state": "AUTHORIZED",
          "owner": "user",
          "evidence_ref": "exact-plan approval"
        }
      ],
      "recovery": null
    }
  ],
  "publication": {
    "mode": "NONE"
  }
}
```

## Stop conditions

- Caller domain is absent, inferred, altered, combined, or maps to zero or multiple routes.
- Any envelope field is missing, invalid, stale, ambiguous, or unauthorized.
- A required source is absent, stale, mismatched, or resolves more than once.
- Loaded input is not both required and allowed.
- Evidence or a skill is used to create authority.
- The invariant inventory is not the exact closed 50-ID set or any required record field is absent.
- Required CI checks, review limit, branch-protection evidence, permitted effects, or another repository adapter value is unresolved when its gate is invoked.
- A Google review or style rule is treated as governing without exact destination adoption.
- Any `PE-01` through `PE-10`, `PB-01` through `PB-10`, or `NC-01` through `NC-18` record is missing, ambiguous, stale, skipped without approved non-applicability, or unauthorized.
- A fourth review cycle is attempted without new explicit owner authorization.
- A workflow file is presented as proof of provider-enforced branch protection.
- Any of the 14 adoption predicates lacks current independent evidence while the destination claims `ADOPTED` or grants implementation authority.
- CI or review evidence does not bind the exact current implementation head.
- A producer attempts to self-accept or convert technical eligibility into merge authority.
- A repeated repair lacks materially new diagnostic evidence.
- A completion claim implies sandbox, host-capability, verifier-protection, immutable-provenance, or external-evaluation guarantees that this bootstrap did not implement and verify.
- A mandatory lifecycle is introduced without independent governing authority.
- Any `G_PC_01` through `G_PC_11` predicate fails.
- An increment exceeds 500 added-plus-deleted lines.
- A mutation path, effect, precondition, verifier, or stop condition is unauthorized or unresolved.
- The candidate changes between deterministic verifier runs.
- Any protected external action is requested.

## Completion authority

User (Emory Harris) after independent verification of the exact candidate. The producer and deterministic verifier cannot promote or release.
