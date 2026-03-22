# Problem 058 — Length of Last Word
# Link: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy | Topics: String
#
# PROBLEM:
#   Return the length of the last word in a string.
#   Words are separated by spaces.
#
# EXAMPLE:
#   "Hello World"        → 5
#   "   fly me   to  the moon  " → 4
#
# IDEA:
#   Strip trailing spaces, then count characters until next space.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        # Count last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLastWord("Hello World")              == 5
    assert sol.lengthOfLastWord("   fly me   to  the moon  ") == 4
    assert sol.lengthOfLastWord("a")                        == 1
    print("All tests passed ✓")
