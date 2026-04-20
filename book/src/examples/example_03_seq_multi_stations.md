# 03a - Multi-station sequence

**Source:** `scheduling/example_03_seq_multi_stations.py`

## What it does

Extends the single-machine model of 02 to multiple machines.

- `presence[m, t]` booleans, with `AddExactlyOne` per task, select which
  machine runs each task.
- Task-level `start[t]`, `end[t]` are linked to `start[m, t]`, `end[m, t]`
  under `OnlyEnforceIf(presence[m, t])`.
- One `AddCircuit` per machine, with a self-loop
  `[t, t, presence[m, t].Not()]` to skip tasks assigned elsewhere.
- The objective is `make_span + total_changeover_time`, with
  `AddMaxEquality` computing the makespan.

## Concepts

- [Circuit and sequencing](../concepts/circuit.md) (multi-machine)
- [Changeover](../concepts/changeover.md) (cost in objective)
