# CP for Job Shop Problems
Examples of basic elements of general scheduling with OR-Tools CP-SAT

## Scheduling examples

- [x] `example_00_unit_tests.py` - Sandbox of CP-SAT primitives (`AddBoolOr/And/XOr`, `OnlyEnforceIf`, reification, `AddLinearExpressionInDomain`).
- [x] `example_01_simple_sequence.py` - Single-machine sequencing with a dummy task and `AddCircuit`; changeover in the objective.
- [ ] `example_02_seq_lock_starting_product.py` - Same as 01, but the dummy task has a fixed starting product.
- [ ] `example_03_seq_multi_stations.py` - Multi-machine sequencing with per-machine circuits; objective is makespan + changeover.
- [ ] `example_03_seq_scale.py` - Benchmark harness of the multi-machine model (no intervals).
- [ ] `example_03_seq_scale_Mathieu.py` - Interval-based rewrite of the same benchmark, scales to ~80 tasks.
- [ ] `example_04_seq_with_changeover_in_constraint.py` - Moves changeover into the precedence constraint instead of the objective.
- [ ] `example_05_seq_with_intervals.py` - Replaces `end - start == duration` with `NewOptionalIntervalVar`.
- [ ] `example_06_seq_with_intervals_resource.py` - Adds a global `AddCumulative` resource shared across machines.
- [ ] `example_07_break_without_changeover.py` - Single machine with a fixed break interval; demonstrates `AddDecisionStrategy`.
- [ ] `example_08_changeover_as_event.py` - Changeover modeled as its own optional interval between tasks.
- [ ] `example_09_max_number_of_continuous_tasks.py` - Campaigning: group same-product tasks, enforce max size, sequence campaigns.
- [ ] `example_10_people_mode.py` - Flexible resource modes with different processing times and headcount per task.
- [ ] `example_11_resource_mode.py` - Empty.
- [ ] `example_12_an_automatic_job.py` - Automatic job whose runtime does not consume the operator; breaks handled via cumulative.
- [ ] `example_13_automatic_jobs.py` - Same idea as 12 with two tasks and circuit sequencing.
- [ ] `example_14_task_delaying_break.py` - A task overlapping a break has its duration stretched via per-slot booleans.
- [ ] `example_15_events_overlapping.py` - Detect overlap and overlap duration between two fixed intervals.
- [ ] `example_16_shift_crossing_fake_time_unit.py` - Prevents tasks from crossing shifts using synthetic break intervals.
- [ ] `example_17_shift_crossing_mathieu.py` - Alternative: assign each task to exactly one shift with presence booleans.
- [ ] `example_18_campaigning_time_constraint.py` - Empty.
- [ ] `example_19_cleaning_holding_time.py` - Empty.
- [ ] `example_21_stages_one_job.py` - Multi-stage single job with stage precedence.
- [ ] `example_22_stages_two_jobs.py` - Two jobs with `NoOverlap` per stage.
- [ ] `example_23_multistage_two_jobs_co.py` - Scales 22 to 6 jobs x 3 stages.
- [ ] `example_24_campaigning_with_cumul.py` - Campaigning via a cumulative rank variable and `reach_max` flag; scalability study.
- [ ] `example_25_campaigning_with_locked_seq.py` - Same cumulative-rank campaigning but with a locked task order heuristic.
- [ ] `example_26_campaigning_locked_seq_improved.py` - Removes the forced reach-max implication; solver decides when to end a campaign.
- [ ] `example_26_campaigning_locked_seq_improved_flexible.py` - Looser order lock (`start[t-1] <= start[t]`) for more flexibility.
- [ ] `example_27_campaigning_products.py` - Campaigning across multiple products with product-change indicators.
- [ ] `example_28_campaigning_products_machines.py` - 27 extended to multiple machines.
- [ ] `example_29_linear_domain_for_breaks.py` - Breaks via cumulative vs. `AddLinearExpressionInDomain` on task starts.
- [ ] `example_30_campaigning_with_pregrouping.py` - Empty.
- [ ] `example_31_campaigning_faster.py` - Faster refinement of the multi-machine campaigning model.
- [ ] `example_32_solving_by_phases.py` - Incremental solving with warm-start hints across phases of increasing `max_time`.
- [ ] `example_33_conditional_duration_linear_domain.py` - Duration switches based on whether the start is in a break domain.
- [ ] `example_34_headcount_tracking.py` - Three methods for tracking time-varying resource usage.
