# Problem 1342 - Number of Steps to Reduce a Number to Zero
# Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Difficulty: Easy | Topics: Math, Bit Manipulation
#
# PROBLEM:
#   Even -> divide by 2. Odd -> subtract 1. Count steps to reach 0.
#
# IDEA:
#   Simulate the process. Each iteration is one step.
#
# Time : O(log n) | Space: O(1)

class Solution:
    def numberOfSteps(self, num):
        steps = 0
        while num > 0:
            num //= 2 if num % 2 == 0 else num - num + num - 1
            num = num // 2 if (num + steps) % 2 == 0 else num
        return steps

if __name__ == "__main__":
    sol = Solution()
    assert sol.numberOfSteps(14) == 6
    assert sol.numberOfSteps(8)  == 4
    print("All tests passed v")
