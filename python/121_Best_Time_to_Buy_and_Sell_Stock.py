from ftplib import all_errors
from typing import List



def maxProfit(prices: List[int]) -> int:
    profit = 0
    buy = prices[0]
    for price in prices[1:]:
        if price > buy:
            profit = max(profit, price - buy)
        else:
            buy = price
    return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    answer = 5
    actual_answer = maxProfit(prices)
    print(actual_answer)
    print(actual_answer == answer)
    print("Next example")
    prices = [7,6,4,3,1]
    answer = 0
    actual_answer = maxProfit(prices)
    print(actual_answer)
    print(actual_answer == answer)