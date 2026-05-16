# Problem 110 — Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/
# Difficulty: Easy | Topics: Tree, DFS
#
# PROBLEM:
#   A tree is height-balanced if for every node, the depth of the
#   left and right subtrees differ by at most 1.
#
# EXAMPLE:
#       3
#      / \
#     9  20
#        / \
#       15   7
#   Output: True (all nodes have |left_depth - right_depth| <= 1)
#
# IDEA:
#   DFS that returns the height of each subtree.
#   If at any point heights differ by more than 1, return -1 (unbalanced).
#   Propagate -1 upward to short-circuit early.
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(node):
            if node is None:
                return 0
            left  = height(node.left)
            right = height(node.right)
            # -1 means "already unbalanced somewhere below"
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return height(root) != -1

if __name__ == "__main__":
    sol = Solution()
    root1 = TreeNode(3, TreeNode(9),
                        TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.isBalanced(root1) == True

    root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)),
                                    TreeNode(3)),
                        TreeNode(2))
    assert sol.isBalanced(root2) == False
    print("All tests passed ✓")
