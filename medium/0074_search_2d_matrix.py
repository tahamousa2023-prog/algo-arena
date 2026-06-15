# Problem 074 — Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium | Topics: Array, Binary Search, Matrix
#
# PROBLEM:
#   An m×n matrix where each row is sorted and the first element
#   of each row > last element of previous row. Search for target.
#
# EXAMPLE:
#   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3 → True
#   matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=13 → False
#
# IDEA:
#   Treat the entire matrix as a flat sorted array.
#   Map 1D index to 2D: row = idx // cols, col = idx % cols
#   Then do standard binary search.
#
#   Matrix has m*n elements. mid=7 in a 3×4 matrix:
#     row = 7 // 4 = 1, col = 7 % 4 = 3 → matrix[1][3] = 20
#
# Time : O(log(m*n))
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D position
            val = matrix[mid // cols][mid % cols]

            if val == target:
                return True
            elif val < target:
                left  = mid + 1
            else:
                right = mid - 1

        return False

if __name__ == "__main__":
    sol = Solution()
    m1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert sol.searchMatrix(m1, 3)  == True
    assert sol.searchMatrix(m1, 13) == False
    assert sol.searchMatrix([[1]], 1) == True
    assert sol.searchMatrix([[1]], 2) == False
    print("All tests passed ✓")
