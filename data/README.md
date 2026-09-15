# Data

The project uses synthetic customer-support ticket data generated with a fixed random seed. No real customer or employer records are included.

Run `python src/generate_data.py` to create `data/tickets.csv`, then `python src/clean_data.py` to create `data/clean_tickets.csv`.

Generated files are intentionally excluded from Git; anyone can reproduce them locally.

Key fields include ticket ID, timestamps, channel, priority, issue type, support team, first-response hours, resolution hours, CSAT, status, reopen flag, and escalation flag.
