# Problem 028 — Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy | Topics: String, Two Pointers
#
# PROBLEM:
#   Given strings haystack and needle, return the index of
#   needle's first occurrence in haystack, or -1 if not found.
#
# EXAMPLE:
#   haystack="sadbutsad", needle="sad" → 0
#   haystack="leetcode",  needle="leeto" → -1
#
# IDEA:
#   Slide a window of len(needle) across haystack.
#   At each position check if substring matches needle.
#
# Time : O(n * m)
# Space: O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("sadbutsad", "sad")   == 0
    assert sol.strStr("leetcode",  "leeto") == -1
    assert sol.strStr("a",         "a")     == 0
    assert sol.strStr("hello",     "ll")    == 2
    print("All tests passed ✓")
