# Circuit and sequencing

To sequence tasks on a machine, you need both the order and the time
constraints that follow from it. CP-SAT's `AddCircuit` is the standard tool.

## What `AddCircuit` does

`AddCircuit(arcs)` takes a list of triples `[i, j, literal]`. It asserts that
the selected arcs (where `literal == 1`) form a single Hamiltonian circuit over
the referenced nodes. Self-arcs `[i, i, literal]` mean node `i` is skipped
when `literal` is true.

```python
arcs = []
for t1 in tasks:
    arcs.append([0, t1, start_literal(t1)])   # dummy -> t1 (first)
    arcs.append([t1, 0, end_literal(t1)])     # t1 -> dummy (last)
    arcs.append([t1, t1, presence[t1].Not()]) # skip t1 if absent
    for t2 in tasks:
        if t1 == t2:
            continue
        arcs.append([t1, t2, seq[t1, t2]])

model.AddCircuit(arcs)
```

Node `0` (or `-1`) is typically a dummy "first/last" node.

## Linking the circuit to time

`AddCircuit` only picks the order. You also need: *if `t1 -> t2` is chosen,
then `end[t1] + gap <= start[t2]`*. This is a reified constraint:

```python
model.Add(end[t1] + gap <= start[t2]).OnlyEnforceIf(seq[t1, t2])
```

`gap` is usually `changeover_time` (see [Changeover](./changeover.md)) or
`0`.

## Multi-machine

With multiple machines, build one circuit per machine and gate absent tasks
with self-loops:

```python
for m in machines:
    arcs = []
    for t in tasks:
        arcs.append([t, t, presence[m, t].Not()])
        for t2 in tasks:
            if t != t2:
                arcs.append([t, t2, seq[m, t, t2]])
    model.AddCircuit(arcs)
```

`AddExactlyOne(presence[m, t] for m in machines)` ensures each task ends up on
exactly one machine.

Examples: `example_01_simple_sequence.py` (single machine),
`example_03_seq_multi_stations.py` (multi-machine).
