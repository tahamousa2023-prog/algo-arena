# Problem 695 - Max Area of Island
# Link: https://leetcode.com/problems/max-area-of-island/
# Difficulty: Medium | Topics: Array, DFS, Matrix
#
# PROBLEM:
#   Binary grid. Find maximum area of island (connected 1s, 4-directional).
#
# IDEA:
#   DFS from each unvisited 1. Mark visited cells as 0. Count cells per island.
#
# Time : O(m*n) | Space: O(m*n)

class Solution:
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        return max(dfs(r,c) for r in range(rows) for c in range(cols))

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxAreaOfIsland([[0,0,1,0,0],[0,1,1,1,0],[0,0,1,0,0]]) == 5
    assert sol.maxAreaOfIsland([[1,1],[1,0]]) == 3
    print("All tests passed v")
