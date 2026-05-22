# Problem 003 — Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium | Topics: String, Sliding Window, Hash Map
#
# PROBLEM:
#   Find the length of the longest substring with no repeating characters.
#
# EXAMPLE:
#   Input : "abcabcbb"
#   Output: 3  ("abc")
#
# IDEA:
#   Sliding window with a set.
#   Maintain a window [left, right] with no duplicates.
#   Expand right. If duplicate found → shrink from left until no duplicate.
#
#   Walkthrough "abcabcbb":
#     add a → {a},    window=a,     len=1
#     add b → {a,b},  window=ab,    len=2
#     add c → {a,b,c},window=abc,   len=3
#     add a → a seen! remove a from left → {b,c}, add a → {b,c,a}, len=3
#     add b → b seen! remove b → {c,a}, add b → {c,a,b}, len=3
#     ...
#     max = 3 ✓
#
# Time : O(n)
# Space: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen  = set()
        left  = 0
        max_len = 0

        for right in range(len(s)):
            # Shrink window from left until no duplicate
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb")    == 1
    assert sol.lengthOfLongestSubstring("pwwkew")   == 3
    assert sol.lengthOfLongestSubstring("")         == 0
    print("All tests passed ✓")
