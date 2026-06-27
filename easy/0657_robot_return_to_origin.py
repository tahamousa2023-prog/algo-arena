# Problem 657 - Robot Return to Origin
# Link: https://leetcode.com/problems/robot-return-to-origin/
# Difficulty: Easy | Topics: String, Simulation
#
# PROBLEM:
#   Robot starts at (0,0). Moves U/D/L/R. Return True if ends at origin.
#
# IDEA:
#   U count must equal D count AND L count must equal R count.
#
# Time : O(n) | Space: O(1)

class Solution:
    def judgeCircle(self, moves):
        return moves.count("U") == moves.count("D") and \
               moves.count("L") == moves.count("R")

if __name__ == "__main__":
    sol = Solution()
    assert sol.judgeCircle("UD")   == True
    assert sol.judgeCircle("LL")   == False
    print("All tests passed v")
