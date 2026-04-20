# Shift crossing (Mathieu)

**Source:** `scheduling/example_17_shift_crossing_mathieu.py`

## What it does

Alternative to 16. Instead of synthetic breaks, every task is assigned to
exactly one shift, and its start/end are constrained to the shift window:

```python
for t in tasks:
    model.add_exactly_one(presence[s, t] for s in shifts)
    for s in shifts:
        model.add(start[t] >= shift_start[s]).only_enforce_if(presence[s, t])
        model.add(end[t]   <= shift_end[s]  ).only_enforce_if(presence[s, t])
```

The rest of the model (real breaks, cumulative, makespan) is the same as
before.

## Concepts

- [Shifts](../concepts/shifts.md) (explicit shift assignment)

## Source

```python
{{#include ../../../scheduling/example_17_shift_crossing_mathieu.py}}
```
