# Problem 628 - Maximum Product of Three Numbers
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/
# Difficulty: Easy | Topics: Array, Math, Sorting
#
# IDEA:
#   After sorting, answer is max of:
#   1. Three largest numbers
#   2. Two smallest (most negative) * largest
#
# Time : O(n log n) | Space: O(1)

class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

if __name__ == "__main__":
    sol = Solution()
    assert sol.maximumProduct([1,2,3])           == 6
    assert sol.maximumProduct([-4,-3,-2,-1,60])  == 720
    assert sol.maximumProduct([-1,-2,-3])        == -6
    print("All tests passed v")
