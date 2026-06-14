# Problem 054 — Spiral Matrix
# Link: https://leetcode.com/problems/spiral-matrix/
# Difficulty: Medium | Topics: Array, Matrix, Simulation
#
# PROBLEM:
#   Return all elements of an m×n matrix in spiral order.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Spiral traversal = coverage path planning pattern.
#   Lawn mower / floor sweeping robots use spiral/boustrophedon patterns.
#   Understanding systematic grid traversal is key in coverage robotics.
#
# IDEA:
#   Shrink boundaries as we traverse each layer.
#   top, bottom, left, right define the current boundary.
#   Go right → go down → go left → go up → shrink → repeat.
#
#   [[1,2,3],        Spiral: 1→2→3→6→9→8→7→4→5
#    [4,5,6],
#    [7,8,9]]
#
# Time : O(n * m)
# Space: O(1) — output list not counted

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Go right along top row
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # Go down along right col
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # Go left along bottom row (if still valid)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # Go up along left col (if still valid)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == \
           [1,2,3,6,9,8,7,4,5]
    assert sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == \
           [1,2,3,4,8,12,11,10,9,5,6,7]
    assert sol.spiralOrder([[1]]) == [1]
    print("All tests passed ✓")
