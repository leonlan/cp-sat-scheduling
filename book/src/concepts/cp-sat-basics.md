# CP-SAT basics

CP-SAT is a constraint-programming solver with integer and boolean variables.
Before looking at scheduling, it helps to be comfortable with a few primitives.

## Variables

```python
x = model.new_int_var(0, 100, 'x')      # integer in [0, 100]
b = model.new_bool_var('b')             # boolean (integer in {0, 1})
```

## Linear constraints

```python
model.add(x + y == 10)
model.add(x <= y)
model.add(sum(bs) == 1)               # exactly-one on a list of bools
model.add_exactly_one(bs)               # same, more idiomatic
```

## Boolean combinations

```python
model.add_bool_or([a, b])               # a or b
model.add_bool_and([a, b])              # a and b
model.add_bool_xor([a, b])              # exactly one of a, b
```

## Reification with `only_enforce_if`

A constraint can be conditioned on a boolean literal. The constraint is only
active when the literal is true.

```python
model.add(x >= 5).only_enforce_if(b)
model.add(x < 5).only_enforce_if(~b)
```

Chaining two `only_enforce_if` calls gives an "and" of conditions:

```python
model.add(y == 1).only_enforce_if(b1).only_enforce_if(b2)  # y == 1 iff b1 and b2
```

For "or", you normally introduce intermediate booleans or use
`add_bool_or`.

## `add_min_equality`, `add_max_equality`, `add_multiplication_equality`

These express `z = min(xs)`, `z = max(xs)`, `z = x * y` (or the product of a
list). `add_max_equality` is how makespan is usually encoded:

```python
model.add_max_equality(make_span, [ends[t] for t in tasks])
```

## Domains

For "x belongs to a non-contiguous set of values" use
`add_linear_expression_in_domain`:

```python
domain = cp_model.Domain.from_intervals([[0, 4], [11, 100]])
model.add_linear_expression_in_domain(x, domain)
```

See `example_00_unit_tests.py` for a collection of small snippets exercising
each of these.

## Solve and read back

```python
solver = cp_model.CpSolver()
status = solver.solve(model)
if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(solver.value(x))
```
