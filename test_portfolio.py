
import pytest

from portfolio import calculate_portfolio_return


def test_calculates_weighted_portfolio_return():
    result = calculate_portfolio_return(
        weights=[0.6, 0.4],
        returns=[0.10, 0.05],
    )
    assert result == pytest.approx(0.08)


def test_handles_a_single_asset():
    result = calculate_portfolio_return(
        weights=[1.0],
        returns=[0.12],
    )
    assert result == pytest.approx(0.12)


def test_rejects_weights_that_do_not_sum_to_one():
    with pytest.raises(ValueError, match="sum to 1.0"):
        calculate_portfolio_return(
            weights=[0.5, 0.4],
            returns=[0.10, 0.05],
        )


def test_rejects_mismatched_input_lengths():
    with pytest.raises(ValueError, match="same length"):
        calculate_portfolio_return(
            weights=[0.6, 0.4],
            returns=[0.10],
        )


def test_rejects_negative_weights():
    with pytest.raises(ValueError, match="negative"):
        calculate_portfolio_return(
            weights=[1.2, -0.2],
            returns=[0.10, 0.05],
        )


def test_rejects_empty_inputs():
    with pytest.raises(ValueError, match="empty"):
        calculate_portfolio_return([], [])
