# Problem 286 — Walls and Gates
# Link: https://leetcode.com/problems/walls-and-gates/
# Difficulty: Medium | Topics: Graph, BFS, Matrix
#
# PROBLEM:
#   You are given a 2D grid:
#     -1 = wall, 0 = gate, INF = empty room
#   Fill each empty room with the distance to its nearest gate.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   This is EXACTLY how robot costmaps and distance fields work.
#   Computing distance-to-obstacle or distance-to-goal on a grid
#   is the foundation of navigation planning (Voronoi fields, EDT).
#   Multi-source BFS from all gates simultaneously = wavefront propagation.
#
# IDEA:
#   Multi-source BFS. Start from ALL gates at once (distance=0).
#   Expand outward — each step adds 1 to distance.
#   This is more efficient than running BFS from each gate separately.
#
#   Grid visualization:
#     INF  -1  0   INF        3  -1  0   1
#     INF  INF INF  -1   →    2   2  1  -1
#      0   -1  INF INF        0  -1  2   3
#     INF  -1  INF INF        1  -1  3   4
#
# Time : O(n * m)
# Space: O(n * m)

from collections import deque

INF = 2**31 - 1

class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Add all gates to the queue simultaneously
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        # BFS outward from all gates at once
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and rooms[nr][nc] == INF):
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))


if __name__ == "__main__":
    sol = Solution()
    grid = [[INF, -1,  0,  INF],
            [INF, INF, INF, -1],
            [INF, -1,  INF, -1],
            [0,   -1,  INF, INF]]
    sol.wallsAndGates(grid)
    expected = [[3, -1, 0,  1],
                [2,  2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3,  4]]
    assert grid == expected
    print("All tests passed ✓")
