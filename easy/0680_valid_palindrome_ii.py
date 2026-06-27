# Problem 680 - Valid Palindrome II
# Link: https://leetcode.com/problems/valid-palindrome-ii/
# Difficulty: Easy | Topics: String, Two Pointers, Greedy
#
# PROBLEM:
#   Return True if string can become palindrome by deleting AT MOST one character.
#
# IDEA:
#   Two pointers. On mismatch, try skipping left OR right character.
#
# Time : O(n) | Space: O(1)

class Solution:
    def validPalindrome(self, s):
        def is_pal(l, r):
            while l < r:
                if s[l] != s[r]: return False
                l += 1; r -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(l+1, r) or is_pal(l, r-1)
            l += 1; r -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.validPalindrome("abca") == True
    assert sol.validPalindrome("abc")  == False
    print("All tests passed v")
