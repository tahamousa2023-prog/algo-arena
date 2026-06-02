# Problem 322 — Coin Change
# Link: https://leetcode.com/problems/coin-change/
# Difficulty: Medium | Topics: Dynamic Programming, BFS
#
# PROBLEM:
#   Given coin denominations and an amount, find the fewest coins needed.
#   Return -1 if it cannot be made.
#
# EXAMPLE:
#   coins=[1,5,10], amount=11 → 2 coins (10+1)
#   coins=[2],      amount=3  → -1 (impossible)
#
# IDEA:
#   DP. Build up solutions from amount=0 to amount=target.
#   dp[i] = fewest coins needed to make amount i
#   dp[0] = 0  (0 coins needed for amount 0)
#   dp[i] = 1 + min(dp[i - coin]) for each coin <= i
#
#   coins=[1,5,10], amount=11:
#   dp[0]=0, dp[1]=1, dp[2]=2, dp[3]=3, dp[4]=4,
#   dp[5]=1, dp[6]=2, ..., dp[10]=1, dp[11]=2  ✓
#
# Time : O(amount * len(coins))
# Space: O(amount)

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Fill with amount+1 as "infinity" (impossible)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # base case

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] <= amount else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1,5,10], 11) == 2
    assert sol.coinChange([1,2,5],  11) == 3
    assert sol.coinChange([2],       3) == -1
    assert sol.coinChange([1],       0) == 0
    print("All tests passed ✓")
