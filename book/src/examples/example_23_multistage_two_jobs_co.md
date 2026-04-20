# Multistage, two jobs

**Source:** `scheduling/example_23_multistage_two_jobs_co.py`

Same flow-shop model scaled to 6 jobs over 3 stages. No new mechanics -
stage precedence, per-stage no-overlap, makespan objective - just more
of everything. It exists to check how CP-SAT handles a realistic-sized
flow-shop instance.

Despite the `co` suffix in the filename, no explicit changeover is
added; treat it as a scalability exercise.

## Concepts

- [Multi-stage jobs](../concepts/multi-stage.md)

## Source

```python
{{#include ../../../scheduling/example_23_multistage_two_jobs_co.py}}
```
