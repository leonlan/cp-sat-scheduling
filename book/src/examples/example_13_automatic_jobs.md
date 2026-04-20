# 13 - Automatic jobs

**Source:** `scheduling/example_13_automatic_jobs.py`

## What it does

Same automatic-task idea as 12, now with two tasks that need to be
sequenced.

- Every task has a full interval plus a size-1 "auto start" interval.
- A circuit with `seq[t1, t2]` booleans orders the tasks; the selected arc
  enforces `end[t1] <= start[t2]`.
- The cumulative uses the auto-start intervals and the break intervals so
  that breaks only block task *starts*.

## Concepts

- [Breaks](../concepts/breaks.md) (automatic jobs)
- [Circuit and sequencing](../concepts/circuit.md)
- [Resources and cumulative](../concepts/resources.md)

## Source

```python
{{#include ../../../scheduling/example_13_automatic_jobs.py}}
```
