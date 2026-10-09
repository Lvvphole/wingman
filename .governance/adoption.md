# Portable governance adoption

Status: `NOT_ADOPTED`.

The repository can transition to `ADOPTED` only when an independent verifier confirms all predicates below for one exact governance candidate:

- [ ] `AD-01` Current root governance authority is present and bound.
- [ ] `AD-02` Current canonical router is present and bound.
- [ ] `AD-03` Canonical Engineering Rules are read and binding.
- [ ] `AD-04` Caller domain, route, and source bindings are valid.
- [ ] `AD-05` Destination-specific configuration is owner-approved.
- [ ] `AD-06` Applicable CI requirements, checks, and trusted identities are registered.
- [ ] `AD-07` Independent reviewer and maximum cycle limit are owner-approved.
- [ ] `AD-08` Applicable Google language-specific style guides are explicitly adopted and bound.
- [ ] `AD-09` Branch protection is independently verified at the provider boundary.
- [ ] `AD-10` Permitted effects and protected resources are explicit.
- [ ] `AD-11` Privileged boundaries and trusted controller are established with enforcement evidence.
- [ ] `AD-12` Required positive and negative controls are defined.
- [ ] `AD-13` Stop conditions and terminal records are defined.
- [ ] `AD-14` No unresolved authority conflict remains.

An unresolved predicate permits only separately authorized read-only work. This file cannot authorize implementation, relax a gate, approve its own evidence, or modify governance.

The approved Google references must be recorded by exact identity before `AD-08` can pass. General source URLs alone are insufficient adoption evidence.
