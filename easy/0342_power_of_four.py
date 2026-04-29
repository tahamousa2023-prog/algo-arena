# Problem 342 — Power of Four
# Link: https://leetcode.com/problems/power-of-four/
# Difficulty: Easy | Topics: Math, Bit Manipulation
#
# PROBLEM:
#   Return True if n is a power of four.
#
# EXAMPLE:
#   16→True (4²), 5→False, 1→True (4⁰)
#
# IDEA:
#   Powers of four are also powers of two (one bit set).
#   Extra condition: the single set bit must be at an even position.
#   0x55555555 = 01010101...01 in binary (marks even bit positions).
#   n>0 AND n is power of two AND n & 0x55555555 != 0.
#
# Time : O(1)
# Space: O(1)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0 and
                (n & (n-1)) == 0 and     # power of two
                (n & 0x55555555) != 0)   # bit at even position

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPowerOfFour(16) == True
    assert sol.isPowerOfFour(5)  == False
    assert sol.isPowerOfFour(1)  == True
    assert sol.isPowerOfFour(8)  == False
    print("All tests passed ✓")
