# Interval variables

An interval variable bundles three integer variables - `start`, `size`, `end` -
with the implicit constraint `start + size == end`. CP-SAT uses intervals to
reason efficiently about scheduling: `add_no_overlap` and `add_cumulative` both
expect intervals.

## Three flavors

### Regular interval

```python
iv = model.new_interval_var(start, size, end, name="t1")
```

Replaces a manual `model.add(end - start == size)`.

### Optional interval

An interval that is only scheduled when a presence boolean is true. Essential
when a task may or may not be assigned to a given machine.

```python
iv = model.new_optional_interval_var(start, size, end, is_present, name="t1_on_m1")
```

If `is_present` is false, the interval disappears from `add_no_overlap` /
`add_cumulative` reasoning.

### Fixed-size interval

Convenient for breaks, shift boundaries, and anything with a known position.

```python
br = model.new_fixed_size_interval_var(start=2, size=1, name="break")
```

## Typical use

```python
intervals = {
    (m, t): model.new_optional_interval_var(
        starts[m, t],
        processing_time[product_of(t)],
        ends[m, t],
        presence[m, t],
        f"t{t}_on_m{m}",
    )
    for t in tasks for m in machines
}

for m in machines:
    model.add_no_overlap([intervals[m, t] for t in tasks])
```

Examples that introduce intervals: `example_05_seq_with_intervals.py` (first
use), `example_03_seq_scale_Mathieu.py` (dramatic speed-up vs. manual duration
constraints).
