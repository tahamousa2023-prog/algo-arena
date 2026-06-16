# Problem 062 — Unique Paths
# Link: https://leetcode.com/problems/unique-paths/
# Difficulty: Medium | Topics: Math, Dynamic Programming
#
# PROBLEM:
#   A robot starts at top-left of an m×n grid.
#   It can only move right or down. How many unique paths to bottom-right?
#
# WHY THIS MATTERS FOR ROBOTICS:
#   This is a simplified motion planning problem.
#   Counting valid paths = understanding combinatorial explosion
#   in grid-based planning. The DP table structure is identical to
#   value iteration tables used in discrete MDP planning.
#
# IDEA:
#   DP. dp[r][c] = number of ways to reach cell (r,c).
#   dp[r][c] = dp[r-1][c] + dp[r][c-1]  (came from above or from left)
#   Base case: top row and left column all have 1 path (only one direction).
#
#   3×3 grid:
#     1  1  1
#     1  2  3
#     1  3  6   → dp[2][2] = 6 ✓
#
# Time : O(m * n)
# Space: O(m * n)  — can be optimized to O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(1, 1) == 1
    assert sol.uniquePaths(3, 3) == 6
    print("All tests passed ✓")
