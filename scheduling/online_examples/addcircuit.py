from ortools.sat.python import cp_model

model = cp_model.CpModel()

a1 = model.new_bool_var("1")
a2 = model.new_bool_var("2")
a3 = model.new_bool_var("3")
a4 = model.new_bool_var("4")
a5 = model.new_bool_var("5")
a6 = model.new_bool_var("6")
a7 = model.new_bool_var("7")
a8 = model.new_bool_var("8")
a9 = model.new_bool_var("9")
a10 = model.new_bool_var("10")


# arc1 = (0, 1, a1)
# arc2 = (1, 2, a2)
# arc3 = (2, 0, a3)
# model.add_circuit([arc1, arc2, arc3])
# solver = cp_model.CpSolver()
# status = solver.solve(model)
# print(solver.value(a1), solver.value(a2), solver.value(a3))


arc1 = (0, 1, a1)
arc2 = (0, 2, a2)
arc3 = (1, 0, a3)
arc4 = (1, 2, a4)
arc5 = (2, 0, a5)
arc6 = (2, 1, a6)
arc7 = (0, 0, a7)
arc8 = (1, 1, a8)
arc9 = (2, 2, a9)
arc10 = (2, 2, a10)


#model.add_circuit([arc1, arc2, arc3, arc4, arc5, arc6,  arc7, arc8, arc9, arc10])
#model.add_circuit([arc1, arc2, arc3, arc4, arc5, arc6,  arc7, arc8])# arc9, arc10])

model.add_circuit([arc1, arc2, arc3, arc4, arc5, arc6,  arc7, arc9, arc10])

#model.add(a1 == 1)
# model.add(a9 == 1)
# model.add(a1 == 1)


solver = cp_model.CpSolver()
status = solver.solve(model)

print(solver.value(a1), solver.value(a2), solver.value(a3),
      solver.value(a4), solver.value(a5), solver.value(a6),
      solver.value(a7), solver.value(a8), solver.value(a9),
      )



from ortools.sat.python import cp_model
model = cp_model.CpModel()
a1 = model.new_bool_var("1")
a2 = model.new_bool_var("2")
a3 = model.new_bool_var("3")
a4 = model.new_bool_var("4")
a5 = model.new_bool_var("5")
a6 = model.new_bool_var("6")
arc1 = (0, 1, a1)
arc2 = (20, 20, a2)
arc3 = (1, 0, a3)
model.add_circuit([arc1, arc2, arc3])
solver = cp_model.CpSolver()
status = solver.solve(model)
print(status)
print(solver.value(a1), solver.value(a2), solver.value(a3),
      solver.value(a4), solver.value(a5), solver.value(a6))

