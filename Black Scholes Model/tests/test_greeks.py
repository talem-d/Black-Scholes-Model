import pytest
import math
from src.models import Option, OptionType
from src.greeks import calculate_delta, calculate_gamma, calculate_vega, calculate_theta

# Standard option parameters for testing
@pytest.fixture
def standard_call():
    return Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=OptionType.CALL)

@pytest.fixture
def standard_put():
    return Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=OptionType.PUT)

def test_call_delta(standard_call):
    """Test that Call Delta is positive and matches known value."""
    delta = calculate_delta(standard_call)
    # Known value for these parameters is ~0.6368
    assert math.isclose(delta, 0.6368, rel_tol=1e-3)
    assert 0 <= delta <= 1

def test_put_delta(standard_put):
    """Test that Put Delta is negative and matches known value."""
    delta = calculate_delta(standard_put)
    # Known value is Call Delta - 1 (so ~-0.3632)
    assert math.isclose(delta, -0.3632, rel_tol=1e-3)
    assert -1 <= delta <= 0

def test_gamma_positive(standard_call, standard_put):
    """Test that Gamma is always positive for long options."""
    gamma_call = calculate_gamma(standard_call)
    gamma_put = calculate_gamma(standard_put)
    
    assert gamma_call > 0
    assert gamma_put > 0
    # Gamma should be the exact same for a call and put with the same strike
    assert math.isclose(gamma_call, gamma_put, rel_tol=1e-4)

def test_vega_identical(standard_call, standard_put):
    """Test that Vega is identical for Calls and Puts."""
    vega_call = calculate_vega(standard_call)
    vega_put = calculate_vega(standard_put)
    
    # Known value for these parameters is ~0.3752
    assert math.isclose(vega_call, 0.3752, rel_tol=1e-3)
    assert math.isclose(vega_call, vega_put, rel_tol=1e-4)

def test_theta_negative(standard_call, standard_put):
    """Test that Theta (time decay) is negative for both calls and puts."""
    theta_call = calculate_theta(standard_call)
    theta_put = calculate_theta(standard_put)
    
    # Time decay means you lose money as time passes (if nothing else changes)
    assert theta_call < 0
    assert theta_put < 0