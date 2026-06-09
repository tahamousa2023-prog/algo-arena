# Problem 417 — Pacific Atlantic Water Flow
# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Difficulty: Medium | Topics: Graph, BFS, DFS, Matrix
#
# PROBLEM:
#   A matrix represents heights of land. Water flows to adjacent cells
#   with equal or lower height. Pacific ocean touches top/left borders.
#   Atlantic ocean touches bottom/right borders.
#   Find all cells where water can flow to BOTH oceans.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   This is a reachability problem on a grid — same structure as
#   occupancy map analysis, flood-fill navigation, and terrain traversal.
#   The reverse-BFS trick is used in multi-source planning (goal-directed).
#
# IDEA:
#   Instead of asking "can water flow FROM cell to ocean?" (hard),
#   we ask "can water flow TO cell FROM ocean?" (easy — reverse BFS).
#   Run BFS from Pacific borders  → mark all Pacific-reachable cells.
#   Run BFS from Atlantic borders → mark all Atlantic-reachable cells.
#   Answer = cells reachable by BOTH.
#
# Time : O(n * m)
# Space: O(n * m)

from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(starts):
            visited = set(starts)
            queue   = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        # Pacific starts: top row + left col
        pacific_starts  = [(r, 0) for r in range(rows)] + \
                          [(0, c) for c in range(cols)]
        # Atlantic starts: bottom row + right col
        atlantic_starts = [(r, cols-1) for r in range(rows)] + \
                          [(rows-1, c) for c in range(cols)]

        pacific  = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        # Cells reachable by both
        return [[r, c] for r, c in pacific & atlantic]


if __name__ == "__main__":
    sol = Solution()
    heights = [[1,2,2,3,5],
               [3,2,3,4,4],
               [2,4,5,3,1],
               [6,7,1,4,5],
               [5,1,1,2,4]]
    result = sol.pacificAtlantic(heights)
    expected = sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])
    assert sorted(result) == expected
    print("All tests passed ✓")
