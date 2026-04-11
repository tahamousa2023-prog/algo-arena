# Problem 172 — Factorial Trailing Zeroes
# Link: https://leetcode.com/problems/factorial-trailing-zeroes/
# Difficulty: Easy | Topics: Math
#
# PROBLEM:
#   Count trailing zeroes in n! (n factorial).
#
# EXAMPLE:
#   3! = 6        → 0 trailing zeroes
#   5! = 120      → 1 trailing zero
#   25! = huge    → 6 trailing zeroes
#
# IDEA:
#   Trailing zeroes come from factors of 10 = 2×5.
#   There are always more 2s than 5s, so count factors of 5.
#   25 contributes TWO 5s (25=5×5), 125 contributes THREE 5s, etc.
#   Count = n//5 + n//25 + n//125 + ...
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        power = 5
        while power <= n:
            count += n // power
            power *= 5
        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.trailingZeroes(3)  == 0
    assert sol.trailingZeroes(5)  == 1
    assert sol.trailingZeroes(25) == 6
    print("All tests passed ✓")
