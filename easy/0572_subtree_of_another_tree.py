# Problem 572 — Subtree of Another Tree
# Link: https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy | Topics: Tree, DFS
#
# PROBLEM:
#   Given roots of two trees root and subRoot,
#   return True if subRoot is a subtree of root.
#
# EXAMPLE:
#   root:       3        subRoot:  4
#              / \                / \
#             4   5              1   2
#            / \
#           1   2
#   Output: True  (left subtree of root matches subRoot)
#
# IDEA:
#   Two helper ideas:
#     isSameTree(s, t) → checks if two trees are identical
#     isSubtree(root, sub) → checks every node of root using isSameTree
#
# Time : O(n * m)  n=nodes in root, m=nodes in subRoot
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        # Check left and right subtrees
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return (s.val == t.val and
                self.isSameTree(s.left,  t.left) and
                self.isSameTree(s.right, t.right))

if __name__ == "__main__":
    sol = Solution()
    root    = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    assert sol.isSubtree(root, subRoot) == True

    root2   = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    assert sol.isSubtree(root2, subRoot) == False
    print("All tests passed ✓")
