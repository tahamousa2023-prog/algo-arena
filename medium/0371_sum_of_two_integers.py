class Solution:
    def getSum(self, a, b):
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)
        return a

if __name__ == "__main__":
    sol = Solution()
    assert sol.getSum(1, 2) == 3
    assert sol.getSum(2, 3) == 5
    print("All tests passed v")
