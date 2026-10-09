# Governance evaluations

The deterministic verifier must evaluate these closed suites:

1. Structure: one root authority, exact Claude pointer, one router, declared files.
2. Routing: caller origin, zero match, one match, multi-match, no inferred or composite route.
3. Envelope: exactly seven fields; every omission and unknown field rejects.
4. Sources and inputs: exact resolution, binding currentness, required subset, allowed superset, bounded discovery.
5. Inventory: exact 50 IDs and six fields per record.
6. Engineering admission: exact 53 rules and PC-01 through PC-11.
7. Configuration: strict CI, review, branch-protection, PE-01 through PE-10, and PB-01 through PB-10 schemas.
8. Review and states: CR-01 through CR-14, independent judgment boundary, exact-head evidence, no automatic merge.
9. Negative controls: NC-01 through NC-18 with exact rejection and independently captured evidence requirement.
10. Adoption: exact AD-01 through AD-14; absent independent evidence preserves NOT_ADOPTED.
11. Mutation: path, effect, preconditions, size, verifier, stop, and post-mutation recheck.
12. Proof boundary: no claim of sandbox, capability suppression, immutable provenance, external verification, adoption, acceptance, merge, or release without independent evidence.
13. Determinism: two runs on one unchanged candidate return identical structured results.

A test must contain a meaningful oracle. Missing, skipped, inconclusive, stale, or self-authored acceptance evidence cannot PASS.
