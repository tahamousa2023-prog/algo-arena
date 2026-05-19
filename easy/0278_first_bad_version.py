# Problem 278 — First Bad Version
# Link: https://leetcode.com/problems/first-bad-version/
# Difficulty: Easy | Topics: Binary Search
#
# PROBLEM:
#   You have n versions [1..n]. Once a version is bad, all after it are bad.
#   Given isBadVersion(v) API, find the first bad version with min API calls.
#
# EXAMPLE:
#   n=5, bad=4
#   isBadVersion(3) → False
#   isBadVersion(4) → True   ← first bad
#   Output: 4
#
# IDEA:
#   Binary search on version numbers.
#   If mid is bad → first bad could be mid or earlier → go left
#   If mid is good → first bad must be after mid → go right
#   When left==right → that's our answer
#
# Time : O(log n)
# Space: O(1)

def isBadVersion(v, bad=4):  # simulated API
    return v >= bad

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid      # mid might be the first bad → keep it
            else:
                left = mid + 1   # mid is good → first bad is after

        return left  # left == right == first bad version

if __name__ == "__main__":
    sol = Solution()
    assert sol.firstBadVersion(5) == 4
    assert sol.firstBadVersion(1) == 1
    print("All tests passed ✓")
