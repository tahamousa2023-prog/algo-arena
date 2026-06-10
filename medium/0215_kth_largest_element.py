# Problem 215 — Kth Largest Element in an Array
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Difficulty: Medium | Topics: Array, Heap, Quickselect
#
# PROBLEM:
#   Find the kth largest element in an unsorted array.
#   (Not kth distinct — if [3,3,3] and k=2, answer is 3.)
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Finding top-k candidates is used everywhere in robotics:
#   top-k nearest neighbors in point clouds, k-best sensor readings,
#   k highest-confidence detections in object detection pipelines.
#
# IDEA:
#   Min-heap of size k.
#   Push each element. If heap size > k → pop the smallest.
#   After processing all elements → heap[0] is the kth largest.
#
#   Why? The heap keeps the k largest elements seen so far.
#   The smallest of those k = kth largest overall.
#
#   Example [3,2,1,5,6,4], k=2:
#     heap=[3], heap=[3,2], heap=[3,2,1]→pop1=[3,2]
#     heap=[3,2,5]→pop2=[3,5], heap=[3,5,6]→pop3=[5,6]
#     heap=[5,6,4]→pop4=[5,6] → heap[0]=5 ✓
#
# Time : O(n log k)
# Space: O(k)

import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # remove the smallest

        return min_heap[0]  # smallest of the k largest = kth largest


if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert sol.findKthLargest([1], 1) == 1
    print("All tests passed ✓")
