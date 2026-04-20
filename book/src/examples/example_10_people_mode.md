# People mode

**Source:** `scheduling/example_10_people_mode.py`

## What it does

Each task can run in one of several "people modes", with different
processing times and headcount requirements. Only the mode choice changes
the model; sequencing is similar to 03.

- `variables_task_resource_mode[t, k]`: one-hot bool for task `t`
  selecting mode `k`. Exactly one mode per task.
- `variables_task_processing_time[t]` is derived from the mode:

  ```python
  model.add(
      processing_time_var[t] == sum(
          processing_time[product[t], k] * mode[t, k] for k in modes
      )
  )
  ```

- Standard machine-assignment variables (`presence[m, t]`,
  `start[m, t]`, `end[m, t]`), per-machine `add_circuit`, and task-level
  links complete the model.

## Concepts

- [Resources and cumulative](../concepts/resources.md) (resource modes)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_10_people_mode.py}}
```
