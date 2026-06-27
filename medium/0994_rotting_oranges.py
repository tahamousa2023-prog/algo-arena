# Problem 994 - Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/
# Difficulty: Medium | Topics: Array, BFS, Matrix
#
# PROBLEM:
#   0=empty, 1=fresh, 2=rotten. Each minute rotten oranges rot 4-dir neighbors.
#   Return minutes until no fresh remain. -1 if impossible.
#
# IDEA:
#   Multi-source BFS from ALL rotten oranges simultaneously. Track fresh count.
#
# Time : O(m*n) | Space: O(m*n)

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: queue.append((r, c, 0))
                elif grid[r][c] == 1: fresh += 1
        if fresh == 0: return 0
        max_time = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r, c, time = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    max_time = max(max_time, time + 1)
                    queue.append((nr, nc, time + 1))
        return max_time if fresh == 0 else -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    print("All tests passed v")
