# Problem 290 — Word Pattern
# Link: https://leetcode.com/problems/word-pattern/
# Difficulty: Easy | Topics: Hash Map, String
#
# PROBLEM:
#   Return True if s follows the same pattern as pattern.
#   Full match: each letter maps to exactly one word and vice versa.
#
# EXAMPLE:
#   pattern="abba", s="dog cat cat dog" → True
#   pattern="abba", s="dog cat cat fish" → False
#   pattern="aaaa", s="dog cat cat dog" → False
#
# IDEA:
#   Same as isomorphic strings. Map chars to words AND words to chars.
#
# Time : O(n)
# Space: O(n)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for ch, word in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != word:
                return False
            if word in word_to_char and word_to_char[word] != ch:
                return False
            char_to_word[ch]   = word
            word_to_char[word] = ch
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.wordPattern("abba", "dog cat cat dog")  == True
    assert sol.wordPattern("abba", "dog cat cat fish") == False
    assert sol.wordPattern("aaaa", "dog cat cat dog")  == False
    print("All tests passed ✓")
