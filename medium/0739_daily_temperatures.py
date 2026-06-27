# Problem 739 - Daily Temperatures
# Link: https://leetcode.com/problems/daily-temperatures/
# Difficulty: Medium | Topics: Array, Monotonic Stack
#
# PROBLEM:
#   Return array where answer[i] = days until warmer temperature. 0 if none.
#
# IDEA:
#   Monotonic decreasing stack of indices. When warmer temp found,
#   pop and compute distance to that index.
#
# Time : O(n) | Space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures):
        n      = len(temperatures)
        answer = [0] * n
        stack  = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        return answer

if __name__ == "__main__":
    sol = Solution()
    assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert sol.dailyTemperatures([30,60,90]) == [1,1,0]
    print("All tests passed v")
