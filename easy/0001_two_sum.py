# ============================================================
#  Problem 001 — Two Sum
#  Link   : https://leetcode.com/problems/two-sum/
#  Difficulty: Easy
#  Topics : Array, Hash Map
# ============================================================
#
#  PROBLEM STATEMENT
#  -----------------
#  Given an array of integers `nums` and an integer `target`,
#  return the indices of the two numbers that add up to target.
#
#  Example:
#    Input : nums = [2, 7, 11, 15], target = 9
#    Output: [0, 1]   because nums[0] + nums[1] = 2 + 7 = 9
#
# ============================================================
#  THINKING PROCESS
# ============================================================
#
#  Brute Force: try every pair (i,j) ? O(n²). Too slow.
#
#  Better — Hash Map (one pass):
#    For each number, the complement we need is: target - num
#    If we have seen the complement before ? found our pair!
#
#  Walkthrough with [2, 7, 11, 15], target = 9:
#    i=0, num=2 ? need 7  ? not seen ? store {2:0}
#    i=1, num=7 ? need 2  ? 2 IS seen at index 0 ? return [0,1] ?
#
#  Time : O(n)
#  Space: O(n)
# ============================================================

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9)        == [0, 1]
    assert sol.twoSum([3, 2, 4], 6)              == [1, 2]
    assert sol.twoSum([3, 3], 6)                 == [0, 1]
    assert sol.twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]
    print("All test cases passed ?")
