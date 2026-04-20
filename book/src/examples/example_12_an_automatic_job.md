# One automatic job

**Source:** `scheduling/example_12_an_automatic_job.py`

Machines differ in how they consume operator time. Some need the operator
for the whole run; others only for setup, after which the machine runs
itself and the operator can go handle breaks or other jobs.

The model uses two intervals per task. The *full* interval is what shows
up on the Gantt chart. The *setup* interval - a size-1 stub at the task's
start - is what goes into the cumulative alongside breaks:

```python
model.add_cumulative(
    intervals=setup_intervals + break_intervals,
    demands=[1] * (len(tasks) + len(breaks)),
    capacity=1,
)
```

Now breaks can push task *starts*, but once an automatic task has begun
it runs through the break uninterrupted.

## Concepts

- [Breaks](../concepts/breaks.md) (automatic jobs)
- [Resources and cumulative](../concepts/resources.md)

## Source

```python
{{#include ../../../scheduling/example_12_an_automatic_job.py}}
```
