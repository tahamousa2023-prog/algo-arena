# Problem 349 — Intersection of Two Arrays
# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy | Topics: Array, Hash Set, Sorting
#
# PROBLEM:
#   Return the intersection of two arrays (unique elements only).
#
# EXAMPLE:
#   [1,2,2,1], [2,2] → [2]
#   [4,9,5], [9,4,9,8,4] → [9,4]
#
# IDEA:
#   Convert both to sets. Return their intersection.
#
# Time : O(n+m)
# Space: O(n+m)

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.intersection([1,2,2,1], [2,2]))       == [2]
    assert sorted(sol.intersection([4,9,5], [9,4,9,8,4]))   == [4,9]
    assert sorted(sol.intersection([1,2,3], [4,5,6]))       == []
    print("All tests passed ✓")
