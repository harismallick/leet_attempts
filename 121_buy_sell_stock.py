## 121. Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

# Difficulty: Easy
# Algorithm to detect "buy low sell high" scenarios. Return option with max profit.
# 2-pointer solution

def maxProfit(prices: list[int]) -> int:
    
    # max_profit: int = 0
    # for i, _ in enumerate(prices):
    #     temp_max_profit: int = 0
    #     for j in range(i+1, len(prices)):
    #         diff: int = prices[j] - prices[i]
    #         if diff > 0 and diff > temp_max_profit:
    #             temp_max_profit = diff
    #     if temp_max_profit > max_profit:
    #         max_profit = temp_max_profit
    # return max_profit

## O(m*n) was too slow. Need faster algorithm
    
# Solution 2:
    # i: int = 0
    # j: int = len(prices)-1
    # while i != j:
    #     max_price: int = max(prices[i:j+1])
    #     min_price: int = min(prices[i:j+1])
    #     if prices.index(min_price) < prices.index(max_price):
    #         return max_price - min_price
    #     i += 1
    #     j -= 1
        
    # return 0
# Solution 2 not accepted by Leet
# Solution 3:
    
        
    pass


if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))
