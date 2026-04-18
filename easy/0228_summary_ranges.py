# Problem 228 — Summary Ranges
# Link: https://leetcode.com/problems/summary-ranges/
# Difficulty: Easy | Topics: Array
#
# PROBLEM:
#   Given a sorted unique integer array, return the smallest sorted list of
#   ranges that cover all numbers exactly. Format: "a->b" or "a".
#
# EXAMPLE:
#   [0,1,2,4,5,7]   → ["0->2","4->5","7"]
#   [0,2,3,4,6,8,9] → ["0","2->4","6","8->9"]
#
# IDEA:
#   Walk array tracking start of each range.
#   When a gap is found → close current range and start new one.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        i = 0
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
            if nums[i] == start:
                result.append(str(start))
            else:
                result.append(f"{start}->{nums[i]}")
            i += 1
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.summaryRanges([0,1,2,4,5,7])   == ["0->2","4->5","7"]
    assert sol.summaryRanges([0,2,3,4,6,8,9]) == ["0","2->4","6","8->9"]
    assert sol.summaryRanges([])              == []
    print("All tests passed ✓")
