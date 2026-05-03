# Problem 350 — Intersection of Two Arrays II
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Difficulty: Easy | Topics: Array, Hash Map, Sorting
#
# PROBLEM:
#   Return intersection including duplicates (each element as many times
#   as it appears in both arrays).
#
# EXAMPLE:
#   [1,2,2,1], [2,2] → [2,2]
#   [4,9,5], [9,4,9,8,4] → [4,9]
#
# IDEA:
#   Count occurrences in smaller array using Counter.
#   For each element in nums2, if count > 0 → include and decrement.
#
# Time : O(n+m)
# Space: O(min(n,m))

from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count  = Counter(nums1)
        result = []
        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.intersect([1,2,2,1], [2,2]))       == [2,2]
    assert sorted(sol.intersect([4,9,5], [9,4,9,8,4]))   == [4,9]
    print("All tests passed ✓")
