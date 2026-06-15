# Problem 374 — Guess Number Higher or Lower
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/
# Difficulty: Easy | Topics: Binary Search, Interactive
#
# PROBLEM:
#   Guess a number between 1 and n.
#   API guess(k) returns: -1 if k > pick, 1 if k < pick, 0 if correct.
#   Find the pick using minimum guesses.
#
# EXAMPLE:
#   n=10, pick=6
#   guess(5) → 1 (too low)
#   guess(8) → -1 (too high)
#   guess(6) → 0 (correct!)
#
# IDEA:
#   Classic binary search. At each mid, call guess() to decide direction.
#
# Time : O(log n)
# Space: O(1)

def guess(k: int, pick: int = 6) -> int:
    if k > pick: return -1
    if k < pick: return 1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid    = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid          # found it!
            elif result == 1:
                left  = mid + 1     # pick is higher
            else:
                right = mid - 1     # pick is lower
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.guessNumber(10) == 6
    print("All tests passed ✓")
