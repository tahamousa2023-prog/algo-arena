# Problem 231 — Power of Two
# Link: https://leetcode.com/problems/power-of-two/
# Difficulty: Easy | Topics: Math, Bit Manipulation
#
# PROBLEM:
#   Return True if n is a power of two.
#
# EXAMPLE:
#   1→True (2⁰), 16→True (2⁴), 3→False
#
# IDEA:
#   Powers of two in binary have exactly ONE bit set: 1, 10, 100, 1000...
#   n & (n-1) removes the lowest set bit.
#   If result is 0 → only one bit was set → power of two.
#
#   16 = 10000, 15 = 01111, 16&15 = 0 → True ✓
#    3 = 011,    2 = 010,    3&2  = 2 → False ✓
#
# Time : O(1)
# Space: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPowerOfTwo(1)  == True
    assert sol.isPowerOfTwo(16) == True
    assert sol.isPowerOfTwo(3)  == False
    assert sol.isPowerOfTwo(0)  == False
    assert sol.isPowerOfTwo(-4) == False
    print("All tests passed ✓")
