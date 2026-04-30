# Problem 344 — Reverse String
# Link: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy | Topics: String, Two Pointers
#
# PROBLEM:
#   Reverse a character array in-place.
#
# EXAMPLE:
#   ["h","e","l","l","o"] → ["o","l","l","e","h"]
#
# IDEA:
#   Two pointers from both ends, swap until they meet.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left  += 1
            right -= 1

if __name__ == "__main__":
    sol = Solution()
    s = ["h","e","l","l","o"]
    sol.reverseString(s)
    assert s == ["o","l","l","e","h"]

    s2 = ["H","a","n","n","a","h"]
    sol.reverseString(s2)
    assert s2 == ["h","a","n","n","a","H"]
    print("All tests passed ✓")
