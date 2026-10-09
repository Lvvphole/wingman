# Engineering admission states

These values belong only to `engineering_admission_state`:

| State | Meaning |
| --- | --- |
| `READY` | Prerequisites for the next authorized action are satisfied |
| `BLOCKED` | Required authority, evidence, configuration, or verification is absent or invalid |
| `FAIL` | An executed check proves a requirement violation |
| `STOP` | A governing terminal condition is reached |
| `REDUCE` | Scope must narrow under existing authority |
| `REDESIGN` | Approach requires governing reconsideration |
| `VERIFIED` | Applicable independent verification succeeded for one exact candidate |
| `REVIEW_ACCEPTED` | Required independent review is complete and current |
| `MERGE_ELIGIBLE` | All merge prerequisites except separately exercised merge authorization are satisfied |

## Allowed transitions

| From | To | Required predicate |
| --- | --- | --- |
| Initial or re-evaluation | `READY` | All prerequisites for one exact next action pass |
| Any non-terminal state | `BLOCKED` | Required input is absent, invalid, stale, ambiguous, or unauthorized |
| `READY` | `FAIL` | An executed required check proves violation |
| `READY` | `STOP` | A governing terminal condition fires |
| `READY` | `REDUCE` | Current scope exceeds authority or reviewability |
| `READY` | `REDESIGN` | Authorized approach is invalidated and requires a new decision |
| `READY` | `VERIFIED` | Independent verification passes on exact candidate |
| `VERIFIED` | `REVIEW_ACCEPTED` | Independent current review has zero unresolved actionable findings |
| `REVIEW_ACCEPTED` | `MERGE_ELIGIBLE` | CI, review, protection, and all non-merge prerequisites pass |

Any mutation after `VERIFIED`, `REVIEW_ACCEPTED`, or `MERGE_ELIGIBLE` transitions to `BLOCKED` until exact-candidate verification and applicable review run again. No state transitions to an actual merge automatically.
