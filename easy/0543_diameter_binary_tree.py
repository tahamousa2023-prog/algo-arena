# Problem 543 — Diameter of Binary Tree
# Link: https://leetcode.com/problems/diameter-of-binary-tree/
# Difficulty: Easy | Topics: Tree, DFS
#
# PROBLEM:
#   The diameter is the length of the longest path between any two nodes.
#   The path may or may not pass through the root.
#
# EXAMPLE:
#       1
#      / \
#     2   3
#    / \
#   4   5
#   Diameter = 3 (path: 4→2→1→3 or 5→2→1→3)
#
# IDEA:
#   For each node, the longest path through it =
#     depth of left subtree + depth of right subtree
#   We track the global maximum as we do a DFS.
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0

        def depth(node):
            if node is None:
                return 0
            left  = depth(node.left)
            right = depth(node.right)
            # Update diameter: path through this node
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.max_diameter

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert sol.diameterOfBinaryTree(root) == 3
    assert sol.diameterOfBinaryTree(TreeNode(1)) == 0
    print("All tests passed ✓")
