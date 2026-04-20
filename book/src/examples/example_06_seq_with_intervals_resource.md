# 06 - Sequence with shared resource

**Source:** `scheduling/example_06_seq_with_intervals_resource.py`

## What it does

Extends 05 with a globally shared resource (a single operator). After
building all machine-task intervals, the model adds a single
`add_cumulative` over them:

```python
intervals = list(variables_machine_task_intervals.values())
model.add_cumulative(intervals, [1] * len(intervals), 1)
```

With capacity `1`, the two machines can no longer run tasks in parallel:
the operator has to pick one at a time.

## Concepts

- [Resources and cumulative](../concepts/resources.md) (shared operator)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_06_seq_with_intervals_resource.py}}
```
