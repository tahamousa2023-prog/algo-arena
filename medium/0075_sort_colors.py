# Problem 075 — Sort Colors
# Link: https://leetcode.com/problems/sort-colors/
# Difficulty: Medium | Topics: Array, Two Pointers
#
# PROBLEM:
#   Sort array of 0s, 1s, 2s in-place. (Dutch National Flag)
#
# EXAMPLE:
#   [2,0,2,1,1,0] -> [0,0,1,1,2,2]
#
# IDEA:
#   Three pointers: low, mid, high.
#   0 -> swap to low section, advance both low and mid
#   1 -> already in place, advance mid
#   2 -> swap to high section, shrink high
#
# Time : O(n)
# Space: O(1)

class Solution:
    def sortColors(self, nums: list) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1; mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

if __name__ == "__main__":
    sol = Solution()
    nums = [2,0,2,1,1,0]
    sol.sortColors(nums)
    assert nums == [0,0,1,1,2,2]
    nums2 = [2,0,1]
    sol.sortColors(nums2)
    assert nums2 == [0,1,2]
    print("All tests passed v")
