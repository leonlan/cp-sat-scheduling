# Sequence with intervals

**Source:** `scheduling/example_05_seq_with_intervals.py`

Cleanup chapter. Replace the hand-written `model.add(end - start ==
duration)` with a proper `new_optional_interval_var`. Behavior is
identical; the model speaks CP-SAT's native scheduling vocabulary instead.

```python
intervals[m, t] = model.new_optional_interval_var(
    start[m, t], processing_time[product_of(t)], end[m, t],
    presence[m, t], name=f"interval_{m}_{t}",
)
```

A small refactor with big downstream payoff: intervals plug directly into
`add_no_overlap`, `add_cumulative`, and the break machinery you will see
next.

## Concepts

- [Interval variables](../concepts/intervals.md) (first introduction)
- [Changeover](../concepts/changeover.md)

## Source

```python
{{#include ../../../scheduling/example_05_seq_with_intervals.py}}
```
