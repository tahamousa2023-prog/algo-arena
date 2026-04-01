# Problem 118 — Pascal's Triangle
# Link: https://leetcode.com/problems/pascals-triangle/
# Difficulty: Easy | Topics: Array, DP
#
# PROBLEM:
#   Given numRows, return the first numRows of Pascal's triangle.
#   Each row starts and ends with 1.
#   Each inner element = sum of two elements above it.
#
# EXAMPLE:
#   numRows=5 →
#   [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# IDEA:
#   Build row by row. Each row starts as [1].
#   Inner values come from previous row: row[j] = prev[j-1] + prev[j].
#
# Time : O(n²)
# Space: O(n²)

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            prev = triangle[i-1]
            row  = [1]
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            triangle.append(row)
        return triangle

if __name__ == "__main__":
    sol = Solution()
    assert sol.generate(1) == [[1]]
    assert sol.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print("All tests passed ✓")
