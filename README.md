# Bluestock Fintech - Mutual Fund Analytics Project

This is my official capstone analytics repository for Bluestock Fintech. This project takes raw mutual fund data and investor history, processes it using Python, and builds clean calculations for a risk and performance dashboard.

##  Project Directory Breakdown
* **01_fund_master.csv:** Contains the unique AMFI tracking codes and official names for the mutual funds.
* **02_nav_history.csv:** Contains the historical daily prices (NAV) used to calculate fund returns.
* **08_investor_transactions.csv:** Contains all tracking history for individual investor buying behaviors.
* **run_pipeline.py:** The master automated Python script that executes all mathematical metrics smoothly.
* **notebooks/:** Contains my working files where I handled data cleaning, exploratory analysis, and advanced risk metrics.

##  Key Performance Insights Found
1. **Downside Tail Risk:** Aggressive funds carry a 95% Value at Risk threshold of -2.4%, with extreme market down-turns averaging a -3.8% drop.
2. **Investor Drop-off Churn:** Exactly 18% of the platform's active users are flagged as "At-Risk" due to systematic investment plan gaps extending past 35 days.
3. **Sector Concentrations:** Specialized thematic options surface with high concentration metrics exceeding 0.32 on the HHI Index scale.