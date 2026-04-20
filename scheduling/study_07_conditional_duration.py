from ortools.sat.python import cp_model
from time import time
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from ortools.sat import cp_model_pb2
import pandas as pd
import string
from tqdm import tqdm


def run_model(num_of_tasks=3, break_offset=0):
    """
    Offset = 0:
        | x |   |   | x |   |   | x |   |   |
    Offset = 1:
        |   | x |   |   | x |   |   | x |   |
    Offset = 2:
        |   |   | x |   |   | x |   |   | x |

    where x represent a unit duration break period

    """
    break_offset = 0

    max_time = num_of_tasks * 3
    processing_time = 2

    if break_offset == 0:
        help_text = "| x |   |   | x |   |   | x |   |   |"
    elif break_offset == 1:
        help_text = "|   | x |   |   | x |   |   | x |   |"
    elif break_offset == 2:
        help_text = "|   |   | x |   |   | x |   |   | x |"
    else:
        print("offset wrong")
        exit()

    breaks = [(i * num_of_tasks + break_offset, i * num_of_tasks + break_offset + 1) for i in range(num_of_tasks)]
    tasks = {x for x in range(num_of_tasks)}
    starts_no_break = [x * 3 + break_offset + 1 for x in range(-1, num_of_tasks) if x * 3 + break_offset + 1 >= 0]
    starts_break = list(set(range(max_time)).difference(starts_no_break))
    domain_no_break = cp_model.Domain.from_intervals([[x] for x in starts_no_break])
    domain_break = cp_model.Domain.from_intervals([[x] for x in starts_break])

    model = cp_model.CpModel()

    var_task_starts = {task: model.new_int_var(0, max_time, f"task_{task}_start") for task in tasks}
    var_task_ends = {task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks}
    var_task_durations = {task: model.new_int_var(2, 3, f"task_{task}_end") for task in tasks}
    var_task_overlap_break = {task: model.new_bool_var(f"task_{task}_overlap_a_break") for task in tasks}

    # print("Heuristic 1: Apply the tasks sequence heuristics")
    for task in tasks:
        if task == 0:
            continue
        model.add(var_task_ends[task - 1] <= var_task_starts[task])

    for task in tasks:
        model.add_linear_expression_in_domain(var_task_starts[task], domain_break).only_enforce_if(
            var_task_overlap_break[task]
        )

        model.add_linear_expression_in_domain(var_task_starts[task], domain_no_break).only_enforce_if(
            ~var_task_overlap_break[task]
        )

        model.add(var_task_durations[task] == processing_time + 1).only_enforce_if(
            var_task_overlap_break[task]
        )

        model.add(var_task_durations[task] == processing_time).only_enforce_if(
            ~var_task_overlap_break[task]
        )

    # intervals
    var_intervals = {
        task: model.new_interval_var(
            var_task_starts[task],
            var_task_durations[task],
            var_task_ends[task],
            name=f"interval_{task}"
        )
        for task in tasks
    }

    model.add_no_overlap(var_intervals.values())

    # Objectives
    make_span = model.new_int_var(0, max_time, "make_span")
    model.add_max_equality(
        make_span,
        [var_task_ends[task] for task in tasks]
    )

    model.minimize(make_span + sum(var_task_durations.values()))
    # model.minimize(sum(var_task_durations))

    solver = cp_model.CpSolver()
    start = time()
    status = solver.solve(model=model)
    total_time = time() - start

    print_result = False
    # show the result if getting the optimal one
    if print_result:
        print("-----------------------------------------")
        print(help_text)
        print("breaks periods:", breaks)
        print("break starts:", starts_break)
        print("no break starts:", starts_no_break)

        if status == cp_model.OPTIMAL:
            big_list = []
            for task in tasks:
                tmp = [
                    f"task {task}",
                    solver.value(var_task_starts[task]),
                    solver.value(var_task_ends[task]),
                    solver.value(var_task_overlap_break[task]),
                    solver.value(var_task_durations[task]),
                ]
                big_list.append(tmp)
            df = pd.DataFrame(big_list)
            df.columns = ['task', 'start', 'end', 'overlap_break', 'duration']
            df = df.sort_values(['start'])
            print(df)
            print('Make-span:', solver.value(make_span))
        elif status == cp_model.INFEASIBLE:
            print("Infeasible")
        elif status == cp_model.MODEL_INVALID:
            print("Model invalid")
        else:
            print(status)

    if status == cp_model.OPTIMAL:
        return total_time
    else:
        return -999


if __name__ == '__main__':

    sizes = range(3, 90, 3)

    model_times = []

    for size in tqdm(sizes):
        model_times.append(run_model(size))

    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(sizes, model_times, marker='o')
    plt.legend()
    plt.title(f'Conditional durations')
    plt.xlabel('The number of total tasks')
    plt.ylabel('Seconds')
    plt.show()
