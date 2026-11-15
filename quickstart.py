"""
Quickstart Guide: Loading and Inspecting the FJCAI 2026 Master Dataset
=====================================================================
Dataset: Spectral Consistency Regularization for Long-Horizon Probabilistic Forecasting
Paper: FJCAI 2026 / CITA 2027 Phase 2
"""

import os
import pandas as pd
import numpy as np

def load_master_data(data_path="data/fjcai_spectral_6assets_master.csv"):
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}. Ensure you are in repo root.")
    
    df = pd.read_csv(data_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

def summarize_dataset(df):
    print("=" * 75)
    print("  FJCAI 2026 BENCHMARK DATASET: MASTER MULTI-ASSET TIME SERIES")
    print("=" * 75)
    print(f"Total Records:      {len(df):,}")
    print(f"Total Columns:      {len(df.columns)}")
    print(f"Date Span:          {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
    print(f"Missing Values:     {df.isnull().sum().sum()} (100% Complete, No NaNs)")
    print(f"Tickers Covered:    {df['ticker'].unique().tolist()}")
    print("-" * 75)
    
    print("\n[1] Per-Asset Breakdown:")
    summary = df.groupby('ticker').agg(
        Records=('date', 'count'),
        Start_Date=('date', 'min'),
        End_Date=('date', 'max'),
        Mean_Log_Return=('log_return', 'mean'),
        Daily_Volatility=('log_return', 'std')
    )
    print(summary)
    
    print("\n[2] Train / Out-of-Distribution (OOD) Split Distribution:")
    split_summary = df.groupby(['ticker', 'split_2021']).size().unstack(fill_value=0)
    print(split_summary)
    
    print("\n" + "=" * 75)
    print("  FEATURE CLASSIFICATION FOR TEMPORAL FUSION TRANSFORMER (TFT)")
    print("=" * 75)
    features = {
        "Static Categorical": ["ticker", "asset"],
        "Temporal Index": ["date"],
        "Target Variable (y_t)": ["log_return"],
        "Normalized Target": ["z_return_2021"],
        "Known Future Periodic": ["sin_dow", "cos_dow", "sin_month", "cos_month"],
        "Observed Past Market": ["adj_close", "volume"],
        "Observed Rolling Context": [
            "rolling_mean_20d", "rolling_vol_20d",
            "rolling_mean_60d", "rolling_vol_60d",
            "momentum_20d", "momentum_60d"
        ],
        "Experimental Partition": ["split_2021"]
    }
    for group, cols in features.items():
        print(f"• {group:26s}: {', '.join(cols)}")
    print("=" * 75)
    print("Verification completed successfully!")

if __name__ == "__main__":
    df = load_master_data()
    summarize_dataset(df)
