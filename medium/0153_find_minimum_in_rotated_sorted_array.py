# Problem 153 — Find Minimum in Rotated Sorted Array
# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Difficulty: Medium | Topics: Array, Binary Search
#
# PROBLEM:
#   A sorted array was rotated. Find the minimum element.
#
# EXAMPLE:
#   Input : [3,4,5,1,2]
#   Output: 1
#
# IDEA:
#   Binary search. The minimum is where the "rotation break" is.
#   If nums[mid] > nums[right] → minimum is in right half
#   Else                       → minimum is in left half (including mid)
#
#   Walkthrough [3,4,5,1,2]:
#     l=0, r=4 → mid=2, nums[2]=5 > nums[4]=2 → go right, l=3
#     l=3, r=4 → mid=3, nums[3]=1 < nums[4]=2 → go left, r=3
#     l=3, r=3 → return nums[3]=1 ✓
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1   # min is in right half
            else:
                right = mid      # min is mid or in left half

        return nums[left]

if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin([3,4,5,1,2])   == 1
    assert sol.findMin([4,5,6,7,0,1,2]) == 0
    assert sol.findMin([11,13,15,17]) == 11
    print("All tests passed ✓")
