# 12 - One automatic job

**Source:** `scheduling/example_12_an_automatic_job.py`

## What it does

Models an "automatic" task: one that consumes the operator only for its
first time unit (setup), after which the machine runs on its own.

- `var_task_intervals[t]` is the full task interval (setup + auto run).
- `var_task_intervals_autojobs[t]` is a size-1 interval at
  `(start, start + 1)`, representing only the setup portion.
- Breaks are added as fixed intervals. The cumulative constraint uses the
  *setup* intervals and the breaks:

  ```python
  model.add_cumulative(
      intervals=setup_intervals + break_intervals,
      demands=[1] * (len(tasks) + len(breaks)),
      capacity=1,
  )
  ```

So breaks push task *starts* around but cannot preempt an already-running
automatic task.

## Concepts

- [Breaks](../concepts/breaks.md) (automatic jobs)
- [Resources and cumulative](../concepts/resources.md)

## Source

```python
{{#include ../../../scheduling/example_12_an_automatic_job.py}}
```
