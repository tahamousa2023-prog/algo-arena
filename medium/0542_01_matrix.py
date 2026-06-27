# Problem 542 - 01 Matrix
# Link: https://leetcode.com/problems/01-matrix/
# Difficulty: Medium | Topics: Array, BFS, Matrix, DP
#
# PROBLEM:
#   Binary matrix. Return matrix where each cell = distance to nearest 0.
#
# IDEA:
#   Multi-source BFS from ALL 0-cells simultaneously.
#   First time BFS reaches a 1-cell = shortest distance to any 0.
#
# Time : O(m*n) | Space: O(m*n)

from collections import deque

class Solution:
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        dist  = [[float("inf")] * cols for _ in range(rows)]
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dist[r][c] + 1 < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))
        return dist

if __name__ == "__main__":
    sol = Solution()
    assert sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]) == [[0,0,0],[0,1,0],[1,2,1]]
    print("All tests passed v")
