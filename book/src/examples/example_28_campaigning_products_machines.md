# Campaigning products x machines

**Source:** `scheduling/example_28_campaigning_products_machines.py`

The last two layers of complexity combine here: multi-product
campaigning runs on multiple machines in parallel. Rank,
`reach_campaign_end`, and `product_change` booleans are all indexed by
`(machine, task)`. Per-machine `add_circuit` with presence self-loops,
per-machine campaigning rules inside each arc.

This is the most structurally involved CP-SAT model in the book and a
good reference for assembling the earlier pieces - presence booleans,
per-machine circuits, cumulative-rank campaigning, product-change
reification - into one coherent model.

## Concepts

- [Campaigning](../concepts/campaigning.md) (multi-product, multi-machine)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_28_campaigning_products_machines.py}}
```
