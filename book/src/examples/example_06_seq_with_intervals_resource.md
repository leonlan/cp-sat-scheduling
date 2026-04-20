# Sequence with shared resource

**Source:** `scheduling/example_06_seq_with_intervals_resource.py`

Two machines, one operator. Even though the machines themselves could run
in parallel, the human can only be in one place at a time.

Now that tasks are intervals, one line expresses the constraint:

```python
intervals = list(variables_machine_task_intervals.values())
model.add_cumulative(intervals, [1] * len(intervals), 1)
```

With capacity 1 across all machine intervals, CP-SAT stops issuing
parallel schedules. This is the first time we see `add_cumulative` doing
real work, and it is the pattern that all later resource and break
constraints build on.

## Concepts

- [Resources and cumulative](../concepts/resources.md) (shared operator)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_06_seq_with_intervals_resource.py}}
```
