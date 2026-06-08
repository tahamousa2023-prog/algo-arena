# Problem 994 — Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/
# Difficulty: Medium | Topics: Graph, BFS, Matrix
#
# PROBLEM:
#   Grid: 0=empty, 1=fresh orange, 2=rotten orange.
#   Every minute, fresh oranges adjacent to rotten ones become rotten.
#   Return the minimum time until no fresh oranges remain, or -1.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   This models simultaneous wavefront propagation from multiple sources —
#   the same principle used in multi-robot coverage planning and
#   sensor coverage problems. BFS level-by-level = time-stepped simulation.
#
# IDEA:
#   Multi-source BFS from all rotten oranges simultaneously.
#   Each BFS level = 1 minute.
#   After BFS, check if any fresh oranges remain → return -1.
#
#   Grid [[2,1,1],[1,1,0],[0,1,1]]:
#     t=0: rotten={(0,0)}, fresh=6
#     t=1: (0,1),(1,0) rot → fresh=4
#     t=2: (0,2),(1,1) rot → fresh=2
#     t=3: (2,1) rots  → fresh=1
#     t=4: (2,2) rots  → fresh=0
#     Return 4 ✓
#
# Time : O(n * m)
# Space: O(n * m)

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue  = deque()
        fresh  = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_time = 0

        while queue:
            r, c, t = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    fresh   -= 1
                    max_time = max(max_time, t + 1)
                    queue.append((nr, nc, t + 1))

        return max_time if fresh == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert sol.orangesRotting([[0,2]])                   == 0
    print("All tests passed ✓")
