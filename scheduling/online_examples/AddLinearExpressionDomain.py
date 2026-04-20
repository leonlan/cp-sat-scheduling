

from ortools.sat.python import cp_model
import pandas as pd

df = pd.DataFrame()

for ind_value in [0, 1]:
    for x_value in range(0, 20):
        model = cp_model.CpModel()

        x = model.new_int_var(0, 20, 'x')
        x_is_in_the_domain = model.new_bool_var('indicator')

        a_domain = cp_model.Domain.from_intervals([[1, 3], [5, 7]])
        b_domain = cp_model.Domain.from_intervals([[0], [4], [8,20]])

        model.add_linear_expression_in_domain(x, a_domain).only_enforce_if(x_is_in_the_domain)
        model.add_linear_expression_in_domain(x, b_domain).only_enforce_if(~x_is_in_the_domain)

        model.add(x_is_in_the_domain==ind_value)
        model.add(x==x_value)

        solver = cp_model.CpSolver()
        status = solver.solve(model=model)

        help_text = '1-3, 5-7' if ind_value==1 else '0, 4, 8-20'

        df_tmp = pd.DataFrame({
            'ind_value': [ind_value],
            'shall_be_in': [help_text],
            'x_value': [x_value],

            'status': [status]
        })

        df = pd.concat([df, df_tmp], axis=0)


from ortools.sat.python import cp_model

model = cp_model.CpModel()

x = model.new_int_var(0, 20, 'x')
x_is_in_the_domain = model.new_bool_var('indicator')

a_domain = cp_model.Domain.from_intervals([[1, 3], [5, 7]])
b_domain = cp_model.Domain.from_intervals([[0], [4], [8, 20]])

model.add_linear_expression_in_domain(x, a_domain).only_enforce_if(x_is_in_the_domain)
model.add_linear_expression_in_domain(x, b_domain).only_enforce_if(~x_is_in_the_domain)

solver = cp_model.CpSolver()
status = solver.solve(model=model)