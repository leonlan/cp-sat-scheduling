# Shift crossing (Mathieu)

**Source:** `scheduling/example_17_shift_crossing_mathieu.py`

Second take on the same shift problem. Instead of a synthetic break at
every boundary, assign each task explicitly to one shift via a one-hot
`presence[shift, task]`. When that presence is true, the task must stay
inside the shift window.

```python
for t in tasks:
    model.add_exactly_one(presence[s, t] for s in shifts)
    for s in shifts:
        model.add(start[t] >= shift_start[s]).only_enforce_if(presence[s, t])
        model.add(end[t]   <= shift_end[s]  ).only_enforce_if(presence[s, t])
```

More variables than the synthetic-break approach, but the assignment is
visible in the solution and easy to extend - per-shift headcount caps,
operator preferences, shift-specific processing times all drop in
naturally.

## Concepts

- [Shifts](../concepts/shifts.md) (explicit shift assignment)

## Source

```python
{{#include ../../../scheduling/example_17_shift_crossing_mathieu.py}}
```
