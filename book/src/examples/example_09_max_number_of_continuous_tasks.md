# Max number of continuous tasks

**Source:** `scheduling/example_09_max_number_of_continuous_tasks.py`

First campaigning chapter. In many process industries, tasks of the same
product can run back-to-back with no changeover, but only up to `N` in a
row - the equipment needs a cleaning cycle after that, even between two
batches of the same product.

This model takes the most direct approach: campaigns are first-class
entities. For every product, enumerate as many candidate campaigns as
there are tasks of that product. Each campaign has `start`, `end`,
`duration`, `presence`; a task is assigned to exactly one campaign via
`var_task_campaign_presences[t, c]`; a campaign is present iff at least
one task is assigned (`add_max_equality`); campaign duration bounded by
`max_conti_task_num` caps the size.

Campaigns (not tasks) are then sequenced with `add_circuit`, with a
changeover distance between consecutive campaigns. Expected pattern for
`A A A B` is `A A -> CO -> A -> CO -> B`.

This is the "business view" of campaigning. A more compact alternative
follows in [Campaigning with cumul](./example_24_campaigning_with_cumul.md).

## Concepts

- [Campaigning](../concepts/campaigning.md) (approach 1: campaigns as entities)
- [Circuit and sequencing](../concepts/circuit.md)
- [Interval variables](../concepts/intervals.md)

## Source

```python
{{#include ../../../scheduling/example_09_max_number_of_continuous_tasks.py}}
```
