# Problem 557 - Reverse Words in a String III
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Difficulty: Easy | Topics: String, Two Pointers
#
# PROBLEM:
#   Reverse characters of each word, preserve word order and spaces.
#
# IDEA:
#   Split on spaces, reverse each word with [::-1], rejoin with spaces.
#
# Time : O(n) | Space: O(n)

class Solution:
    def reverseWords(self, s):
        return ' '.join(word[::-1] for word in s.split())

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert sol.reverseWords("God Ding") == "doG gniD"
    print("All tests passed v")
