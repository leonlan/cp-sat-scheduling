# Changeover in constraint

**Source:** `scheduling/example_04_seq_with_changeover_in_constraint.py`

## What it does

Moves the changeover out of the objective and into the precedence
constraint. If `seq[m, t1, t2]` is true, then

```python
model.add(end[t1] + distance <= start[t2]).only_enforce_if(seq[m, t1, t2])
```

where `distance` is the changeover time between the two products. The
objective becomes just the makespan.

Now schedule and objective agree: a changeover physically pushes the next
task later, it is not only charged abstractly.

## Concepts

- [Changeover](../concepts/changeover.md) (approach 2: in constraint)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_04_seq_with_changeover_in_constraint.py}}
```
