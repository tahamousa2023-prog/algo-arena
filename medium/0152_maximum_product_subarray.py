# Problem 152 — Maximum Product Subarray
# Link: https://leetcode.com/problems/maximum-product-subarray/
# Difficulty: Medium | Topics: Array, Dynamic Programming
#
# PROBLEM:
#   Find the contiguous subarray with the largest product.
#
# EXAMPLE:
#   Input : [2,3,-2,4]
#   Output: 6  (subarray [2,3])
#
# IDEA:
#   Unlike sum (Kadane's), negatives matter here.
#   A negative * negative = positive (could become max).
#   So we track BOTH max and min product at each step.
#
#   At each number:
#     new_max = max(num, max*num, min*num)
#     new_min = min(num, max*num, min*num)
#
#   Walkthrough [2,3,-2,4]:
#     num=2:  max=2,  min=2
#     num=3:  max=6,  min=3   (best so far: 6)
#     num=-2: max=-2, min=-12 (best so far: 6)
#     num=4:  max=-8, min=-48 (best so far: 6)
#     Return 6 ✓
#
# Time : O(n)
# Space: O(1)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        best     = nums[0]

        for num in nums[1:]:
            # All three candidates for new max/min
            candidates = (num, max_prod * num, min_prod * num)
            max_prod   = max(candidates)
            min_prod   = min(candidates)
            best       = max(best, max_prod)

        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProduct([2,3,-2,4])    == 6
    assert sol.maxProduct([-2,0,-1])     == 0
    assert sol.maxProduct([-2,3,-4])     == 24
    assert sol.maxProduct([-2])          == -2
    print("All tests passed ✓")
