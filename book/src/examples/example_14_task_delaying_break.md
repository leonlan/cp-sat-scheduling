# 14 - Task delaying a break

**Source:** `scheduling/example_14_task_delaying_break.py`

## What it does

When a task runs across a break, its total machine time grows by the
length of the break. This is encoded per time slot:

- `var_task_duration_timeslots[t, i]` = 1 iff task `t` occupies slot `i`.
  Built from two reified booleans, "starts before i" AND "ends after i",
  combined with `AddMultiplicationEquality`.
- `var_task_new_duration[t] = base + sum(is_break[i] * uses[t, i] for i)`
  computes the stretched duration.
- The task interval uses this stretched duration directly.

```python
var_task_intervals[t] = model.NewIntervalVar(
    start[t], new_duration[t], end[t], ...,
)
```

Break intervals are added to `AddCumulative` alongside the task *start*
intervals (since breaks do not preempt an auto-type task once started).

## Concepts

- [Breaks](../concepts/breaks.md) (approach 2: duration stretched)
- [CP-SAT basics](../concepts/cp-sat-basics.md) (reification,
  `AddMultiplicationEquality`)
