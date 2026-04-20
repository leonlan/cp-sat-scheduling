# Changeover

A changeover is the time needed to switch a machine from producing one product
to another. There are three common ways to model it.

## 1. In the objective

Charge a cost for each `seq[t1, t2]` whose products differ. The cost does not
appear in the schedule itself, only the cost minimised.

```python
total_co = sum(seq[t1, t2] * changeover_cost[t1, t2] for ...)
model.minimize(make_span + total_co)
```

Simple, but time and cost are decoupled: the schedule may not leave physical
room for the changeover.

Example: `example_01_simple_sequence.py`.

## 2. In the precedence constraint

Include the changeover in the gap between tasks:

```python
gap = changeover_time if products_differ(t1, t2) else 0
model.add(end[t1] + gap <= start[t2]).only_enforce_if(seq[t1, t2])
```

Now time and cost agree: a changeover actually pushes the next task later.

Example: `example_04_seq_with_changeover_in_constraint.py`.

## 3. As a first-class event

Create an optional interval for every `(t1, t2)` that represents the
changeover itself. When `t1 -> t2` is chosen, the interval is present, sits
between the two tasks, and has the right duration.

```python
co_iv = model.new_optional_interval_var(co_start, co_duration, co_end, co_present, ...)
model.add(end[t1] <= co_start).only_enforce_if(seq[t1, t2])
model.add(co_end <= start[t2]).only_enforce_if(seq[t1, t2])
model.add(co_present == 1).only_enforce_if(seq[t1, t2])
```

This lets you add the changeover interval to `add_cumulative` (it consumes
operator time) or apply cleaning-resource constraints to it.

Example: `example_08_changeover_as_event.py`.

## Starting product

A machine usually begins with some product already loaded. Model it with a
dummy task 0 whose "product" is the starting product; the cost from dummy to
the first real task is zero if they match, else the usual changeover.

Example: `example_02_seq_lock_starting_product.py`.
