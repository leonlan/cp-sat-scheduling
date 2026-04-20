# Sequence with locked starting product

**Source:** `scheduling/example_02_seq_lock_starting_product.py`

A machine rarely starts empty. Usually some product is already loaded, and
if the first task happens to be that same product no changeover is needed.

The model is identical to the previous chapter with one change: the
changeover table depends on the machine's starting product. From the dummy
task, going to a task of the starting product is free; going to any other
product costs the regular changeover.

```python
m_cost = {
    (t1, t2): 0 if task_to_product[t1] == task_to_product[t2]
                 or (task_to_product[t1] == 'dummy'
                     and task_to_product[t2] == starting_product)
              else changeover_time[task_to_product[t2]]
    for (t1, t2) in m
}
```

This small tweak is the template for every "initial state" extension later
in the book.

## Concepts

- [Changeover](../concepts/changeover.md) (starting product)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_02_seq_lock_starting_product.py}}
```
