# Problem 238 — Product of Array Except Self
# Link: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium | Topics: Array, Prefix Product
#
# PROBLEM:
#   Return array where output[i] = product of all elements except nums[i].
#   O(n) time, no division allowed.
#
# EXAMPLE:
#   [1,2,3,4] -> [24,12,8,6]
#
# IDEA:
#   Two passes:
#   Pass 1 left to right:  result[i] = product of everything LEFT of i
#   Pass 2 right to left:  multiply result[i] by product of everything RIGHT of i
#
# Time : O(n) | Space: O(1)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n      = len(nums)
        result = [1] * n
        left   = 1
        for i in range(n):
            result[i] = left
            left     *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right
            right     *= nums[i]
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert sol.productExceptSelf([1,1])     == [1,1]
    print("All tests passed v")
