# Problem 136 — Single Number
# Link: https://leetcode.com/problems/single-number/
# Difficulty: Easy | Topics: Array, Bit Manipulation
#
# PROBLEM:
#   Every element appears twice except one. Find the single element.
#   Must be O(n) time and O(1) space.
#
# EXAMPLE:
#   [2,2,1]   → 1
#   [4,1,2,1,2] → 4
#
# IDEA:
#   XOR trick: a ^ a = 0, a ^ 0 = a.
#   XOR all numbers together. Pairs cancel out, leaving the single number.
#
#   [4,1,2,1,2]: 4^1^2^1^2 = 4^(1^1)^(2^2) = 4^0^0 = 4 ✓
#
# Time : O(n)
# Space: O(1)

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.singleNumber([2,2,1])     == 1
    assert sol.singleNumber([4,1,2,1,2]) == 4
    assert sol.singleNumber([1])         == 1
    print("All tests passed ✓")
