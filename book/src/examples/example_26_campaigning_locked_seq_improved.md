# Campaigning, locked sequence improved

**Source:** `scheduling/example_26_campaigning_locked_seq_improved.py`

The previous chapter forced a campaign to end only when the rank hit
the cap. Sometimes ending earlier gives a better schedule - for example
when a near-deadline task of a different product is waiting. This
chapter lets the solver decide.

The "force reach_max when cumul hits cap" implication is dropped. The
order lock loosens to `start[t-1] <= start[t]` (from the stricter
`end <= start`), which is compatible with flexible campaign ends.

The chapter also introduces a recurring trick: since `add_max_equality`
cannot be wrapped in `only_enforce_if`, compute the next rank outside
the literal and then assign it conditionally.

```python
model.add_max_equality(
    max_values[t1, t2],
    [0, cumul[t1] + 1 - reach_end[t1] * campaign_size],
)
model.add(cumul[t2] == max_values[t1, t2]).only_enforce_if(literals[t1, t2])
```

## Concepts

- [Campaigning](../concepts/campaigning.md) (flexible campaign ends)

## Source

```python
{{#include ../../../scheduling/example_26_campaigning_locked_seq_improved.py}}
```
