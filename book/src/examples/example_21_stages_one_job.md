# 21 - Stages, one job

**Source:** `scheduling/example_21_stages_one_job.py`

## What it does

A single job with three stages. Each stage is a task indexed by
`(job, stage)`.

- `var_job_starts`/`var_job_ends` are the min/max of task starts/ends via
  `AddMinEquality` / `AddMaxEquality`.
- Stage precedence: `end[job, s] <= start[job, s + 1]`.
- Each stage has an interval, and no-overlap is enforced per stage (only
  one job at a time per stage).

## Concepts

- [Multi-stage jobs](../concepts/multi-stage.md)
- [Interval variables](../concepts/intervals.md)
