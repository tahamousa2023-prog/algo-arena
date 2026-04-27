# Problem 326 — Power of Three
# Link: https://leetcode.com/problems/power-of-three/
# Difficulty: Easy | Topics: Math, Recursion
#
# PROBLEM:
#   Return True if n is a power of three.
#
# EXAMPLE:
#   27→True (3³), 9→True (3²), 45→False
#
# IDEA:
#   Keep dividing by 3. If we reach 1 → power of three.
#   If remainder is ever non-zero → not a power of three.
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPowerOfThree(27) == True
    assert sol.isPowerOfThree(9)  == True
    assert sol.isPowerOfThree(45) == False
    assert sol.isPowerOfThree(0)  == False
    assert sol.isPowerOfThree(1)  == True
    print("All tests passed ✓")
