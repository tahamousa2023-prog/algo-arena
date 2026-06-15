# Problem 392 — Is Subsequence
# Link: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy | Topics: String, Two Pointers
#
# PROBLEM:
#   Return True if s is a subsequence of t (relative order preserved).
#
# EXAMPLE:
#   s="ace", t="abcde" -> True  (pick a,c,e in order)
#   s="aec", t="abcde" -> False (e comes before c in t)
#
# IDEA:
#   Walk t. Whenever t[j] matches s[i], advance i.
#   If i reaches len(s) -> all chars matched.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isSubsequence("ace", "abcde") == True
    assert sol.isSubsequence("aec", "abcde") == False
    assert sol.isSubsequence("",    "abc")   == True
    print("All tests passed v")
