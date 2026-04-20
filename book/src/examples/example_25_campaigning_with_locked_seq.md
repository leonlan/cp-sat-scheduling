# Campaigning, locked sequence

**Source:** `scheduling/example_25_campaigning_with_locked_seq.py`

## What it does

Same cumulative-rank campaigning as 24, but adds a heuristic that locks
the task order:

```python
for task in tasks:
    if task != 0:
        model.add(var_task_ends[task - 1] <= var_task_starts[task])
```

When tasks happen to be indexed in the desired priority/deadline order,
this can provide a large speed-up without changing the optimum.

## Concepts

- [Campaigning](../concepts/campaigning.md) (task-order heuristic)

## Source

```python
{{#include ../../../scheduling/example_25_campaigning_with_locked_seq.py}}
```
