# 27 - Campaigning across products

**Source:** `scheduling/example_27_campaigning_products.py`

## What it does

Extends the cumulative-rank campaigning to **multiple products**.

- `product_change_indicator[t1, t2]` is 1 iff `t1` and `t2` belong to
  different products.
- `var_product_change[t1]` captures whether the arc out of `t1` crosses a
  product boundary.
- `var_reach_campaign_end[t1] >= var_product_change[t1]`: a product
  change forces the campaign to end (and therefore a changeover).
- The `add_max_equality` trick from 26 is used to reset or increment the
  rank under `only_enforce_if(literals[t1, t2])`.
- An optional heuristic locks `cumul[t-1] <= cumul[t]` per product group
  to speed things up.

The `__main__` block prints the expected vs. solver make-span for a
parameter set, making it a small sanity check.

## Concepts

- [Campaigning](../concepts/campaigning.md) (multi-product)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_27_campaigning_products.py}}
```
