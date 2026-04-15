# Problem 203 — Remove Linked List Elements
# Link: https://leetcode.com/problems/remove-linked-list-elements/
# Difficulty: Easy | Topics: Linked List, Recursion
#
# PROBLEM:
#   Remove all nodes with value equal to val from a linked list.
#
# EXAMPLE:
#   1→2→6→3→4→5→6, val=6 → 1→2→3→4→5
#
# IDEA:
#   Use a dummy head to simplify edge cases (val at head).
#   Walk list, skip nodes with matching value.
#
# Time : O(n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1, head)
        curr  = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next  # skip this node
            else:
                curr = curr.next
        return dummy.next

def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals: cur.next = ListNode(v); cur = cur.next
    return dummy.next

def to_array(node):
    res = []
    while node: res.append(node.val); node = node.next
    return res

if __name__ == "__main__":
    sol = Solution()
    assert to_array(sol.removeElements(make_list([1,2,6,3,4,5,6]), 6)) == [1,2,3,4,5]
    assert to_array(sol.removeElements(make_list([]), 1))               == []
    assert to_array(sol.removeElements(make_list([7,7,7,7]), 7))        == []
    print("All tests passed ✓")
