from ortools.sat.python import cp_model

# Initiate
model = cp_model.CpModel()

tasks = {1}
processing_times = {1: 3}
max_time = 10
breaks = {(0, 2)}
shifts = {1, 2}
shift_starts = {1:0, 2:4}
shift_ends = {1:4, 2:8}


var_task_starts = {
    task: model.new_int_var(0, max_time, f"task_{task}_start") for task in tasks
}
var_task_ends = {
    task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks
}

var_shift_task_presence = {
    (shift, task): model.new_bool_var(f'task_{task}_is_in_shift_{shift}')
    for shift in shifts for task in tasks
}

for task in tasks:
    model.add(sum(var_shift_task_presence[shift, task] for shift in shifts) == 1 )

    for shift in shifts:
        model.add(var_task_starts[task] >= shift_starts[shift]).only_enforce_if(
            var_shift_task_presence[shift, task]
        )
        model.add(var_task_ends[task] <= shift_ends[shift]).only_enforce_if(
            var_shift_task_presence[shift, task]
        )


var_task_intervals = {
    task: model.new_interval_var(
        var_task_starts[task], processing_times[task], var_task_ends[task], name=f"interval_t{task}"
    ) for task in tasks
}

# Add break time
var_break_intervals = {
    (start, end): model.new_fixed_size_interval_var(start=start, size=end-start, name='a_break')
    for (start, end) in breaks
}


intervals = list(var_task_intervals.values()) + list(var_break_intervals.values())

demands = [1]*len(tasks) + [1]*len(breaks)

model.add_cumulative(intervals=intervals, demands=demands, capacity=1)


# 3. Objectives

make_span = model.new_int_var(0, max_time, "make_span")

model.add_max_equality(
    make_span,
    [var_task_ends[task] for task in tasks]
)

model.minimize(make_span)


# 4. Solve

solver = cp_model.CpSolver()
status = solver.solve(model=model)


# 5. Results

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:

    print('===========================  TASKS SUMMARY  ===========================')
    for task in tasks:
        print(f'Task {task} ',
              solver.value(var_task_starts[task]), solver.value(var_task_ends[task]),
              )

    print('Make-span:', solver.value(make_span))

elif status == cp_model.INFEASIBLE:
    print("Infeasible")
elif status == cp_model.MODEL_INVALID:
    print("Model invalid")
else:
    print(status)
