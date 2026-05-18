# Problem 704 — Binary Search
# Link: https://leetcode.com/problems/binary-search/
# Difficulty: Easy | Topics: Array, Binary Search
#
# PROBLEM:
#   Given a sorted array and a target, return its index. Return -1 if not found.
#
# EXAMPLE:
#   Input : nums=[-1,0,3,5,9,12], target=9
#   Output: 4
#
# IDEA:
#   Classic binary search. Each step cuts the search space in half.
#   Look at the middle element:
#     - If it equals target → found it!
#     - If target is larger  → search right half
#     - If target is smaller → search left half
#
#   Walkthrough [-1,0,3,5,9,12], target=9:
#     l=0, r=5 → mid=2, nums[2]=3 < 9 → go right, l=3
#     l=3, r=5 → mid=4, nums[4]=9 = 9 → return 4 ✓
#
# Time : O(log n)
# Space: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1   # target is in right half
            else:
                right = mid - 1  # target is in left half

        return -1  # target not found

if __name__ == "__main__":
    sol = Solution()
    assert sol.search([-1,0,3,5,9,12], 9)  ==  4
    assert sol.search([-1,0,3,5,9,12], 2)  == -1
    assert sol.search([5], 5)              ==  0
    assert sol.search([5], 3)              == -1
    print("All tests passed ✓")
