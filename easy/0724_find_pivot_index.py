class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.pivotIndex([1,7,3,6,5,6]) == 3
    assert sol.pivotIndex([1,2,3]) == -1
    print("All tests passed v")
