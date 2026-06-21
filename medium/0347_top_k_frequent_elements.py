from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        result = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.topKFrequent([1,1,1,2,2,3], 2)) == [1,2]
    print("All tests passed v")
