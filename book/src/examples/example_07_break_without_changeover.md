# Break without changeover

**Source:** `scheduling/example_07_break_without_changeover.py`

Time to introduce breaks. Single machine, four identical tasks, and a
fixed break window at `(2, 3)` during which the machine is unavailable.

The trick is to treat the break as just another interval. A
`new_fixed_size_interval_var` is placed at the break window and dropped
into an `add_cumulative(intervals, capacity=1)` alongside the task
intervals. Tasks have nowhere to go during the break and spread around it.

Because all tasks share one product, no changeover logic is needed - a
deliberate simplification to isolate the break mechanic. Two
`add_decision_strategy` calls are thrown in to force the solver to emit
the canonical order `0 1 2 3 4 0`; without them it returns a correct but
oddly permuted sequence.

## Concepts

- [Breaks](../concepts/breaks.md) (approach 1: fixed interval in cumulative)
- [Solver techniques](../concepts/solver-techniques.md) (decision strategies)

## Source

```python
{{#include ../../../scheduling/example_07_break_without_changeover.py}}
```
