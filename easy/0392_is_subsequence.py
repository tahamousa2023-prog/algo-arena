# Problem 392 — Is Subsequence
# Link: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy | Topics: String, Two Pointers, DP
#
# PROBLEM:
#   Return True if s is a subsequence of t.
#   A subsequence keeps relative order but doesn't have to be contiguous.
#
# EXAMPLE:
#   s="ace", t="abcde" → True  (a→b→c→d→e, pick a,c,e)
#   s="aec", t="abcde" → False (e comes after c in t, but before c in s)
#
# IDEA:
#   Two pointers. Walk t with pointer j.
#   Whenever t[j] == s[i], advance i (matched one char of s).
#   If i reaches len(s) → all chars matched → True.
#
#   s="ace", t="abcde":
#     j=0(a)=s[0](a) → i=1
#     j=1(b)≠s[1](c) → skip
#     j=2(c)=s[1](c) → i=2
#     j=3(d)≠s[2](e) → skip
#     j=4(e)=s[2](e) → i=3 = len(s) → True ✓
#
# Time : O(n)   n = len(t)
# Space: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0   # pointer for s
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)

if __name__ == "__main__":
    sol = Solution()
    assert sol.isSubsequence("ace", "abcde") == True
    assert sol.isSubsequence("aec", "abcde") == False
    assert sol.isSubsequence("",    "ahbgdc") == True
    assert sol.isSubsequence("b",   "abc")    == True
    print("All tests passed ✓")
