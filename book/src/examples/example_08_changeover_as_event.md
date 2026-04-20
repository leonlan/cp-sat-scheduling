# 08 - Changeover as event

**Source:** `scheduling/example_08_changeover_as_event.py`

## What it does

Promotes the changeover to a first-class scheduled event. For every
ordered pair `(t1, t2)` there is an optional interval with its own start,
end, and presence:

```python
co_iv[m, t1, t2] = model.new_optional_interval_var(
    co_start[m, t1, t2],
    changeover_time[product_of(t2)],
    co_end[m, t1, t2],
    co_present[m, t1, t2],
    ...,
)
```

When `seq[m, t1, t2]` is chosen, the model forces the co interval to be
present, sit between the two tasks, and have the right size:

```python
model.add(end[t1] <= co_start[t1, t2]).only_enforce_if(seq[m, t1, t2])
model.add(co_end[t1, t2] <= start[t2]).only_enforce_if(seq[m, t1, t2])
model.add(co_end - co_start == distance).only_enforce_if(seq[m, t1, t2])
model.add(co_present == 1).only_enforce_if(seq[m, t1, t2])
model.add(co_present == 0).only_enforce_if(~seq[m, t1, t2])
```

Because the changeover is now an interval, it can take part in cumulative
constraints (cleaning resource, operator availability, etc.).

## Concepts

- [Changeover](../concepts/changeover.md) (approach 3: as event)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_08_changeover_as_event.py}}
```
