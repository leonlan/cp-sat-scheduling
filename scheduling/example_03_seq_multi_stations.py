"""
About changeover:
   - changeover cost is independently in objective function
   - The time index of tasks are not reflecting changeover events

function s is to see a sorted dict indexed by tuples

task 0 is only used in arcs

duration constraint is by end - start = duration
In Matthieu approach, no such constraint but there is new_optional_interval_var constraints that did this ?

We need task level start and end for convenience of working with more complicated constraints
"""


from ortools.sat.python import cp_model

# Initiate
M = 99999
model = cp_model.CpModel()


def s(x):
    sorted_keys = sorted(x)
    for key in sorted_keys:
        print(f"{key}, {x[key]}")

'''
task   product
1       A
2       B
3       A
4       B
'''

# 1. Data

tasks = {1, 2, 3, 4}
tasks_0 = tasks.union({0})
task_to_product = {0: 'dummy', 1: 'A', 2: 'B', 3: 'A', 4: 'B'}
processing_time = {'dummy': 0, 'A': 1, 'B': 1}
changeover_time = {'dummy': 0, 'A': 1, 'B': 1}
machines = {0, 1}
machines_starting_products = {0: 'A', 1: 'A'}

X = {
    (m, t1, t2)
    for t1 in tasks_0
    for t2 in tasks_0
    for m in machines
    if t1 != t2
}

m_cost = {
    (m, t1, t2): 0
    if task_to_product[t1] == task_to_product[t2] or (
            task_to_product[t1] == 'dummy' and task_to_product[t2] == machines_starting_products[m]
    )
    else changeover_time[task_to_product[t2]]
    for (m, t1, t2) in X
}

# 2. Decision variables
max_time = 8

variables_task_ends = {
    task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks
}

variables_task_starts = {
    task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks
}

variables_machine_task_starts = {
    (m, t): model.new_int_var(0, max_time, f"start_{m}_{t}")
    for t in tasks
    for m in machines
}
variables_machine_task_ends = {
    (m, t): model.new_int_var(0, max_time, f"start_{m}_{t}")
    for t in tasks
    for m in machines
}
variables_machine_task_presences = {
    (m, t): model.new_bool_var(f"presence_{m}_{t}")
    for t in tasks
    for m in machines
}

variables_machine_task_sequence = {
    (m, t1, t2): model.new_bool_var(f"Machine {m} task {t1} --> task {t2}")
    for (m, t1, t2) in X
}

# 3. Objectives

total_changeover_time = model.new_int_var(0, max_time, "total_changeover_time")

total_changeover_time = sum(
    [variables_machine_task_sequence[(m, t1, t2)]*m_cost[(m, t1, t2)] for (m, t1, t2) in X]
)

make_span = model.new_int_var(0, max_time, "make_span")

model.add_max_equality(
    make_span,
    [variables_task_ends[task] for task in tasks]
)
model.minimize(make_span + total_changeover_time)


# 4. Constraints

for task in tasks:

    # For this task

    # get all allowed machines
    task_candidate_machines = machines

    # find the subset in presence matrix related to this task
    tmp = [
        variables_machine_task_presences[m, task]
        for m in task_candidate_machines
    ]

    # this task is only present in one machine
    model.add_exactly_one(tmp)

    # task level link to machine-task level
    for m in task_candidate_machines:
        model.add(
            variables_task_starts[task] == variables_machine_task_starts[m, task]
        ).only_enforce_if(variables_machine_task_presences[m, task])

        model.add(
            variables_task_ends[task] == variables_machine_task_ends[m, task]
        ).only_enforce_if(variables_machine_task_presences[m, task])

        # The changeover consideration is done here by Mattheiu's approach


# This can be replaced by inverval variable ?
for task in tasks:
    model.add(
        variables_task_ends[task] - variables_task_starts[task] == processing_time[task_to_product[task]]
    )

# add_circuits

for machine in machines:

    arcs = list()

    tmp = [x for x in X if x[0] == machine]

    for (m, from_task, to_task) in tmp:
        arcs.append(
            [
                from_task,
                to_task,
                variables_machine_task_sequence[(m, from_task, to_task)]
            ]
        )

        if from_task != 0 and to_task != 0:
            model.add(
                variables_task_ends[from_task] <= variables_task_starts[to_task]
            ).only_enforce_if(variables_machine_task_sequence[(m, from_task, to_task)])

    for task in tasks:
        arcs.append([
            task, task, ~variables_machine_task_presences[(machine, task)]
        ])

    model.add_circuit(arcs)





# Solve

solver = cp_model.CpSolver()
status = solver.solve(model=model)

# Post-process

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    for task in tasks:
        print(f'Task {task} ',
              solver.value(variables_task_starts[task]), solver.value(variables_task_ends[task])
              )

    print(solver.value(make_span))

    for (m, t1, t2) in sorted(X):
        value = solver.value(variables_machine_task_sequence[(m, t1, t2)])
        if value == 1:
            print(f'Machine {m}: {t1} --> {t2}  ')

elif status == cp_model.INFEASIBLE:
    print("Infeasible")
