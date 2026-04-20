# Changeover in constraint

**Source:** `scheduling/example_04_seq_with_changeover_in_constraint.py`

There is a subtle bug in the earlier models. We charged changeover cost in
the objective, but the schedule itself was free to place the next task
right after the previous one - with no physical gap for the changeover to
happen. Cost and schedule disagreed.

The fix is to put the changeover into the precedence constraint:

```python
model.add(end[t1] + distance <= start[t2]).only_enforce_if(seq[m, t1, t2])
```

Now a changeover actually pushes the next task later. The objective can go
back to being just the makespan, and the resulting schedule is physically
executable.

## Concepts

- [Changeover](../concepts/changeover.md) (approach 2: in constraint)
- [Circuit and sequencing](../concepts/circuit.md)

## Source

```python
{{#include ../../../scheduling/example_04_seq_with_changeover_in_constraint.py}}
```
