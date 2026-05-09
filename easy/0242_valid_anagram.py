# Problem 242 — Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy | Topics: String, Hash Map
#
# PROBLEM:
#   Given two strings s and t, return True if t is an anagram of s.
#   Anagram = same letters, same counts, different order.
#
# EXAMPLE:
#   Input : s="anagram", t="nagaram"
#   Output: True
#
# IDEA:
#   Count each character in both strings.
#   If the counts match → anagram!
#   Python's Counter does exactly this.
#
#   "anagram" → {a:3, n:1, g:1, r:1, m:1}
#   "nagaram" → {a:3, n:1, g:1, r:1, m:1}
#   Equal → True ✓
#
# Time : O(n)
# Space: O(1) — at most 26 letters in counter

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True
    assert sol.isAnagram("rat",     "car")     == False
    assert sol.isAnagram("a",       "a")       == True
    assert sol.isAnagram("ab",      "a")       == False
    print("All tests passed ✓")
