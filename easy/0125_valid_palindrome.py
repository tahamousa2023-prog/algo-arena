# Problem 125 — Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy | Topics: String, Two Pointers
#
# PROBLEM:
#   A string is a palindrome if it reads the same forward and backward,
#   considering only alphanumeric characters and ignoring case.
#
# EXAMPLE:
#   Input : "A man, a plan, a canal: Panama"
#   Output: True  →  "amanaplanacanalpanama" is a palindrome
#
# IDEA:
#   Two pointers — one from the left, one from the right.
#   Skip non-alphanumeric characters.
#   Compare characters (lowercased) as we move inward.
#
#   "racecar":
#     l=0(r) r=6(r) → match, move in
#     l=1(a) r=5(a) → match, move in
#     l=2(c) r=4(c) → match, move in
#     l=3(e) r=3(e) → l>=r, stop → True ✓
#
# Time : O(n)
# Space: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric from right
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left  += 1
            right -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    assert sol.isPalindrome("race a car")                    == False
    assert sol.isPalindrome(" ")                             == True
    assert sol.isPalindrome("racecar")                       == True
    print("All tests passed ✓")
