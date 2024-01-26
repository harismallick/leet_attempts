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
    
    hashmap: dict = {
        "stock_low": None,
        "stock_high": None,
        "potential_low": None,
        "high_index": None
    }
    for price in prices:

        if hashmap["stock_low"] is None:
            hashmap["stock_low"] = price
            continue
        if hashmap["potential_low"] is not None and price - hashmap["potential_low"] > hashmap["stock_high"] - hashmap["stock_low"]:
            hashmap["stock_low"] = hashmap["potential_low"]
            hashmap["stock_high"] = price
            hashmap["potential_low"] = None

        elif price < hashmap["stock_low"] and hashmap["stock_high"] is None:
            hashmap["stock_low"] = price
        elif price < hashmap["stock_low"]:
            if hashmap["potential_low"] is None: 
                hashmap["potential_low"] = price
            elif price < hashmap["potential_low"]:
                hashmap["potential_low"] = price
        elif price > hashmap["stock_low"]:
            if hashmap["stock_high"] is not None:
                if price >= hashmap["stock_high"]:
                    hashmap["stock_high"] = price
                    if hashmap["potential_low"] is not None:
                        hashmap["stock_low"] = hashmap["potential_low"]
                        hashmap["potential_low"] = None
                elif hashmap["potential_low"] is not None and price - hashmap["potential_low"] > hashmap["stock_high"] - hashmap["stock_low"]:
                    hashmap["stock_low"] = hashmap["potential_low"]
                    hashmap["stock_high"] = price
                    hashmap["potential_low"] = None
            else:
                hashmap["stock_high"] = price

    if hashmap["stock_high"] is not None and hashmap["stock_low"] is not None:
        return hashmap["stock_high"] - hashmap["stock_low"]
    return 0
# Solution accepted but 2-pointer suggested solution involves much less lines of code:

def maxProfit2(prices):
    left = 0 #Buy
    right = 1 #Sell
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left] #our current Profit
        if prices[left] < prices[right]:
            max_profit =max(currentProfit,max_profit)
        else:
            left = right
        right += 1
    return max_profit

if __name__ == "__main__":
    print(maxProfit2([7,1,5,3,6,4]))
    print(maxProfit2([2,1,2,1,0,1,2]))
    print(maxProfit2([3,3,5,0,0,3,1,4]))
    print(maxProfit2([5,6,1,3]))

