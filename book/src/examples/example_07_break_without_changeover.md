# 07 - Break without changeover

**Source:** `scheduling/example_07_break_without_changeover.py`

## What it does

Single machine, four same-product tasks, and a fixed break at `(2, 3)`.

- The break is a `NewFixedSizeIntervalVar` added to an `AddCumulative(
  intervals, capacity=1)` alongside task intervals, so tasks are pushed
  around it.
- Since all tasks share one product, no changeover logic is needed.
- Two `AddDecisionStrategy` calls (on starts and on sequence literals) are
  used to force the solver to produce the canonical `0 1 2 3 4 0` order
  instead of a symmetric alternative.

## Concepts

- [Breaks](../concepts/breaks.md) (approach 1: fixed interval in cumulative)
- [Solver techniques](../concepts/solver-techniques.md) (decision strategies)
