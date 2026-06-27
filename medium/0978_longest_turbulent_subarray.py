# Problem 978 - Longest Turbulent Subarray
# Link: https://leetcode.com/problems/longest-turbulent-subarray/
# Difficulty: Medium | Topics: Array, Sliding Window, DP
#
# PROBLEM:
#   Turbulent subarray: comparisons alternate between > and <.
#   Return length of longest turbulent subarray.
#
# IDEA:
#   Walk array tracking current turbulent length.
#   Reset when equal elements found or direction doesnt alternate.
#
# Time : O(n) | Space: O(1)

class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n < 2:
            return n
        max_len = curr_len = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                curr_len = 1
            elif i == 1:
                curr_len = 2
            else:
                prev_up = arr[i-1] > arr[i-2]
                curr_up = arr[i]   > arr[i-1]
                curr_len = curr_len + 1 if prev_up != curr_up else 2
            max_len = max(max_len, curr_len)
        return max_len

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) == 5
    assert sol.maxTurbulenceSize([4,8,12,16])           == 2
    assert sol.maxTurbulenceSize([100])                 == 1
    print("All tests passed v")
