# Problem 205 — Isomorphic Strings
# Link: https://leetcode.com/problems/isomorphic-strings/
# Difficulty: Easy | Topics: Hash Map, String
#
# PROBLEM:
#   Two strings are isomorphic if characters in s can be replaced to get t.
#   Each character maps to exactly one other, no two chars map to the same.
#
# EXAMPLE:
#   s="egg", t="add" → True  (e→a, g→d)
#   s="foo", t="bar" → False (o maps to both a and r)
#   s="paper", t="title" → True
#
# IDEA:
#   Use two maps: s→t and t→s (both directions needed).
#   If any mapping conflict → not isomorphic.
#
# Time : O(n)
# Space: O(1) — at most 256 characters

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for cs, ct in zip(s, t):
            if cs in s_to_t and s_to_t[cs] != ct:
                return False
            if ct in t_to_s and t_to_s[ct] != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isIsomorphic("egg",   "add")   == True
    assert sol.isIsomorphic("foo",   "bar")   == False
    assert sol.isIsomorphic("paper", "title") == True
    assert sol.isIsomorphic("badc",  "baba")  == False
    print("All tests passed ✓")
