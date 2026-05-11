# Problem 020 — Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy | Topics: String, Stack
#
# PROBLEM:
#   Given a string of brackets, return True if they are valid.
#   Every open bracket must be closed in the correct order.
#
# EXAMPLE:
#   Input : "()[]{}"  → True
#   Input : "([)]"    → False
#   Input : "{[]}"    → True
#
# IDEA:
#   Use a stack.
#   When we see an opening bracket → push it.
#   When we see a closing bracket → check if top of stack matches.
#   If stack is empty at the end → all brackets matched ✓
#
#   Walkthrough "{[]}":
#     see { → stack=[{]
#     see [ → stack=[{, []
#     see ] → top is [ → match! stack=[{]
#     see } → top is { → match! stack=[]
#     stack empty → True ✓
#
# Time : O(n)
# Space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                # Closing bracket — stack must have the matching opener
                if not stack or stack[-1] != matches[char]:
                    return False
                stack.pop()

        return len(stack) == 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()")     == True
    assert sol.isValid("()[]{}")  == True
    assert sol.isValid("(]")     == False
    assert sol.isValid("([)]")   == False
    assert sol.isValid("{[]}")   == True
    assert sol.isValid("")       == True
    print("All tests passed ✓")
