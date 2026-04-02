# Problem 119 — Pascal's Triangle II
# Link: https://leetcode.com/problems/pascals-triangle-ii/
# Difficulty: Easy | Topics: Array, DP
#
# PROBLEM:
#   Return the rowIndex-th (0-indexed) row of Pascal's triangle.
#
# EXAMPLE:
#   rowIndex=3 → [1,3,3,1]
#   rowIndex=0 → [1]
#
# IDEA:
#   Build row iteratively. Update in-place from right to left
#   to avoid using previous row values before they're updated.
#
# Time : O(n²)
# Space: O(n)

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i-1, 0, -1):  # right to left!
                row[j] += row[j-1]
        return row

if __name__ == "__main__":
    sol = Solution()
    assert sol.getRow(0) == [1]
    assert sol.getRow(1) == [1,1]
    assert sol.getRow(3) == [1,3,3,1]
    assert sol.getRow(4) == [1,4,6,4,1]
    print("All tests passed ✓")
