# Problem 067 — Add Binary
# Link: https://leetcode.com/problems/add-binary/
# Difficulty: Easy | Topics: Math, String, Bit Manipulation
#
# PROBLEM:
#   Given two binary strings a and b, return their sum as a binary string.
#
# EXAMPLE:
#   a="11", b="1"   → "100"
#   a="1010", b="1011" → "10101"
#
# IDEA:
#   Walk both strings from right to left, adding digits + carry.
#   Build result string in reverse, then flip it.
#
# Time : O(max(n,m))
# Space: O(max(n,m))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j   = len(a)-1, len(b)-1
        carry  = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            total   = digit_a + digit_b + carry
            result.append(str(total % 2))
            carry = total // 2
            i -= 1
            j -= 1
        return ''.join(reversed(result))

if __name__ == "__main__":
    sol = Solution()
    assert sol.addBinary("11",   "1")    == "100"
    assert sol.addBinary("1010", "1011") == "10101"
    assert sol.addBinary("0",    "0")    == "0"
    print("All tests passed ✓")
