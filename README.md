# Multi-Pair Statistical Arbitrage Portfolio

A reproducible quantitative research implementation of a **multi-pair statistical arbitrage portfolio** on NIFTY 50 daily price data.

The project extends single-pair pairs trading into a portfolio setting by screening multiple candidate pairs, validating their out-of-sample behavior, selecting a final pair set, and evaluating the resulting portfolio on an untouched test period.

---

## Research Objective

The first stage of the research focused on a single cointegrated pair.

This project asks a broader question:

> **Can multiple statistically related equity pairs be combined into a portfolio while maintaining strict separation between model development, validation, and final out-of-sample evaluation?**

The research focuses on:

- pair selection
- cointegration
- hedge-ratio estimation
- mean-reversion signals
- portfolio construction
- execution timing
- transaction costs
- portfolio-level risk
- out-of-sample evaluation

The objective is to build a reproducible research pipeline rather than optimize the final test period for maximum historical performance.

---

## Research Pipeline

```text
NIFTY 50 Daily Prices
        │
        ▼
Candidate Pair Universe
        │
        ▼
Training Period
2017–2020
        │
        ├── Return Correlation Screening
        │
        ├── Engle–Granger Cointegration
        │
        └── OLS Hedge-Ratio Estimation
        │
        ▼
Validation Period
2021–2023
        │
        ├── Pair Performance Evaluation
        ├── Pair Selection
        └── Threshold Selection
        │
        ▼
Freeze Model
        │
        ▼
Untouched Test Period
2024–2026
        │
        ▼
One-Day Execution Lag
        │
        ▼
Transaction Costs
        │
        ▼
Portfolio P&L
        │
        ▼
Risk & Performance Analysis
