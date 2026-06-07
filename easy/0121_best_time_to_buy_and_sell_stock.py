# ============================================================
#  Problem 121 — Best Time to Buy and Sell Stock
#  Link   : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#  Difficulty: Easy
#  Topics : Array, Greedy
# ============================================================
#
#  PROBLEM STATEMENT
#  -----------------
#  Given prices[i] = stock price on day i, return max profit
#  from one buy and one sell. Return 0 if no profit possible.
#
#  Example:
#    Input : [7, 1, 5, 3, 6, 4]
#    Output: 5  ? buy day 2 (price=1), sell day 5 (price=6)
#
# ============================================================
#  THINKING PROCESS
# ============================================================
#
#  Brute Force: try every (buy, sell) pair ? O(n²). Too slow.
#
#  One Pass Greedy:
#    Track min_price seen so far (best day to have bought).
#    For each price: profit = price - min_price ? update best.
#
#  Walkthrough with [7, 1, 5, 3, 6, 4]:
#    price=7 ? min=7,  profit=0
#    price=1 ? min=1,  profit=0   (new low!)
#    price=5 ? min=1,  profit=4
#    price=3 ? min=1,  profit=4
#    price=6 ? min=1,  profit=5   ? best
#    price=4 ? min=1,  profit=5
#    Return 5 ?
#
#  Time : O(n)
#  Space: O(1)
# ============================================================

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price  = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1])    == 0
    assert sol.maxProfit([1, 2, 3, 4, 5])    == 4
    assert sol.maxProfit([5])                == 0
    print("All test cases passed ?")
