# Multi-station scale (intervals)

**Source:** `scheduling/example_03_seq_scale_Mathieu.py`

Same benchmark as the previous chapter, but the duration constraint is
replaced with `new_optional_interval_var` plus per-machine
`add_no_overlap`. CP-SAT's scheduling engine propagates on intervals far
more effectively than on generic integer constraints, and the speed-up is
dramatic: the same hardware that topped out around 12 tasks now handles
~80.

The per-machine circuit is factored into `add_circuit_constraints(...)`
so the main loop stays readable. That helper is the template for every
later multi-machine model.

## Concepts

- [Interval variables](../concepts/intervals.md) (optional intervals)
- [Circuit and sequencing](../concepts/circuit.md) (factored helper)
- [Solver techniques](../concepts/solver-techniques.md) (parallel workers)

## Source

```python
{{#include ../../../scheduling/example_03_seq_scale_Mathieu.py}}
```
