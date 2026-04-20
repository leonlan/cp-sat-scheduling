from ortools.sat.python import cp_model


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        print(variables)
        self.__solution_count = 0

    def on_solution_callback(self):
        self.__solution_count += 1
        # print('----------------------------------')
        # print(self.__variables)
        # for x in self.__variables:
        #     print(x)
        #     print(self)
        #     print(self.value(x))

        for v in self.__variables:
            # print(v)
            # print(self.value(vars[v]))
            print('%s=%i' % (v, self.value(v)), end=' ')

            # print(f"{v}, {self.value(v)}", end=' ')


        print()

    def solution_count(self):
        return self.__solution_count


def SearchForAllSolutionsSampleSat():
    """Showcases calling the solver to search for all solutions."""
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.
    num_vals = 3
    tasks = {'a', 'b', 'c'}
    vars = {
        task: model.new_int_var(0, num_vals - 1, f"task_{task}") for task in tasks
    }
    # x = model.new_int_var(0, num_vals - 1, 'x')
    # y = model.new_int_var(0, num_vals - 1, 'y')
    # z = model.new_int_var(0, num_vals - 1, 'z')

    # Create the constraints.
    model.add(vars['a'] != vars['b'])

    # Create a solver and solve.
    solver = cp_model.CpSolver()
    # solution_printer = VarArraySolutionPrinter([x, y, z])
    solution_printer = VarArraySolutionPrinter(vars.values())

    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # Solve.
    status = solver.solve(model, solution_printer)

    #status = solver.solve(model)


    # print('Status = %s' % solver.status_name(status))
    # print('Number of solutions found: %i' % solution_printer.solution_count())


SearchForAllSolutionsSampleSat()
