# Route predicates

Let `R` be the registered routes and `E` the caller-supplied task envelope.

`M(E) = {r in R | P_r(E) = true}`

`G_ROUTE_UNIQUE(E) := |M(E)| = 1`

| Match count | Result |
| --- | --- |
| `0` | `BLOCKED/ROUTE_ZERO_MATCH` |
| `1` | Continue to source and envelope validation |
| greater than `1` | `BLOCKED/ROUTE_MULTI_MATCH` |

The executing agent cannot supply, infer, combine, decompose, or substitute `task_domains`. A multi-domain task requires one separately registered composite route. Route success does not grant execution authority.

Current closed route registry: `GOVERNANCE_BOOTSTRAP` only.
