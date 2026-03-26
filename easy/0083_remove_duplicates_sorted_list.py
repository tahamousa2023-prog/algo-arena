# Problem 083 — Remove Duplicates from Sorted List
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy | Topics: Linked List
#
# PROBLEM:
#   Given a sorted linked list, delete all duplicates so each value appears once.
#
# EXAMPLE:
#   1->1->2       → 1->2
#   1->1->2->3->3 → 1->2->3
#
# IDEA:
#   Walk the list. If current val == next val → skip next node.
#   Otherwise move forward.
#
# Time : O(n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # skip duplicate
            else:
                current = current.next
        return head

def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v); cur = cur.next
    return dummy.next

def to_array(node):
    res = []
    while node:
        res.append(node.val); node = node.next
    return res

if __name__ == "__main__":
    sol = Solution()
    assert to_array(sol.deleteDuplicates(make_list([1,1,2])))       == [1,2]
    assert to_array(sol.deleteDuplicates(make_list([1,1,2,3,3])))   == [1,2,3]
    assert to_array(sol.deleteDuplicates(make_list([])))            == []
    print("All tests passed ✓")
