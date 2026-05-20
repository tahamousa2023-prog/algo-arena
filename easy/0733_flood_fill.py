# Problem 733 — Flood Fill
# Link: https://leetcode.com/problems/flood-fill/
# Difficulty: Easy | Topics: Array, DFS, BFS
#
# PROBLEM:
#   Given an image (2D grid), a starting pixel (sr, sc), and a new color,
#   flood fill starting from (sr,sc) — like the paint bucket tool.
#
# EXAMPLE:
#   image = [[1,1,1],[1,1,0],[1,0,1]], sr=1, sc=1, color=2
#   Output: [[2,2,2],[2,2,0],[2,0,1]]
#
# IDEA:
#   DFS from the starting pixel.
#   Spread to all 4 neighbors that have the same original color.
#   Change each visited pixel to the new color.
#
# Time : O(n * m) — at most visit every cell
# Space: O(n * m) — recursion stack

class Solution:
    def floodFill(self, image: list[list[int]],
                  sr: int, sc: int, color: int) -> list[list[int]]:

        original = image[sr][sc]

        # If already the target color, nothing to do
        if original == color:
            return image

        def dfs(r, c):
            # Out of bounds or not the original color → stop
            if r < 0 or r >= len(image): return
            if c < 0 or c >= len(image[0]): return
            if image[r][c] != original: return

            image[r][c] = color  # fill this pixel

            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left

        dfs(sr, sc)
        return image

if __name__ == "__main__":
    sol = Solution()
    img = [[1,1,1],[1,1,0],[1,0,1]]
    assert sol.floodFill(img, 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]

    img2 = [[0,0,0],[0,0,0]]
    assert sol.floodFill(img2, 0, 0, 0) == [[0,0,0],[0,0,0]]
    print("All tests passed ✓")
