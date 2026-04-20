
from ortools.sat.python import cp_model

model = cp_model.CpModel()

num_vals = 3

x = model.new_int_var(0, num_vals - 1, 'x')
y = model.new_int_var(0, num_vals - 1, 'y')
z = model.new_int_var(0, num_vals - 1, 'z')


model.add(x != y)

solver = cp_model.CpSolver()

status = solver.solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print('x = %i' % solver.value(x))
    print('y = %i' % solver.value(y))
    print('z = %i' % solver.value(z))
else:
    print('No solution found.')


####################################################################


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        for v in self.__variables:
            print('%s=%i' % (v, self.value(v)), end=' ')
        print()

    def solution_count(self):
        return self.__solution_count


solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x, y, z])
# Enumerate all solutions.
solver.parameters.enumerate_all_solutions = True
# Solve.
status = solver.solve(model, solution_printer)

