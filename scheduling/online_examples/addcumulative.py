from ortools.sat.python import cp_model

model = cp_model.CpModel()

a1 = model.new_int_var(0, 100, 'a1')
a2 = model.new_int_var(0, 100, 'a2')
a3 = model.new_int_var(0, 100, 'a3')

x1 = model.new_interval_var(a1, 10, a1+10, 'x1')
x2 = model.new_interval_var(a2, 10, a2+10, 'x2')
x3 = model.new_interval_var(a3, 10, a3+10, 'x3')

# x1 = model.new_interval_var(start = a1, size = 3, end = a1+4, name = 'x1')
# x2 = model.new_interval_var(a2, 3, a2+3, 'x2')
# x3 = model.new_interval_var(a3, 3, a3+3, 'x3')


#model.add_no_overlap([x1, x2, x3])

#model.add_cumulative([x1, x2, x3], [1,1,1], 1)

#model.add_cumulative([x1, x2, x3], [1,1,1], 2)

model.add_cumulative([x1, x2, x3], [1,1,1], 1)


solver = cp_model.CpSolver()
status = solver.solve(model)
solver.parameters.log_search_progress = True
print(solver.value(a1), solver.value(a2), solver.value(a3))

