# Problem 509 - Fibonacci Number
# Link: https://leetcode.com/problems/fibonacci-number/
# Difficulty: Easy | Topics: Math, DP
#
# IDEA:
#   Iterative DP. Keep only last two values. O(1) space.
#   n=4: a=0,b=1 -> 1,1 -> 1,2 -> 2,3 -> return 3
#
# Time : O(n) | Space: O(1)

class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    sol = Solution()
    assert sol.fib(0) == 0
    assert sol.fib(4) == 3
    assert sol.fib(10) == 55
    print("All tests passed v")
