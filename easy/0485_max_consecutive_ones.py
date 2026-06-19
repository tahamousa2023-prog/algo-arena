# Problem 485 — Max Consecutive Ones
# Link: https://leetcode.com/problems/max-consecutive-ones/
# Difficulty: Easy | Topics: Array
#
# PROBLEM:
#   Find the maximum number of consecutive 1s in a binary array.
#
# EXAMPLE:
#   [1,1,0,1,1,1] -> 3
#
# IDEA:
#   Walk array. Count consecutive 1s, reset on 0. Track max.
#
# Time : O(n) | Space: O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        count     = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count

if __name__ == "__main__":
    sol = Solution()
    assert sol.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
    assert sol.findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
    assert sol.findMaxConsecutiveOnes([0,0,0])        == 0
    print("All tests passed v")
