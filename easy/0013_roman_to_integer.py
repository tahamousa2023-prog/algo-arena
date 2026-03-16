# Problem 013 — Roman to Integer
# Link: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy | Topics: Hash Map, Math, String
#
# PROBLEM:
#   Convert a Roman numeral string to an integer.
#   Roman numerals: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
#   Subtraction rule: if smaller value precedes larger → subtract it.
#   e.g. IV = 4, IX = 9, XL = 40
#
# EXAMPLE:
#   "III"  → 3
#   "LVIII" → 58  (L=50, V=5, III=3)
#   "MCMXCIV" → 1994
#
# IDEA:
#   Walk right to left. If current value < previous value → subtract it.
#   Otherwise add it.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total  = 0
        prev   = 0
        for ch in reversed(s):
            curr = values[ch]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total

if __name__ == "__main__":
    sol = Solution()
    assert sol.romanToInt("III")     == 3
    assert sol.romanToInt("LVIII")   == 58
    assert sol.romanToInt("MCMXCIV") == 1994
    assert sol.romanToInt("IV")      == 4
    print("All tests passed ✓")
