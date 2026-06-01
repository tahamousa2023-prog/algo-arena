# Problem 070 — Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/
# Difficulty: Easy | Topics: Dynamic Programming
#
# PROBLEM:
#   To climb n stairs, you can take 1 or 2 steps at a time.
#   How many distinct ways can you reach the top?
#
# EXAMPLE:
#   n=3 → 3 ways: (1+1+1), (1+2), (2+1)
#
# IDEA:
#   This is Fibonacci! The number of ways to reach stair n equals
#   ways to reach stair n-1 (take 1 step) +
#   ways to reach stair n-2 (take 2 steps)
#
#   n=1: 1 way
#   n=2: 2 ways
#   n=3: ways(2) + ways(1) = 2+1 = 3 ✓
#   n=4: ways(3) + ways(2) = 3+2 = 5
#
# Time : O(n)
# Space: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1  # ways to reach stair 1
        prev1 = 2  # ways to reach stair 2

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2   = prev1
            prev1   = current

        return prev1

if __name__ == "__main__":
    sol = Solution()
    assert sol.climbStairs(1) == 1
    assert sol.climbStairs(2) == 2
    assert sol.climbStairs(3) == 3
    assert sol.climbStairs(5) == 8
    assert sol.climbStairs(10) == 89
    print("All tests passed ✓")
