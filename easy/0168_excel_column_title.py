# Problem 168 — Excel Sheet Column Title
# Link: https://leetcode.com/problems/excel-sheet-column-title/
# Difficulty: Easy | Topics: Math, String
#
# PROBLEM:
#   Convert a column number to its Excel title.
#   1→A, 2→B, ..., 26→Z, 27→AA, 28→AB, ...
#
# EXAMPLE:
#   1 → "A",  28 → "AB",  701 → "ZY"
#
# IDEA:
#   Like base-26 conversion but 1-indexed (no zero).
#   Subtract 1 before each modulo to shift range from [1,26] to [0,25].
#
# Time : O(log n)
# Space: O(log n)

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # shift to 0-indexed
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))

if __name__ == "__main__":
    sol = Solution()
    assert sol.convertToTitle(1)   == "A"
    assert sol.convertToTitle(28)  == "AB"
    assert sol.convertToTitle(701) == "ZY"
    assert sol.convertToTitle(26)  == "Z"
    print("All tests passed ✓")
