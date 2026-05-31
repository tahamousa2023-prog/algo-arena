# Problem 053 — Maximum Subarray
# Link: https://leetcode.com/problems/maximum-subarray/
# Difficulty: Medium | Topics: Array, Dynamic Programming, Greedy
#
# PROBLEM:
#   Find the contiguous subarray with the largest sum.
#
# EXAMPLE:
#   Input : [-2,1,-3,4,-1,2,1,-5,4]
#   Output: 6  (subarray [4,-1,2,1])
#
# IDEA:
#   Kadane's Algorithm.
#   At each index, decide: extend current subarray OR start fresh?
#   current = max(nums[i], current + nums[i])
#   If current goes negative → starting fresh from next element is better.
#
#   Walkthrough [-2,1,-3,4,-1,2,1,-5,4]:
#     curr=-2,  max=-2
#     curr=1,   max=1   (fresh start, -2+1 < 1)
#     curr=-2,  max=1   (1-3=-2)
#     curr=4,   max=4   (fresh start)
#     curr=3,   max=4   (4-1=3)
#     curr=5,   max=5   (3+2=5)
#     curr=6,   max=6   (5+1=6) ← best
#     curr=1,   max=6
#     curr=5,   max=6
#     Return 6 ✓
#
# Time : O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current = nums[0]
        best    = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            best    = max(best, current)

        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert sol.maxSubArray([1])                      == 1
    assert sol.maxSubArray([5,4,-1,7,8])             == 23
    assert sol.maxSubArray([-1,-2,-3])               == -1
    print("All tests passed ✓")
