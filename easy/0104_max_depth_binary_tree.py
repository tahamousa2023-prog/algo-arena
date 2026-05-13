# Problem 104 — Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy | Topics: Tree, Recursion, DFS
#
# PROBLEM:
#   Given root of a binary tree, return its maximum depth.
#   Depth = number of nodes along the longest path from root to leaf.
#
# EXAMPLE:
#       3
#      / \
#     9  20
#        / \
#       15   7
#   Output: 3
#
# IDEA:
#   Recursion (DFS). The depth of a tree is:
#     1 + max(depth of left subtree, depth of right subtree)
#   Base case: empty node → depth = 0
#
#   maxDepth(3) = 1 + max(maxDepth(9), maxDepth(20))
#              = 1 + max(1, 2)
#              = 3 ✓
#
# Time : O(n) — visit every node once
# Space: O(h) — call stack depth = tree height

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_depth  = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

if __name__ == "__main__":
    sol = Solution()
    # Build: 3 -> (9, 20 -> (15, 7))
    root = TreeNode(3)
    root.left  = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert sol.maxDepth(root) == 3
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth(TreeNode(1)) == 1
    print("All tests passed ✓")
