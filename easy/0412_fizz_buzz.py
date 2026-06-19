# Problem 412 — Fizz Buzz
# Link: https://leetcode.com/problems/fizz-buzz/
# Difficulty: Easy | Topics: Math, String, Simulation
#
# PROBLEM:
#   For each number 1 to n, return "FizzBuzz" if divisible by 3 and 5,
#   "Fizz" if by 3, "Buzz" if by 5, else the number as a string.
#
# IDEA:
#   Check divisibility in order: 15 first, then 3, then 5, else number.
#
# Time : O(n) | Space: O(n)

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:   result.append("FizzBuzz")
            elif i % 3 == 0:  result.append("Fizz")
            elif i % 5 == 0:  result.append("Buzz")
            else:             result.append(str(i))
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
    assert sol.fizzBuzz(15)[-1] == "FizzBuzz"
    print("All tests passed v")
