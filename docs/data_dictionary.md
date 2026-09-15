# Data Dictionary

| Field | Meaning | Analytical use |
|---|---|---|
| ticket_id | Unique synthetic ticket identifier | Validation and traceability |
| created_at | Ticket creation timestamp | Demand and trend analysis |
| resolved_at | Ticket resolution timestamp | Resolution-time analysis |
| channel | Customer contact channel | Channel workload comparison |
| priority | Ticket priority | SLA and workload segmentation |
| issue_type | Support issue category | Root-cause analysis |
| agent_team | Team handling the ticket | Team performance |
| first_response_hours | Hours until first response | Responsiveness KPI |
| resolution_hours | Hours until resolution | Resolution KPI |
| sla_met | Whether the SLA target was met | SLA attainment |
| customer_satisfaction | Customer satisfaction score | Customer outcome |
| escalated | Whether the ticket was escalated | Operational complexity |
| reopened | Whether the ticket was reopened | Resolution quality |

## Interpretation rules

- Percentages are calculated from ticket-level observations.
- P90 response/resolution metrics are used to expose long-tail customer experiences that averages can hide.
- Segment comparisons should consider volume before operational decisions are made.
- Data is synthetic and contains no private customer, employer, or production support records.
