# Problem 144 — Binary Tree Preorder Traversal
# Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Difficulty: Easy | Topics: Tree, DFS, Stack
#
# PROBLEM:
#   Return preorder traversal of binary tree: Root → Left → Right
#
# EXAMPLE:
#       1
#        \
#         2
#        /
#       3
#   Output: [1,2,3]
#
# IDEA:
#   Iterative with a stack. Push root. Pop → record val.
#   Push right then left (left processed first since stack is LIFO).
#
# Time : O(n)
# Space: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result = []
        stack  = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right: stack.append(node.right)
            if node.left:  stack.append(node.left)
        return result

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert sol.preorderTraversal(root) == [1,2,3]
    assert sol.preorderTraversal(None) == []
    print("All tests passed ✓")
