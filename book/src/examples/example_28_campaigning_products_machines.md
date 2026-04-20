# Campaigning products x machines

**Source:** `scheduling/example_28_campaigning_products_machines.py`

## What it does

Combines 27 (multi-product campaigning) with the multi-machine structure
from 03.

- Rank, `reach_campaign_end`, and `product_change` booleans become
  indexed by `(machine, task)`.
- Per-machine `add_circuit`, with machine-task presence self-loops.
- Per-machine campaigning rules (continue vs. end campaign) inside each
  circuit's arc constraints.
- Objective is still `make_span`.

## Concepts

- [Campaigning](../concepts/campaigning.md) (multi-product, multi-machine)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_28_campaigning_products_machines.py}}
```
