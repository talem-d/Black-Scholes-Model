import math
from .models import Option, OptionType

def norm_cdf(x: float) -> float:
    """Cumulative distribution function for the standard normal distribution."""
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def calculate_price(option: Option) -> float:
    """Calculates the Black-Scholes price for a European option."""
    # Edge case: If time to expiration is 0, the option is worth its intrinsic value
    if option.T <= 0:
        if option.option_type == OptionType.CALL:
            return max(option.S - option.K, 0.0)
        else:
            return max(option.K - option.S, 0.0)
            
    # Prevent division by zero if volatility is 0
    if option.sigma <= 0:
        raise ValueError("Volatility (sigma) must be greater than 0.")

    # Calculate d1 and d2
    d1 = (math.log(option.S / option.K) + (option.r + 0.5 * option.sigma**2) * option.T) / (option.sigma * math.sqrt(option.T))
    d2 = d1 - option.sigma * math.sqrt(option.T)

    # Calculate Call or Put price
    if option.option_type == OptionType.CALL:
        price = (option.S * norm_cdf(d1)) - (option.K * math.exp(-option.r * option.T) * norm_cdf(d2))
    else:
        price = (option.K * math.exp(-option.r * option.T) * norm_cdf(-d2)) - (option.S * norm_cdf(-d1))
        
    return price