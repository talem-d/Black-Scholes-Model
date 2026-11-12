from dataclasses import dataclass
from enum import Enum

class OptionType(Enum):
    CALL = "call"
    PUT = "put"

@dataclass
class Option:
    S: float      # Spot price (current stock price)
    K: float      # Strike price
    T: float      # Time to expiration in years (e.g., 0.5 for 6 months)
    r: float      # Risk-free interest rate (e.g., 0.05 for 5%)
    sigma: float  # Volatility (e.g., 0.2 for 20%)
    option_type: OptionType