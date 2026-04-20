# This script benchmark MIP style Constraints V.S. Using add_circuit

from ortools.sat.python import cp_model
from time import time
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from tqdm import tqdm


def add_circuit_constraints(model, tasks, var_task_starts, var_task_ends, literals):
    arcs = []
    for t1 in tasks:
        arcs.append([0, t1, model.new_bool_var(f"first_to_{t1}")])
        arcs.append([t1, 0, model.new_bool_var(f"{t1}_to_last")])
        for t2 in tasks:
            if t1 == t2:
                continue
            arcs.append([t1, t2, literals[t1, t2]])
            model.add(var_task_ends[t1] <= var_task_starts[t2]).only_enforce_if(literals[t1, t2])
    model.add_circuit(arcs)


def add_mip_style_constraints(model, tasks, var_task_starts, var_task_ends, literals):
    for task in tasks:
        literals.update({(0, task): model.new_bool_var(f"first_to_{task}")})
        literals.update({(task, 0): model.new_bool_var(f"{task}_to_last")})

    tasks_aug = tasks.union({0})

    # Only one task go to this task
    for t_j in tasks_aug:
        tmp = [literals[task, t_j] for task in tasks_aug if task != t_j]
        model.add(sum(tmp) == 1)

    # This task only goes to one task
    for t_i in tasks_aug:
        tmp = [literals[t_i, task] for task in tasks_aug if t_i != task]
        model.add(sum(tmp) == 1)

    #
    for t1 in tasks:
        for t2 in tasks:
            if t1 == t2:
                continue
            model.add(var_task_ends[t1] <= var_task_starts[t2]).only_enforce_if(literals[t1, t2])


def run_model_add_circuit(num_tasks):
    """ Using add_circuit for sequence optimization """
    model = cp_model.CpModel()
    max_time = num_tasks
    tasks = {i+1 for i in range(num_tasks)}
    processing_time = 1
    var_task_starts = {
        task: model.new_int_var(0, max_time, f"task_{task}_start") for task in tasks
    }
    var_task_ends = {
        task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks
    }
    var_intervals = {
        task: model.new_interval_var(
            var_task_starts[task], processing_time, var_task_ends[task], f"interval_{task}"
        )
        for task in tasks
    }
    model.add_no_overlap(var_intervals.values())
    # Sequence optimizing Using add_circuit
    literals = {(t1, t2): model.new_bool_var(f"{t1} -> {t2}") for t1 in tasks for t2 in tasks if t1!=t2}
    add_circuit_constraints(model, tasks, var_task_starts, var_task_ends, literals)
    # Objective
    make_span = model.new_int_var(0, max_time, "make_span")
    model.add_max_equality(make_span, [var_task_ends[task] for task in tasks])
    model.minimize(make_span)
    # Solve
    solver = cp_model.CpSolver()
    start = time()
    status = solver.solve(model=model)
    total_time = time() - start
    if status == cp_model.OPTIMAL:
        return total_time
    else:
        return -999


def run_model_MIPStyle(num_tasks):
    """ Using MIP style constraints for sequence optimization """

    model = cp_model.CpModel()
    max_time = num_tasks
    tasks = {i+1 for i in range(num_tasks)}
    processing_time = 1
    var_task_starts = {
        task: model.new_int_var(0, max_time, f"task_{task}_start") for task in tasks
    }
    var_task_ends = {
        task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks
    }
    var_intervals = {
        task: model.new_interval_var(
            var_task_starts[task], processing_time, var_task_ends[task], f"interval_{task}"
        )
        for task in tasks
    }
    model.add_no_overlap(var_intervals.values())
    # Sequence optimizing Using MIP style
    literals = {(t1, t2): model.new_bool_var(f"{t1} -> {t2}") for t1 in tasks for t2 in tasks if t1 != t2}
    add_mip_style_constraints(model, tasks, var_task_starts, var_task_ends, literals)
    # Objective
    make_span = model.new_int_var(0, max_time, "make_span")
    model.add_max_equality(make_span, [var_task_ends[task] for task in tasks])
    model.minimize(make_span)
    # Solve
    solver = cp_model.CpSolver()
    start = time()
    status = solver.solve(model=model)
    total_time = time() - start
    if status == cp_model.OPTIMAL:
        return total_time
    else:
        return -999


if __name__ == '__main__':

    N = 80

    sizes_1 = list(range(2, N))
    sizes_2 = list(range(2, N))

    model_1_times = []
    model_2_times = []

    print("\nadd_circuit\n")
    for size in tqdm(sizes_1):
        model_1_times.append(run_model_add_circuit(size))

    print("\nMIP-style\n")
    for size in tqdm(sizes_2):
        model_2_times.append(run_model_MIPStyle(size))

    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(sizes_1, model_1_times, marker='o', label='add_circuit')
    plt.plot(sizes_2, model_2_times, '-.', marker='o', label='MIP-style')
    plt.legend()
    plt.title('Performance benchmarking')
    plt.xlabel('The number of tasks')
    plt.ylabel('Seconds')
    plt.show()
