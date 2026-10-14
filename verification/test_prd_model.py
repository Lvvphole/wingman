import itertools
import unittest
from verification.prd_model import ACTIVE, Edge, STATES, transition, route_accepted, episode_reusable, effective_capabilities, intimacy_action_feasible, may_commit, model_check

class PRDModelTests(unittest.TestCase):
    def test_model(self):
        self.assertEqual(model_check()["result"], "PASS")

    def test_transition_matrix(self):
        for source, target, event in itertools.product(STATES, STATES, ("RECIPROCAL_INTERACTION", "CONFIRMED_IN_PERSON_ENCOUNTER", "VALID_CLOSURE", "REOPEN", "INTIMACY")):
            if source == target:
                continue
            allowed = ((source, target, event) in {
                ("NEW", "TALKING", "RECIPROCAL_INTERACTION"),
                ("TALKING", "SEEING_EACH_OTHER", "CONFIRMED_IN_PERSON_ENCOUNTER"),
                *((s, "CLOSED", "VALID_CLOSURE") for s in ACTIVE),
            })
            edge = Edge(source, event, target, "RESOLVER")
            if allowed:
                self.assertEqual(transition(edge), target)
            else:
                with self.assertRaises(ValueError):
                    transition(edge)

    def test_no_unapproved_self_transitions(self):
        for state in STATES:
            for event in ("RECIPROCAL_INTERACTION", "VALID_CLOSURE", "INTIMACY", "GOAL_CHANGE"):
                with self.subTest(state=state, event=event), self.assertRaisesRegex(ValueError, "UNAUTHORIZED_TRANSITION"):
                    transition(Edge(state, event, state, "RESOLVER"))

    def test_reopen_confirmation_and_actor(self):
        for target in ACTIVE:
            with self.assertRaises(ValueError):
                transition(Edge("CLOSED", "REOPEN", target, "RESOLVER"))
            self.assertEqual(transition(Edge("CLOSED", "REOPEN", target, "RESOLVER", True)), target)
        for actor in ("USER", "JEV", "WINGMAN", "OPTIMIZER", "VERIFIER", "EVE"):
            with self.assertRaises(ValueError):
                transition(Edge("NEW", "RECIPROCAL_INTERACTION", "TALKING", actor))

    def test_route_mutation_controls(self):
        valid = dict(served_model="m", accepted_model="m", served_provider="p", accepted_providers=frozenset({"p"}), zdr=True, no_training=True, metadata_complete=True, route_digest="d", accepted_digest="d", gateway_bypassed=False)
        self.assertTrue(route_accepted(**valid))
        for key, value in dict(served_model="x", served_provider="x", zdr=False, no_training=False, metadata_complete=False, route_digest="x", gateway_bypassed=True).items():
            self.assertFalse(route_accepted(**{**valid, key: value}), key)

    def test_reuse_truth_table(self):
        for a, b, c in itertools.product((False, True), repeat=3):
            for status in ("COMPLETED", "PENDING", "FAILED"):
                self.assertEqual(episode_reusable(hash_equal=a, status=status, validity_current=b, policy_equal=c), a and b and c and status == "COMPLETED")

    def test_capability_subset(self):
        manifest = frozenset({"PLAY", "BLACK_BOOK"})
        for control in (frozenset({"PLAY", "EVE"}), frozenset({"EVE"}), frozenset()):
            self.assertLessEqual(effective_capabilities(manifest, control), manifest)

    def test_commit_truth_table(self):
        for actor, deletion, lease, confirmed, required in itertools.product(("RESOLVER", "JEV"), (False, True), (False, True), (False, True), (False, True)):
            expected = actor == "RESOLVER" and not deletion and lease and (not required or confirmed)
            self.assertEqual(may_commit(actor=actor, deletion_in_progress=deletion, lease_valid=lease, user_confirmed=confirmed, confirmation_required=required), expected)

    def test_intimacy_requires_current_consent_and_clear_boundary(self):
        for current_consent, boundary_blocked in itertools.product((False, True), repeat=2):
            expected = current_consent and not boundary_blocked
            self.assertEqual(intimacy_action_feasible(current_consent=current_consent, boundary_blocked=boundary_blocked), expected)

if __name__ == "__main__":
    unittest.main()
