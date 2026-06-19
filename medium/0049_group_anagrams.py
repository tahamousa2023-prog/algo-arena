# Problem 049 — Group Anagrams
# Link: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium | Topics: Hash Map, String, Sorting
#
# PROBLEM:
#   Group a list of strings into lists of anagrams.
#
# EXAMPLE:
#   ["eat","tea","tan","ate","nat","bat"]
#   -> [["eat","tea","ate"],["tan","nat"],["bat"]]
#
# IDEA:
#   Sorted version of a string is the same for all its anagrams.
#   Use it as a dictionary key to group them.
#   "eat" sorted -> "aet" (same as "tea" and "ate")
#
# Time : O(n * k log k) | Space: O(n * k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

if __name__ == "__main__":
    sol = Solution()
    result   = sorted([sorted(g) for g in sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])])
    expected = sorted([sorted(g) for g in [["eat","tea","ate"],["tan","nat"],["bat"]]])
    assert result == expected
    print("All tests passed v")
