# Problem 283 — Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy | Topics: Array, Two Pointers
#
# PROBLEM:
#   Move all zeroes to the end while maintaining relative order of non-zeroes.
#   Must be done in-place.
#
# EXAMPLE:
#   [0,1,0,3,12] → [1,3,12,0,0]
#   [0]          → [0]
#
# IDEA:
#   Slow pointer tracks where next non-zero goes.
#   Fast pointer finds non-zero elements.
#   After placing all non-zeroes, fill the rest with 0.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        # Fill rest with zeroes
        for i in range(slow, len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    assert nums == [1,3,12,0,0]

    nums2 = [0]
    sol.moveZeroes(nums2)
    assert nums2 == [0]
    print("All tests passed ✓")
