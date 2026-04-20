# Shifts

A shift is a working window. Tasks must fit inside one shift (or, depending on
policy, be split / disallowed from crossing shifts).

## Synthetic shift breaks

Insert a tiny "fake break" interval at each shift boundary and forbid any
task from overlapping it with `AddNoOverlap`. This prevents shift-crossing
without enumerating shift assignments.

```python
for (s, e) in synthetic_shift_breaks:
    br = model.NewFixedSizeIntervalVar(start=s, size=e - s, name="shift_edge")
    for t in tasks:
        model.AddNoOverlap([task_interval[t], br])
```

Example: `example_16_shift_crossing_fake_time_unit.py`.

## Explicit shift assignment

Alternatively, give every task a one-hot `presence[shift, task]` and enforce
the shift window when present:

```python
for t in tasks:
    model.AddExactlyOne(presence[s, t] for s in shifts)
    for s in shifts:
        model.Add(start[t] >= shift_start[s]).OnlyEnforceIf(presence[s, t])
        model.Add(end[t]   <= shift_end[s]  ).OnlyEnforceIf(presence[s, t])
```

More variables, but the assignment is explicit and easy to extend (e.g. to
per-shift capacity).

Example: `example_17_shift_crossing_mathieu.py`.
