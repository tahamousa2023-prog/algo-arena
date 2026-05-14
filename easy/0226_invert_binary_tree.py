# Problem 226 — Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy | Topics: Tree, Recursion, DFS
#
# PROBLEM:
#   Given root of a binary tree, invert it (mirror image) and return root.
#
# EXAMPLE:
#   Input :     4          Output:     4
#              / \                    / \
#             2   7                  7   2
#            / \ / \                / \ / \
#           1  3 6  9              9  6 3  1
#
# IDEA:
#   Recursion. To invert a tree:
#     1. Swap left and right children
#     2. Recursively invert both subtrees
#
#   invertTree(4):
#     swap(2, 7) → children are now 7, 2
#     invertTree(7) → swap(6,9)
#     invertTree(2) → swap(1,3)
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Recursively invert both subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)),
                       TreeNode(7, TreeNode(6), TreeNode(9)))
    inverted = sol.invertTree(root)
    assert inverted.val       == 4
    assert inverted.left.val  == 7
    assert inverted.right.val == 2
    print("All tests passed ✓")
