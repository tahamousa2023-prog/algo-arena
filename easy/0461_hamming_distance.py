# Problem 461 — Hamming Distance
# Link: https://leetcode.com/problems/hamming-distance/
# Difficulty: Easy | Topics: Bit Manipulation
#
# PROBLEM:
#   Count positions where corresponding bits of x and y differ.
#
# EXAMPLE:
#   x=1 (0001), y=4 (0100) -> distance = 2
#
# IDEA:
#   XOR gives 1 wherever bits differ. Count the 1-bits.
#   1 ^ 4 = 0101 -> two 1-bits -> distance = 2
#
# Time : O(1) | Space: O(1)

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")

if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingDistance(1, 4)   == 2
    assert sol.hammingDistance(3, 1)   == 1
    assert sol.hammingDistance(93, 73) == 2
    print("All tests passed v")
