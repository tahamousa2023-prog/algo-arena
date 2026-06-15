# Problem 091 — Decode Ways
# Link: https://leetcode.com/problems/decode-ways/
# Difficulty: Medium | Topics: String, Dynamic Programming
#
# PROBLEM:
#   A=1, B=2, ..., Z=26. Count ways to decode a digit string.
#
# EXAMPLE:
#   "12"  -> 2 ways: "AB"(1,2) or "L"(12)
#   "226" -> 3 ways: "BZ","VF","BBF"
#   "06"  -> 0 (invalid leading zero)
#
# IDEA:
#   DP. dp[i] = ways to decode s[:i]
#   One digit valid (1-9)  -> dp[i] += dp[i-1]
#   Two digits valid (10-26) -> dp[i] += dp[i-2]
#
# Time : O(n)
# Space: O(n)

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if int(s[i-1]) >= 1:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]

if __name__ == "__main__":
    sol = Solution()
    assert sol.numDecodings("12")  == 2
    assert sol.numDecodings("226") == 3
    assert sol.numDecodings("06")  == 0
    assert sol.numDecodings("10")  == 1
    print("All tests passed v")
