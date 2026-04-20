# 08 - Changeover as event

**Source:** `scheduling/example_08_changeover_as_event.py`

## What it does

Promotes the changeover to a first-class scheduled event. For every
ordered pair `(t1, t2)` there is an optional interval with its own start,
end, and presence:

```python
co_iv[m, t1, t2] = model.NewOptionalIntervalVar(
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
model.Add(end[t1] <= co_start[t1, t2]).OnlyEnforceIf(seq[m, t1, t2])
model.Add(co_end[t1, t2] <= start[t2]).OnlyEnforceIf(seq[m, t1, t2])
model.Add(co_end - co_start == distance).OnlyEnforceIf(seq[m, t1, t2])
model.Add(co_present == 1).OnlyEnforceIf(seq[m, t1, t2])
model.Add(co_present == 0).OnlyEnforceIf(seq[m, t1, t2].Not())
```

Because the changeover is now an interval, it can take part in cumulative
constraints (cleaning resource, operator availability, etc.).

## Concepts

- [Changeover](../concepts/changeover.md) (approach 3: as event)
- [Interval variables](../concepts/intervals.md)
