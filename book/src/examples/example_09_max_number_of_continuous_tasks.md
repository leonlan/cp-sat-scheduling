# Max number of continuous tasks

**Source:** `scheduling/example_09_max_number_of_continuous_tasks.py`

## What it does

Introduces campaigning by modeling campaigns explicitly as entities:

- For every product, pre-compute as many candidate campaigns as there are
  tasks of that product.
- Campaign variables: `start`, `end`, `duration`, `presence`.
- `var_task_campaign_presences[t, c]`: task `t` is assigned to campaign
  `c`. Exactly one per task.
- Campaign duration is the sum of task durations assigned to it. Campaign
  start/end bound task starts/ends of its members.
- A campaign is present iff at least one task is assigned
  (`add_max_equality`).
- `var_campaign_durations[c] <= max_conti_task_num` caps campaign size.
- Campaigns are sequenced with a campaign-level `add_circuit`, with a
  changeover `distance` enforced between consecutive campaigns.

The expected pattern for four tasks `A A A B` is
`A A -> CO -> A -> CO -> B`.

## Concepts

- [Campaigning](../concepts/campaigning.md) (approach 1: campaigns as entities)
- [Circuit and sequencing](../concepts/circuit.md)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_09_max_number_of_continuous_tasks.py}}
```
