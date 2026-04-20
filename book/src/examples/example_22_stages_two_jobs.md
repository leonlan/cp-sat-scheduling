# 22 - Stages, two jobs

**Source:** `scheduling/example_22_stages_two_jobs.py`

## What it does

Extends 21 with a second job. The per-stage `AddNoOverlap` now actually
does work: with two jobs, stage `s` can only run one of them at a time.

Structure is otherwise identical to 21 (min/max for job start/end, stage
precedence, make-span minimisation).

## Concepts

- [Multi-stage jobs](../concepts/multi-stage.md) (stage-level no-overlap)
