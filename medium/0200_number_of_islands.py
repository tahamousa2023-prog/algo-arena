# Problem 200 — Number of Islands
# Link: https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium | Topics: Array, DFS, BFS
#
# PROBLEM:
#   Given a 2D grid of '1's (land) and '0's (water), count the islands.
#   An island is surrounded by water and formed by connecting adjacent land.
#
# EXAMPLE:
#   Input:
#     11110
#     11010
#     11000
#     00000
#   Output: 1
#
# IDEA:
#   DFS. For each unvisited '1', start a DFS that marks all
#   connected land as visited ('0'). Each DFS start = one island.
#
# Time : O(n * m)
# Space: O(n * m)

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        islands = 0

        def dfs(r, c):
            if r < 0 or r >= len(grid):    return
            if c < 0 or c >= len(grid[0]): return
            if grid[r][c] != '1':          return

            grid[r][c] = '0'  # mark as visited
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands

if __name__ == "__main__":
    sol = Solution()
    grid1 = [["1","1","1","1","0"],
             ["1","1","0","1","0"],
             ["1","1","0","0","0"],
             ["0","0","0","0","0"]]
    assert sol.numIslands(grid1) == 1

    grid2 = [["1","1","0","0","0"],
             ["1","1","0","0","0"],
             ["0","0","1","0","0"],
             ["0","0","0","1","1"]]
    assert sol.numIslands(grid2) == 3
    print("All tests passed ✓")
