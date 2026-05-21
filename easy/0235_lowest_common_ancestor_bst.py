# Problem 235 — Lowest Common Ancestor of a BST
# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-bst/
# Difficulty: Easy | Topics: Tree, BST
#
# PROBLEM:
#   Find the lowest common ancestor (LCA) of two nodes in a BST.
#   LCA = lowest node that has both p and q as descendants.
#
# EXAMPLE:
#         6
#        / \
#       2   8
#      / \ / \
#     0  4 7  9
#   LCA(2, 8) = 6
#   LCA(2, 4) = 2
#
# IDEA:
#   In a BST, values are ordered. So:
#   - If both p and q are less than root → LCA is in left subtree
#   - If both p and q are greater → LCA is in right subtree
#   - Otherwise → root is the LCA (they split here)
#
# Time : O(h) — h = height of tree
# Space: O(1)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode,
                              p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left   # both smaller → go left
            elif p.val > root.val and q.val > root.val:
                root = root.right  # both larger  → go right
            else:
                return root        # they split here → this is LCA

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(6,
             TreeNode(2, TreeNode(0), TreeNode(4)),
             TreeNode(8, TreeNode(7), TreeNode(9)))
    assert sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(8)).val == 6
    assert sol.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)).val == 2
    print("All tests passed ✓")
