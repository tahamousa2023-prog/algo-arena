# Problem 056 — Merge Intervals
# Link: https://leetcode.com/problems/merge-intervals/
# Difficulty: Medium | Topics: Array, Sorting
#
# PROBLEM:
#   Given a list of intervals, merge all overlapping ones.
#
# EXAMPLE:
#   [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
#   [1,3] and [2,6] overlap → merged to [1,6]
#
# IDEA:
#   Sort by start time. Walk through intervals.
#   If current interval overlaps with last merged → extend it.
#   Otherwise → add as new interval.
#
#   Overlap condition: current.start <= last.end
#   Merge by: last.end = max(last.end, current.end)
#
#   [[1,3],[2,6],[8,10],[15,18]]:
#     result=[[1,3]]
#     [2,6]: 2<=3 → merge → [[1,6]]
#     [8,10]: 8>6 → new  → [[1,6],[8,10]]
#     [15,18]: 15>10 → new → [[1,6],[8,10],[15,18]] ✓
#
# Time : O(n log n)  — sorting dominates
# Space: O(n)

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])   # sort by start
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]
            if start <= last_end:
                # Overlapping — extend the last interval if needed
                merged[-1][1] = max(last_end, end)
            else:
                # No overlap — start a new interval
                merged.append([start, end])

        return merged

if __name__ == "__main__":
    sol = Solution()
    assert sol.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert sol.merge([[1,4],[4,5]])                == [[1,5]]
    assert sol.merge([[1,4],[0,4]])                == [[0,4]]
    assert sol.merge([[1,4],[2,3]])                == [[1,4]]  # contained
    print("All tests passed ✓")
