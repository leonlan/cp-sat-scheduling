# Conditional duration via linear domain

**Source:** `scheduling/example_33_conditional_duration_linear_domain.py`

Combines the ideas of two earlier chapters. Like
[Task delaying a break](./example_14_task_delaying_break.md), a task
that hits a break takes longer. Like
[Linear domain for breaks](./example_29_linear_domain_for_breaks.md),
the break pattern is periodic enough to encode as start-time domains.

Two start domains are precomputed: `domain_break` (starts that would
overlap a break) and `domain_no_break` (safe starts). A reified bool
`overlap_break[t]` toggles which domain the start belongs to, and the
duration switches by one time unit accordingly:

```python
model.add(duration[t] == processing_time + 1).only_enforce_if(overlap_break[t])
model.add(duration[t] == processing_time    ).only_enforce_if(~overlap_break[t])
```

Because the task interval is built from start/duration/end, everything
downstream - no-overlap, cumulative, makespan - sees the correct
effective duration with no extra bookkeeping.

## Concepts

- [Breaks](../concepts/breaks.md) (conditional duration)
- [CP-SAT basics](../concepts/cp-sat-basics.md) (`add_linear_expression_in_domain`)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_33_conditional_duration_linear_domain.py}}
```
