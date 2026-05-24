# Problem 046 — Permutations
# Link: https://leetcode.com/problems/permutations/
# Difficulty: Medium | Topics: Array, Backtracking
#
# PROBLEM:
#   Given a list of distinct integers, return all possible permutations.
#
# EXAMPLE:
#   Input : [1,2,3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# IDEA:
#   Backtracking. Build permutation one element at a time.
#   At each step, try every unused number.
#   When current permutation is full → add to result.
#   Backtrack by removing the last added element.
#
#   Tree for [1,2,3]:
#     pick 1 → pick 2 → pick 3 → [1,2,3] ✓
#           → pick 3 → pick 2 → [1,3,2] ✓
#     pick 2 → ...
#
# Time : O(n * n!)
# Space: O(n)

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []

        def backtrack(current, remaining):
            if not remaining:
                results.append(current[:])  # found a complete permutation
                return

            for i in range(len(remaining)):
                current.append(remaining[i])
                backtrack(current, remaining[:i] + remaining[i+1:])
                current.pop()  # undo the choice (backtrack)

        backtrack([], nums)
        return results

if __name__ == "__main__":
    sol = Solution()
    result = sol.permute([1,2,3])
    assert len(result) == 6
    assert [1,2,3] in result
    assert [3,2,1] in result

    result2 = sol.permute([1])
    assert result2 == [[1]]
    print("All tests passed ✓")
