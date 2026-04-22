# Problem 258 — Add Digits
# Link: https://leetcode.com/problems/add-digits/
# Difficulty: Easy | Topics: Math, Number Theory
#
# PROBLEM:
#   Repeatedly add digits of a number until result is single digit.
#
# EXAMPLE:
#   38 → 3+8=11 → 1+1=2
#
# IDEA:
#   Digital root formula: answer is n % 9, with special cases.
#   If n==0 → 0
#   If n%9==0 → 9
#   Else → n%9
#
# Time : O(1)
# Space: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9

if __name__ == "__main__":
    sol = Solution()
    assert sol.addDigits(38) == 2
    assert sol.addDigits(0)  == 0
    assert sol.addDigits(9)  == 9
    assert sol.addDigits(18) == 9
    print("All tests passed ✓")
