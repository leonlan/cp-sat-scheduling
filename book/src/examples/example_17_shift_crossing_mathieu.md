# 17 - Shift crossing (Mathieu)

**Source:** `scheduling/example_17_shift_crossing_mathieu.py`

## What it does

Alternative to 16. Instead of synthetic breaks, every task is assigned to
exactly one shift, and its start/end are constrained to the shift window:

```python
for t in tasks:
    model.AddExactlyOne(presence[s, t] for s in shifts)
    for s in shifts:
        model.Add(start[t] >= shift_start[s]).OnlyEnforceIf(presence[s, t])
        model.Add(end[t]   <= shift_end[s]  ).OnlyEnforceIf(presence[s, t])
```

The rest of the model (real breaks, cumulative, makespan) is the same as
before.

## Concepts

- [Shifts](../concepts/shifts.md) (explicit shift assignment)

## Source

```python
{{#include ../../../scheduling/example_17_shift_crossing_mathieu.py}}
```
