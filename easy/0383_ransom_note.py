# Problem 383 — Ransom Note
# Link: https://leetcode.com/problems/ransom-note/
# Difficulty: Easy | Topics: Hash Map, String, Counting
#
# PROBLEM:
#   Return True if ransomNote can be constructed using letters from magazine.
#   Each letter in magazine can only be used once.
#
# EXAMPLE:
#   ransomNote="aa", magazine="aab" → True
#   ransomNote="aa", magazine="ab"  → False (only one 'a' in magazine)
#
# IDEA:
#   Count letters in magazine. For each letter in ransomNote,
#   check if we have enough supply. Decrement count as we use letters.
#
# Time : O(n + m)
# Space: O(1) — at most 26 letters

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        supply = Counter(magazine)
        for ch in ransomNote:
            if supply[ch] == 0:
                return False    # not enough of this letter
            supply[ch] -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.canConstruct("a",  "b")   == False
    assert sol.canConstruct("aa", "ab")  == False
    assert sol.canConstruct("aa", "aab") == True
    print("All tests passed ✓")
