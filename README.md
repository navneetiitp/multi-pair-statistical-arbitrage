# Multi-Pair Statistical Arbitrage Portfolio

A reproducible research implementation of a multi-pair statistical arbitrage strategy on the supplied NIFTY 50 daily price dataset.

## What was rebuilt

The original project selected cointegrated pairs and evaluated many pairs across the full sample. This version separates model development, validation, and final evaluation to reduce look-ahead bias.

### Pipeline

1. Use the 2017–2020 training period to screen candidate pairs.
2. Filter candidates using return correlation and the Engle–Granger cointegration test.
3. Estimate log-price OLS hedge ratios using training data.
4. Evaluate candidate pairs on 2021–2023 validation data.
5. Select the final pair subset and tune trading thresholds using validation data only.
6. Freeze the model before running the untouched 2024–2026 test period.
7. Shift signals by one trading day and deduct 5 bps per unit of position change.

## Final test results

| Metric | Result |
|---|---:|
| Total return | 4.37% |
| CAGR | 1.98% |
| Annualized volatility | 3.18% |
| Sharpe ratio | 0.63 |
| Sortino ratio | 0.90 |
| Maximum drawdown | -2.18% |
| Calmar ratio | 0.91 |

These are historical backtest results, not live trading performance or a guarantee of future returns.

## Strategy

For each selected pair, the spread is defined as:

`spread = log(P1) - beta * log(P2)`

The spread is standardized using a 60-day rolling mean and standard deviation. A position is opened at Z = ±2.5 and closed when |Z| < 0.25. Signals are shifted by one trading day before returns are applied.

Pair returns are normalized as:

`pair_return = (r1 - beta * r2) / (1 + abs(beta))`

## Important limitations

- The supplied universe is a manually defined NIFTY 50 ticker list rather than a historical constituent database, so survivorship bias may remain.
- The dataset begins in November 2017.
- This is a daily-bar backtest and does not model intraday execution, bid/ask spread, borrow constraints, market impact, or order-book effects.
- The final test period is kept separate from model selection and parameter tuning.

## Repository structure

```text
├── data/nifty50_prices.csv
├── src/strategy.py
├── outputs/plots/equity_curve.png
├── outputs/plots/drawdown.png
├── outputs/tables/strategy_metrics.csv
├── outputs/tables/final_pairs.csv
├── outputs/tables/pair_test_performance.csv
├── outputs/tables/test_portfolio_returns.csv
├── docs/INTERVIEW.md
├── README.md
└── requirements.txt
```
