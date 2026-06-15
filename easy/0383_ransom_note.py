# Problem 383 — Ransom Note
# Link: https://leetcode.com/problems/ransom-note/
# Difficulty: Easy | Topics: Hash Map, String
#
# PROBLEM:
#   Return True if ransomNote can be built using letters from magazine.
#   Each letter in magazine can only be used once.
#
# EXAMPLE:
#   ransomNote="aa", magazine="aab" -> True
#   ransomNote="aa", magazine="ab"  -> False
#
# IDEA:
#   Count letters in magazine. Decrement as we use them for ransomNote.
#
# Time : O(n+m)
# Space: O(1)

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        supply = Counter(magazine)
        for ch in ransomNote:
            if supply[ch] == 0:
                return False
            supply[ch] -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.canConstruct("a",  "b")   == False
    assert sol.canConstruct("aa", "ab")  == False
    assert sol.canConstruct("aa", "aab") == True
    print("All tests passed v")
