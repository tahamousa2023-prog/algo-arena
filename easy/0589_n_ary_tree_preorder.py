# Problem 589 - N-ary Tree Preorder Traversal
# Link: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
# Difficulty: Easy | Topics: Tree, DFS, Stack
#
# PROBLEM:
#   Preorder traversal of N-ary tree: Root then each child subtree left to right.
#
# IDEA:
#   Stack. Push root. Pop, record val, push children in REVERSE order
#   so leftmost child is processed first (LIFO).
#
# Time : O(n) | Space: O(n)

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

class Solution:
    def preorder(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return result

if __name__ == "__main__":
    sol = Solution()
    n5 = Node(5); n6 = Node(6)
    n3 = Node(3, [n5, n6])
    n2 = Node(2); n4 = Node(4)
    n1 = Node(1, [n3, n2, n4])
    assert sol.preorder(n1) == [1,3,5,6,2,4]
    print("All tests passed v")
