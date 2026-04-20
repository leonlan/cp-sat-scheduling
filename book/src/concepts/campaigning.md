# Campaigning

A **campaign** is a run of same-product tasks on a machine between two
changeovers. Typical rules:

- tasks within a campaign are the same product and pay no changeover cost,
- a campaign has a maximum size (e.g. at most `N` tasks),
- switching products or hitting the cap triggers a changeover.

## Approach 1: campaigns as entities

Create a set of potential campaigns, each with start/end/duration/presence,
and variables linking tasks to campaigns. Sequence campaigns (not tasks)
using `AddCircuit`. The campaign-level changeover cost sits in the gap
between campaigns.

Pros: close to the business view. Cons: more variables, scales worse.

Example: `example_09_max_number_of_continuous_tasks.py`.

## Approach 2: cumulative rank per task

Keep tasks as the atomic unit and attach a rank variable
`cumul[t] in [0, campaign_size - 1]`. On each `t1 -> t2` arc:

- if the campaign continues, `cumul[t2] = cumul[t1] + 1`,
- if a changeover happens, `cumul[t2] = 0` and `end[t1] + changeover <= start[t2]`.

A `reach_max[t]` boolean fires when `cumul[t] == campaign_size - 1`, forcing a
reset and changeover. `AddMaxEquality(max_value, [0, cumul[t1] + 1 -
reach_end[t1] * campaign_size])` is a useful trick to compute the next rank
under an `OnlyEnforceIf`.

Pros: fewer variables, scales better. Cons: trickier to explain.

Examples: `example_24_campaigning_with_cumul.py` (base),
`example_27_campaigning_products.py` (multi-product),
`example_28_campaigning_products_machines.py` (multi-machine).

## Locking the task order

When tasks have deadlines that align with their index, locking
`start[t-1] <= start[t]` (or the stricter `end[t-1] <= start[t]`) is a cheap
heuristic that often gives a 10x+ solve-time improvement. See
`example_25_campaigning_with_locked_seq.py` and the two
`example_26_campaigning_locked_seq_improved*.py` variants.

## Flexible campaign ends

If the model should be free to end a campaign early (not just at the cap),
drop the "force reach_end when cumul hits max" implication and let the
solver choose. This usually gives better objective values at a small solve-
time cost. See the two `example_26_*_improved*.py` files for the comparison.
