# Multistage, two jobs

**Source:** `scheduling/example_23_multistage_two_jobs_co.py`

## What it does

Scales the multi-stage model of 22 up to 6 jobs over 3 stages. The model
is identical in shape: stage precedence, per-stage no-overlap,
`add_max_equality` for makespan, `Minimize(make_span)`.

Despite the filename mentioning `co` (changeover), this version does not
actually add a changeover constraint; it is a scalability exercise.

## Concepts

- [Multi-stage jobs](../concepts/multi-stage.md)

## Source

```python
{{#include ../../../scheduling/example_23_multistage_two_jobs_co.py}}
```
