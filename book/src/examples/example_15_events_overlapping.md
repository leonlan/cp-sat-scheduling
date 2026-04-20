# Events overlapping

**Source:** `scheduling/example_15_events_overlapping.py`

Utility chapter. Given two intervals with fixed times, how do you
express "do they overlap, and by how much"?

Two reified booleans - *t1 starts before t2* AND *t1 ends after t2 starts* -
combined with `add_multiplication_equality` give the overlap indicator.
The overlap duration is then a conditional `end[t1] - start[t2]`:

```python
model.add(duration[t1, t2] == end[t1] - start[t2]).only_enforce_if(overlap[t1, t2])
model.add(duration[t1, t2] == 0).only_enforce_if(~overlap[t1, t2])
```

The pattern recurs whenever you need to *measure* overlap rather than
*forbid* it. The duration-stretching break model already used a close
relative; more will show up in the headcount-tracking chapter.

## Concepts

- [CP-SAT basics](../concepts/cp-sat-basics.md) (reification,
  `add_multiplication_equality`)

## Source

```python
{{#include ../../../scheduling/example_15_events_overlapping.py}}
```
