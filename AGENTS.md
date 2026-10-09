# AGENTS.md

The authenticated owner is the ultimate repository authority. Current owner instructions override repository-local rules. See `.governance/authority.md`.

## Route
- Use the caller-selected route in `CONTEXT.md`; never infer or combine task domains.
- Load only its exact `.harness/contracts/` contract and admitted context. Engineering Rules binding lives in `.governance/authority.md`.

## Pre-Code
Before any action that can generate or modify code, tests, schemas,
migrations, build logic, or harness logic, read the canonical
engineering-rules document from its authoritative location.

Do not generate or mutate code until the engineering-rules
Pre-Code Readiness Gate is satisfied.

## Work units
Every `INC-*` or `SPRINT-*` follows isolated worktree and branch → PR → green exact-head `PR Verification` → Codex review. Details: `.harness/runtime-loop.md`.

## Finish
Verify under `.governance/verification.md`, bind `.governance/evidence.md`, and decide through `.governance/completion.md`; review never authorizes merge.
Exact standalone owner response `Approved` executes the immediately preceding bounded proposal under `.governance/authority.md`.
