from ortools.sat.python import cp_model
model = cp_model.CpModel()
def get(x):
    return solver.value(x)

#
x = model.new_bool_var('x')
y = model.new_bool_var('y')
model.add_bool_or(x, y)
model.minimize(x+y)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(get(x), get(y))

#
x = model.new_bool_var('x')
y = model.new_bool_var('y')
model.add_bool_and(x, y)
model.minimize(x+y)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(get(x), get(y))

#
x = model.new_bool_var('x')
y = model.new_bool_var('y')
model.add_bool_xor(x, y)
model.minimize(x+y)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(get(x), get(y))


#
x = model.new_bool_var('x')
y = model.new_bool_var('y')
model.add(x+y == 2)
model.minimize(x+y)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(get(x), get(y))

#
x = model.new_bool_var('x')
y = model.new_bool_var('y')
model.add(x+y == 1)
model.minimize(x+y)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(get(x), get(y))

#
x = model.new_bool_var('x')
y = model.new_bool_var('y')
model.add(x+y == 0)
model.minimize(x+y)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(get(x), get(y))


#
model = cp_model.CpModel()
x = model.new_bool_var('x')
y = model.new_bool_var('y')
model.add(x==1).only_enforce_if(~x)
#model.add(x==0).only_enforce_if(~x)
# model.add(x==1).only_enforce_if(x)
model.add(x==0).only_enforce_if(x)
#model.add(y==1).only_enforce_if(x)
model.minimize(x)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(get(x))


#

model = cp_model.CpModel()
x_is_between_5_and_10 = model.new_bool_var('x_is_between_5_and_10')
x = model.new_int_var(0, 100, 'x')
model.add(x == 7)
model.add(x_is_between_5_and_10 == 1).only_enforce_if(5 <= x).only_enforce_if(x <= 10)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print('x', get(x))
print('x_is_between_5_and_10', get(x_is_between_5_and_10))









model = cp_model.CpModel()
x_is_between_5_and_10 = model.new_bool_var('x_is_between_5_and_10')
x_is_no_less_than_5 = model.new_bool_var('x_is_no_less_than_5')
x_is_no_more_than_10 = model.new_bool_var('x_is_no_more_than_10')
x = model.new_int_var(0, 100, 'x')
model.add(x == 7)

model.add(x_is_no_less_than_5 == x >= 5)


# model.add(x_is_no_less_than_5 == 1).only_enforce_if(x>=5)
# model.add(x_is_no_more_than_10 == 1).only_enforce_if(x <= 10)

model.add(x_is_between_5_and_10 == 1).only_enforce_if(5 <= x).only_enforce_if(x <= 10)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print('x', get(x))
print('x_is_between_5_and_10', get(x_is_between_5_and_10))





##########################################

from ortools.sat.python import cp_model
model = cp_model.CpModel()
x_is_greater_than_5 = model.new_bool_var('x_is_greater_than_5')
x = model.new_int_var(0, 100, 'x')
model.add(x == 7)
model.add(x >= 5).only_enforce_if(x_is_greater_than_5)
model.add(x < 5).only_enforce_if(~x_is_greater_than_5)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print('x', solver.value(x))
print('x_is_greater_than_5', solver.value(x_is_greater_than_5))



from ortools.sat.python import cp_model
model = cp_model.CpModel()
x = model.new_int_var(0, 100, 'x')
x_is_between_5_and_10 = model.new_bool_var('x_is_between_5_and_10')
model.add(x >= 5).only_enforce_if(x_is_between_5_and_10)
#model.add(x <= 10).only_enforce_if(x_is_between_5_and_10)
model.add(x < 10).only_enforce_if(~x_is_between_5_and_10)
#model.add(x >10).only_enforce_if(~x_is_greater_than_5)
# This gives invalid
model.add(x == 3)
model.add(x_is_between_5_and_10 == 1)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(status)
if status == 1 or status == 4:
    print('x', solver.value(x))
    print('x_is_greater_than_5', solver.value(x_is_between_5_and_10))




