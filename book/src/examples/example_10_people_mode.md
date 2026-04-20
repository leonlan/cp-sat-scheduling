# People mode

**Source:** `scheduling/example_10_people_mode.py`

Not every task has a fixed resource profile. A common pattern: you can
run a task with 2 people for 3 time units, or with 3 people for 2.
Different modes, different (duration, headcount) pairs, same outcome.

The solver needs to pick the mode. A one-hot `mode[t, k]` per task drives
the derivation:

```python
model.add(
    proc_time[t] == sum(
        processing_time[product[t], k] * mode[t, k] for k in modes
    )
)
```

With `proc_time[t]` now a variable rather than a constant, the rest of
the sequencing machinery (machine presence, per-machine `add_circuit`,
task-level links) carries over unchanged.

## Concepts

- [Resources and cumulative](../concepts/resources.md) (resource modes)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_10_people_mode.py}}
```
