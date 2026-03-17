# Problem 014 — Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy | Topics: String
#
# PROBLEM:
#   Find the longest common prefix string among an array of strings.
#   Return "" if no common prefix exists.
#
# EXAMPLE:
#   ["flower","flow","flight"] → "fl"
#   ["dog","racecar","car"]   → ""
#
# IDEA:
#   Take the first string as reference. Compare it character by character
#   against all other strings. Stop when mismatch found.
#
# Time : O(S)   S = total characters across all strings
# Space: O(1)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            # Shrink prefix until it matches start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert sol.longestCommonPrefix(["dog","racecar","car"])    == ""
    assert sol.longestCommonPrefix(["a"])                      == "a"
    assert sol.longestCommonPrefix(["ab","a"])                 == "a"
    print("All tests passed ✓")
