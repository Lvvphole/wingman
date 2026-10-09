# Pre-Code Readiness Gate

`G_PRE_CODE_READY := AND(PC-01..PC-11)`

Every predicate must be true before protected mutation. Missing evidence is `BLOCKED`; a deterministically false predicate is `FAIL` for engineering evaluation and cannot authorize continuation.

| ID | Required predicate | Required evidence | Failure |
| --- | --- | --- | --- |
| `PC-01` | Current root `AGENTS.md` read | authority identity and read record | `BLOCKED/ROOT_AUTHORITY_UNREAD` |
| `PC-02` | Current root `CONTEXT.md` read | router identity and read record | `BLOCKED/ROUTER_UNREAD` |
| `PC-03` | Exactly one route resolved | caller selector and route result | `BLOCKED/ROUTE_NOT_UNIQUE` |
| `PC-04` | Canonical Engineering Rules read | rule identity and read record | `BLOCKED/ENGINEERING_RULES_UNREAD` |
| `PC-05` | Exact routed governing sources read | section and binding ledger | `BLOCKED/ROUTED_SOURCE_UNREAD` |
| `PC-06` | Observable defect or gap verified | bound gap evidence | `BLOCKED/GAP_UNVERIFIED` |
| `PC-07` | Exact path and effect scope established | authorized scope record | `BLOCKED/SCOPE_UNRESOLVED` |
| `PC-08` | Deterministic verifier or explicit blocked condition defined | verifier identity and oracle | `BLOCKED/VERIFIER_UNDEFINED` |
| `PC-09` | Immediate stop condition defined | stop predicate | `BLOCKED/STOP_UNDEFINED` |
| `PC-10` | All authority conflicts resolved | precedence result | `BLOCKED/AUTHORITY_CONFLICT` |
| `PC-11` | Approved change-size gate satisfied | added-plus-deleted line count at most 500 or verified owner exception | `BLOCKED/CHANGE_SIZE` |

Before each mutation, record the verified gap, governing rule, required evidence, exact next permitted action, and stop condition. A prior mutation record cannot authorize a later mutation.
