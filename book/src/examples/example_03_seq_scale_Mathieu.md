# 03c - Multi-station scale (intervals)

**Source:** `scheduling/example_03_seq_scale_Mathieu.py`

## What it does

Same benchmark as 03b, but switches to `NewOptionalIntervalVar` plus
`AddNoOverlap` per machine. A helper `add_circuit_constraints(...)`
factors out the per-machine circuit.

The interval-based model scales much better: the main loop here runs
`num_tasks` up to ~80 on the same hardware that 03b handled only up to 12.

## Concepts

- [Interval variables](../concepts/intervals.md) (optional intervals)
- [Circuit and sequencing](../concepts/circuit.md) (factored helper)
- [Solver techniques](../concepts/solver-techniques.md) (parallel workers)

## Source

```python
{{#include ../../../scheduling/example_03_seq_scale_Mathieu.py}}
```
