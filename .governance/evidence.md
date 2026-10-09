# Evidence governance

Evidence records observations under an exact source, task, run, base, candidate, verifier, toolchain, and environment binding. Evidence never creates a requirement, permission, waiver, route, review acceptance, merge authorization, or release decision.

Classes:

- `OBSERVED`: directly captured result.
- `INFERRED`: reasoned conclusion that is not independent proof.
- `VERIFIED`: result accepted by the designated independent verifier for one exact candidate.

Producer tests and reports remain `OBSERVED`. They cannot self-promote to `VERIFIED`. Any candidate mutation invalidates prior exact-candidate verification.

Required evidence must identify the command or external operation, exit/result state, candidate identity, verifier identity, and evidence reference. Missing, cancelled, inconclusive, skipped without approved non-applicability, stale, mismatched, or agent-forged evidence cannot establish PASS.

Verification records for zero-trust harness claims must be captured and bound outside the implementing agent's control. Until that mechanism exists and is independently proven, the destination remains `NOT_ADOPTED`.
