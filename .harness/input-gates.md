# Input and discovery gates

## Required inputs

`G_REQUIRED_INPUTS := I_required subset_of I_loaded`

Every routed required input must be loaded. A missing required input returns `BLOCKED/REQUIRED_INPUT_MISSING`.

## Allowed inputs

`G_ALLOWED_INPUTS := I_loaded subset_of I_allowed`

Every loaded input must be selected by the route and envelope. An unrelated or extra input returns `BLOCKED/INPUT_NOT_ALLOWED`.

## Source integrity

`G_SOURCE_PRESENT := AND(s in S_routed, exists(s) AND resolution_count(s) = 1 AND bindingValid(s))`

Missing, duplicate, stale, ambiguous, or mismatched sources return `BLOCKED/SOURCE_BINDING`.

## Discovery

`G_DISCOVERY := caller_domain_present AND trusted_binding AND bounded_reads AND no_mutation`

Pre-envelope discovery can only localize declared source and path identities. It cannot execute a workpiece, mutate a repository, load content beyond the locator need, grant authority, choose a route, or establish readiness. A violation returns `BLOCKED/DISCOVERY_MUTATION` or `BLOCKED/CONTEXT_OVERREAD`.

## Evidence

Evidence can satisfy an observation requirement only when selected, current, and bound. It cannot create authority or alter a requirement.
