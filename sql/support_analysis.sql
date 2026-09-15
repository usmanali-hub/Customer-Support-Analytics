-- Assumes a table named support_tickets.

-- 1. Overall KPI snapshot
SELECT
    COUNT(*) AS tickets,
    ROUND(100.0 * AVG(CASE WHEN resolution_hours <= sla_hours THEN 1 ELSE 0 END), 2) AS sla_attainment_pct,
    ROUND(AVG(first_response_hours), 2) AS avg_first_response_hours,
    ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours,
    ROUND(AVG(customer_satisfaction), 2) AS avg_csat,
    ROUND(100.0 * AVG(CASE WHEN escalated THEN 1 ELSE 0 END), 2) AS escalation_rate_pct
FROM support_tickets;

-- 2. Performance by channel
SELECT channel, COUNT(*) AS tickets,
       ROUND(AVG(first_response_hours), 2) AS avg_first_response_hours,
       ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours,
       ROUND(AVG(customer_satisfaction), 2) AS avg_csat
FROM support_tickets
GROUP BY channel
ORDER BY tickets DESC;

-- 3. SLA performance by priority
SELECT priority, COUNT(*) AS tickets,
       ROUND(100.0 * AVG(CASE WHEN resolution_hours <= sla_hours THEN 1 ELSE 0 END), 2) AS sla_attainment_pct
FROM support_tickets
GROUP BY priority
ORDER BY sla_attainment_pct;

-- 4. Issue types driving support workload
SELECT issue_type, COUNT(*) AS tickets,
       ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours,
       ROUND(100.0 * AVG(CASE WHEN escalated THEN 1 ELSE 0 END), 2) AS escalation_rate_pct
FROM support_tickets
GROUP BY issue_type
ORDER BY tickets DESC;

-- 5. Monthly support trend
SELECT DATE_TRUNC('month', created_at) AS month,
       COUNT(*) AS tickets,
       ROUND(AVG(customer_satisfaction), 2) AS avg_csat,
       ROUND(AVG(resolution_hours), 2) AS avg_resolution_hours
FROM support_tickets
GROUP BY 1
ORDER BY 1;
