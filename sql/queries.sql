-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV by month
SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. Average 1-year return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 4. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Transactions by state
SELECT state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 6. SIP transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='SIP';

-- 7. Redemption transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type='Redemption';

-- 8. Highest Sharpe ratio funds
SELECT scheme_name, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 9. Average expense ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- 10. Funds by category
SELECT category,
COUNT(*)
FROM fact_performance
GROUP BY category;