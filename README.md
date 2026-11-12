# Black-Scholes Options Pricing Engine

A modular, object-oriented Python library designed to price European options and calculate risk sensitivities (the "Greeks") using the Black-Scholes-Merton mathematical model.

## Features

*   **Option Pricing:** Accurate calculations for European Call and Put options.
*   **Risk Metrics (Greeks):** Calculates Delta, Gamma, Vega, and Theta to measure price sensitivity to underlying asset movement, time decay, and volatility.
*   **Implied Volatility Solver:** Utilizes the Newton-Raphson root-finding algorithm to reverse-engineer market volatility from an option's market price.
*   **Automated Testing:** Includes a comprehensive unit test suite using `pytest` to ensure mathematical accuracy and edge-case handling.

## Architecture

The project is structured for modularity and scalability:

*   `src/models.py`: Object-oriented data structures (using `@dataclass`) to represent options and enforce type safety.
*   `src/pricing.py`: The core Black-Scholes mathematical pricing formula.
*   `src/greeks.py`: Mathematical implementations of the risk sensitivities.
*   `src/implied_vol.py`: The iterative algorithm to solve for volatility.
*   `tests/`: Automated unit tests covering standard pricing, expired options, and error handling.

## Tech Stack

*   **Language:** Python 3
*   **Testing:** `pytest`
*   **Libraries:** `math` (for core math), `dataclasses` (for data models)

## Usage Example

```python
from src.models import Option, OptionType
from src.pricing import calculate_price
from src.greeks import calculate_delta

# Initialize a Call Option
opt = Option(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type=OptionType.CALL)

# Calculate Price and Delta
price = calculate_price(opt)
delta = calculate_delta(opt)

print(f"Call Price: ${price:.2f}")
print(f"Delta: {delta:.4f}")
```

## Visualizations

### Call Option Payoff
<img src="Black%20Scholes%20Model/visualization/payoff_diagram.png" alt="Payoff Diagram" width="600">

### The Volatility Smile
<img src="Black%20Scholes%20Model/visualization/volatility_smile.png" alt="Volatility Smile" width="600">