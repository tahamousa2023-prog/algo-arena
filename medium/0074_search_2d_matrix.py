# Problem 074 — Search a 2D Matrix
# Link: https://leetcode.com/problems/search-a-2d-matrix/
# Difficulty: Medium | Topics: Binary Search, Matrix
#
# PROBLEM:
#   Sorted matrix (each row sorted, first of next row > last of prev).
#   Search for target in O(log(m*n)).
#
# IDEA:
#   Treat matrix as flat sorted array. Map 1D index -> 2D.
#   row = idx // cols,  col = idx % cols
#
# Time : O(log(m*n))
# Space: O(1)

class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // cols][mid % cols]
            if val == target:   return True
            elif val < target:  left  = mid + 1
            else:               right = mid - 1
        return False

if __name__ == "__main__":
    sol = Solution()
    m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert sol.searchMatrix(m, 3)  == True
    assert sol.searchMatrix(m, 13) == False
    print("All tests passed v")
