# Shift crossing (fake time unit)

**Source:** `scheduling/example_16_shift_crossing_fake_time_unit.py`

## What it does

Prevents tasks from straddling shift boundaries by inserting a tiny fake
break at each boundary. Every task is required to not overlap those fake
breaks.

```python
var_shift_break_intervals[s, e] = model.new_fixed_size_interval_var(
    start=s, size=e - s, name="shift_edge",
)
for s, e in synthetic_shift_breaks:
    for t in tasks:
        model.add_no_overlap([var_task_intervals[t], var_shift_break_intervals[s, e]])
```

Real breaks are still modeled with `add_cumulative` as usual.

## Concepts

- [Shifts](../concepts/shifts.md) (synthetic break approach)
- [Breaks](../concepts/breaks.md)

## Source

```python
{{#include ../../../scheduling/example_16_shift_crossing_fake_time_unit.py}}
```
