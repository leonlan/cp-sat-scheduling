# Simple sequence

**Source:** `scheduling/example_01_simple_sequence.py`

Three tasks, two products, one machine. Switching between products costs
time. What is the cheapest order?

The smallest useful scheduling model. A dummy task 0 represents "machine
idle" so the circuit has a start and an end; sequencing booleans
`seq[t1, t2]` are stitched together with `add_circuit`; when an arc is
chosen, `end[t1] <= start[t2]` is enforced. Changeover lives in the
objective as a cost-weighted sum over the selected arcs, and task duration
is the manual `end - start == duration`.

Everything after this chapter is a variation: more machines, different
changeover semantics, extra constraints for breaks or shifts. Understanding
where the circuit, the presence booleans, and the order-to-time link go is
the hard part.

## Concepts

- [Circuit and sequencing](../concepts/circuit.md)
- [Changeover](../concepts/changeover.md) (approach 1: cost in objective)

## Source

```python
{{#include ../../../scheduling/example_01_simple_sequence.py}}
```
