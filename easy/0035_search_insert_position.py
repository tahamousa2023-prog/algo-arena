# Problem 035 — Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy | Topics: Array, Binary Search
#
# PROBLEM:
#   Given a sorted array and a target, return the index where target is found,
#   or where it would be inserted to keep the array sorted.
#
# EXAMPLE:
#   [1,3,5,6], target=5 → 2
#   [1,3,5,6], target=2 → 1
#   [1,3,5,6], target=7 → 4
#
# IDEA:
#   Standard binary search. When loop ends, left = insertion point.
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left  # insertion point when not found

if __name__ == "__main__":
    sol = Solution()
    assert sol.searchInsert([1,3,5,6], 5) == 2
    assert sol.searchInsert([1,3,5,6], 2) == 1
    assert sol.searchInsert([1,3,5,6], 7) == 4
    assert sol.searchInsert([1,3,5,6], 0) == 0
    print("All tests passed ✓")
