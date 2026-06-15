# Problem 401 — Binary Watch
# Link: https://leetcode.com/problems/binary-watch/
# Difficulty: Easy | Topics: Bit Manipulation, Backtracking
#
# PROBLEM:
#   A binary watch has 4 LEDs for hours (0-11) and 6 LEDs for minutes (0-59).
#   Given turnedOn = number of LEDs lit, return all possible times.
#
# EXAMPLE:
#   turnedOn=1 → ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
#
# IDEA:
#   Try all valid hours (0-11) and minutes (0-59).
#   Count total 1-bits in (hour, minute) combined.
#   If count == turnedOn → valid time.
#
# Time : O(1) — at most 12*60 = 720 combinations
# Space: O(1)

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        for h in range(12):       # hours: 0 to 11
            for m in range(60):   # minutes: 0 to 59
                # Count total lit LEDs for this (h, m) combination
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append(f"{h}:{m:02d}")   # e.g. "3:05"
        return result

if __name__ == "__main__":
    sol = Solution()
    result = sol.readBinaryWatch(1)
    assert "1:00" in result
    assert "0:01" in result
    assert len(result) == 10

    assert sol.readBinaryWatch(9) == []  # impossible
    print("All tests passed ✓")
