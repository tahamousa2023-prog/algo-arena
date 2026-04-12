# Problem 190 — Reverse Bits
# Link: https://leetcode.com/problems/reverse-bits/
# Difficulty: Easy | Topics: Bit Manipulation
#
# PROBLEM:
#   Reverse bits of a 32-bit unsigned integer.
#
# EXAMPLE:
#   n = 00000010100101000001111010011100
#   output = 00111001011110000010100101000000 = 964176192
#
# IDEA:
#   For 32 iterations: extract last bit of n, shift it into result.
#   Right shift n, left shift result.
#
# Time : O(1) — always 32 iterations
# Space: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)  # shift result left, add last bit of n
            n >>= 1
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseBits(0b00000010100101000001111010011100) == 964176192
    assert sol.reverseBits(0b11111111111111111111111111111101) == 3221225471
    print("All tests passed ✓")
