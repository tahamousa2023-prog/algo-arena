# Problem 171 — Excel Sheet Column Number
# Link: https://leetcode.com/problems/excel-sheet-column-number/
# Difficulty: Easy | Topics: Math, String
#
# PROBLEM:
#   Convert an Excel column title to its column number.
#   A→1, B→2, ..., Z→26, AA→27, AB→28 ...
#
# EXAMPLE:
#   "A"  → 1,  "AB" → 28,  "ZY" → 701
#
# IDEA:
#   Process left to right like reading a base-26 number.
#   result = result * 26 + value_of_current_char
#
# Time : O(n)
# Space: O(1)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.titleToNumber("A")  == 1
    assert sol.titleToNumber("AB") == 28
    assert sol.titleToNumber("ZY") == 701
    assert sol.titleToNumber("Z")  == 26
    print("All tests passed ✓")
