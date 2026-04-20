# This script analyze the scalability of the campaigning concept
# This script is based on example_09_max_number_of_continuous_tasks.py

from ortools.sat.python import cp_model
from time import time
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from tqdm import tqdm


def generate_data(num_tasks):
    tasks = {i+1 for i in range(num_tasks)}
    tasks_0 = tasks.union({0})
    task_to_product = {0: 'dummy'}
    task_to_product.update({x+1: 'A' for x in range(int(num_tasks/2))})
    task_to_product.update({x+1: 'B' for x in range(int(num_tasks/2), int(num_tasks))})
    return tasks, tasks_0, task_to_product


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


def run_model(num_tasks, max_conti_task_num):

    # data preparation
    # The examples in the code afterward is for num_tasks = 4 and max_conti_task_num = 2
    processing_time = 1
    changeover_time = 2
    max_time = num_tasks*2
    products = {'A', 'B'}
    tasks, _, task_to_product = generate_data(num_tasks)

    model = cp_model.CpModel()

    # Campaign related data pre=processing/mapping
    max_product_campaigns = {
        product: len([task for task in tasks if task_to_product[task] == product])
        for product in products
    }
    # {'B': 2, 'A': 2}

    product_campaigns = {
        (product, f"{product}_{campaign}")
        for product in max_product_campaigns
        for campaign in list(range(0, max_product_campaigns[product]))
    }
    # {('A', 'A_0'), ('A', 'A_1'), ('B', 'B_0'), ('B', 'B_1')}

    campaign_to_product = {
        campaign: product for product, campaign in product_campaigns
    }
    # {'A_0': 'A', 'B_0': 'B', 'B_1': 'B', 'A_1': 'A'}

    campaigns = {campaign for product, campaign in product_campaigns}
    # {'A_0', 'A_1', 'B_0', 'B_1'}

    product_to_campaigns = {
        product: [c for c in campaigns if campaign_to_product[c] == product] for product in products
    }
    # {'B': ['B_0', 'B_1'], 'A': ['A_1', 'A_0']}

    task_to_campaigns = {
        task: [
            campaign for campaign in campaigns if
            campaign_to_product[campaign] == task_to_product[task]
        ]
        for task in tasks
    }
    # {1: ['A_1', 'A_0'], 2: ['A_1', 'A_0'], 3: ['B_0', 'B_1'], 4: ['B_0', 'B_1']}

    campaign_size = {campaign: max_conti_task_num for campaign in campaigns}
    # {'A_1': 2, 'A_0': 2, 'B_0': 2, 'B_1': 2}

    campaign_duration = {campaign: max_conti_task_num for campaign in campaigns}
    # {'A_1': 2, 'A_0': 2, 'B_0': 2, 'B_1': 2}

    campaign_to_tasks = {
        campaign:
            [
                task for task in tasks if campaign in task_to_campaigns[task]
            ]
        for campaign in campaigns
    }
    # {'A_1': [1, 2], 'A_0': [1, 2], 'B_0': [3, 4], 'B_1': [3, 4]}

    distances_campaign = {
        (c1, c2): 0
        if campaign_to_product[c1] == campaign_to_product[c2] else changeover_time
        for c1 in campaigns for c2 in campaigns
        if c1 != c2
    }
    # {('A_1', 'A_0'): 0,
    #  ('A_1', 'B_0'): 1,
    #  ('A_1', 'B_1'): 1,
    #  ('A_0', 'A_1'): 0,
    #  ('A_0', 'B_0'): 1,
    #  ('A_0', 'B_1'): 1,
    #  ('B_0', 'A_1'): 1,
    #  ('B_0', 'A_0'): 1,
    #  ('B_0', 'B_1'): 0,
    #  ('B_1', 'A_1'): 1,
    #  ('B_1', 'A_0'): 1,
    #  ('B_1', 'B_0'): 0}

    # Task level
    variables_task_ends = {
        task: model.new_int_var(0, max_time, f"task_{task}_end") for task in tasks
    }
    variables_task_starts = {
        task: model.new_int_var(0, max_time, f"task_{task}_start") for task in tasks
    }

    var_task_intervals = {
        t: model.new_interval_var(
            variables_task_starts[t],
            processing_time,
            variables_task_ends[t],
            f"task_{t}_interval"
        )
        for t in tasks
    }
    # model.add_no_overlap([x for x in var_task_intervals.values()])
    model.add_no_overlap(list(var_task_intervals.values()))

    # Objectives
    make_span = model.new_int_var(0, max_time, "make_span")
    model.add_max_equality(
        make_span,
        [variables_task_ends[task] for task in tasks]
    )
    model.minimize(make_span)

    # Campaigning related

    var_campaign_starts = {
        c: model.new_int_var(0, max_time, f"start_{c}") for c in campaigns
    }

    var_campaign_ends = {
        c: model.new_int_var(0, max_time, f"c_end_{c}") for c in campaigns
    }

    var_campaign_durations = {
        c: model.new_int_var(0, max_time, f"c_duration_{c}") for c in campaigns
    }

    var_campaign_presences = {
        c: model.new_bool_var(f"c_presence_{c}") for c in campaigns
    }

    var_campaign_intervals = {
        c: model.new_optional_interval_var(
            var_campaign_starts[c],
            var_campaign_durations[c],
            var_campaign_ends[c],
            var_campaign_presences[c],
            f"c_interval_{c}"
        )
        for c in campaigns
    }

    model.add_no_overlap(list(var_campaign_intervals.values()))

    # If a task in allocated to a campaign
    var_task_campaign_presences = {
        (t, c): model.new_bool_var(f"task_{t}_presence_in_campaign_{c}") for t in tasks for c in task_to_campaigns[t]
    }

    # add_campaign_definition_constraints
    # 1. Campaign definition: Start & duration based on tasks that belongs to the campaign

    for c in campaigns:
        #  1. Duration definition
        model.add(
            var_campaign_durations[c] == sum(
                processing_time * var_task_campaign_presences[t, c]
                for t in campaign_to_tasks[c]
            )
        )
        # 2. Start-end definition
        for t in campaign_to_tasks[c]:

            model.add(var_campaign_starts[c] <= variables_task_starts[t]).only_enforce_if(
                var_task_campaign_presences[t, c]
            )
            model.add(variables_task_ends[t] <= var_campaign_ends[c]).only_enforce_if(
                var_task_campaign_presences[t, c]
            )
        # 3. Link c & tc presence: If 1 task is scheduled on a campaign -> presence[t, c] = 1 ==> presence[c] == 1
        # as long as there is one task in a campaign, this campaign must be present
        model.add_max_equality(
            var_campaign_presences[c], [var_task_campaign_presences[t, c] for t in campaign_to_tasks[c]]
        )

    # 2. Definition of the bool var: if a task belongs to a campaign
    for task in tasks:
        # One task belongs to at most 1 campaign
        # task_to_campaigns[task]
        model.add(
            sum(var_task_campaign_presences[task, campaign]
                for campaign in campaigns
                if campaign in task_to_campaigns[task]
                ) == 1
            )

    for c in campaigns:
        model.add(
            var_campaign_durations[c] <= max_conti_task_num
        )


    # Add campaign circuit

    arcs = []

    var_campaign_sequence = {}

    for node_1, campaign_1 in enumerate(campaigns):

        tmp1 = model.new_bool_var(f'first_to_{campaign_1}')
        arcs.append([
            0, node_1 + 1, tmp1
        ])

        tmp2 = model.new_bool_var(f'{campaign_1}_to_last')
        arcs.append([
            node_1 + 1, 0, tmp2
        ])

        arcs.append([node_1 + 1, node_1 + 1, ~var_campaign_presences[campaign_1]])

        # for outputting
        var_campaign_sequence.update({(0, campaign_1): tmp1})
        var_campaign_sequence.update({(campaign_1, 0): tmp2})

        for node_2, campaign_2 in enumerate(campaigns):

            if node_1 == node_2:
                continue

            indicator_node_1_to_node_2 = model.new_bool_var(f'{campaign_1}_to_{campaign_2}')

            var_campaign_sequence.update({(campaign_1, campaign_2): indicator_node_1_to_node_2})

            distance = distances_campaign[campaign_1, campaign_2]

            arcs.append([node_1 + 1, node_2 + 1, indicator_node_1_to_node_2])

            model.add(
                var_campaign_ends[campaign_1] + distance <= var_campaign_starts[campaign_2]
            ).only_enforce_if(
                indicator_node_1_to_node_2
            ).only_enforce_if(
                var_campaign_presences[campaign_1]
            ).only_enforce_if(
                var_campaign_presences[campaign_2]
            )

    model.add_circuit(arcs)

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

    sizes = [2, 4, 6, 8]

    max_conti_task_num = 2

    model_times = []

    for size in tqdm(sizes):
        model_times.append(run_model(size, max_conti_task_num))

    ax = plt.figure().gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(sizes, model_times, marker='o')
    plt.legend()
    plt.title(f'Campaigning with {int(size/2)} A/B orders respectively and campaign limit {max_conti_task_num}')
    plt.xlabel('The number of total tasks (A+B)')
    plt.ylabel('Seconds')
    plt.show()
