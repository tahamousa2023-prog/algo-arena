# Problem 263 — Ugly Number
# Link: https://leetcode.com/problems/ugly-number/
# Difficulty: Easy | Topics: Math
#
# PROBLEM:
#   An ugly number is a positive integer whose prime factors are 2, 3, and 5.
#   Return True if n is an ugly number.
#
# EXAMPLE:
#   6=2×3 → True,  8=2³ → True,  14=2×7 → False
#
# IDEA:
#   Divide out all factors of 2, 3, and 5.
#   If what remains is 1 → ugly. Otherwise not.
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        return n == 1

if __name__ == "__main__":
    sol = Solution()
    assert sol.isUgly(6)  == True
    assert sol.isUgly(8)  == True
    assert sol.isUgly(14) == False
    assert sol.isUgly(1)  == True
    assert sol.isUgly(0)  == False
    print("All tests passed ✓")
