import pytest
import math
from src.models import Option, OptionType
from src.pricing import calculate_price
from src.implied_vol import calculate_implied_vol

def test_expired_call_option():
    """T=0: Expired Call is worth max(S - K, 0)."""
    # Case 1: In the money
    opt_itm = Option(S=110, K=100, T=0, r=0.05, sigma=0.2, option_type=OptionType.CALL)
    assert calculate_price(opt_itm) == 10.0
    
    # Case 2: Out of the money
    opt_otm = Option(S=90, K=100, T=0, r=0.05, sigma=0.2, option_type=OptionType.CALL)
    assert calculate_price(opt_otm) == 0.0

def test_expired_put_option():
    """T=0: Expired Put is worth max(K - S, 0)."""
    # Case 1: In the money
    opt_itm = Option(S=90, K=100, T=0, r=0.05, sigma=0.2, option_type=OptionType.PUT)
    assert calculate_price(opt_itm) == 10.0
    
    # Case 2: Out of the money
    opt_otm = Option(S=110, K=100, T=0, r=0.05, sigma=0.2, option_type=OptionType.PUT)
    assert calculate_price(opt_otm) == 0.0

def test_zero_volatility():
    """sigma=0: Should raise a ValueError to prevent division by zero."""
    opt = Option(S=100, K=100, T=1, r=0.05, sigma=0, option_type=OptionType.CALL)
    with pytest.raises(ValueError, match="Volatility \\(sigma\\) must be greater than 0."):
        calculate_price(opt)

def test_deep_in_the_money_call():
    """Deep ITM Call: Price should be close to S - K*e^(-rT)."""
    # If stock is 150 and strike is 50, the option is deeply in the money
    opt = Option(S=150, K=50, T=1, r=0.05, sigma=0.2, option_type=OptionType.CALL)
    price = calculate_price(opt)
    
    # Intrinsic value is 100, but because of time value, it should be slightly higher
    assert price > 100.0
    # The delta should be very close to 1.0 for deep ITM calls
    from src.greeks import calculate_delta
    assert calculate_delta(opt) > 0.95

def test_implied_volatility_no_convergence():
    """Implied Vol: If the market price is impossible (e.g., negative), it should raise an error."""
    opt = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=OptionType.CALL)
    # It's impossible to have a negative option price
    impossible_market_price = -5.0 
    
    with pytest.raises(ValueError, match="Implied volatility did not converge."):
        calculate_implied_vol(impossible_market_price, opt)