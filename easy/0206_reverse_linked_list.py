# Problem 206 — Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy | Topics: Linked List
#
# PROBLEM:
#   Given the head of a linked list, reverse it and return the new head.
#
# EXAMPLE:
#   Input : 1 -> 2 -> 3 -> 4 -> 5
#   Output: 5 -> 4 -> 3 -> 2 -> 1
#
# IDEA:
#   Walk through the list and reverse each arrow one by one.
#   We need three pointers: prev, current, next
#
#   Walkthrough 1->2->3:
#     prev=None, curr=1
#     save next=2, point 1→None, move: prev=1, curr=2
#     save next=3, point 2→1,    move: prev=2, curr=3
#     save next=None, point 3→2, move: prev=3, curr=None
#     curr is None → stop → return prev (which is 3) ✓
#
# Time : O(n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev    = None
        current = head

        while current:
            next_node    = current.next  # save next before overwriting
            current.next = prev          # reverse the arrow
            prev         = current       # move prev forward
            current      = next_node     # move current forward

        return prev  # prev is now the new head

def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_array(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    sol = Solution()
    assert to_array(sol.reverseList(make_list([1,2,3,4,5]))) == [5,4,3,2,1]
    assert to_array(sol.reverseList(make_list([1,2])))       == [2,1]
    assert to_array(sol.reverseList(make_list([])))          == []
    print("All tests passed ✓")
