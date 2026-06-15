# Problem 079 — Word Search
# Link: https://leetcode.com/problems/word-search/
# Difficulty: Medium | Topics: Array, Backtracking, DFS, Matrix
#
# PROBLEM:
#   Given an m×n grid of characters, return True if the word exists
#   using adjacent (up/down/left/right) cells. Each cell used once.
#
# WHY THIS MATTERS FOR ROBOTICS:
#   This is constrained path search on a grid — same structure as:
#   - Finding feasible trajectories through a maze
#   - Checking if a robot can navigate a sequence of waypoints
#   - Symbolic plan verification on a spatial map
#   The backtracking + visited-marking pattern is universal in planning.
#
# IDEA:
#   DFS + Backtracking from every starting cell.
#   At each step: check if current cell matches word[index].
#   Mark as visited (temporarily), recurse on neighbors, unmark.
#   If we matched all characters → True.
#
# Time : O(n * m * 4^L) — L = word length
# Space: O(L)            — recursion stack depth

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True  # matched all characters
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or board[r][c] != word[idx]):
                return False

            # Mark as visited by temporarily changing the cell
            temp = board[r][c]
            board[r][c] = '#'

            found = (dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1))

            board[r][c] = temp  # restore (backtrack)
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert sol.exist(board1, "ABCCED") == True
    assert sol.exist(board1, "SEE")    == True
    assert sol.exist(board1, "ABCB")   == False
    print("All tests passed ✓")
