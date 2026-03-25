# Problem 069 — Sqrt(x)
# Link: https://leetcode.com/problems/sqrtx/
# Difficulty: Easy | Topics: Math, Binary Search
#
# PROBLEM:
#   Return the integer square root of x (floor value).
#
# EXAMPLE:
#   4 → 2,  8 → 2 (floor of 2.82),  0 → 0
#
# IDEA:
#   Binary search between 0 and x.
#   Find largest m where m*m <= x.
#
# Time : O(log x)
# Space: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right  # right = floor(sqrt(x))

if __name__ == "__main__":
    sol = Solution()
    assert sol.mySqrt(4)  == 2
    assert sol.mySqrt(8)  == 2
    assert sol.mySqrt(0)  == 0
    assert sol.mySqrt(1)  == 1
    assert sol.mySqrt(9)  == 3
    print("All tests passed ✓")
