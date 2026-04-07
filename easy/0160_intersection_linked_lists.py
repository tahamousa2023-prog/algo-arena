# Problem 160 — Intersection of Two Linked Lists
# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Difficulty: Easy | Topics: Linked List, Two Pointers, Hash Table
#
# PROBLEM:
#   Find the node where two linked lists intersect.
#   Return None if they don't intersect.
#
# IDEA:
#   Two pointers. When pointer A reaches end → redirect to head of B.
#   When pointer B reaches end → redirect to head of A.
#   They will meet at intersection (or both reach None if no intersection).
#   Both travel same total distance: len(A) + len(B).
#
# Time : O(m+n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a  # intersection node or None

if __name__ == "__main__":
    sol = Solution()
    # Shared tail: 8→4→5
    shared = ListNode(8, ListNode(4, ListNode(5)))
    A = ListNode(4, ListNode(1, shared))
    B = ListNode(5, ListNode(6, ListNode(1, shared)))
    assert sol.getIntersectionNode(A, B) is shared

    # No intersection
    C = ListNode(1, ListNode(2))
    D = ListNode(3)
    assert sol.getIntersectionNode(C, D) is None
    print("All tests passed ✓")
