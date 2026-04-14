# Problem 202 — Happy Number
# Link: https://leetcode.com/problems/happy-number/
# Difficulty: Easy | Topics: Hash Set, Math, Two Pointers
#
# PROBLEM:
#   A number is "happy" if repeatedly replacing it with the sum of squares
#   of its digits eventually reaches 1. Return True if happy, False if it loops.
#
# EXAMPLE:
#   19: 1²+9²=82 → 8²+2²=68 → 6²+8²=100 → 1²+0²+0²=1 ✓  → True
#    2: 2→4→16→37→58→89→145→42→20→4→... (loop) → False
#
# IDEA:
#   Use a set to detect cycles. If we see a number twice → not happy.
#   If we reach 1 → happy.
#
# Time : O(log n)
# Space: O(log n)

class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squares(x):
            total = 0
            while x:
                x, digit = divmod(x, 10)
                total += digit * digit
            return total

        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squares(n)
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isHappy(19) == True
    assert sol.isHappy(2)  == False
    assert sol.isHappy(1)  == True
    print("All tests passed ✓")
