# Problem 268 — Missing Number
# Link: https://leetcode.com/problems/missing-number/
# Difficulty: Easy | Topics: Array, Math, Bit Manipulation
#
# PROBLEM:
#   Given array of n distinct numbers in range [0,n], find the missing one.
#
# EXAMPLE:
#   [3,0,1]  → 2
#   [9,6,4,2,3,5,7,0,1] → 8
#
# IDEA:
#   Sum formula: expected sum = n*(n+1)/2
#   Missing number = expected - actual sum
#
# Time : O(n)
# Space: O(1)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        return expected - sum(nums)

if __name__ == "__main__":
    sol = Solution()
    assert sol.missingNumber([3,0,1])              == 2
    assert sol.missingNumber([0,1])                == 2
    assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    print("All tests passed ✓")
