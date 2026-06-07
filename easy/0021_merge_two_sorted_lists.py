# ============================================================
#  Problem 021 — Merge Two Sorted Lists
#  Link   : https://leetcode.com/problems/merge-two-sorted-lists/
#  Difficulty: Easy
#  Topics : Linked List
# ============================================================
#
#  PROBLEM STATEMENT
#  -----------------
#  Merge two sorted linked lists and return the merged head.
#
#  Example:
#    Input : 1->4->5  and  1->3->4
#    Output: 1->1->3->4->4->5
#
# ============================================================
#  THINKING PROCESS
# ============================================================
#
#  Like merging two sorted piles of cards:
#    Pick the smaller top card each time.
#    When one pile is empty, attach the rest of the other.
#
#  We use a dummy head node — avoids special-casing first insert.
#
#  Walkthrough: list1=1->4->5, list2=1->3->4
#    pick 1 (list1), pick 1 (list2), pick 3, pick 4 (list1),
#    pick 4 (list2), list2 done ? attach 5
#    Result: 1->1->3->4->4->5 ?
#
#  Time : O(n + m)
#  Space: O(1)
# ============================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy   = ListNode(-1)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next

def make_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    sol = Solution()
    assert to_array(sol.mergeTwoLists(make_list([1,4,5]), make_list([1,3,4]))) == [1,1,3,4,4,5]
    assert to_array(sol.mergeTwoLists(make_list([]),      make_list([0])))      == [0]
    assert to_array(sol.mergeTwoLists(make_list([]),      make_list([])))       == []
    print("All test cases passed ?")
