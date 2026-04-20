# Task delaying a break

**Source:** `scheduling/example_14_task_delaying_break.py`

A different way of mixing tasks and breaks. Here the task is *not*
automatic; if it runs through a break, its effective machine time grows
by the length of the break.

The encoding is per time slot. For every slot `i`, a boolean
`uses[t, i]` fires iff task `t` covers slot `i`. Built as the AND of
"started by `i`" and "still running after `i`", it becomes one via
`add_multiplication_equality`. Then

```python
duration[t] = base + sum(is_break[i] * uses[t, i] for i)
```

adds back the length of every break the task straddles. The task
interval uses this stretched duration directly.

Heavy on per-slot booleans, but it is the canonical pattern whenever a
duration depends on a time-dependent condition.

## Concepts

- [Breaks](../concepts/breaks.md) (approach 2: duration stretched)
- [CP-SAT basics](../concepts/cp-sat-basics.md) (reification,
  `add_multiplication_equality`)

## Source

```python
{{#include ../../../scheduling/example_14_task_delaying_break.py}}
```
