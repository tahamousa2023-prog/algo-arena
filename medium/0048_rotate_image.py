# Problem 048 — Rotate Image
# Link: https://leetcode.com/problems/rotate-image/
# Difficulty: Medium | Topics: Array, Math, Matrix
#
# PROBLEM:
#   Rotate an n×n matrix 90 degrees clockwise, in-place.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   2D matrix rotations are fundamental in:
#   - Rotating robot sensor frames (LiDAR, camera)
#   - Transforming occupancy grids when robot rotates
#   - Coordinate frame transformations in 2D navigation
#   Understanding in-place rotation = understanding rotation matrices.
#
# IDEA:
#   Rotate 90° clockwise = Transpose + Reverse each row
#
#   Step 1 — Transpose (flip over diagonal):
#     [1,2,3]      [1,4,7]
#     [4,5,6]  →   [2,5,8]
#     [7,8,9]      [3,6,9]
#
#   Step 2 — Reverse each row:
#     [1,4,7]      [7,4,1]
#     [2,5,8]  →   [8,5,2]
#     [3,6,9]      [9,6,3]  ✓
#
# Time : O(n²)
# Space: O(1) — in-place

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose — swap matrix[i][j] with matrix[j][i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    sol = Solution()

    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(m1)
    assert m1 == [[7,4,1],[8,5,2],[9,6,3]]

    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(m2)
    assert m2 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    print("All tests passed ✓")
