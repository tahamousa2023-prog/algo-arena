# Problem 009 — Palindrome Number
# Link: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy | Topics: Math
#
# PROBLEM:
#   Return True if an integer reads the same forwards and backwards.
#   Negative numbers are never palindromes.
#
# EXAMPLE:
#   121  → True   (reads 121 both ways)
#   -121 → False  (negative)
#   10   → False  (reads 01 backwards)
#
# IDEA:
#   Convert to string, compare with its reverse.
#   Negative numbers fail immediately.
#
# Time : O(n)   n = number of digits
# Space: O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(121)  == True
    assert sol.isPalindrome(-121) == False
    assert sol.isPalindrome(10)   == False
    assert sol.isPalindrome(0)    == True
    print("All tests passed ✓")
