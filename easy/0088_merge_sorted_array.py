# Problem 088 — Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy | Topics: Array, Two Pointers, Sorting
#
# PROBLEM:
#   Merge nums2 into nums1 in-place. nums1 has extra space at the end.
#   nums1 has m valid elements, nums2 has n valid elements.
#
# EXAMPLE:
#   nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3 → [1,2,2,3,5,6]
#
# IDEA:
#   Fill from the END of nums1 (avoids overwriting unread elements).
#   Compare nums1[m-1] and nums2[n-1], place the larger one at position m+n-1.
#
# Time : O(m+n)
# Space: O(1)

class Solution:
    def merge(self, nums1: list[int], m: int,
              nums2: list[int], n: int) -> None:
        p1 = m - 1      # pointer for nums1 valid part
        p2 = n - 1      # pointer for nums2
        p  = m + n - 1  # pointer for merged position

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    sol.merge(nums1, 3, [2,5,6], 3)
    assert nums1 == [1,2,2,3,5,6]

    nums2 = [1]
    sol.merge(nums2, 1, [], 0)
    assert nums2 == [1]

    nums3 = [0]
    sol.merge(nums3, 0, [1], 1)
    assert nums3 == [1]
    print("All tests passed ✓")
