# 32 - Solving by phases

**Source:** `scheduling/example_32_solving_by_phases.py`

## What it does

Demonstrates warm-starting CP-SAT across multiple solves of the same
model.

- `create_model(...)` returns a campaigning-with-machines model similar
  to 28.
- A list of `phases` with growing `max_time` is defined.
- For each phase, the model is solved. The resulting solution is read
  back with `get_solutions(model, solver)` and fed as hints to the next
  phase using a custom `add_hints(model, solution)` helper.
- `model.ClearHints()` resets between phases.

This is useful when a large horizon is needed for feasibility but a short
horizon gives a fast starting point.

## Concepts

- [Solver techniques](../concepts/solver-techniques.md) (hints, phases)
- [Campaigning](../concepts/campaigning.md)
