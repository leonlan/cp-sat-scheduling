# Campaigning with pregrouping (empty)

**Source:** `scheduling/example_30_campaigning_with_pregrouping.py`

Empty file. Likely intended to pre-group tasks into candidate campaigns
outside the solver, then let CP-SAT only sequence the pre-built groups.
The closest working realisation is
[Max number of continuous tasks](./example_09_max_number_of_continuous_tasks.md);
fixing which tasks go into which campaign before solving gives you the
pregrouping variant.
