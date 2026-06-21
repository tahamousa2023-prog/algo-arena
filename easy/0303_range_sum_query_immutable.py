class NumArray:
    def __init__(self, nums):
        self.prefix = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + num
    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]

if __name__ == "__main__":
    na = NumArray([-2, 0, 3, -5, 2, -1])
    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    print("All tests passed v")
