# Problem 367 — Valid Perfect Square
# Link: https://leetcode.com/problems/valid-perfect-square/
# Difficulty: Easy | Topics: Math, Binary Search
#
# PROBLEM:
#   Return True if num is a perfect square WITHOUT using sqrt().
#
# EXAMPLE:
#   16 → True  (4*4=16)
#   14 → False
#
# IDEA:
#   Binary search between 1 and num.
#   Find if any integer mid satisfies mid*mid == num.
#
#   num=16: l=1,r=16 → mid=8, 64>16 → r=7
#           l=1,r=7  → mid=4, 16=16 → True ✓
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPerfectSquare(16) == True
    assert sol.isPerfectSquare(14) == False
    assert sol.isPerfectSquare(1)  == True
    assert sol.isPerfectSquare(4)  == True
    print("All tests passed ✓")