from ortools.sat.python import cp_model
model = cp_model.CpModel()
x = model.new_int_var(0, 100, 'x')
x_is_between_5_and_10 = model.new_bool_var('x_is_between_5_and_10')
model.add(x >= 5).only_enforce_if(x_is_between_5_and_10)
#model.add(x <= 10).only_enforce_if(x_is_between_5_and_10)
model.add(x < 10).only_enforce_if(~x_is_between_5_and_10)
#model.add(x >10).only_enforce_if(~x_is_greater_than_5)
#model.add(x == 3)
model.add(x_is_between_5_and_10 == 1)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(status)
if status == 1 or status == 4:
    print('x', solver.value(x))
    print('x_is_greater_than_5', solver.value(x_is_between_5_and_10))




from ortools.sat.python import cp_model
model = cp_model.CpModel()
x = model.new_int_var(0, 100, 'x')
x_is_between_5_and_10 = model.new_bool_var('x_is_between_5_and_10')
model.add(x >= 5).only_enforce_if(x_is_between_5_and_10)
model.add(x <= 10).only_enforce_if(x_is_between_5_and_10)

model.add(x < 5).only_enforce_if(~x_is_between_5_and_10)
model.add(x >10).only_enforce_if(~x_is_between_5_and_10)

model.add(x == 3)
# model.add(x_is_between_5_and_10 == 0)

solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(status)
if status == 1 or status == 4:
    print('x', solver.value(x))
    print('x_is_greater_than_5', solver.value(x_is_between_5_and_10))





from ortools.sat.python import cp_model
model = cp_model.CpModel()
x = model.new_int_var(0, 100, 'x')
x_is_between_5_and_10 = model.new_bool_var('5<x<10')
x_greater_than_5 = model.new_bool_var('5<x')
x_less_than_10 = model.new_bool_var('x<10')


model.add(x > 5).only_enforce_if(x_greater_than_5)
model.add(x <= 5).only_enforce_if(~x_greater_than_5)

model.add(x < 10).only_enforce_if(x_less_than_10)
model.add(x >= 10).only_enforce_if(~x_less_than_10)

model.add(x_is_between_5_and_10==x_greater_than_5*x_less_than_10)
model.add_multiplication_equality(x_is_between_5_and_10, )

model.add(x == 3)
# model.add(x_is_between_5_and_10 == 0)

solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(status)
if status == 1 or status == 4:
    print('x', solver.value(x))
    print('x_is_greater_than_5', solver.value(x_is_between_5_and_10))









from ortools.sat.python import cp_model
model = cp_model.CpModel()
x_is_between_5_and_10 = model.new_bool_var('5<x<10')
x = model.new_int_var(0, 100, 'x')

model.add_linear_constraint(x, 5, 10).only_enforce_if(x_is_between_5_and_10)
model.add_linear_expression_in_domain(
    x,
    cp_model.Domain.from_intervals([[0, 4], [11, 100]])
).only_enforce_if(~x_is_between_5_and_10)

model.add(x == 3)
solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(status)
if status == 1 or status == 4:
    print('x', solver.value(x))
    print('x_is_greater_than_5', solver.value(x_is_between_5_and_10))





from ortools.sat.python import cp_model
model = cp_model.CpModel()
x = model.new_int_var(0, 100, 'x')
x_is_between_5_and_10 = model.new_bool_var('5<x<10')
x_greater_than_5 = model.new_bool_var('5<x')
x_less_than_10 = model.new_bool_var('x<10')

model.add(x > 5).only_enforce_if(x_greater_than_5)
model.add(x <= 5).only_enforce_if(~x_greater_than_5)

model.add(x < 10).only_enforce_if(x_less_than_10)
model.add(x >= 10).only_enforce_if(~x_less_than_10)

model.add_multiplication_equality(x_is_between_5_and_10, [x_greater_than_5, x_less_than_10])

model.add(x_is_between_5_and_10 == 1)

solver = cp_model.CpSolver()
status = solver.solve(model=model)
print(status)
if status == 1 or status == 4:
    print('x', solver.value(x))
    print('x_is_greater_than_5', solver.value(x_is_between_5_and_10))
