# Problem 743 — Network Delay Time
# Link: https://leetcode.com/problems/network-delay-time/
# Difficulty: Medium | Topics: Graph, Dijkstra, Heap
#
# PROBLEM:
#   A network of n nodes with directed weighted edges (travel times).
#   A signal is sent from node k. Find the time for ALL nodes to receive it.
#   Return -1 if not all nodes are reachable.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Dijkstra is the backbone of many path planners (A* is Dijkstra + heuristic).
#   Network delay = shortest path from source to all nodes = Dijkstra's algorithm.
#   Same concept used in ROS costmap navigation and waypoint routing.
#
# IDEA:
#   Dijkstra's algorithm with a min-heap.
#   dist[node] = shortest signal arrival time from k.
#   Greedily pick the unvisited node with smallest dist, then relax neighbors.
#
#   Walkthrough (k=2, times=[[2,1,1],[2,3,1],[3,4,1]]):
#     Start: dist={2:0}, heap=[(0,2)]
#     Pop (0,2): relax 1→dist=1, 3→dist=1. heap=[(1,1),(1,3)]
#     Pop (1,1): no outgoing edges. heap=[(1,3)]
#     Pop (1,3): relax 4→dist=2. heap=[(2,4)]
#     Pop (2,4): done.
#     dist={2:0, 1:1, 3:1, 4:2} → max = 2 ✓
#
# Time : O(E log V)
# Space: O(V + E)

import heapq
import math

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:

        # Build adjacency list
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra from source k
        dist = {i: math.inf for i in range(1, n + 1)}
        dist[k] = 0
        heap  = [(0, k)]  # (distance, node)

        while heap:
            d, node = heapq.heappop(heap)

            if d > dist[node]:
                continue  # already found a shorter path

            for neighbor, weight in graph[node]:
                new_dist = dist[node] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        max_time = max(dist.values())
        return max_time if max_time != math.inf else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
    assert sol.networkDelayTime([[1,2,1]], 2, 1)                  == 1
    assert sol.networkDelayTime([[1,2,1]], 2, 2)                  == -1
    print("All tests passed ✓")
