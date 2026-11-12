import pytest
import math
from src.models import Option, OptionType
from src.pricing import calculate_price

def test_call_option_price():
    """Test standard Black-Scholes call price."""
    opt = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=OptionType.CALL)
    # The known exact price for these parameters is ~10.4506
    assert math.isclose(calculate_price(opt), 10.4506, rel_tol=1e-4)

def test_put_option_price():
    """Test standard Black-Scholes put price."""
    opt = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=OptionType.PUT)
    # The known exact price is ~5.5735
    assert math.isclose(calculate_price(opt), 5.5735, rel_tol=1e-4)

def test_expired_option():
    """Test that an expired option (T=0) equals its intrinsic value."""
    # Expired Call: If stock is 105 and strike is 100, it's worth 5
    opt_call = Option(S=105, K=100, T=0, r=0.05, sigma=0.2, option_type=OptionType.CALL)
    assert calculate_price(opt_call) == 5.0
    
    # Expired Put: If stock is 95 and strike is 100, it's worth 5
    opt_put = Option(S=95, K=100, T=0, r=0.05, sigma=0.2, option_type=OptionType.PUT)
    assert calculate_price(opt_put) == 5.0

def test_zero_volatility_raises_error():
    """Test that zero volatility raises a ValueError."""
    opt = Option(S=100, K=100, T=1, r=0.05, sigma=0, option_type=OptionType.CALL)
    with pytest.raises(ValueError):
        calculate_price(opt)