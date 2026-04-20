# Shifts

A shift is a working window. Tasks must fit inside one shift (or, depending on
policy, be split / disallowed from crossing shifts).

## Synthetic shift breaks

Insert a tiny "fake break" interval at each shift boundary and forbid any
task from overlapping it with `add_no_overlap`. This prevents shift-crossing
without enumerating shift assignments.

```python
for (s, e) in synthetic_shift_breaks:
    br = model.new_fixed_size_interval_var(start=s, size=e - s, name="shift_edge")
    for t in tasks:
        model.add_no_overlap([task_interval[t], br])
```

Example: `example_16_shift_crossing_fake_time_unit.py`.

## Explicit shift assignment

Alternatively, give every task a one-hot `presence[shift, task]` and enforce
the shift window when present:

```python
for t in tasks:
    model.add_exactly_one(presence[s, t] for s in shifts)
    for s in shifts:
        model.add(start[t] >= shift_start[s]).only_enforce_if(presence[s, t])
        model.add(end[t]   <= shift_end[s]  ).only_enforce_if(presence[s, t])
```

More variables, but the assignment is explicit and easy to extend (e.g. to
per-shift capacity).

Example: `example_17_shift_crossing_mathieu.py`.
