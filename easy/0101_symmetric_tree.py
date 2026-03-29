# Problem 101 — Symmetric Tree
# Link: https://leetcode.com/problems/symmetric-tree/
# Difficulty: Easy | Topics: Tree, DFS, BFS
#
# PROBLEM:
#   Check if a binary tree is a mirror of itself (symmetric around center).
#
# EXAMPLE:
#       1
#      / \
#     2   2   → True (mirror)
#    / \ / \
#   3  4 4  3
#
# IDEA:
#   Recursively check if left subtree mirrors right subtree.
#   Two nodes mirror each other if:
#     - Both are None, OR
#     - Same value AND their children mirror each other crosswise.
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirrors(left, right):
            if left is None and right is None: return True
            if left is None or right is None:  return False
            return (left.val == right.val and
                    mirrors(left.left,  right.right) and
                    mirrors(left.right, right.left))
        return mirrors(root.left, root.right)

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),
                        TreeNode(2, TreeNode(4), TreeNode(3)))
    assert sol.isSymmetric(root1) == True

    root2 = TreeNode(1, TreeNode(2, None, TreeNode(3)),
                        TreeNode(2, None, TreeNode(3)))
    assert sol.isSymmetric(root2) == False
    print("All tests passed ✓")
