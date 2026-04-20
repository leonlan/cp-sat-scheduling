# 03a - Multi-station sequence

**Source:** `scheduling/example_03_seq_multi_stations.py`

## What it does

Extends the single-machine model of 02 to multiple machines.

- `presence[m, t]` booleans, with `add_exactly_one` per task, select which
  machine runs each task.
- Task-level `start[t]`, `end[t]` are linked to `start[m, t]`, `end[m, t]`
  under `only_enforce_if(presence[m, t])`.
- One `add_circuit` per machine, with a self-loop
  `[t, t, ~presence[m, t]]` to skip tasks assigned elsewhere.
- The objective is `make_span + total_changeover_time`, with
  `add_max_equality` computing the makespan.

## Concepts

- [Circuit and sequencing](../concepts/circuit.md) (multi-machine)
- [Changeover](../concepts/changeover.md) (cost in objective)

## Source

```python
{{#include ../../../scheduling/example_03_seq_multi_stations.py}}
```
