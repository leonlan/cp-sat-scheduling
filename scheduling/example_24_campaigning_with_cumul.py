# Inspired by https://stackoverflow.com/questions/75554536

from ortools.sat.python import cp_model
from time import time
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

model = cp_model.CpModel()


def generate_one_product_data(num_tasks):
    """ Generate N tasks of product A """
    tasks = {i for i in range(num_tasks)}
    task_to_product = ({i: 'A' for i in range(int(num_tasks))})
    return tasks, task_to_product


def run_model(num_tasks, campaign_size, print_result = True):

    # if campaign size is 2, then we need cumul indicator to be 0, 1

    changeover_time = 2
    max_time = num_tasks*2
    processing_time = 1

    tasks, task_to_product = generate_one_product_data(num_tasks)
    var_task_starts = {task: model.new_int_var(0, max_time, f"task_{task}_start") for task in tasks}
    var_task_ends = {task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks}
    var_task_cumul = {task: model.new_int_var(0, campaign_size-1, f"task_{task}_cumul") for task in tasks}
    var_task_reach_max = {task: model.new_bool_var(f"task_{task}_reach_max") for task in tasks}

    for task in tasks:
        model.add(var_task_cumul[task] == campaign_size-1).only_enforce_if(var_task_reach_max[task])
        model.add(var_task_cumul[task] < campaign_size-1).only_enforce_if(~var_task_reach_max[task])

    var_task_intervals = {
        t: model.new_interval_var(
            var_task_starts[t],
            processing_time,
            var_task_ends[t],
            f"task_{t}_interval"
        )
        for t in tasks
    }
    model.add_no_overlap(var_task_intervals.values())

    make_span = model.new_int_var(0, max_time, "make_span")
    model.add_max_equality(make_span, [var_task_ends[task] for task in tasks])
    model.minimize(make_span)

    literals = {(t1, t2): model.new_bool_var(f"{t1} -> {t2}") for t1 in tasks for t2 in tasks if t1 != t2}

    arcs = []
    for t1 in tasks:
        arcs.append([-1, t1, model.new_bool_var(f"first_to_{t1}")])
        arcs.append([t1, -1, model.new_bool_var(f"{t1}_to_last")])
        for t2 in tasks:
            if t1 == t2:
                continue
            arcs.append([t1, t2, literals[t1, t2]])

            # if from task has not reached MAX, continue the campaign
            model.add(var_task_ends[t1] <= var_task_starts[t2]).only_enforce_if(
                literals[t1, t2]
            ).only_enforce_if(~var_task_reach_max[t1])
            model.add(var_task_cumul[t2] == var_task_cumul[t1] + 1).only_enforce_if(
                literals[t1, t2]
            ).only_enforce_if(~var_task_reach_max[t1])

            # if from task has reached MAX, apply changeover and reset its cumulative indicator
            model.add(var_task_cumul[t2] == 0).only_enforce_if(
                literals[t1, t2]
            ).only_enforce_if(var_task_reach_max[t1])
            model.add(var_task_ends[t1] + changeover_time <= var_task_starts[t2]).only_enforce_if(
                literals[t1, t2]
            ).only_enforce_if(var_task_reach_max[t1])

    model.add_circuit(arcs)

    solver = cp_model.CpSolver()
    start = time()
    status = solver.solve(model=model)
    total_time = time() - start

    if print_result:
        if status == cp_model.OPTIMAL:
            for task in tasks:
                print(f'Task {task} ',
                      solver.value(var_task_starts[task]),
                      solver.value(var_task_ends[task]),
                      solver.value(var_task_cumul[task]),
                      )
            print('-------------------------------------------------')
            print('Make-span:', solver.value(make_span))
        elif status == cp_model.INFEASIBLE:
            print("Infeasible")
        elif status == cp_model.MODEL_INVALID:
            print("Model invalid")
        else:
            print(status)

    return total_time


def print_unit_test_result(x, y1, y2, title=''):
    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(x, y1, marker='o', label = 'Campaign size: 2')
    plt.plot(x, y2, marker='o', label = 'Campaign size: 3')
    plt.legend()
    plt.title(title)
    plt.xlabel('The number of tasks')
    plt.ylabel('Seconds')
    plt.show()


if __name__ == '__main__':

    N = 8
    sizes = range(2, N+1)
    model_times_campaign_2 = []
    model_times_campaign_3 = []

    for num_task in sizes:
        model_times_campaign_2.append(run_model(num_task, campaign_size=2, print_result=False))
        model_times_campaign_3.append(run_model(num_task, campaign_size=3, print_result=False))

    print_unit_test_result(sizes, model_times_campaign_2, model_times_campaign_3,
                           'Scalability of Campaigning with Cumulative Indicator')