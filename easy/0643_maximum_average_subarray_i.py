# Problem 643 - Maximum Average Subarray I
# Link: https://leetcode.com/problems/maximum-average-subarray-i/
# Difficulty: Easy | Topics: Array, Sliding Window
#
# PROBLEM:
#   Find contiguous subarray of length k with maximum average.
#
# IDEA:
#   Sliding window. Add next element, remove leftmost. Track max sum.
#
# Time : O(n) | Space: O(1)

class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = sum(nums[:k])
        max_sum    = window_sum
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        return max_sum / k

if __name__ == "__main__":
    sol = Solution()
    assert sol.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
    print("All tests passed v")
