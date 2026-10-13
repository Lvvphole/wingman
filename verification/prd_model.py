"""Finite PRD-v0.2 safety model. Does not execute candidate code.

These checks prove properties of this explicit abstraction only.
They do not establish implementation conformance or release acceptance.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass

STATES = ("NEW", "TALKING", "SEEING_EACH_OTHER", "CLOSED")
ACTIVE = frozenset(STATES[:-1])
GOALS = frozenset(("EXPLORATORY", "ONE_TIME_INTIMACY", "RECURRING_CASUAL", "COMMITTED_RELATIONSHIP"))
FAMILIES = frozenset(("RECIPROCITY", "FOLLOW_THROUGH", "INTENT", "INTIMACY_INTEREST", "BOUNDARY"))


@dataclass(frozen=True)
class Edge:
    source: str
    event: str
    target: str
    actor: str
    confirmed: bool = False


def transition(edge: Edge) -> str:
    """Reject transitions without an explicit PRD authorization."""
    if edge.source not in STATES or edge.target not in STATES:
        raise ValueError("UNKNOWN_STATE")
    if edge.actor != "RESOLVER":
        raise ValueError("UNAUTHORIZED_MUTATION")
    if edge.source == edge.target:
        return edge.target
    if edge.source == "NEW" and edge.target == "TALKING":
        if edge.event == "RECIPROCAL_INTERACTION":
            return edge.target
    elif edge.source == "TALKING" and edge.target == "SEEING_EACH_OTHER":
        if edge.event == "CONFIRMED_IN_PERSON_ENCOUNTER":
            return edge.target
    elif edge.source in ACTIVE and edge.target == "CLOSED":
        if edge.event == "VALID_CLOSURE":
            return edge.target
    elif edge.source == "CLOSED" and edge.target in ACTIVE:
        if edge.event == "REOPEN" and edge.confirmed:
            return edge.target
    raise ValueError("UNAUTHORIZED_TRANSITION")


def route_accepted(*, served_model: str, accepted_model: str,
                   served_provider: str, accepted_providers: frozenset[str],
                   zdr: bool, no_training: bool, metadata_complete: bool,
                   route_digest: str, accepted_digest: str) -> bool:
    return (bool(served_model) and served_model == accepted_model
            and served_provider in accepted_providers
            and zdr is True and no_training is True
            and metadata_complete is True and bool(route_digest)
            and route_digest == accepted_digest)


def episode_reusable(*, hash_equal: bool, status: str,
                     validity_current: bool, policy_equal: bool) -> bool:
    return hash_equal and status == "COMPLETED" and validity_current and policy_equal


def effective_capabilities(manifest: frozenset[str], *controls: frozenset[str]) -> frozenset[str]:
    result = manifest
    for control in controls:
        result = result & control
    return result


def may_commit(*, actor: str, deletion_in_progress: bool,
               lease_valid: bool, user_confirmed: bool,
               confirmation_required: bool) -> bool:
    return (actor == "RESOLVER" and not deletion_in_progress and lease_valid
            and (not confirmation_required or user_confirmed))


def model_check() -> dict[str, object]:
    """Explore the finite, explicitly enumerated relationship-state abstraction."""
    edges = (
        Edge("NEW", "RECIPROCAL_INTERACTION", "TALKING", "RESOLVER"),
        Edge("TALKING", "CONFIRMED_IN_PERSON_ENCOUNTER", "SEEING_EACH_OTHER", "RESOLVER"),
        Edge("NEW", "VALID_CLOSURE", "CLOSED", "RESOLVER"),
        Edge("TALKING", "VALID_CLOSURE", "CLOSED", "RESOLVER"),
        Edge("SEEING_EACH_OTHER", "VALID_CLOSURE", "CLOSED", "RESOLVER"),
        *(Edge("CLOSED", "REOPEN", state, "RESOLVER", True) for state in ACTIVE),
    )
    queue = deque([("NEW", ("NEW",))])
    seen = set()
    while queue:
        state, path = queue.popleft()
        if state in seen:
            continue
        seen.add(state)
        for edge in edges:
            if edge.source != state:
                continue
            try:
                target = transition(edge)
            except ValueError as exc:
                return {"result": "REJECTED", "counterexample": list(path) + [edge.target], "error": str(exc)}
            queue.append((target, path + (target,)))
    if seen != set(STATES):
        return {"result": "BLOCKED", "error": "INCOMPLETE_STATE_COVERAGE", "seen": sorted(seen)}
    return {"result": "PASS", "states": len(seen), "edges": len(edges),
            "scope": "ABSTRACT_MODEL_ONLY", "release_authority": False}
