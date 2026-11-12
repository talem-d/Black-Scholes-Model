from .models import Option, OptionType
from .pricing import calculate_price
from .greeks import calculate_vega

def calculate_implied_vol(market_price: float, option: Option, max_iterations: int = 100, tolerance: float = 1e-5) -> float:
    """
    Calculates the implied volatility of an option using the Newton-Raphson method.
    """
    # Start with an initial guess for volatility (e.g., 20%)
    sigma_guess = 0.2
    
    for i in range(max_iterations):
        # Update the option's sigma with our current guess
        option.sigma = sigma_guess
        
        # Calculate the theoretical price and the Vega (derivative with respect to sigma)
        price = calculate_price(option)
        
        # Vega in our greeks.py is divided by 100 for a 1% change. 
        # We need the raw derivative for Newton-Raphson, so we multiply by 100.
        vega = calculate_vega(option) * 100
        
        # Calculate the difference between the market price and our calculated price
        diff = price - market_price
        
        # If the difference is within our tolerance, we found the root!
        if abs(diff) < tolerance:
            return sigma_guess
            
        # Prevent division by zero if Vega is extremely small
        if vega < 1e-8:
            break
            
        # Newton-Raphson step: x_new = x_old - f(x)/f'(x)
        # Here, f(x) is (Calculated Price - Market Price), and f'(x) is Vega
        sigma_guess = sigma_guess - (diff / vega)
        
        # Volatility cannot be negative. If it drops below zero, reset it to a small positive number.
        if sigma_guess <= 0:
            sigma_guess = 0.001
            
    raise ValueError(f"Implied volatility did not converge after {max_iterations} iterations.")