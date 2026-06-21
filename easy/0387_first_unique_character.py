from collections import Counter
class Solution:
    def firstUniqChar(self, s):
        counts = Counter(s)
        for i, ch in enumerate(s):
            if counts[ch] == 1:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.firstUniqChar("leetcode") == 0
    assert sol.firstUniqChar("aabb") == -1
    print("All tests passed v")
