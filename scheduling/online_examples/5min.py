import collections
from ortools.sat.python import cp_model

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

##########################################################
model = cp_model.CpModel()
x1 = model.new_int_var(0, 10, 'x1')
y = model.new_int_var(0, 20, 'y')
model.add(y==x1)
model.maximize(y)
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x1, y])
status = solver.solve(model, solution_printer)

##########################################################

model = cp_model.CpModel()
# x1 = model.new_int_varFromDomain(
#     cp_model.Domain.from_values([1, 3, 4, 6]), 'x1'
# )
domain = cp_model.Domain.from_values([1, 3, 4, 6])
x1 = model.new_int_varFromDomain(domain,'x1')
y = model.new_int_var(0, 20, 'y')
model.add(y==x1)
model.maximize(y)
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x1, y])
status = solver.solve(model, solution_printer)



##########################################################

model = cp_model.CpModel()

x1 = model.new_bool_var('x1')
x2 = model.new_bool_var('x2')
y = model.new_int_var(0,20, 'y')
model.add_bool_or([])
model.add(y == x1 + x2)
model.maximize(y)
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x1, x2, y])
status = solver.solve(model, solution_printer)


##########################################################

#A channeling constraint
# Channeling is usually implemented using half-reified linear constraints:
# one constraint implies another (a → b),
# but not necessarily the other way around (a ← b).

# if x < 0, y = 0
# else, y = 10 -x

#  b ->     y = 10 -x
# !b ->     y = 0

# Create the CP-SAT model.

if True:
    model = cp_model.CpModel()

    # Declare our two primary variables.
    x = model.new_int_var(0, 10, 'x')
    y = model.new_int_var(0, 10, 'y')

    # Declare our intermediate boolean variable.
    b = model.new_bool_var('b')

    # Implement b == (x >= 5).
    model.add(x >= 5).only_enforce_if(b)
    model.add(x < 5).only_enforce_if(~b)

    # Create our two half-reified constraints.
    # First, b implies (y == 10 - x).
    model.add(y == 10 - x).only_enforce_if(b)
    # Second, not(b) implies y == 0.
    model.add(y == 0).only_enforce_if(~b)

    # Search for x values in increasing order.
    model.add_decision_strategy([x], cp_model.CHOOSE_FIRST,
                              cp_model.SELECT_MIN_VALUE)

    # Create a solver and solve with a fixed search.
    solver = cp_model.CpSolver()

    # Force the solver to follow the decision strategy exactly.
    solver.parameters.search_branching = cp_model.FIXED_SEARCH
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True

    # Search and print out all solutions.
    solution_printer = VarArraySolutionPrinter([x, y, b])
    solver.solve(model, solution_printer)



from ortools.sat.python import cp_model
solver = cp_model.CpSolver()


#https://developers.google.com/optimization/cp/channeling

model = cp_model.CpModel()
x = model.new_int_var(0, 10, 'x')
b = model.new_bool_var('b')
y = model.new_int_var(0, 10, 'y')
solution_printer = VarArraySolutionPrinter([x, b, y])
model.add(x >= 5).only_enforce_if(b)
model.add(x < 5).only_enforce_if(~b)
model.add(y == b*5 - x)
model.maximize(y)
status = solver.solve(model, solution_printer)



model = cp_model.CpModel()
x = model.new_int_var(0, 10, 'x')
b = model.new_bool_var('b')
y = model.new_int_var(0, 10, 'y')
solution_printer = VarArraySolutionPrinter([x, b, y])
model.add(x >= 5).only_enforce_if(b)
model.add(x < 5).only_enforce_if(~b)
model.add(y == b*5 - x)
model.maximize(y)
status = solver.solve(model, solution_printer)



model = cp_model.CpModel()
a = model.new_bool_var('a')
b = model.new_bool_var('b')
c = model.new_bool_var('c')
x = model.new_int_var(0, 10, 'x')
y = model.new_int_var(0, 10, 'y')
z = model.new_int_var(0, 10, 'z')

solution_printer = VarArraySolutionPrinter([x,y,z,a,b,c])

model.add_bool_or(a,b,c)
model.add_bool_and(a,b,c)
#model.add_bool_and(x,b,c)
#TypeError: TypeError: x is not a boolean variable


model.maximize(c)
status = solver.solve(model, solution_printer)

# if x < 0, y = 0
# else, y = 10 -x

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__doc__='yyyy'

s1 = Student('Mike', 12)
s2 = s1
print(s2.name)
s1.name = 'Lucy'
print(s2.name)
from copy import deepcopy
s3 = deepcopy(s1)
print(s3.name)
s1.name = 'OOO'
print(s3.name)



vars(Student)

vars(list)

x = 1
y = x
print(y)
x = 2
print(y)

