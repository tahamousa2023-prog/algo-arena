# Problem 033 — Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium | Topics: Array, Binary Search
#
# PROBLEM:
#   A sorted array was rotated at an unknown pivot.
#   Search for target in O(log n).
#
# EXAMPLE:
#   Input : [4,5,6,7,0,1,2], target=0
#   Output: 4
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Searching in partially ordered data appears in sensor processing —
#   e.g., searching in a circular buffer of timestamps, or finding
#   a specific encoder value in a wrapped angle array.
#   The key insight (one half is always sorted) generalizes to
#   any search problem where partial structure exists.
#
# IDEA:
#   Modified binary search. One of the two halves is ALWAYS sorted.
#   Check which half is sorted, then decide which half target is in.
#
#   [4,5,6,7,0,1,2], target=0:
#     l=0, r=6, mid=3, nums[3]=7
#     Left half [4,5,6,7] is sorted. Is 0 in [4,7]? No → go right.
#     l=4, r=6, mid=5, nums[5]=1
#     Left half [0,1] is sorted. Is 0 in [0,1]? Yes → go left.
#     l=4, r=4 → return 4 ✓
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1   # target in left half
                else:
                    left  = mid + 1   # target in right half
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left  = mid + 1   # target in right half
                else:
                    right = mid - 1   # target in left half

        return -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4,5,6,7,0,1,2], 0) == 4
    assert sol.search([4,5,6,7,0,1,2], 3) == -1
    assert sol.search([1], 0)             == -1
    assert sol.search([1], 1)             == 0
    print("All tests passed ✓")
