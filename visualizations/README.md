# Visualizations

The portfolio charts are committed as SVG so they render directly on GitHub.

- `monthly_ticket_volume.svg` — demand trend
- `sla_by_priority.svg` — SLA attainment by priority
- `csat_by_channel.svg` — customer satisfaction by channel
- `resolution_by_issue.svg` — median resolution time by issue type

Regenerate them with `python src/create_visualizations.py` after generating and cleaning the fixed-seed synthetic dataset.