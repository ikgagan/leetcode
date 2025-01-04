# Question : Best Time to Buy and Sell Stock
# Description:
# You are given an array prices where prices[i] is the price of a given stock on the i-th day.
# Find the maximum profit you can achieve. You may complete at most one transaction.

# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.


def maxProfit(prices: list[int]) -> int:
    # Initialize variables
    min_price = float('inf')  # Start with a very high minimum price
    max_profit = 0            # Initialize max profit as 0

    # Traverse through the prices
    for price in prices:
        # Update the minimum price seen so far
        if price < min_price:
            min_price = price
        # Calculate potential profit
        potential_profit = price - min_price
        # Update max profit if the potential profit is higher
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # Output: 5

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))  # Output: 0 (No profitable transaction possible)

