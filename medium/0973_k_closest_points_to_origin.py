# Problem 973 — K Closest Points to Origin
# Link: https://leetcode.com/problems/k-closest-points-to-origin/
# Difficulty: Medium | Topics: Array, Math, Heap, Sorting
#
# PROBLEM:
#   Given a list of 2D points, return the k closest to the origin (0,0).
#   Distance = sqrt(x² + y²) but we can compare x²+y² directly.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Finding k nearest neighbors is CORE to robotics:
#   - k-nearest in point clouds (KD-tree does this at scale)
#   - Finding k closest obstacles in a sensor scan
#   - Selecting k best candidates from a detection list
#   This problem is the foundation of NN search in 2D.
#
# IDEA:
#   Max-heap of size k (negate distances to simulate max-heap with heapq).
#   Keep the k closest points seen so far.
#   If heap grows beyond k → remove the farthest (largest distance).
#
# Time : O(n log k)
# Space: O(k)

import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []  # stores (-distance², x, y)

        for x, y in points:
            dist_sq = x*x + y*y
            heapq.heappush(max_heap, (-dist_sq, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)  # remove farthest

        return [[x, y] for _, x, y in max_heap]


if __name__ == "__main__":
    sol = Solution()

    result = sol.kClosest([[1,3],[-2,2]], 1)
    assert result == [[-2,2]]

    result = sol.kClosest([[3,3],[5,-1],[-2,4]], 2)
    assert sorted(result) == sorted([[3,3],[-2,4]])

    print("All tests passed ✓")
