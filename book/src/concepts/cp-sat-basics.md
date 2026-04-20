# CP-SAT basics

CP-SAT is a constraint-programming solver with integer and boolean variables.
Before looking at scheduling, it helps to be comfortable with a few primitives.

## Variables

```python
x = model.NewIntVar(0, 100, 'x')      # integer in [0, 100]
b = model.NewBoolVar('b')             # boolean (integer in {0, 1})
```

## Linear constraints

```python
model.Add(x + y == 10)
model.Add(x <= y)
model.Add(sum(bs) == 1)               # exactly-one on a list of bools
model.AddExactlyOne(bs)               # same, more idiomatic
```

## Boolean combinations

```python
model.AddBoolOr([a, b])               # a or b
model.AddBoolAnd([a, b])              # a and b
model.AddBoolXOr([a, b])              # exactly one of a, b
```

## Reification with `OnlyEnforceIf`

A constraint can be conditioned on a boolean literal. The constraint is only
active when the literal is true.

```python
model.Add(x >= 5).OnlyEnforceIf(b)
model.Add(x < 5).OnlyEnforceIf(b.Not())
```

Chaining two `OnlyEnforceIf` calls gives an "and" of conditions:

```python
model.Add(y == 1).OnlyEnforceIf(b1).OnlyEnforceIf(b2)  # y == 1 iff b1 and b2
```

For "or", you normally introduce intermediate booleans or use
`AddBoolOr`.

## `AddMinEquality`, `AddMaxEquality`, `AddMultiplicationEquality`

These express `z = min(xs)`, `z = max(xs)`, `z = x * y` (or the product of a
list). `AddMaxEquality` is how makespan is usually encoded:

```python
model.AddMaxEquality(make_span, [ends[t] for t in tasks])
```

## Domains

For "x belongs to a non-contiguous set of values" use
`AddLinearExpressionInDomain`:

```python
domain = cp_model.Domain.FromIntervals([[0, 4], [11, 100]])
model.AddLinearExpressionInDomain(x, domain)
```

See `example_00_unit_tests.py` for a collection of small snippets exercising
each of these.

## Solve and read back

```python
solver = cp_model.CpSolver()
status = solver.Solve(model)
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(solver.Value(x))
```
