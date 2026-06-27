# Problem 496 - Next Greater Element I
# Link: https://leetcode.com/problems/next-greater-element-i/
# Difficulty: Easy | Topics: Array, Hash Map, Monotonic Stack
#
# PROBLEM:
#   For each element in nums1, find the next greater element in nums2.
#   Next greater = first element to the right that is larger. -1 if none.
#
# IDEA:
#   Monotonic stack on nums2. Walk left to right.
#   When num > stack top, that num is the next greater for stack top.
#   Pop and record in hash map. Look up each nums1 element in map.
#
# Time : O(n + m) | Space: O(n)

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        return [next_greater[n] for n in nums1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.nextGreaterElement([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert sol.nextGreaterElement([2,4], [1,2,3,4])   == [3,-1]
    print("All tests passed v")
