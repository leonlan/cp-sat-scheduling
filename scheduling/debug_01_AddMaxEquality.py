# https://stackoverflow.com/questions/75588142
# The answer is No. They are not compatible.

from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = model.new_bool_var('x')
y = model.new_bool_var('y')
z = model.new_bool_var('z')

model.add_max_equality(z, [0, y]).only_enforce_if(x)
model.minimize(1)

solver = cp_model.CpSolver()
status = solver.solve(model=model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f'x {solver.value(x)}, y {solver.value(y)}, z {solver.value(z)}')
elif status == cp_model.INFEASIBLE:
    print("Infeasible")
elif status == cp_model.MODEL_INVALID:
    print("Model invalid")
else:
    print(status)


###################################################################################

from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = model.new_bool_var('x')
y = model.new_bool_var('y')
z = model.new_bool_var('z')

Max = model.new_bool_var('max')
Min = model.new_bool_var('min')

model.add_max_equality(Max, [0, y])
model.add_min_equality(Min, [0, y])

model.add(z == Max).only_enforce_if(z)
model.add(z == Min).only_enforce_if(~z)

model.minimize(1)

solver = cp_model.CpSolver()
status = solver.solve(model=model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f'x {solver.value(x)}, y {solver.value(y)}, z {solver.value(z)}')
elif status == cp_model.INFEASIBLE:
    print("Infeasible")
elif status == cp_model.MODEL_INVALID:
    print("Model invalid")
else:
    print(status)
