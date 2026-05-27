# Problem 015 — 3Sum
# Link: https://leetcode.com/problems/3sum/
# Difficulty: Medium | Topics: Array, Two Pointers, Sorting
#
# PROBLEM:
#   Find all unique triplets in the array that sum to zero.
#
# EXAMPLE:
#   Input : [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]
#
# IDEA:
#   Sort the array. For each number nums[i], use two pointers
#   on the rest of the array to find pairs that sum to -nums[i].
#   Skip duplicates to avoid repeated triplets.
#
#   Sorted: [-4,-1,-1,0,1,2]
#   i=0 (-4): need pair summing to 4 → no pair found
#   i=1 (-1): need pair summing to 1 → (0,1) ✓ and (-1,2) ✓
#   i=2 (-1): skip (same as previous)
#   i=3 (0) : need pair summing to 0 → no pair
#
# Time : O(n²)
# Space: O(1)

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates for second and third elements
                    while left < right and nums[left]  == nums[left+1]:  left  += 1
                    while left < right and nums[right] == nums[right-1]: right -= 1
                    left  += 1
                    right -= 1
                elif total < 0:
                    left  += 1  # need larger sum
                else:
                    right -= 1  # need smaller sum

        return results

if __name__ == "__main__":
    sol = Solution()
    assert sol.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert sol.threeSum([0,1,1])          == []
    assert sol.threeSum([0,0,0])          == [[0,0,0]]
    print("All tests passed ✓")
