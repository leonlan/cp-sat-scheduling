# Campaigning, locked sequence improved (flexible)

**Source:** `scheduling/example_26_campaigning_locked_seq_improved_flexible.py`

## What it does

Twin of [26a](./example_26_campaigning_locked_seq_improved.md) with the
same flexible campaign-end semantics, plus a comment line that warns
against forcibly setting `reach_max` when the cap is reached - the
intended behavior is to let the solver decide.

The two 26 files exist side by side to document the tweak explicitly.

## Concepts

- [Campaigning](../concepts/campaigning.md) (flexible campaign ends)

## Source

```python
{{#include ../../../scheduling/example_26_campaigning_locked_seq_improved_flexible.py}}
```
