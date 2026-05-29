# Problem 098 — Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium | Topics: Tree, DFS
#
# PROBLEM:
#   Given root of a binary tree, determine if it is a valid BST.
#   BST: left subtree values < node < right subtree values (for all nodes).
#
# EXAMPLE:
#       2
#      / \
#     1   3
#   Output: True
#
#       5
#      / \
#     1   4      ← 4 is in right subtree but 4 < 5 → INVALID
#        / \
#       3   6
#   Output: False
#
# IDEA:
#   DFS with valid range (min_val, max_val) for each node.
#   Root can be anything: (-inf, +inf)
#   Left child must be: (min_val, node.val)
#   Right child must be: (node.val, max_val)
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, min_val, max_val):
            if node is None:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (validate(node.left,  min_val,   node.val) and
                    validate(node.right, node.val,  max_val))

        return validate(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert sol.isValidBST(root1) == True

    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert sol.isValidBST(root2) == False
    print("All tests passed ✓")
