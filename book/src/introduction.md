# Introduction

This book collects notes and examples of scheduling models built with
[OR-Tools CP-SAT](https://developers.google.com/optimization/cp/cp_solver). The
focus is on job-shop style problems: sequencing tasks on machines, handling
changeovers, respecting breaks and shifts, modeling resources, and grouping
tasks into campaigns.

The book is split into two parts.

- **Concepts** walks through the core modeling ideas once. Read these first if
  CP-SAT or constraint programming is new to you.
- **Examples** indexes the Python files in the `scheduling/` folder and links
  each one back to the concepts it demonstrates. Examples are numbered and
  build on each other, so reading them in order is usually easiest.

All code lives in the `scheduling/` directory of the repo. Open a file in your
editor while reading the corresponding chapter to see the full model.

## A minimal CP-SAT template

Almost every example follows the same five-step shape.

```python
from ortools.sat.python import cp_model

# 1. Data
# ... sets, durations, changeover table, etc.

# 2. Decision variables
model = cp_model.CpModel()
# ... start/end/interval/bool vars

# 3. Objective
make_span = model.new_int_var(0, max_time, "make_span")
model.add_max_equality(make_span, [ends[t] for t in tasks])
model.minimize(make_span)

# 4. Constraints
# ... precedence, resources, circuits, ...

# 5. Solve and post-process
solver = cp_model.CpSolver()
status = solver.solve(model)
```

The rest of the book explains what goes into step 4.
