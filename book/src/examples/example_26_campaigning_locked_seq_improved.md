# 26a - Campaigning, locked sequence improved

**Source:** `scheduling/example_26_campaigning_locked_seq_improved.py`

## What it does

Refines 25 by removing the "force `reach_max` when `cumul` hits the cap"
implication. The solver is now free to end a campaign *before* reaching
the size limit if that gives a better objective.

The order lock becomes `start[t-1] <= start[t]` (no longer `end <= start`),
which is looser and compatible with flexible campaign ends.

Also introduces the `AddMaxEquality(max_values, [0, cumul[t1] + 1 -
reach_max[t1] * campaign_size])` trick for computing the next rank
variable under an `OnlyEnforceIf`.

## Concepts

- [Campaigning](../concepts/campaigning.md) (flexible campaign ends)
