# Linear domain for breaks

**Source:** `scheduling/example_29_linear_domain_for_breaks.py`

When breaks are periodic - a fixed pattern every shift, every day -
modeling each break as an interval inflates the model. An alternative
is to precompute the set of valid task start times (every position that
doesn't overlap a break) and restrict starts to that set with
`add_linear_expression_in_domain`.

The file defines two model variants and benchmarks them:

- **Method 1**: breaks as fixed intervals in `add_cumulative` or
  `add_no_overlap`.
- **Method 2**: breaks disappear; start domains are constrained.

For highly periodic schedules the domain method wins: CP-SAT propagates
on a small set of start values directly and avoids all the break
intervals. The trade-off is loss of generality - arbitrary break
patterns don't translate to clean domains.

## Concepts

- [Breaks](../concepts/breaks.md) (approach 3: start-domain restriction)
- [Solver techniques](../concepts/solver-techniques.md)

## Source

```python
{{#include ../../../scheduling/example_29_linear_domain_for_breaks.py}}
```
