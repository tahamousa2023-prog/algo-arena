# Problem 011 — Container With Most Water
# Link: https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium | Topics: Array, Two Pointers, Greedy
#
# PROBLEM:
#   Given heights of walls, find two walls that hold the most water.
#
# EXAMPLE:
#   Input : [1,8,6,2,5,4,8,3,7]
#   Output: 49  (walls at index 1 and 8, height=min(8,7)=7, width=7)
#
# IDEA:
#   Two pointers from both ends.
#   Water = min(height[left], height[right]) * (right - left)
#   Move the pointer with the SMALLER height inward.
#   (Moving the taller one can only make things worse or equal.)
#
# Time : O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water   = 0

        while left < right:
            # Water limited by the shorter wall
            water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, water)

            # Move the shorter wall inward (maybe we find a taller one)
            if height[left] < height[right]:
                left  += 1
            else:
                right -= 1

        return max_water

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert sol.maxArea([1,1])                == 1
    assert sol.maxArea([4,3,2,1,4])          == 16
    print("All tests passed ✓")
