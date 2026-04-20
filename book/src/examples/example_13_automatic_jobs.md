# Automatic jobs

**Source:** `scheduling/example_13_automatic_jobs.py`

Two automatic jobs need an order. The two-interval trick from the
previous chapter carries over: each task has a full interval and a
size-1 setup interval.

A small `add_circuit` with `seq[t1, t2]` booleans picks the order; each
selected arc enforces `end[t1] <= start[t2]`. The cumulative still uses
only the setup intervals and the breaks, so once a task is running no
break can interrupt it.

## Concepts

- [Breaks](../concepts/breaks.md) (automatic jobs)
- [Circuit and sequencing](../concepts/circuit.md)
- [Resources and cumulative](../concepts/resources.md)

## Source

```python
{{#include ../../../scheduling/example_13_automatic_jobs.py}}
```
