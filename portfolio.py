
import math


def calculate_portfolio_return(weights: list[float], returns: list[float]) -> float:
    """Calculate the weighted return of a portfolio.

    Args:
        weights: Fraction of portfolio allocated to each asset.
        returns: Return of each asset as a decimal (0.10 = 10%).

    Returns:
        Portfolio return as a decimal.

    Raises:
        ValueError: If inputs are empty, mismatched, invalid,
                    or weights do not sum to 1.
    """
    if not weights or not returns:
        raise ValueError("Weights and returns must not be empty.")

    if len(weights) != len(returns):
        raise ValueError("Weights and returns must have the same length.")

    if not all(math.isfinite(x) for x in weights + returns):
        raise ValueError("Weights and returns must be finite numbers.")

    if any(weight < 0 for weight in weights):
        raise ValueError("Weights must not be negative.")

    if not math.isclose(sum(weights), 1.0, abs_tol=1e-9):
        raise ValueError("Weights must sum to 1.0.")

    return sum(weight * asset_return for weight, asset_return in zip(weights, returns))
