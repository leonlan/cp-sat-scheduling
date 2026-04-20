# Campaigning faster

**Source:** `scheduling/example_31_campaigning_faster.py`

Tuned companion to the multi-product, multi-machine chapter. Same
problem, same model skeleton; what changes is which heuristics are on,
how the constraints are ordered, and a few implementation shortcuts.

Treat this as the "after tuning" version: when the earlier model starts
to struggle on larger instances, walk through the differences here to
see which levers were pulled.

## Concepts

- [Campaigning](../concepts/campaigning.md) (tuning)
- [Solver techniques](../concepts/solver-techniques.md)

## Source

```python
{{#include ../../../scheduling/example_31_campaigning_faster.py}}
```
