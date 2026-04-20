# Breaks

A break is a time window during which a machine or operator is unavailable.
Three techniques cover most cases.

## 1. Break as a fixed interval in `AddCumulative`

For each break, build a `NewFixedSizeIntervalVar` and add it alongside task
intervals with the full demand. Tasks are pushed around the break.

```python
break_intervals = [
    model.NewFixedSizeIntervalVar(start=s, size=e - s, name="break")
    for (s, e) in breaks
]
all_intervals = task_intervals + break_intervals
demands = [1] * len(task_intervals) + [1] * len(break_intervals)
model.AddCumulative(all_intervals, demands, capacity=1)
```

Example: `example_07_break_without_changeover.py`.

## 2. Task duration stretched by overlapping breaks

When a task may run through a break and the break simply extends its total
time on the machine, use per-time-slot booleans that indicate whether the
task uses slot `i`, then add `is_break[i]` for each covered slot.

```python
uses[t, i] = starts_before_i AND ends_after_i
duration[t] = base + sum(is_break[i] * uses[t, i] for i)
interval[t] = NewIntervalVar(start, duration, end, ...)
```

Example: `example_14_task_delaying_break.py`.

## 3. Break-aware start domains

If the break pattern is periodic, restrict task starts to the valid slots
with `AddLinearExpressionInDomain`. Much faster than per-slot booleans.

```python
domain_no_break = cp_model.Domain.FromValues([...])
model.AddLinearExpressionInDomain(start[t], domain_no_break)
```

Example: `example_29_linear_domain_for_breaks.py`,
`example_33_conditional_duration_linear_domain.py`.

## Automatic jobs

Some "automatic" tasks don't consume the operator while running (think: a
machine runs itself after a short manual setup). Model only the setup portion
inside the cumulative, using a 1-unit interval at the task's start.

Example: `example_12_an_automatic_job.py`, `example_13_automatic_jobs.py`.
