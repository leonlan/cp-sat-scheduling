# 02 - Sequence with locked starting product

**Source:** `scheduling/example_02_seq_lock_starting_product.py`

## What it does

Same single-machine model as 01, but the dummy task is given a fixed
"starting product". The changeover table is adjusted so that the arc from
dummy to a task costs zero only when that task's product matches the
starting product.

```python
m_cost = {
    (t1, t2): 0 if task_to_product[t1] == task_to_product[t2]
                 or (task_to_product[t1] == 'dummy'
                     and task_to_product[t2] == starting_product)
              else changeover_time[task_to_product[t2]]
    for (t1, t2) in m
}
```

## Concepts

- [Changeover](../concepts/changeover.md) (starting product)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_02_seq_lock_starting_product.py}}
```
