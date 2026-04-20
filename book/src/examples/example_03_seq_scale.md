# Multi-station scale benchmark

**Source:** `scheduling/example_03_seq_scale.py`

How does the previous chapter's model scale? Wrap it in a function over
`num_tasks`, crank the size up to 12, measure wall time with eight search
workers, plot with matplotlib.

Spoiler: with a manual `end - start == duration` constraint it gets slow
fast. This chapter sets the baseline; the next one shows the fix. The
objective is makespan only - the changeover term is commented out to keep
the experiment clean.

## Concepts

- [Solver techniques](../concepts/solver-techniques.md) (parallel workers)
- Pairs with the [interval-based rewrite](./example_03_seq_scale_Mathieu.md)
  which is orders of magnitude faster.

## Source

```python
{{#include ../../../scheduling/example_03_seq_scale.py}}
```
