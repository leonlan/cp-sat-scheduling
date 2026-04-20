from ortools.sat.python import cp_model

# Initiate
model = cp_model.CpModel()

jobs = {1, 2}
stages = {1, 2, 3}
tasks = {(job, stage) for job in jobs for stage in stages}

processing_time = 3
max_time = 20

# 1. Jobs
var_job_starts = {
    job: model.new_int_var(0, max_time, f"job_{job}_start") for job in jobs
}

var_job_ends = {
    job: model.new_int_var(0, max_time, f"job_{job}_end") for job in jobs
}

# 2. Tasks
var_task_starts = {
    (job, stage): model.new_int_var(0, max_time, f"job_{job}_stage_{stage}_start") for (job, stage) in tasks
}

var_task_ends = {
    (job, stage): model.new_int_var(0, max_time, f"job_{job}_stage_{stage}_end") for (job, stage) in tasks
}


for job in jobs:
    model.add_min_equality(var_job_starts[job], [var_task_starts[job, stage] for stage in stages])
    model.add_max_equality(var_job_ends[job], [var_task_ends[job, stage] for stage in stages])

    for stage in stages:
        if stage == len(stages):
            continue
        model.add(var_task_ends[job, stage] <= var_task_starts[job, stage + 1])


var_task_intervals = {
    (job, stage): model.new_interval_var(
        var_task_starts[job, stage],
        processing_time,
        var_task_ends[job, stage],
        name=f"interval_job_{job}_stage_{stage}"
    )
    for job in jobs
    for stage in stages
}

for stage in stages:
    model.add_no_overlap(var_task_intervals[job, stage] for job in jobs)

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
    for job in jobs:
        print(f"job_{job}  start: {solver.value(var_job_starts[job])}   end:{solver.value(var_job_ends[job])}")
        for stage in stages:
            print(f'Stage {stage} ',
                  solver.value(var_task_starts[job, stage]), solver.value(var_task_ends[job, stage]),
                  )

    print('Make-span:', solver.value(make_span))

elif status == cp_model.INFEASIBLE:
    print("Infeasible")
elif status == cp_model.MODEL_INVALID:
    print("Model invalid")
else:
    print(status)
