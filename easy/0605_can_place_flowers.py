class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        bed = flowerbed[:]
        count = 0
        for i in range(len(bed)):
            if bed[i] == 0:
                left_empty = (i == 0 or bed[i-1] == 0)
                right_empty = (i == len(bed)-1 or bed[i+1] == 0)
                if left_empty and right_empty:
                    bed[i] = 1
                    count += 1
        return count >= n

if __name__ == "__main__":
    sol = Solution()
    assert sol.canPlaceFlowers([1,0,0,0,1], 1) == True
    assert sol.canPlaceFlowers([1,0,0,0,1], 2) == False
    print("All tests passed v")
