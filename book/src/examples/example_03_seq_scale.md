# Multi-station scale benchmark

**Source:** `scheduling/example_03_seq_scale.py`

## What it does

Benchmark harness of the multi-machine model from 03a. The model is
wrapped in a `model(num_tasks)` function and solved for `num_tasks` in
`[2, 3, ..., 12]`, recording wall-clock solve time and plotting with
matplotlib.

- Uses `solver.parameters.num_search_workers = 8`.
- Still uses the manual `end - start == duration` constraint (no intervals
  yet).
- Objective is `make_span` only; changeover line is commented out.

## Concepts

- [Solver techniques](../concepts/solver-techniques.md) (parallel workers)
- Sets the baseline that [03c](./example_03_seq_scale_Mathieu.md)
  accelerates.

## Source

```python
{{#include ../../../scheduling/example_03_seq_scale.py}}
```
