# Solving by phases

**Source:** `scheduling/example_32_solving_by_phases.py`

Large campaigning models can be slow to find even their first feasible
solution. A pragmatic trick: build the full model once, solve it
repeatedly with a growing `max_time`, and carry each phase's solution
forward as hints to the next.

The chapter ships a small pair of helpers around `model.proto()`:

```python
def get_solutions(model, solver):
    return {v.name: solver.response_proto().solution[i]
            for i, v in enumerate(model.proto().variables)}

def add_hints(model, solution):
    for i, v in enumerate(model.proto().variables):
        if v.name in solution:
            model.proto().solution_hint.vars.append(i)
            model.proto().solution_hint.values.append(solution[v.name])
```

With `model.clear_hints()` between runs, the solver gets a clean warm
start each phase. For hard instances this is often the difference
between "no feasible answer in 10 minutes" and a smooth ramp from
trivial horizon to the full one.

## Concepts

- [Solver techniques](../concepts/solver-techniques.md) (hints, phases)
- [Campaigning](../concepts/campaigning.md)

## Source

```python
{{#include ../../../scheduling/example_32_solving_by_phases.py}}
```
