# Problem 338 — Counting Bits
# Link: https://leetcode.com/problems/counting-bits/
# Difficulty: Easy | Topics: DP, Bit Manipulation
#
# PROBLEM:
#   Return array ans of length n+1 where ans[i] = number of 1s in binary of i.
#
# EXAMPLE:
#   n=2 → [0,1,1]
#   n=5 → [0,1,1,2,1,2]
#
# IDEA:
#   DP. ans[i] = ans[i >> 1] + (i & 1)
#   i>>1 = i with last bit removed (already computed).
#   i&1  = the last bit (0 or 1).
#
#   i=5 (101): ans[5] = ans[2] + 1 = 1+1 = 2 ✓
#
# Time : O(n)
# Space: O(1) — output not counted

class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.countBits(2) == [0,1,1]
    assert sol.countBits(5) == [0,1,1,2,1,2]
    assert sol.countBits(0) == [0]
    print("All tests passed ✓")
