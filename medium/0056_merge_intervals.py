# Problem 056 — Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium | Topics: Array, Sorting
#
# PROBLEM:
#   Merge all overlapping intervals.
#
# EXAMPLE:
#   [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
#
# IDEA:
#   Sort by start. Walk through.
#   If current overlaps last merged -> extend it.
#   Otherwise -> add new interval.
#
# Time : O(n log n)
# Space: O(n)

class Solution:
    def merge(self, intervals: list) -> list:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

if __name__ == "__main__":
    sol = Solution()
    assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert sol.merge([[1,4],[4,5]])                == [[1,5]]
    assert sol.merge([[1,4],[2,3]])                == [[1,4]]
    print("All tests passed v")
