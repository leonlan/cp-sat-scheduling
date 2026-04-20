# Examples overview

Each example in this section corresponds to one Python file under
`scheduling/`. Chapters are kept short: a brief description, the concepts it
demonstrates (linked back to the [Concepts](../concepts/cp-sat-basics.md)
section), and the source file inlined at the bottom.

Examples are grouped by topic in the sidebar:

- **Basics** - CP-SAT primitives and small modeling tricks.
- **Sequencing** - ordering tasks on one or more machines.
- **Changeover and intervals** - different ways to model switches between
  products and the move from manual durations to interval variables.
- **Breaks** - unavailable time windows, including breaks that extend a
  task's duration and automatic jobs that only need an operator for setup.
- **Shifts** - preventing tasks from crossing shift boundaries.
- **Multi-stage jobs** - jobs with ordered stages and per-stage capacity.
- **Resources** - flexible resource/headcount modes and time-varying
  demand tracking.
- **Campaigning** - grouping same-product tasks between changeovers, with
  multiple modelling approaches.
- **Solver techniques** - warm-starting CP-SAT across phases with hints.

A few files (`example_11`, `example_18`, `example_19`, `example_30`) are
empty placeholders kept for numbering; their chapters only note what they
would have covered.
