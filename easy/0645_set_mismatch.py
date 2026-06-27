# Problem 645 - Set Mismatch
# Link: https://leetcode.com/problems/set-mismatch/
# Difficulty: Easy | Topics: Array, Hash Map
#
# PROBLEM:
#   Set [1..n] has one duplicate and one missing. Return [dup, missing].
#
# IDEA:
#   Counter. count==2 -> duplicate. count==0 -> missing.
#
# Time : O(n) | Space: O(n)

from collections import Counter

class Solution:
    def findErrorNums(self, nums):
        count = Counter(nums)
        dup = missing = 0
        for i in range(1, len(nums) + 1):
            if count[i] == 2:   dup = i
            elif count[i] == 0: missing = i
        return [dup, missing]

if __name__ == "__main__":
    sol = Solution()
    assert sol.findErrorNums([1,2,2,4]) == [2,3]
    print("All tests passed v")
