# Solver techniques

Beyond modeling, CP-SAT exposes a few knobs that help on hard instances.

## Decision strategies

Tell the solver which variables to branch on first, and which value to try
first. Often needed when a symmetric model returns a "correct but ugly"
schedule.

```python
model.add_decision_strategy(
    starts.values(),
    cp_model.CHOOSE_FIRST,
    cp_model.SELECT_MIN_VALUE,
)
```

Example: `example_07_break_without_changeover.py` applies two strategies
(one on starts, one on sequence literals) to get a canonical output.

## Parallel workers

```python
solver.parameters.num_search_workers = 8
```

Uses `N` worker threads. Examples `example_03_seq_scale*.py` benchmark the
resulting speedup.

## Warm-starting with hints

You can seed the search with values for any subset of variables:

```python
model.proto().solution_hint.vars.append(var_index)
model.proto().solution_hint.values.append(value)
```

Or clear and re-set them between solves:

```python
model.clear_hints()
add_hints(model, previous_solution)
```

This is the basis of *phase solving*: build the full model once, then run it
repeatedly with an increasing `max_time`, feeding each phase's solution in
as hints to the next. Example: `example_32_solving_by_phases.py`.

## Reading back values

```python
status = solver.solve(model)
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(solver.value(var))
    print(solver.objective_value())
```

`MODEL_INVALID` almost always means a constraint references a variable that
was never bound to the right model instance, or an `only_enforce_if` was
attached to something that is not a literal.
