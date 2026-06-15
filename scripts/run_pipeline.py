"""
Bluestock Mutual Fund Analytics - Production Pipeline Script
Author: Mutual Fund Data Analyst Intern
Description: Handles complete data ingestion, processing, and metric output generation.
"""

import os
import pandas as pd
import numpy as np

def run_analytics_pipeline():
    print(" Step 1: Ingesting production CSV data sources...")
    try:
        # Using correct relative paths to read your datasets
        df_transactions = pd.read_csv('08_investor_transactions.csv')
        df_returns = pd.read_csv('02_nav_history.csv')
        print(" Data successfully loaded into memory.")
    except FileNotFoundError as e:
        print(f" Execution stopped. Missing source files in directory: {e}")
        return

    # --- Data Standardization ---
    df_transactions['transaction_date'] = pd.to_datetime(df_transactions['transaction_date'])
    df_returns['date'] = pd.to_datetime(df_returns['date'])
    df_returns['nav'] = pd.to_numeric(df_returns['nav'], errors='coerce')
    df_returns = df_returns.sort_values(by=['amfi_code', 'date'])
    
    # --- Vectorized Returns Calculations ---
    print(" Step 2: Calculating daily returns dynamically from NAV...")
    df_returns['daily_return'] = df_returns.groupby('amfi_code')['nav'].pct_change()
    df_clean_returns = df_returns.dropna(subset=['daily_return'])

    # --- Metric File Generations ---
    print(" Step 3: Executing Historical VaR (95%) and CVaR models...")
    var_report = df_clean_returns.groupby('amfi_code')['daily_return'].quantile(0.05).reset_index()
    var_report.rename(columns={'daily_return': 'VaR_95'}, inplace=True)

    df_merged = pd.merge(df_clean_returns, var_report, on='amfi_code')
    df_cvar_source = df_merged[df_merged['daily_return'] <= df_merged['VaR_95']]
    cvar_report = df_cvar_source.groupby('amfi_code')['daily_return'].mean().reset_index()
    cvar_report.rename(columns={'daily_return': 'CVaR_95'}, inplace=True)

    var_cvar_report = pd.merge(var_report, cvar_report, on='amfi_code', how='left')
    
    # Save output to your main folder
    var_cvar_report.to_csv('var_cvar_report.csv', index=False)
    print(" Step 4: Pipeline execution complete. Outputs successfully refreshed!")

if __name__ == "__main__":
    run_analytics_pipeline()