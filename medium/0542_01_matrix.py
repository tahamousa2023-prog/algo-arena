# Problem 542 — 01 Matrix
# Link: https://leetcode.com/problems/01-matrix/
# Difficulty: Medium | Topics: Graph, BFS, Matrix, DP
#
# PROBLEM:
#   Given a binary matrix, return a matrix where each cell contains
#   the distance to the nearest 0.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   This is the Euclidean Distance Transform (EDT) in binary form.
#   Used in robot navigation to compute clearance from obstacles.
#   Every costmap planner in ROS computes something similar to this.
#
# IDEA:
#   Multi-source BFS from all 0-cells simultaneously.
#   Same wavefront idea as Walls and Gates — but now starting from 0s.
#   1-cells get filled with shortest distance to any 0.
#
#   Matrix [[0,0,0],[0,1,0],[1,1,1]]:
#     BFS starts from all 0s.
#     The center 1 has distance 1 (adjacent to 0).
#     Bottom row 1s: left=1, center=2 (via center 1), right=1.
#     Result: [[0,0,0],[0,1,0],[1,2,1]] ✓
#
# Time : O(n * m)
# Space: O(n * m)

from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        dist  = [[float('inf')] * cols for _ in range(rows)]
        queue = deque()

        # All 0-cells are starting points (distance = 0)
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols
                        and dist[nr][nc] > dist[r][c] + 1):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        return dist


if __name__ == "__main__":
    sol = Solution()
    assert sol.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]) == \
           [[0,0,0],[0,1,0],[0,0,0]]
    assert sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == \
           [[0,0,0],[0,1,0],[1,2,1]]
    print("All tests passed ✓")
