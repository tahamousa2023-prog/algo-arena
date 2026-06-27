# Problem 763 - Partition Labels
# Link: https://leetcode.com/problems/partition-labels/
# Difficulty: Medium | Topics: Hash Map, String, Greedy
#
# PROBLEM:
#   Partition string into max parts so each letter appears in at most one part.
#   Return list of partition sizes.
#
# IDEA:
#   Record last occurrence of each letter. Walk left to right,
#   extending current partition end to last occurrence of each seen letter.
#   Close partition when i reaches the end.
#
# Time : O(n) | Space: O(1)

class Solution:
    def partitionLabels(self, s):
        last = {ch: i for i, ch in enumerate(s)}
        result = []
        start = end = 0
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.partitionLabels("ababcbacadefegdehijhklij") == [9,7,8]
    assert sol.partitionLabels("a") == [1]
    print("All tests passed v")
