# Stages, one job

**Source:** `scheduling/example_21_stages_one_job.py`

A job can consist of ordered stages. Think of a bakery batch: prepare,
bake, pack. Each stage uses its own equipment and must follow the
previous one.

Model: tasks are indexed `(job, stage)`. The job's start and end are the
min and max over its stage starts and ends:

```python
model.add_min_equality(job_start[job], [start[job, s] for s in stages])
model.add_max_equality(job_end[job],   [end  [job, s] for s in stages])
```

Stage precedence is a chain of `end[s] <= start[s + 1]`. With only one
job, the per-stage `add_no_overlap` is a no-op here, but the scaffolding
is ready for the next chapter.

## Concepts

- [Multi-stage jobs](../concepts/multi-stage.md)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_21_stages_one_job.py}}
```
