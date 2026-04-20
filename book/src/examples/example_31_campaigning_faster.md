# Campaigning faster

**Source:** `scheduling/example_31_campaigning_faster.py`

## What it does

A tuned variant of 28 (multi-product, multi-machine campaigning) aiming
for faster solves. The structure is the same; differences are in which
heuristics are enabled and how the constraints are ordered.

It is the natural next step after 28 when experimenting with scalability.

## Concepts

- [Campaigning](../concepts/campaigning.md) (tuning)
- [Solver techniques](../concepts/solver-techniques.md)

## Source

```python
{{#include ../../../scheduling/example_31_campaigning_faster.py}}
```
