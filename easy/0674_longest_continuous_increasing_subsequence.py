# Problem 674 - Longest Continuous Increasing Subsequence
# Link: https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# Difficulty: Easy | Topics: Array, Sliding Window
#
# PROBLEM:
#   Return the length of the longest continuous strictly increasing subarray.
#
# IDEA:
#   Track current streak, reset to 1 on non-increase. Track max.
#
# Time : O(n) | Space: O(1)

class Solution:
    def findLengthOfLCIS(self, nums):
        if not nums: return 0
        max_len = curr = 1
        for i in range(1, len(nums)):
            curr = curr + 1 if nums[i] > nums[i-1] else 1
            max_len = max(max_len, curr)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    assert sol.findLengthOfLCIS([1,3,5,4,7]) == 3
    assert sol.findLengthOfLCIS([2,2,2,2])   == 1
    print("All tests passed v")
