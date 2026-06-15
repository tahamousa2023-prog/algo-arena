# Problem 078 — Subsets
# Link: https://leetcode.com/problems/subsets/
# Difficulty: Medium | Topics: Array, Backtracking, Bit Manipulation
#
# PROBLEM:
#   Given an array of unique integers, return all possible subsets (power set).
#
# EXAMPLE:
#   [1,2,3] → [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
# IDEA:
#   Backtracking. At each index, decide: include or skip this element.
#   Build subsets by exploring both choices.
#
#   Tree for [1,2,3]:
#     [] → include 1 → [1] → include 2 → [1,2] → include 3 → [1,2,3]
#                                        → skip 3  → [1,2]
#               → skip 2  → [1]  → include 3 → [1,3]
#                                 → skip 3  → [1]
#     [] → skip 1 → [] → ...
#
# Time : O(n * 2^n)
# Space: O(n)

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result  = []

        def backtrack(start, current):
            result.append(current[:])   # add current subset (even empty)

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()           # backtrack

        backtrack(0, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    result = sol.subsets([1,2,3])
    assert len(result) == 8             # 2^3 subsets
    assert [] in result
    assert [1,2,3] in result
    assert [1,3] in result

    result2 = sol.subsets([0])
    assert sorted(result2) == sorted([[], [0]])
    print("All tests passed ✓")
