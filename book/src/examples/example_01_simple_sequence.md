# 01 - Simple sequence

**Source:** `scheduling/example_01_simple_sequence.py`

## What it does

The smallest end-to-end scheduling model in the book. Three tasks across two
products on a single machine.

- A dummy task `0` acts as the start/end node.
- `seq[t1, t2]` booleans select the order via `AddCircuit`.
- If `t1 -> t2` is chosen, `end[t1] <= start[t2]` is enforced.
- The changeover cost lives in the objective: `Minimize(sum(seq * cost))`.
- Duration is encoded manually with `end - start == duration`.

## Concepts

- [Circuit and sequencing](../concepts/circuit.md)
- [Changeover](../concepts/changeover.md) (approach 1: cost in objective)
