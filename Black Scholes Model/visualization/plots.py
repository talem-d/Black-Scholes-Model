import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Add the src folder to the path so we can import our modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models import Option, OptionType
from src.pricing import calculate_price

def plot_payoff_diagram():
    """Plots the profit/loss of a Call option at expiration."""
    S_range = np.linspace(50, 150, 100)
    K = 100
    premium = 10.45 # The price we calculated earlier
    
    # Call payoff is max(S - K, 0)
    payoff = np.maximum(S_range - K, 0)
    profit = payoff - premium
    
    plt.figure(figsize=(8, 5))
    plt.plot(S_range, profit, label="Call Option Profit", color='green', linewidth=2)
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.axvline(K, color='red', linestyle='--', linewidth=1, label=f'Strike Price (${K})')
    
    plt.title("Call Option Payoff Diagram at Expiration")
    plt.xlabel("Stock Price at Expiration ($)")
    plt.ylabel("Profit / Loss ($)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot as an image
    plt.savefig('Black Scholes Model/visualization/payoff_diagram.png', bbox_inches='tight')
    plt.show()

def plot_volatility_smile():
    """Plots the Implied Volatility Smile across different strike prices."""
    strikes = np.linspace(80, 120, 20)
    S = 100
    
    # Simulate the "smile" curve (OTM options have higher implied vol)
    implied_vols = 0.15 + 0.002 * (strikes - S)**2 
    
    plt.figure(figsize=(8, 5))
    plt.plot(strikes, implied_vols * 100, marker='o', color='blue', label="Implied Volatility")
    
    plt.title("The Volatility Smile")
    plt.xlabel("Strike Price ($)")
    plt.ylabel("Implied Volatility (%)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save the plot as an image
    plt.savefig('Black Scholes Model/visualization/volatility_smile.png', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    print("Generating charts...")
    plot_payoff_diagram()
    plot_volatility_smile()