# Problem 078 — Subsets
# Link: https://leetcode.com/problems/subsets/
# Difficulty: Medium | Topics: Backtracking
#
# PROBLEM:
#   Return all possible subsets (power set) of unique integers.
#
# EXAMPLE:
#   [1,2,3] -> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# IDEA:
#   Backtracking. At each index: include or skip this element.
#   Add current subset to result at every step (including empty).
#
# Time : O(n * 2^n)
# Space: O(n)

class Solution:
    def subsets(self, nums: list) -> list:
        result = []
        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        backtrack(0, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    result = sol.subsets([1,2,3])
    assert len(result) == 8
    assert [] in result
    assert [1,2,3] in result
    print("All tests passed v")
