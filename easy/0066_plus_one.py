# Problem 066 — Plus One
# Link: https://leetcode.com/problems/plus-one/
# Difficulty: Easy | Topics: Array, Math
#
# PROBLEM:
#   Given a large integer as an array of digits, increment it by 1.
#
# EXAMPLE:
#   [1,2,3] → [1,2,4]
#   [1,2,9] → [1,3,0]
#   [9,9,9] → [1,0,0,0]
#
# IDEA:
#   Walk from right to left. Add 1 to last digit.
#   If digit becomes 10 → set to 0, carry 1 to next digit.
#   If carry remains after all digits → prepend 1.
#
# Time : O(n)
# Space: O(1)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # was 9, becomes 0, carry continues
        return [1] + digits  # all digits were 9

if __name__ == "__main__":
    sol = Solution()
    assert sol.plusOne([1,2,3]) == [1,2,4]
    assert sol.plusOne([1,2,9]) == [1,3,0]
    assert sol.plusOne([9,9,9]) == [1,0,0,0]
    assert sol.plusOne([9])     == [1,0]
    print("All tests passed ✓")
