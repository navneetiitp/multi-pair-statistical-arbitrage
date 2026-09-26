from pathlib import Path
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint
import statsmodels.api as sm

ENTRY_Z = 2.5
EXIT_Z = 0.25
Z_WINDOW = 60
TRANSACTION_COST = 0.0005

def find_candidates(prices):
    log_prices = np.log(prices)
    corr = log_prices.diff().corr()
    rows = []
    cols = list(prices.columns)
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            if corr.loc[a, b] < 0.50:
                continue
            _, pvalue, _ = coint(log_prices[a], log_prices[b])
            if pvalue >= 0.05:
                continue
            beta = sm.OLS(log_prices[a], sm.add_constant(log_prices[b])).fit().params.iloc[1]
            if beta > 0 and np.isfinite(beta):
                rows.append((a, b, pvalue, beta))
    return pd.DataFrame(rows, columns=['a', 'b', 'pvalue', 'beta']).sort_values('pvalue')

def pair_returns(prices, a, b, beta, entry_z=ENTRY_Z, exit_z=EXIT_Z, z_window=Z_WINDOW):
    spread = np.log(prices[a]) - beta * np.log(prices[b])
    z = (spread - spread.rolling(z_window).mean()) / spread.rolling(z_window).std()
    state = 0.0
    signal = []
    for value in z:
        if not np.isfinite(value):
            state = 0.0
        elif state == 0:
            state = 1.0 if value < -entry_z else (-1.0 if value > entry_z else 0.0)
        elif abs(value) < exit_z:
            state = 0.0
        signal.append(state)
    position = pd.Series(signal, index=prices.index).shift(1).fillna(0.0)
    raw = (prices[a].pct_change() - beta * prices[b].pct_change()) / (1 + abs(beta))
    turnover = position.diff().abs().fillna(position.abs())
    return position * raw - TRANSACTION_COST * turnover
