# 29 - Linear domain for breaks

**Source:** `scheduling/example_29_linear_domain_for_breaks.py`

## What it does

Compares two ways of enforcing that tasks never overlap a periodic break:

- **Method 1** (`run_model_1`): model every break as a fixed interval and
  put them in `AddCumulative` (or `AddNoOverlap`) along with tasks.
- **Method 2**: keep tasks as intervals but restrict their start values
  to a domain that excludes break-overlapping starts, using
  `AddLinearExpressionInDomain`.

The second method skips creating many break intervals and lets CP-SAT
propagate directly on the start domain, which can be faster for
highly periodic schedules. The file includes a benchmark loop.

## Concepts

- [Breaks](../concepts/breaks.md) (approach 3: start-domain restriction)
- [Solver techniques](../concepts/solver-techniques.md)

## Source

```python
{{#include ../../../scheduling/example_29_linear_domain_for_breaks.py}}
```
