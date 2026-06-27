# Problem 598 - Range Addition II
# Link: https://leetcode.com/problems/range-addition-ii/
# Difficulty: Easy | Topics: Array, Math
#
# PROBLEM:
#   m x n zero matrix. Each op [a,b] increments rectangle [0..a-1][0..b-1].
#   Return count of maximum-value elements after all operations.
#
# IDEA:
#   Max value cells = intersection of all rectangles = min(a) x min(b).
#
# Time : O(k) | Space: O(1)

class Solution:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxCount(3, 3, [[2,2],[3,3]]) == 4
    assert sol.maxCount(3, 3, [])            == 9
    print("All tests passed v")
