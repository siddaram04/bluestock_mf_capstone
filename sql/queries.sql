--1. Top 5 Funds by Highest Average Return Profile
SELECT scheme_code, AVG(return_1y) as avg_1y_return 
FROM fact_performance 
GROUP BY scheme_code 
ORDER BY avg_1y_return DESC 
LIMIT 5;

-- 2. Average NAV Metric per Month 
SELECT STRFTIME('%Y-%m', date) as month, AVG(nav) as average_nav 
FROM fact_nav 
GROUP BY month 
ORDER BY month ASC;

-- 3. Total Transaction Volume Grouped by Operational State Location
SELECT state, COUNT(*) as transaction_count, SUM(amount) as total_invested_capital
FROM fact_transactions 
GROUP BY state 
ORDER BY total_invested_capital DESC;

-- 4. Active Mutual Funds with Lean Operational Expense Ratios (< 1.0%)
SELECT scheme_code, expense_ratio 
FROM fact_performance 
WHERE expense_ratio < 1.0 
ORDER BY expense_ratio ASC;

-- 5. Aggregate Inflow Allocations by Structural Transaction Channels
SELECT transaction_type, COUNT(*) as volume, SUM(amount) as gross_amount
FROM fact_transactions 
GROUP BY transaction_type;

-- 6. High-Value Investment Allocations Exceeding 1 Lakh Units
SELECT transaction_id, scheme_code, amount, state 
FROM fact_transactions 
WHERE amount > 100000 
ORDER BY amount DESC;

-- 7. Audit Tracker for Identity Verifications (KYC Compliance Ratios)
SELECT kyc_status, COUNT(*) as total_investors, ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM fact_transactions), 2) as percentage
FROM fact_transactions 
GROUP BY kyc_status;

-- 8. Unique Assets Tracking Matrix Registry
SELECT COUNT(DISTINCT scheme_code) as total_active_schemes_monitored 
FROM fact_nav;

-- 9. Peak Operational Assets Valuation Performance Limits
SELECT scheme_code, MAX(nav) as historical_peak_nav, MIN(nav) as historical_floor_nav
FROM fact_nav 
GROUP BY scheme_code;

-- 10. Trailing Asset Growth Running Log Metrics
SELECT scheme_code, date, nav 
FROM fact_nav 
WHERE date >= DATE('now', '-30 days')
ORDER BY date DESC;