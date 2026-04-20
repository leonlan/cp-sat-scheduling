# Campaigning, locked sequence

**Source:** `scheduling/example_25_campaigning_with_locked_seq.py`

Same cumulative-rank campaigning, with a single heuristic bolted on:
lock the task order.

```python
for task in tasks:
    if task != 0:
        model.add(var_task_ends[task - 1] <= var_task_starts[task])
```

In practice, task indices often already reflect priority or deadline
order. Telling the solver so upfront prunes a lot of symmetric branches
without changing the optimum. The speed-up can be an order of magnitude.

## Concepts

- [Campaigning](../concepts/campaigning.md) (task-order heuristic)

## Source

```python
{{#include ../../../scheduling/example_25_campaigning_with_locked_seq.py}}
```
