# Problem 234 — Palindrome Linked List
# Link: https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy | Topics: Linked List, Two Pointers, Recursion
#
# PROBLEM:
#   Return True if a linked list is a palindrome.
#
# EXAMPLE:
#   1→2→2→1 → True
#   1→2     → False
#
# IDEA:
#   Simple approach: collect values into a list, check if it's a palindrome.
#
# Time : O(n)
# Space: O(n)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals: cur.next = ListNode(v); cur = cur.next
    return dummy.next

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(make_list([1,2,2,1])) == True
    assert sol.isPalindrome(make_list([1,2]))      == False
    assert sol.isPalindrome(make_list([1]))        == True
    print("All tests passed ✓")
