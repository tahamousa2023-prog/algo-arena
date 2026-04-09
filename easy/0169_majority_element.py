# Problem 169 — Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy | Topics: Array, Hash Map, Sorting
#
# PROBLEM:
#   Find the majority element — appears more than n/2 times.
#   Guaranteed to always exist.
#
# EXAMPLE:
#   [3,2,3]      → 3
#   [2,2,1,1,1,2,2] → 2
#
# IDEA:
#   Boyer-Moore Voting Algorithm.
#   Maintain a candidate and count. When count=0 → new candidate.
#   +1 if same as candidate, -1 if different.
#   Majority element always survives.
#
#   [2,2,1,1,1,2,2]:
#     2(+1) 2(+1) 1(-1) 1(-1) 1→new_cand count=1 2(-1) 2(+1-1=new) 2 → 2 ✓
#
# Time : O(n)
# Space: O(1)

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count     = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([3,2,3])          == 3
    assert sol.majorityElement([2,2,1,1,1,2,2])  == 2
    assert sol.majorityElement([1])              == 1
    print("All tests passed ✓")
