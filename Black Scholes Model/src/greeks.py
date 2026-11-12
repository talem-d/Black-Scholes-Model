import math
from .models import Option, OptionType
from .pricing import norm_cdf

def calculate_delta(option: Option) -> float:
    """Measures price change per $1 change in the underlying asset."""
    d1 = (math.log(option.S / option.K) + (option.r + 0.5 * option.sigma**2) * option.T) / (option.sigma * math.sqrt(option.T))
    if option.option_type == OptionType.CALL:
        return norm_cdf(d1)
    else:
        return norm_cdf(d1) - 1.0

def calculate_gamma(option: Option) -> float:
    """Measures the rate of change in Delta."""
    d1 = (math.log(option.S / option.K) + (option.r + 0.5 * option.sigma**2) * option.T) / (option.sigma * math.sqrt(option.T))
    return math.exp(-0.5 * d1**2) / (math.sqrt(2 * math.pi) * option.S * option.sigma * math.sqrt(option.T))

def calculate_vega(option: Option) -> float:
    """Measures price change per 1% change in volatility."""
    d1 = (math.log(option.S / option.K) + (option.r + 0.5 * option.sigma**2) * option.T) / (option.sigma * math.sqrt(option.T))
    # Divide by 100 to represent a 1% change in volatility
    return (option.S * math.sqrt(option.T) * math.exp(-0.5 * d1**2)) / (math.sqrt(2 * math.pi) * 100)

def calculate_theta(option: Option) -> float:
    """Measures price change per day passing (time decay)."""
    d1 = (math.log(option.S / option.K) + (option.r + 0.5 * option.sigma**2) * option.T) / (option.sigma * math.sqrt(option.T))
    d2 = d1 - option.sigma * math.sqrt(option.T)
    
    term1 = -(option.S * math.exp(-0.5 * d1**2)) / (2 * math.sqrt(2 * math.pi) * math.sqrt(option.T))
    
    if option.option_type == OptionType.CALL:
        term2 = option.r * option.K * math.exp(-option.r * option.T) * norm_cdf(d2)
        # Divide by 365 to get daily theta
        return (term1 - term2) / 365
    else:
        term2 = option.r * option.K * math.exp(-option.r * option.T) * norm_cdf(-d2)
        return (term1 + term2) / 365