# Multi-stage jobs

A job can consist of several stages that must run in order. Each stage is a
task with its own start/end; the job start is the earliest task start and the
job end is the latest task end.

## Job - stage - task structure

```python
tasks = {(job, stage) for job in jobs for stage in stages}

for job in jobs:
    model.AddMinEquality(job_start[job], [start[job, s] for s in stages])
    model.AddMaxEquality(job_end[job],   [end  [job, s] for s in stages])

    # stage precedence
    for s in sorted(stages)[:-1]:
        model.Add(end[job, s] <= start[job, s + 1])
```

Example: `example_21_stages_one_job.py`.

## Stage-level no-overlap

If each stage has a single shared machine, forbid two jobs from sitting on
the same stage simultaneously:

```python
for s in stages:
    model.AddNoOverlap([intervals[job, s] for job in jobs])
```

Examples: `example_22_stages_two_jobs.py`,
`example_23_multistage_two_jobs_co.py`.
