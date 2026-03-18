# Problem 026 — Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy | Topics: Array, Two Pointers
#
# PROBLEM:
#   Given a sorted array, remove duplicates in-place.
#   Return the number of unique elements k.
#   The first k elements of the array should hold the unique values.
#
# EXAMPLE:
#   [1,1,2]       → k=2, array=[1,2,_]
#   [0,0,1,1,1,2,2,3,3,4] → k=5, array=[0,1,2,3,4,_,_,_,_,_]
#
# IDEA:
#   Two pointers: slow pointer marks where next unique goes,
#   fast pointer scans for new unique values.
#
#   [1,1,2]: slow=0
#     fast=1: nums[1]==nums[0] → skip
#     fast=2: nums[2]!=nums[0] → slow=1, nums[1]=2
#   k = slow+1 = 2 ✓
#
# Time : O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,2]
    assert sol.removeDuplicates(nums) == 2
    assert nums[:2] == [1,2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    assert sol.removeDuplicates(nums2) == 5
    assert nums2[:5] == [0,1,2,3,4]
    print("All tests passed ✓")
