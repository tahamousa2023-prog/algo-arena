# Problem 128 — Longest Consecutive Sequence
# Link: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium | Topics: Array, Hash Set
#
# PROBLEM:
#   Find the length of the longest consecutive sequence in an unsorted array.
#   Must run in O(n) time.
#
# EXAMPLE:
#   Input : [100,4,200,1,3,2]
#   Output: 4   (sequence: 1,2,3,4)
#
# WHY THIS MATTERS FOR ROBOTICS:
#   Detecting consecutive sequences in sensor data = identifying
#   continuous segments, scan lines, or contiguous point clusters.
#   Same O(n) reasoning applies to range detection in LiDAR processing.
#
# IDEA:
#   Use a hash set for O(1) lookup.
#   For each number, only start counting if it's the BEGINNING of a sequence
#   (i.e., num-1 is NOT in the set).
#   Then count upward: how far can we go?
#
#   [100,4,200,1,3,2] → set={1,2,3,4,100,200}
#   num=1: 1-1=0 not in set → start: 1,2,3,4 → length=4 ✓
#   num=100: 99 not in set → start: 100 alone → length=1
#   num=200: 199 not in set → start: 200 alone → length=1
#   num=2,3,4: each has num-1 in set → skip (not a sequence start)
#
# Time : O(n)
# Space: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        best    = 0

        for num in num_set:
            # Only start counting from sequence beginnings
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                best = max(best, length)

        return best


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
    assert sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([1]) == 1
    print("All tests passed ✓")
