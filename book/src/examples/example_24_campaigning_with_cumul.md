# Campaigning with cumul

**Source:** `scheduling/example_24_campaigning_with_cumul.py`

The [campaigns-as-entities](./example_09_max_number_of_continuous_tasks.md)
model works, but it creates a lot of variables. This chapter introduces
the compact alternative: keep tasks as the atomic unit and attach a
*rank* variable `cumul[t] in [0, campaign_size - 1]`.

On each `t1 -> t2` arc the model branches on `reach_max[t1]`:

- **Campaign continues** (`reach_max[t1]` false): `end[t1] <= start[t2]`
  and `cumul[t2] == cumul[t1] + 1`.
- **Campaign ends** (`reach_max[t1]` true): a changeover is inserted and
  `cumul[t2] = 0` resets the rank.

The circuit uses `-1` as the first/last dummy node. The `__main__` block
benchmarks solve time at campaign sizes 2 and 3, showing the approach
scales better than the entity model.

## Concepts

- [Campaigning](../concepts/campaigning.md) (approach 2: cumulative rank)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_24_campaigning_with_cumul.py}}
```
