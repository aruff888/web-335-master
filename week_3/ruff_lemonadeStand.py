"""
Author: Amanda Ruff
Date: January 28, 2026
File Name: ruff_lemonadeStand.py
Description: This program calculates the cost and profit of running a lemonade stand
using Python functions, variables, and string concatenation.
"""

# Function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    total_cost = lemons_cost + sugar_cost
    return total_cost

# Function to calculate profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    profit = selling_price - (lemons_cost + sugar_cost)
    return profit

# Variables for testing
lemons_cost = 5
sugar_cost = 3
selling_price = 12

# Build strings for output
cost_string = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(calculate_cost(lemons_cost, sugar_cost))
profit_string = "Profit: " + str(calculate_profit(lemons_cost, sugar_cost, selling_price))

# Output results
print("Total Cost:", cost_string)
print(profit_string)
