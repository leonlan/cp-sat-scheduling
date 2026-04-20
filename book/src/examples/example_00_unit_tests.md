# Unit tests

**Source:** `scheduling/example_00_unit_tests.py`

Before modeling a scheduling problem you have to be fluent in the constraint
primitives CP-SAT actually speaks. This file is a bench of tiny self-contained
models, each exercising one feature: boolean combinators, reified equalities
with `only_enforce_if`, combining conditions via `add_multiplication_equality`,
and domain constraints for non-contiguous value sets.

It is the only chapter with no scheduling content. Everything later assumes
you are comfortable with what lives here. Useful as a cheat sheet when you
want to remember how to express, for example, "b = (5 <= x <= 10)". Several
snippets are commented-out alternatives kept for comparison.

## Concepts

- [CP-SAT basics](../concepts/cp-sat-basics.md)

## Source

```python
{{#include ../../../scheduling/example_00_unit_tests.py}}
```
