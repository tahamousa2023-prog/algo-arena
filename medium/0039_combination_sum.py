# Problem 039 — Combination Sum
# Link: https://leetcode.com/problems/combination-sum/
# Difficulty: Medium | Topics: Array, Backtracking
#
# PROBLEM:
#   Given an array of distinct integers and a target,
#   return all unique combinations that sum to target.
#   Each number can be used unlimited times.
#
# EXAMPLE:
#   Input : candidates=[2,3,6,7], target=7
#   Output: [[2,2,3],[7]]
#
# IDEA:
#   Backtracking. At each step, either:
#     - Include current candidate (and try again with same candidate)
#     - Skip to next candidate
#   To avoid duplicates, only move forward in the candidates list.
#
# Time : O(n^(t/m))  t=target, m=min candidate
# Space: O(t/m)

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []

        def backtrack(start, current, remaining):
            if remaining == 0:
                results.append(current[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, remaining - candidates[i])
                current.pop()  # backtrack

        backtrack(0, [], target)
        return results

if __name__ == "__main__":
    sol = Solution()
    result = sol.combinationSum([2,3,6,7], 7)
    assert sorted(result) == sorted([[2,2,3],[7]])

    result2 = sol.combinationSum([2,3,5], 8)
    assert sorted(result2) == sorted([[2,2,2,2],[2,3,3],[3,5]])
    print("All tests passed ✓")
