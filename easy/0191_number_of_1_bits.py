# Problem 191 — Number of 1 Bits
# Link: https://leetcode.com/problems/number-of-1-bits/
# Difficulty: Easy | Topics: Bit Manipulation
#
# PROBLEM:
#   Return the number of set bits (1s) in a 32-bit integer.
#   Also known as Hamming weight.
#
# EXAMPLE:
#   11 = 0b1011 → 3 set bits
#   128 = 0b10000000 → 1 set bit
#
# IDEA:
#   n & (n-1) removes the lowest set bit each time.
#   Count how many times we can do this before n=0.
#
#   11 (1011): 11&10=1010 → 1010&1001=1000 → 1000&0111=0 → 3 ops ✓
#
# Time : O(k)   k = number of set bits
# Space: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1  # remove lowest set bit
            count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(11)  == 3
    assert sol.hammingWeight(128) == 1
    assert sol.hammingWeight(0)   == 0
    assert sol.hammingWeight(0b11111111111111111111111111111101) == 31
    print("All tests passed ✓")
