# Campaigning across products

**Source:** `scheduling/example_27_campaigning_products.py`

So far every campaigning example has used one product. Real plants run
many. A campaign must now end both when it hits the size cap and
whenever the product changes.

Two extra booleans per task plug the product-change rule into the
cumulative-rank model:

```python
model.add(var_product_change[t1] == product_change_indicator[t1, t2]).only_enforce_if(literals[t1, t2])
model.add(var_reach_campaign_end[t1] >= var_product_change[t1])
```

The first line captures whether the outgoing arc crosses a product
boundary; the second escalates any such crossing into a campaign end,
which in turn forces a changeover via the familiar rank-reset machinery.

An optional per-product order lock (`cumul[t-1] <= cumul[t]`) speeds up
larger instances. The `__main__` block checks the solver's makespan
against a closed-form expected value - a handy sanity test.

## Concepts

- [Campaigning](../concepts/campaigning.md) (multi-product)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_27_campaigning_products.py}}
```
