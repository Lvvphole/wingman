# Mutation admission

For proposed mutation `m`:

`G_MUTATION(m) := path(m) in P AND effect(m) in A AND AND(Preconditions(m))`

Admission also requires `G_PRE_CODE_READY`, a deterministic verifier or explicit `BLOCKED` condition, and an immediate stop condition.

## Per-mutation record

Before each mutation record:

- verified defect, approved requirement, or Definition of Done remainder;
- applicable governing rule;
- required evidence;
- exact path and effect;
- exact next permitted action;
- preconditions;
- verifier and oracle;
- immediate stop condition.

After each mutation, record the observed effect and re-evaluate path, effect, preconditions, current bindings, verifier, and stop condition. A previous record cannot authorize the next mutation.

## Failure

An unauthorized path or effect, missing precondition, absent verifier, absent stop, stale binding, size violation, or protected action returns a schema-valid `BLOCKED` result. No fallback route or speculative continuation is permitted.
