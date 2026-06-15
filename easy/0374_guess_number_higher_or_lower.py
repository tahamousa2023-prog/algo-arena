# Problem 374 — Guess Number Higher or Lower
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/
# Difficulty: Easy | Topics: Binary Search
#
# PROBLEM:
#   guess(k) returns -1 if k > pick, 1 if k < pick, 0 if correct.
#   Find the picked number using binary search.
#
# IDEA:
#   Standard binary search. Use guess() result to decide direction.
#
# Time : O(log n)
# Space: O(1)

def guess(k, pick=6):
    if k > pick: return -1
    if k < pick: return 1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:   return mid
            elif result == 1: left  = mid + 1
            else:             right = mid - 1
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.guessNumber(10) == 6
    print("All tests passed v")
