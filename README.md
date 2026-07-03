# Bluestock Mutual Fund Analytics Capstone

## Data Analyst Internship Project

This project was developed as part of the **Data Analyst Internship at Bluestock Fintech**. The objective is to analyze mutual fund data, perform data cleaning, build an analytical database, conduct exploratory data analysis (EDA), evaluate fund performance, compute financial risk metrics, and generate actionable investment insights using **Python, SQL, SQLite, and data visualization**.

---

## Project Structure

```text
Bluestock_MF_Capstone/
│
├── charts/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── reports/
├── scripts/
├── sql/
│
├── bluestock_mf.db
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- SQL
- Jupyter Notebook
- Matplotlib
- Seaborn
- Plotly
- SciPy
- Git & GitHub

---

# Day 1: Data Ingestion

## Tasks Completed

- Created the project folder structure.
- Initialized Git and GitHub repositories.
- Installed required Python libraries.
- Loaded and explored all datasets using Pandas.
- Developed data ingestion scripts.
- Retrieved live NAV data using the Mutual Fund API.
- Performed initial data validation.
- Generated data quality reports.

## Deliverables

- Data Ingestion Notebook
- Data Quality Report
- Live NAV Fetch Script
- Requirements File

---

# Day 2: Data Cleaning & Database Design

## Tasks Completed

- Cleaned and standardized mutual fund datasets.
- Validated NAV history and transaction records.
- Created processed datasets.
- Designed a relational SQLite database schema.
- Loaded cleaned datasets into SQLite using SQLAlchemy.
- Wrote analytical SQL queries.
- Prepared a comprehensive data dictionary.

## Deliverables

- Cleaned CSV Files
- SQLite Database (`bluestock_mf.db`)
- SQL Schema
- SQL Queries
- Data Dictionary

---

# Day 3: Exploratory Data Analysis (EDA)

## Tasks Completed

- Analyzed NAV trends across schemes.
- Studied Assets Under Management (AUM) growth.
- Evaluated monthly SIP inflows.
- Analyzed category-wise inflows.
- Examined investor demographics.
- Performed geographic investment analysis.
- Conducted fund correlation analysis.
- Analyzed portfolio allocations.
- Generated business insights using visualizations.

## Deliverables

- EDA Notebook
- Trend Charts
- Correlation Analysis
- Business Insights

---

# Day 4: Performance Analytics & Fund Evaluation

## Tasks Completed

- Calculated Daily Returns.
- Computed CAGR for all schemes.
- Calculated Sharpe Ratio.
- Calculated Sortino Ratio.
- Performed Alpha & Beta analysis.
- Calculated Maximum Drawdown.
- Measured Tracking Error.
- Developed a composite Fund Scorecard (0–100).
- Ranked mutual funds using multiple performance metrics.
- Compared fund performance against NIFTY benchmarks.
- Generated benchmark comparison visualizations.

## Deliverables

- Performance_Analytics.ipynb
- CAGR Report
- Sharpe Ratio Report
- Sortino Ratio Report
- Alpha-Beta Report
- Maximum Drawdown Report
- Fund Scorecard
- Benchmark Comparison Chart

---

# Day 5: Advanced Analytics & Risk Metrics

## Tasks Completed

### Risk Analytics

- Calculated Historical Value at Risk (VaR 95%) for all mutual fund schemes.
- Computed Conditional Value at Risk (CVaR) to measure expected downside loss.
- Generated comprehensive risk reports for all funds.

### Rolling Performance Analysis

- Calculated Rolling 90-Day Sharpe Ratio.
- Visualized risk-adjusted performance trends for selected mutual funds.

### Investor Analytics

- Performed Investor Cohort Analysis based on first investment year.
- Computed average SIP amount and total investment for each cohort.
- Identified the most preferred mutual fund for every investor cohort.

### SIP Continuity Analysis

- Calculated average gap between SIP transactions.
- Identified investors with irregular SIP investments.
- Classified investors as **Healthy** or **At-Risk** based on SIP continuity.

### Fund Recommendation System

- Developed a rule-based mutual fund recommender.
- Recommended Top 3 funds based on:
  - Risk Appetite
  - Risk Grade
  - Sharpe Ratio

### Portfolio Concentration Analysis

- Calculated Herfindahl-Hirschman Index (HHI) using sector allocation weights.
- Compared diversification levels across equity mutual funds.

### Business Insights

- Generated advanced financial insights covering:
  - Downside Risk
  - Risk-Adjusted Returns
  - Investor Behaviour
  - SIP Continuity
  - Portfolio Diversification

## Deliverables

- Advanced_Analytics.ipynb
- var_cvar_report.csv
- rolling_sharpe_chart.png
- cohort_analysis.csv
- sip_continuity_report.csv
- hhi_report.csv
- recommender.py

---

# Dataset Files

1. Fund Master
2. NAV History
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

# Key Financial Metrics Implemented

## Return Metrics

- Daily Returns
- CAGR
- Rolling Returns

## Risk Metrics

- Historical VaR (95%)
- Conditional VaR (CVaR)
- Standard Deviation
- Maximum Drawdown
- Tracking Error

## Risk-Adjusted Performance

- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta

## Portfolio Analytics

- Fund Scorecard
- Sector HHI Concentration
- Rolling Sharpe Ratio

## Investor Analytics

- Investor Cohort Analysis
- SIP Continuity Analysis
- Fund Recommendation System

---

# Skills Demonstrated

- Data Analysis
- Financial Data Analytics
- Mutual Fund Analytics
- Risk Analytics
- Performance Evaluation
- Portfolio Analytics
- Statistical Analysis
- Time Series Analysis
- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL & Database Design
- SQLite
- Python Programming
- Data Visualization
- Business Intelligence
- Investment Analytics
- Git & GitHub

---

# Project Highlights

- Built an end-to-end mutual fund analytics pipeline using Python and SQLite.
- Processed and analyzed multiple financial datasets containing historical NAV, transactions, performance, and portfolio holdings.
- Implemented industry-standard financial metrics for return, risk, and portfolio evaluation.
- Developed investor behavior analytics and a rule-based mutual fund recommendation engine.
- Generated actionable business insights through advanced analytics and visualizations.

---

# Author

**Kapish**

**Data Analyst Intern**

**Bluestock Fintech Internship**