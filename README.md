
# QuantForge

A quantitative finance project focused on portfolio analytics,
risk measurement, and systematic strategy evaluation.

## Current Features

- Weighted portfolio return calculation
- Input validation for weights and asset returns
- Automated tests using pytest

## Requirements

- Python 3.11+
- pytest

## Run Tests

```powershell
.\.venv\Scripts\python.exe -m pytest -v
```

## Example

```python
from portfolio import calculate_portfolio_return

result = calculate_portfolio_return(
    weights=[0.6, 0.4],
    returns=[0.10, 0.05],
)

print(result)  # 0.08, or 8%
```

## Roadmap

- Historical market data ingestion
- Portfolio volatility and risk metrics
- Value at Risk and Expected Shortfall
- Strategy backtesting with transaction costs
- API and dashboard

## Status

Early development. Features will be added with tests and
documented as they are implemented.
