# Problem 141 — Linked List Cycle
# Link: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy | Topics: Linked List, Two Pointers
#
# PROBLEM:
#   Return True if a linked list has a cycle.
#
# IDEA:
#   Floyd's Cycle Detection — "tortoise and hare".
#   Slow pointer moves 1 step, fast pointer moves 2 steps.
#   If they meet → there's a cycle.
#   If fast reaches None → no cycle.
#
# Time : O(n)
# Space: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val  = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    # No cycle
    a = ListNode(1, ListNode(2, ListNode(3)))
    assert sol.hasCycle(a) == False

    # Cycle: 3→2
    b = ListNode(1)
    b2 = ListNode(2)
    b3 = ListNode(3)
    b.next = b2; b2.next = b3; b3.next = b2
    assert sol.hasCycle(b) == True
    print("All tests passed ✓")
