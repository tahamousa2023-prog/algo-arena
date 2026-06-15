# Problem 401 — Binary Watch
# Link: https://leetcode.com/problems/binary-watch/
# Difficulty: Easy | Topics: Bit Manipulation
#
# PROBLEM:
#   Binary watch: 4 LEDs for hours (0-11), 6 LEDs for minutes (0-59).
#   Given turnedOn LEDs, return all possible times "h:mm".
#
# IDEA:
#   Try all (hour, minute) pairs. Count their total 1-bits.
#   If count == turnedOn -> valid time.
#
# Time : O(1) - max 720 combinations
# Space: O(1)

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list:
        result = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    result.append(f"{h}:{m:02d}")
        return result

if __name__ == "__main__":
    sol = Solution()
    result = sol.readBinaryWatch(1)
    assert "1:00" in result
    assert "0:01" in result
    assert len(result) == 10
    print("All tests passed v")
