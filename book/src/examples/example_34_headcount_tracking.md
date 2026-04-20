# 34 - Headcount tracking

**Source:** `scheduling/example_34_headcount_tracking.py`

## What it does

Compares three ways of tracking resource (headcount) usage over time when
task durations are state-dependent (can be 2 or 3 depending on whether
the task overlaps a break).

- **Method 0 - native cumulative.** One `AddCumulative` with the actual
  task intervals.
- **Method 1 - cumulative with start time.** Per-time-slot booleans
  `var_task_starts_presence[t, i]` indicate task start. Per-duration
  "did a task starting within the last `d` slots cover this slot?"
  booleans are combined with `AddMaxEquality`. Per-task, per-time
  resource variables are then switched by `var_task_overlap_break[t]`.
- **Method 2 - cumulative with overlap.** Encodes the same "is this
  slot inside the task?" using per-slot overlap booleans (`start <= t`
  AND `end > t`).

The file also defines a `Variables` dataclass and an
`extract_solution(...)` helper that converts variable dicts into their
solved values, handling `IntervalVar` specially.

## Concepts

- [Resources and cumulative](../concepts/resources.md) (time-varying demand)
- [Breaks](../concepts/breaks.md) (state-dependent duration)
- [Interval variables](../concepts/intervals.md)
