# 33 - Conditional duration via linear domain

**Source:** `scheduling/example_33_conditional_duration_linear_domain.py`

## What it does

A task's duration depends on whether its start falls in a break slot.

- Two domains are built: `domain_break` (start values that overlap a
  break) and `domain_no_break` (safe start values).
- A reified bool `var_task_overlap_break[t]` toggles which domain the
  start must belong to, via `add_linear_expression_in_domain`.
- Under `only_enforce_if`, the task duration is either
  `processing_time` or `processing_time + 1`.
- The interval is built from start/duration/end, so everything downstream
  (no-overlap, cumulative) sees the correct effective duration.

## Concepts

- [Breaks](../concepts/breaks.md) (conditional duration)
- [CP-SAT basics](../concepts/cp-sat-basics.md) (`add_linear_expression_in_domain`)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_33_conditional_duration_linear_domain.py}}
```
