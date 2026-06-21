class Solution:
    def repeatedSubstringPattern(self, s):
        doubled = (s + s)[1:-1]
        return s in doubled

if __name__ == "__main__":
    sol = Solution()
    assert sol.repeatedSubstringPattern("abab") == True
    assert sol.repeatedSubstringPattern("aba") == False
    print("All tests passed v")
