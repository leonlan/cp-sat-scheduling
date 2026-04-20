# 15 - Events overlapping

**Source:** `scheduling/example_15_events_overlapping.py`

## What it does

Tutorial on detecting whether two intervals overlap, and by how much.

- `var_start_earlier_than_start[t1, t2]` = "t1 starts before t2".
- `var_end_later_than_start[t1, t2]` = "t1 ends after t2 starts".
- `var_overlap[t1, t2]` is the product of the two, i.e. the AND.
- `var_overlap_duration[t1, t2]` equals `end[t1] - start[t2]` when there
  is overlap, else zero.

Both tasks here have fixed start/end for illustration; the interest is in
how the overlap indicator is built.

## Concepts

- [CP-SAT basics](../concepts/cp-sat-basics.md) (reification,
  `AddMultiplicationEquality`)
