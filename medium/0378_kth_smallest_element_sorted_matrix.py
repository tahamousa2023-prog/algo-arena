# Problem 378 — Kth Smallest Element in a Sorted Matrix
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Difficulty: Medium | Topics: Matrix, Binary Search, Heap
#
# PROBLEM:
#   Given an n×n matrix where rows and columns are sorted,
#   find the kth smallest element.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Efficiently finding ranked elements in sorted structures is common
#   in sensor processing pipelines — e.g., finding the kth nearest
#   obstacle, the kth closest waypoint, or median filtering on depth images.
#
# IDEA:
#   Binary search on the VALUE range (not index).
#   For a given mid value, count how many elements are <= mid.
#   If count < k → kth is in right half.
#   If count >= k → kth is in left half (mid might be the answer).
#
#   Count elements <= mid efficiently:
#     Start from bottom-left corner.
#     If matrix[r][c] <= mid → all rows above in this col are too → add r+1
#     Else → move up
#
# Time : O(n log(max-min))
# Space: O(1)

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        def count_lte(mid):
            """Count elements <= mid using staircase traversal."""
            count = 0
            r, c  = n - 1, 0
            while r >= 0 and c < n:
                if matrix[r][c] <= mid:
                    count += r + 1  # all rows 0..r in this column are <= mid
                    c += 1
                else:
                    r -= 1
            return count

        lo, hi = matrix[0][0], matrix[n-1][n-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if count_lte(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        return lo


if __name__ == "__main__":
    sol = Solution()
    assert sol.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
    assert sol.kthSmallest([[-5]], 1) == -5
    print("All tests passed ✓")
