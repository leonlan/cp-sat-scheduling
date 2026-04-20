# Resources and cumulative

`AddNoOverlap` says "at most one interval at a time". `AddCumulative` is the
generalisation: each interval consumes some amount of a shared resource, and
the total consumption must not exceed a capacity.

## No-overlap

```python
model.AddNoOverlap(intervals)
```

Used per machine (one task at a time) and per stage (one job at a time in a
flow-shop style).

## Cumulative

```python
model.AddCumulative(intervals, demands, capacity)
```

`demands[i]` is the amount of resource taken by `intervals[i]` while it runs.
Typical uses:

- **Shared operator across machines.** If two machines need the same operator,
  cumulative over all their task intervals with demand `1` and capacity `1`
  forbids parallel runs. Example: `example_06_seq_with_intervals_resource.py`.
- **Breaks.** Treat a break as an interval that fully occupies the resource.
  Example: `example_07_break_without_changeover.py`.
- **Automatic jobs.** Only the setup portion consumes the operator, modeled as
  a size-1 interval at each task's start.

## Resource modes

Some tasks can run in different modes with different durations and
headcounts. Encode the choice with a one-hot bool per mode and derive the
actual processing time from it:

```python
for t in tasks:
    model.AddExactlyOne([mode[t, k] for k in modes])
    model.Add(
        proc_time[t] == sum(processing_time[product[t], k] * mode[t, k] for k in modes)
    )
```

Example: `example_10_people_mode.py`.

## Headcount tracking

If the per-task resource depends on whether the task overlaps a break (or
some other condition), plain `AddCumulative` may be insufficient. Build an
explicit per-timestep resource variable and link it to task-start presence
booleans. Three methods are compared in
`example_34_headcount_tracking.py`.
