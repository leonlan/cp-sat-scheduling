# Changeover as event

**Source:** `scheduling/example_08_changeover_as_event.py`

The two earlier changeover approaches - cost in objective, gap in
precedence - both treat the changeover as a number. This chapter promotes
it to a first-class scheduled event: every ordered pair `(t1, t2)` gets
its own optional interval with presence, start, end, and duration.

```python
co_iv[m, t1, t2] = model.new_optional_interval_var(
    co_start[m, t1, t2],
    changeover_time[product_of(t2)],
    co_end[m, t1, t2],
    co_present[m, t1, t2],
    ...
)
```

When `seq[m, t1, t2]` is chosen, the model forces the interval to be
present, sit between the two tasks, and have the right size:

```python
model.add(end[t1] <= co_start[t1, t2]).only_enforce_if(seq[m, t1, t2])
model.add(co_end[t1, t2] <= start[t2]).only_enforce_if(seq[m, t1, t2])
model.add(co_end - co_start == distance).only_enforce_if(seq[m, t1, t2])
model.add(co_present == 1).only_enforce_if(seq[m, t1, t2])
model.add(co_present == 0).only_enforce_if(~seq[m, t1, t2])
```

Why bother with all this? Because once the changeover is an interval, it
can live inside `add_cumulative` just like a task. Need a cleaner that
can only do one changeover at a time across multiple machines? Put the
co-intervals under a shared resource. Not possible with the simpler
formulations.

## Concepts

- [Changeover](../concepts/changeover.md) (approach 3: as event)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_08_changeover_as_event.py}}
```
