# Cleaning holding time (empty)

**Source:** `scheduling/example_19_cleaning_holding_time.py`

Empty file. Likely intended to model "cleaning events with a minimum or
maximum holding time" between tasks - a changeover interval that must
sit inside a specific window. See
[Changeover as event](./example_08_changeover_as_event.md); adding an
extra `min_hold <= co_duration <= max_hold` bound gives you the idea.
