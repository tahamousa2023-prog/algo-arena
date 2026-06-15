# Problem 075 — Sort Colors
# Link: https://leetcode.com/problems/sort-colors/
# Difficulty: Medium | Topics: Array, Two Pointers, Sorting
#
# PROBLEM:
#   Sort an array containing only 0s, 1s, and 2s in-place.
#   (Dutch National Flag problem)
#
# EXAMPLE:
#   [2,0,2,1,1,0] → [0,0,1,1,2,2]
#
# IDEA:
#   Three pointers: low, mid, high.
#   low  = boundary between 0s and 1s
#   mid  = current element being examined
#   high = boundary between 1s and 2s
#
#   If nums[mid]==0 → swap with low, advance both low and mid
#   If nums[mid]==1 → it's in right place, advance mid
#   If nums[mid]==2 → swap with high, shrink high (don't advance mid yet)
#
#   [2,0,2,1,1,0]: low=0,mid=0,high=5
#     mid=2 → swap(0,5) → [0,0,2,1,1,2], high=4
#     mid=0 → swap(0,0) → [0,0,2,1,1,2], low=1,mid=1
#     mid=0 → swap(1,1) → low=2,mid=2
#     mid=2 → swap(2,4) → [0,0,1,1,2,2], high=3
#     mid=1 → mid=3
#     mid=1 → mid=4 > high=3 → done ✓
#
# Time : O(n)
# Space: O(1)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1   # don't advance mid — need to check swapped value

if __name__ == "__main__":
    sol = Solution()
    nums = [2,0,2,1,1,0]
    sol.sortColors(nums)
    assert nums == [0,0,1,1,2,2]

    nums2 = [2,0,1]
    sol.sortColors(nums2)
    assert nums2 == [0,1,2]

    nums3 = [0]
    sol.sortColors(nums3)
    assert nums3 == [0]
    print("All tests passed ✓")
