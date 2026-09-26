# Interview Notes

## What did you build?
A multi-pair statistical arbitrage research pipeline that screens a stock universe for cointegrated pairs, validates candidate pairs on a separate period, and evaluates a market-neutral mean-reversion portfolio on an untouched test set.

## Why cointegration instead of correlation?
Correlation measures co-movement, while cointegration asks whether a linear combination of non-stationary price series can be stationary. Pairs trading needs the latter because the strategy trades deviations of the spread from equilibrium.

## How did you avoid look-ahead bias?
Pair screening and hedge-ratio estimation use only the training period. Candidate pairs are evaluated during validation, and the final parameters and pair subset are frozen before the 2024–2026 test period. Signals are shifted one day before returns are applied.

## What is the spread?
For log prices, `spread = log(P1) - beta * log(P2)`. Beta is estimated by OLS during model development.

## Signal logic
Enter long when Z < -2.5, enter short when Z > +2.5, and exit when |Z| < 0.25. The Z-score uses a 60-day rolling window.

## Final test result
CAGR: 1.98%, Sharpe: 0.63, Sortino: 0.90, maximum drawdown: -2.18%.

## What would you improve next?
Use historical index constituents, model borrow availability and bid/ask spreads, incorporate sector/industry constraints, use walk-forward re-selection, test stability across sub-periods, and compare static OLS hedge ratios against Kalman-filter dynamic hedge ratios.
