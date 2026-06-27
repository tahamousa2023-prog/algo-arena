# Problem 566 - Reshape the Matrix
# Link: https://leetcode.com/problems/reshape-the-matrix/
# Difficulty: Easy | Topics: Array, Matrix
#
# PROBLEM:
#   Reshape m x n matrix into r x c. Return original if impossible.
#
# IDEA:
#   Flatten to 1D then slice into rows of length c.
#   Valid only if m*n == r*c.
#
# Time : O(m*n) | Space: O(m*n)

class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        flat = [mat[i][j] for i in range(m) for j in range(n)]
        return [flat[i*c:(i+1)*c] for i in range(r)]

if __name__ == "__main__":
    sol = Solution()
    assert sol.matrixReshape([[1,2],[3,4]], 1, 4) == [[1,2,3,4]]
    assert sol.matrixReshape([[1,2],[3,4]], 2, 4) == [[1,2],[3,4]]
    print("All tests passed v")
