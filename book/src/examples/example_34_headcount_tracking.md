# Headcount tracking

**Source:** `scheduling/example_34_headcount_tracking.py`

The big-picture chapter on resources. `add_cumulative` works when each
interval's demand is a known constant. But if the demand depends on
state - the task's mode, whether it overlaps a break, which operator is
assigned - you need something more flexible.

Three approaches are benchmarked:

- **Method 0 - native `add_cumulative`.** Fastest when it applies, but
  assumes fixed durations and demands.
- **Method 1 - per-slot start-presence booleans.**
  `var_task_starts_presence[t, i]` fires when task `t` starts at slot
  `i`. A "did a task starting within the last `d` slots cover this
  slot?" indicator (built with `add_max_equality`) lets the duration
  vary per task. Per-time resource variables are the sum.
- **Method 2 - per-slot overlap booleans.** The same information
  encoded via `start <= t < end` booleans for every task-slot pair.

Methods 1 and 2 trade model size for flexibility; the chapter also
ships a small `Variables` dataclass and `extract_solution(...)` helper
that keeps the boilerplate manageable.

## Concepts

- [Resources and cumulative](../concepts/resources.md) (time-varying demand)
- [Breaks](../concepts/breaks.md) (state-dependent duration)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_34_headcount_tracking.py}}
```
