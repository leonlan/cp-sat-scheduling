# Stages, two jobs

**Source:** `scheduling/example_22_stages_two_jobs.py`

Add a second job and the previous chapter's scaffolding earns its keep.
Each stage has only one instance of its equipment, so two jobs cannot
sit in the same stage at the same time:

```python
for s in stages:
    model.add_no_overlap([intervals[j, s] for j in jobs])
```

This is the classic flow-shop pattern. The solver now has to interleave
the two jobs across stages such that no stage is double-booked and the
makespan is minimised.

## Concepts

- [Multi-stage jobs](../concepts/multi-stage.md) (stage-level no-overlap)

## Source

```python
{{#include ../../../scheduling/example_22_stages_two_jobs.py}}
```
