# Shift crossing (fake time unit)

**Source:** `scheduling/example_16_shift_crossing_fake_time_unit.py`

The working day is split into shifts. A task is allowed to run entirely
inside one shift, but not straddle a boundary.

The first approach borrows the break mechanic. Place a one-unit "fake
break" interval at each shift boundary, then forbid every task from
overlapping it:

```python
for s, e in synthetic_shift_breaks:
    br = model.new_fixed_size_interval_var(start=s, size=e - s, name="shift_edge")
    for t in tasks:
        model.add_no_overlap([task_interval[t], br])
```

Concise and scales well. Real breaks continue to use `add_cumulative`.
Compare with the [explicit shift-assignment](./example_17_shift_crossing_mathieu.md)
alternative next.

## Concepts

- [Shifts](../concepts/shifts.md) (synthetic break approach)
- [Breaks](../concepts/breaks.md)

## Source

```python
{{#include ../../../scheduling/example_16_shift_crossing_fake_time_unit.py}}
```
