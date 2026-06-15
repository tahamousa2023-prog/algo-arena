# Problem 091 — Decode Ways
# Link: https://leetcode.com/problems/decode-ways/
# Difficulty: Medium | Topics: String, Dynamic Programming
#
# PROBLEM:
#   A message is encoded as numbers: 'A'→1, 'B'→2, ..., 'Z'→26.
#   Given a string of digits, count the number of ways to decode it.
#
# EXAMPLE:
#   "12" → 2 ways: "AB" (1,2) or "L" (12)
#   "226" → 3 ways: "BZ"(2,26), "VF"(22,6), "BBF"(2,2,6)
#   "06" → 0 (leading zero is invalid)
#
# IDEA:
#   DP. dp[i] = number of ways to decode s[:i]
#   At each position, we can decode:
#     - One digit:  s[i-1] alone (valid if not '0')
#     - Two digits: s[i-2:i] together (valid if between 10-26)
#
#   dp[0] = 1  (empty string = 1 way)
#   dp[1] = 1 if s[0]!='0' else 0
#
#   "226":
#     dp[0]=1, dp[1]=1
#     dp[2]: '2'→valid(+dp[1]=1), '22'→valid(+dp[0]=1) → dp[2]=2
#     dp[3]: '6'→valid(+dp[2]=2), '26'→valid(+dp[1]=1) → dp[3]=3 ✓
#
# Time : O(n)
# Space: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n  = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1   # base: empty string
        dp[1] = 1   # base: first char (already checked it's not '0')

        for i in range(2, n + 1):
            one_digit = int(s[i-1])         # last single digit
            two_digit = int(s[i-2:i])       # last two digits

            if one_digit >= 1:              # valid single digit (1-9)
                dp[i] += dp[i-1]
            if 10 <= two_digit <= 26:       # valid two-digit code (10-26)
                dp[i] += dp[i-2]

        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    assert sol.numDecodings("12")  == 2
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("06")  == 0
    assert sol.numDecodings("10")  == 1
    assert sol.numDecodings("1")   == 1
    print("All tests passed ✓")
