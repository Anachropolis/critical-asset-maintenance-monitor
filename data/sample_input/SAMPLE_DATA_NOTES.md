# Sample Input Data Notes

This folder contains fictional sample input data for the Critical Asset Maintenance Monitor project.

## Files

- `maintenance_events.json`: Mock API event data representing scheduled maintenance/outage events.
- `critical_assets.csv`: Internal reference list of assets, criticality, redundancy groups, and path roles.
- `event_status_reference.csv`: Optional reference explaining which event statuses should be included in analysis.

## Intentional Test Cases

The sample data includes:

1. High-criticality assets affected by scheduled events.
2. Overlapping events in the same redundancy group:
   - North Supply: EVT-1001 and EVT-1002 overlap.
   - East Supply: EVT-1003 and EVT-1004 overlap.
   - South Supply: EVT-1009 and EVT-1010 overlap.
3. Medium and low criticality assets.
4. Completed and cancelled events that should usually be excluded.
5. An unmapped event asset, `UNK-999`, that does not appear in the critical asset list.

All data is fictional and safe for public GitHub use.
