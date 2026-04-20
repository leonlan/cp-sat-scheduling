# 00 - Unit tests

**Source:** `scheduling/example_00_unit_tests.py`

## What it does

A scratchpad of CP-SAT primitives. Not a scheduling model. It runs through
small self-contained models that each exercise one feature:

- `AddBoolOr`, `AddBoolAnd`, `AddBoolXOr` over two booleans.
- Plain linear constraints with `Minimize`.
- Reifying "x is between 5 and 10" with chained `OnlyEnforceIf`, with
  `AddMultiplicationEquality`, and with `AddLinearExpressionInDomain`.
- Reading back results with `solver.Value`.

## Concepts

- [CP-SAT basics](../concepts/cp-sat-basics.md)

## Notes

Useful as a cheat sheet when you want to remember how to express, for
example, "b = (5 <= x <= 10)". Several of the snippets are commented out
alternatives, kept for comparison.

## Source

```python
{{#include ../../../scheduling/example_00_unit_tests.py}}
```
