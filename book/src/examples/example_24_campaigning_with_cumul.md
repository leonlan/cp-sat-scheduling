# 24 - Campaigning with cumul

**Source:** `scheduling/example_24_campaigning_with_cumul.py`

## What it does

Introduces the **cumulative rank** approach to campaigning. One product,
many tasks, a configurable `campaign_size`.

- `var_task_cumul[t]` is a rank in `[0, campaign_size - 1]`.
- `var_task_reach_max[t]` fires when the rank hits the cap.
- On each `t1 -> t2` arc:

  - **Continue campaign** (`reach_max[t1]` false): `end[t1] <= start[t2]`
    and `cumul[t2] == cumul[t1] + 1`.
  - **End campaign** (`reach_max[t1]` true): insert changeover, reset
    `cumul[t2] == 0`.

The circuit uses a node `-1` as the first/last dummy.

The `__main__` block benchmarks solve times over campaign sizes 2 and 3,
plotting scalability.

## Concepts

- [Campaigning](../concepts/campaigning.md) (approach 2: cumulative rank)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_24_campaigning_with_cumul.py}}
```
