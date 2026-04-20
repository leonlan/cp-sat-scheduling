# 05 - Sequence with intervals

**Source:** `scheduling/example_05_seq_with_intervals.py`

## What it does

Same setup as 04, but replaces the manual duration constraint
`end - start == duration` with `new_optional_interval_var`:

```python
variables_machine_task_intervals[m, t] = model.new_optional_interval_var(
    start[m, t], processing_time[product_of(t)], end[m, t],
    presence[m, t], name=f"interval_{m}_{t}",
)
```

The changeover is still encoded as `end[t1] + distance <= start[t2]`
under `only_enforce_if(seq[m, t1, t2])`.

## Concepts

- [Interval variables](../concepts/intervals.md) (first introduction)
- [Changeover](../concepts/changeover.md)

## Source

```python
{{#include ../../../scheduling/example_05_seq_with_intervals.py}}
```
