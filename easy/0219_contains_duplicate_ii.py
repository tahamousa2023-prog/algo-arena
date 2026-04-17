# Problem 219 — Contains Duplicate II
# Link: https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy | Topics: Array, Sliding Window, Hash Map
#
# PROBLEM:
#   Return True if there are two indices i,j such that
#   nums[i]==nums[j] and abs(i-j)<=k.
#
# EXAMPLE:
#   [1,2,3,1], k=3 → True  (indices 0,3: |0-3|=3<=3)
#   [1,0,1,1], k=1 → True  (indices 2,3)
#   [1,2,3,1,2,3], k=2 → False
#
# IDEA:
#   Sliding window of size k using a set.
#   If current num already in window → found duplicate within k.
#   Remove oldest element when window exceeds size k.
#
# Time : O(n)
# Space: O(k)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)
            if len(window) > k:
                window.remove(nums[i - k])  # remove oldest
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.containsNearbyDuplicate([1,2,3,1],     3) == True
    assert sol.containsNearbyDuplicate([1,0,1,1],     1) == True
    assert sol.containsNearbyDuplicate([1,2,3,1,2,3], 2) == False
    print("All tests passed ✓")
