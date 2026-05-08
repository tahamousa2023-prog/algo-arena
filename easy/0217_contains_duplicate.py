# Problem 217 — Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy | Topics: Array, Hash Set
#
# PROBLEM:
#   Given an array, return True if any value appears at least twice.
#
# EXAMPLE:
#   Input : [1, 2, 3, 1]
#   Output: True   (1 appears twice)
#
# IDEA:
#   Use a set. Sets only store unique values.
#   If we try to add a number that's already in the set → duplicate found!
#
#   Walkthrough [1, 2, 3, 1]:
#     see 1 → set={1}
#     see 2 → set={1,2}
#     see 3 → set={1,2,3}
#     see 1 → 1 already in set → return True ✓
#
# Time : O(n)
# Space: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1])    == True
    assert sol.containsDuplicate([1, 2, 3, 4])    == False
    assert sol.containsDuplicate([1, 1, 1, 3, 3]) == True
    print("All tests passed ✓")
