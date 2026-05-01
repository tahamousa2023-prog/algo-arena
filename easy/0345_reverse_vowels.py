# Problem 345 — Reverse Vowels of a String
# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Difficulty: Easy | Topics: String, Two Pointers
#
# PROBLEM:
#   Reverse only the vowels in a string.
#
# EXAMPLE:
#   "IceCreAm" → "AceCreIm"
#   "hello"    → "holle"
#
# IDEA:
#   Two pointers. Move inward skipping non-vowels. Swap vowels when found.
#
# Time : O(n)
# Space: O(n) — strings are immutable in Python

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left]  not in vowels: left  += 1
            while left < right and s[right] not in vowels: right -= 1
            s[left], s[right] = s[right], s[left]
            left  += 1
            right -= 1
        return ''.join(s)

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseVowels("IceCreAm") == "AceCreIm"
    assert sol.reverseVowels("hello")    == "holle"
    assert sol.reverseVowels("aA")       == "Aa"
    print("All tests passed ✓")
