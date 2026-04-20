# Campaigning, locked sequence improved (flexible)

**Source:** `scheduling/example_26_campaigning_locked_seq_improved_flexible.py`

Twin of the previous chapter. The two files exist side by side to
document an important design choice explicitly: *don't* force the
campaign to end just because the rank hit the cap. Let the solver
decide.

Model structure is identical to its sibling; the comments here are the
main difference. Read both to see the "before / after" of the
refinement.

## Concepts

- [Campaigning](../concepts/campaigning.md) (flexible campaign ends)

## Source

```python
{{#include ../../../scheduling/example_26_campaigning_locked_seq_improved_flexible.py}}
```
