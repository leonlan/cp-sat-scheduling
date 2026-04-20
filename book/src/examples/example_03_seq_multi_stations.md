# Multi-station sequence

**Source:** `scheduling/example_03_seq_multi_stations.py`

Scale up to two machines in parallel. The solver now decides both which
machine runs each task and in what order.

Variables split in two levels. `presence[m, t]` is the machine assignment,
one-hot per task via `add_exactly_one`. Task-level `start[t]`, `end[t]`
mirror the chosen machine via `only_enforce_if(presence[m, t])`. Each
machine gets its own `add_circuit`, with self-loop arcs
`[t, t, ~presence[m, t]]` that let a task skip any machine it is not on.
Objective remains makespan plus changeover, with `add_max_equality`
computing the former.

The two-level structure (task-level + machine-task-level) recurs almost
unchanged in every subsequent multi-machine chapter.

## Concepts

- [Circuit and sequencing](../concepts/circuit.md) (multi-machine)
- [Changeover](../concepts/changeover.md) (cost in objective)

## Source

```python
{{#include ../../../scheduling/example_03_seq_multi_stations.py}}
```
