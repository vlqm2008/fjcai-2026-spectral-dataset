# 📈 FJCAI 2026 Master Dataset & Benchmark Suite

[![Dataset License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Paper: FJCAI 2026](https://img.shields.io/badge/Paper-FJCAI_2026-blue.svg)](#paper-reference)
[![Target Assets: 6 Tier-1 Financial Series](https://img.shields.io/badge/Assets-6_Tier_1_Series-brightgreen.svg)](#asset-coverage)
[![Total Records: 19,033 Daily Steps](https://img.shields.io/badge/Records-19%2C033_Steps-orange.svg)](#dataset-statistics)
[![Missing Values: 0 Nulls](https://img.shields.io/badge/Data_Quality-100%25_Clean_0_Nulls-success.svg)](#data-quality)

Official standalone repository containing the complete benchmark dataset, empirical evaluation tables, and interactive visualizations for the research paper:

> **"Spectral Consistency Regularization for Long-Horizon Probabilistic Forecasting with Temporal Fusion Transformers"**  
> *Under Review at FJCAI 2026 / CITA 2027 Phase 2*

---

## 📑 Table of Contents
1. [Dataset Overview](#-dataset-overview)
2. [Data Dictionary & TFT Variable Classification](#-data-dictionary--tft-variable-classification)
3. [Asset Coverage & Summary Statistics](#-asset-coverage--summary-statistics)
4. [Empirical Replication Tables (Paper Results)](#-empirical-replication-tables)
5. [Visualizations & Interactive Dashboard](#-visualizations--interactive-dashboard)
6. [Repository Structure](#-repository-structure)

---

## 📊 Dataset Overview

This dataset was designed specifically for **multi-horizon probabilistic time-series forecasting** ($H \in \{60, 120, 250\}$ trading days) under non-stationary market regimes. It eliminates low-frequency spectral leakage while preserving autoregressive feedback integrity across long prediction horizons.

- **Master File:** [`data/fjcai_spectral_6assets_master.csv`](data/fjcai_spectral_6assets_master.csv)
- **Time Range:** 2010-01-04 to 2022-12-30 (13 years of continuous market trading sessions).
- **Dimensions:** 19,033 rows $\times$ 18 feature columns.
- **Completeness:** 100% complete (0 missing values, zero NaN, zero imputed synthetic artifacts).
- **Assets Covered:** 5 Mega-cap Tech Equities (`AAPL`, `MSFT`, `GOOG`, `AMZN`, `META`) + 1 Macroeconomic Benchmark Index (`^GSPC` / S&P 500). Individual asset series are also available under [`data/individual_assets/`](data/individual_assets/).

---

## 🧬 Data Dictionary & TFT Variable Classification

In the **Temporal Fusion Transformer (TFT)** and **Spectral Consistency TFT** architectures, variables are decoupled into strict functional roles:

| Column Name | Data Type | Functional TFT Role | Mathematical Formula / Description |
| :--- | :--- | :--- | :--- |
| `date` | `string (YYYY-MM-DD)` | **Temporal Stamp** | Trading session date in ISO 8601. |
| `ticker` | `categorical (str)` | **Static Categorical Entity** | Ticker code embedded into static entity space $e_i \in \mathbb{R}^{d_{model}}$. |
| `asset` | `categorical (str)` | Static Metadata | Human-readable asset name identifier. |
| `adj_close` | `float64` | Observed Past Input | Dividend/split adjusted closing price. |
| `volume` | `float64` | Observed Past Input | Daily trading volume. |
| `log_return` | `float64` | **Target Variable ($y_t$)** | Logarithmic return: $r_t = \ln(P_t / P_{t-1})$. Modeled with quantile regression ($q_{0.1}, q_{0.5}, q_{0.9}$). |
| `sin_dow` | `float64` | **Known Future Periodic** | Sine encoding of Day of Week: $\sin(2\pi \cdot \text{dow} / 5)$. |
| `cos_dow` | `float64` | **Known Future Periodic** | Cosine encoding of Day of Week: $\cos(2\pi \cdot \text{dow} / 5)$. |
| `sin_month` | `float64` | **Known Future Periodic** | Sine encoding of Calendar Month: $\sin(2\pi \cdot m / 12)$. |
| `cos_month` | `float64` | **Known Future Periodic** | Cosine encoding of Calendar Month: $\cos(2\pi \cdot m / 12)$. |
| `rolling_mean_20d` | `float64` | Observed Past Input | 20-day rolling simple moving average of log returns. |
| `rolling_vol_20d` | `float64` | Observed Past Input | 20-day rolling standard deviation of log returns (short-term volatility). |
| `rolling_mean_60d` | `float64` | Observed Past Input | 60-day rolling simple moving average of log returns. |
| `rolling_vol_60d` | `float64` | Observed Past Input | 60-day rolling standard deviation of log returns (medium-term volatility). |
| `momentum_20d` | `float64` | Observed Past Input | 20-day cumulative price momentum: $(P_t - P_{t-20}) / P_{t-20}$. |
| `momentum_60d` | `float64` | Observed Past Input | 60-day cumulative price momentum: $(P_t - P_{t-60}) / P_{t-60}$. |
| `split_2021` | `categorical (str)` | **Experimental Partition** | Partition flag: `train_val` (pre-2021, 16,759 rows) vs `test_ood` (2021-2022 OOD, 2,274 rows). |
| `z_return_2021` | `float64` | **Normalized Target** | Z-score standardized return computed strictly on pre-2021 parameters to avoid data leakage. |

---

## 📈 Asset Coverage & Summary Statistics

| Ticker | Asset Class | Total Samples | Start Date | End Date | Mean Log Return | Daily Volatility ($\sigma$) | OOD Test Samples |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `AAPL` | Equities (Apple Inc.) | 3,272 | 2010-01-04 | 2022-12-30 | +0.000915 | 0.0181 | 379 |
| `MSFT` | Equities (Microsoft Corp.) | 3,272 | 2010-01-04 | 2022-12-30 | +0.000708 | 0.0164 | 379 |
| `GOOG` | Equities (Alphabet Inc.) | 3,272 | 2010-01-04 | 2022-12-30 | +0.000531 | 0.0170 | 379 |
| `AMZN` | Equities (Amazon.com Inc.) | 3,272 | 2010-01-04 | 2022-12-30 | +0.000773 | 0.0208 | 379 |
| `META` | Equities (Meta Platforms) | 2,673 | 2012-05-18 | 2022-12-30 | +0.000429 | 0.0254 | 379 |
| `^GSPC` | Macro Index (S&P 500) | 3,272 | 2010-01-04 | 2022-12-30 | +0.000373 | 0.0113 | 379 |
| **Total** | **Master Benchmark Suite** | **19,033** | **2010-01-04** | **2022-12-30** | **+0.000622** | **0.0182** | **2,274** |

---

## 🏆 Empirical Replication Tables

All experiment metrics reported in the paper have been strictly reproduced across 54 configurations ($6 \text{ assets} \times 3 \text{ horizons} \times 3 \text{ spectral variants}$):

### Table 1: Global Performance Benchmark ($H=120$)
Located at [`benchmark_results/fjcai_table1_global_performance_h120.csv`](benchmark_results/fjcai_table1_global_performance_h120.csv)

| Metric | Baseline TFT | SpectralTFT ($k_c=8$) | SpectralTFT ($k_c=16$) | Improvement vs TFT |
| :--- | :---: | :---: | :---: | :---: |
| **Quantile Loss ($q_{0.5}$ / MAE)** | 0.01648 | 0.01467 | **0.01429** | **+13.3%** |
| **RMSE** | 0.02235 | 0.01982 | **0.01918** | **+14.2%** |
| **Coverage 80%** | 71.4% | 78.6% | **79.9%** | **+8.5% (Well-calibrated)** |
| **Winkler Score (80%)** | 0.0712 | 0.0614 | **0.0598** | **-16.0%** |
| **Spectral Error ($E_{spec}$)** | 0.0412 | 0.0174 | **0.0118** | **-71.4%** |

### Table 2: Spectral Cutoff Sensitivity ($H=120$)
Located at [`benchmark_results/fjcai_table2_spectral_cutoffs_h120.csv`](benchmark_results/fjcai_table2_spectral_cutoffs_h120.csv)

| Cutoff Frequency $k_c$ | MAE | RMSE | 80% Coverage | Winkler Score | Spectral Drift $E_{spec}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Baseline ($k_c=0$, No Reg) | 0.01648 | 0.02235 | 71.4% | 0.0712 | 0.0412 |
| $k_c = 4$ | 0.01521 | 0.02071 | 76.8% | 0.0645 | 0.0234 |
| $k_c = 8$ | 0.01467 | 0.01982 | 78.6% | 0.0614 | 0.0174 |
| **$k_c = 16$ (Optimal)** | **0.01429** | **0.01918** | **79.9%** | **0.0598** | **0.0118** |
| $k_c = 32$ | 0.01452 | 0.01945 | 79.2% | 0.0608 | 0.0132 |

### Table 3: Cross-Horizon Consistency ($H=60, 120, 250$)
Located at [`benchmark_results/fjcai_table3_cross_horizon_cutoffs.csv`](benchmark_results/fjcai_table3_cross_horizon_cutoffs.csv)

| Horizon | Baseline MAE | SpectralTFT MAE | Baseline Coverage | SpectralTFT Coverage | MAE Reduction |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **$H = 60$** | 0.01412 | **0.01289** | 76.5% | **80.4%** | **-8.7%** |
| **$H = 120$** | 0.01648 | **0.01429** | 71.4% | **79.9%** | **-13.3%** |
| **$H = 250$** | 0.01984 | **0.01631** | 64.2% | **78.8%** | **-17.8%** |

---

## 🎨 Visualizations & Interactive Dashboard

- **Interactive Dashboard:** [`reports/interactive_dashboard.html`](reports/interactive_dashboard.html) — Open directly in any web browser to search, filter, and compare all 54 metric sets.
- **Error Accumulation Chart:** [`figures/fig1_fjcai_error_accumulation_all_assets.png`](figures/fig1_fjcai_error_accumulation_all_assets.png)
- **Coverage Calibration Chart:** [`figures/fig2_fjcai_coverage_calibration_by_horizon.png`](figures/fig2_fjcai_coverage_calibration_by_horizon.png)
- **Multi-Asset Performance Radar:** [`figures/fig3_fjcai_asset_performance_radar.png`](figures/fig3_fjcai_asset_performance_radar.png)

---

## 📁 Repository Structure

```text
fjcai-2026-spectral-dataset/
├── data/
│   ├── fjcai_spectral_6assets_master.csv  <-- Master 19,033-row dataset
│   └── individual_assets/                 <-- Subdivided single-ticker CSVs
│       ├── AAPL_daily.csv
│       ├── AMZN_daily.csv
│       ├── BTCUSDT_daily.csv
│       ├── GOOG_daily.csv
│       ├── META_daily.csv
│       ├── MSFT_daily.csv
│       └── SPY_daily.csv
├── benchmark_results/                     <-- Paper experiment CSVs
│   ├── fjcai_all_6assets_comprehensive_metrics.csv
│   ├── fjcai_table1_global_performance_h120.csv
│   ├── fjcai_table2_spectral_cutoffs_h120.csv
│   └── fjcai_table3_cross_horizon_cutoffs.csv
├── figures/                               <-- High-resolution charts (300 DPI)
│   ├── fig1_fjcai_error_accumulation_all_assets.png
│   ├── fig2_fjcai_coverage_calibration_by_horizon.png
│   ├── fig3_fjcai_asset_performance_radar.png
│   ├── fig1_paper_data_spectral_foundation.png
│   ├── fig2_paper_model_benchmarks_replication.png
│   └── fig3_cross_market_spy_vs_btc.png
├── reports/                               <-- Standalone handoff documents
│   ├── FJCAI_2026_Data_And_Model_Report.docx
│   ├── FJCAI_2026_Data_And_Model_Report.html
│   └── interactive_dashboard.html
├── quickstart.py                          <-- Verification & inspection script
├── .gitignore
└── README.md
```

