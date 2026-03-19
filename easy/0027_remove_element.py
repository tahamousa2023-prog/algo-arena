# Problem 027 — Remove Element
# Link: https://leetcode.com/problems/remove-element/
# Difficulty: Easy | Topics: Array, Two Pointers
#
# PROBLEM:
#   Remove all occurrences of val from nums in-place.
#   Return k = number of elements not equal to val.
#
# EXAMPLE:
#   nums=[3,2,2,3], val=3 → k=2, nums=[2,2,_,_]
#   nums=[0,1,2,2,3,0,4,2], val=2 → k=5
#
# IDEA:
#   Slow pointer tracks where next non-val element goes.
#   Fast pointer scans every element.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,2,3]
    assert sol.removeElement(nums, 3) == 2
    assert sorted(nums[:2]) == [2,2]

    nums2 = [0,1,2,2,3,0,4,2]
    assert sol.removeElement(nums2, 2) == 5
    print("All tests passed ✓")
