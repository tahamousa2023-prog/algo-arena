# Problem 787 — Cheapest Flights Within K Stops
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Difficulty: Medium | Topics: Graph, BFS, Dynamic Programming
#
# PROBLEM:
#   There are n cities connected by flights. Each flight (u→v) has a cost.
#   Find the cheapest price from src to dst with at most k stops.
#   Return -1 if no route exists.
#
# EXAMPLE:
#   n=4, flights=[[0,1,100],[1,2,100],[2,3,100],[0,2,500]]
#   src=0, dst=3, k=1
#   Output: 500  (0→2→3, cost=200 needs 1 stop; 0→1→2→3 needs 2 stops)
#   Wait — 0→2→3 = 100+100 = 200 with 1 stop ✓ → Output: 200
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Path planning with constrained hops = navigation with energy/step limits.
#   Same idea used in multi-hop route planning for mobile robots.
#
# IDEA:
#   Bellman-Ford with k+1 relaxations.
#   prices[v] = cheapest cost to reach v.
#   Run k+1 rounds (each round = one more edge/stop allowed).
#   Key: use a COPY of prices each round to avoid using same-round updates.
#
#   Round 0 (0 stops): prices = [0, inf, inf, inf]
#   Round 1 (1 stop):  prices = [0, 100, 500, inf]
#   Round 2 (2 stops): prices = [0, 100, 200, 600]  ← 0→2→3
#   k=1 → we can take at most 2 rounds → return prices[3] after round 2
#
# Time : O(k * |flights|)
# Space: O(n)

import math

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]],
                          src: int, dst: int, k: int) -> int:

        # Start with infinity for all cities except source
        prices = [math.inf] * n
        prices[src] = 0

        # Run k+1 relaxations (k stops = k+1 edges)
        for _ in range(k + 1):
            # IMPORTANT: copy prices to avoid using this round's updates
            temp = prices[:]

            for u, v, cost in flights:
                if prices[u] != math.inf:
                    temp[v] = min(temp[v], prices[u] + cost)

            prices = temp

        return prices[dst] if prices[dst] != math.inf else -1


if __name__ == "__main__":
    sol = Solution()
    flights1 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    assert sol.findCheapestPrice(4, flights1, 0, 3, 1) == 700

    flights2 = [[0,1,100],[1,2,100],[0,2,500]]
    assert sol.findCheapestPrice(3, flights2, 0, 2, 1) == 200

    # No path
    flights3 = [[0,1,100]]
    assert sol.findCheapestPrice(3, flights3, 0, 2, 1) == -1

    print("All tests passed ✓")
