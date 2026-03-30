# Problem 111 — Minimum Depth of Binary Tree
# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Difficulty: Easy | Topics: Tree, BFS, DFS
#
# PROBLEM:
#   Return the minimum depth — shortest path from root to a leaf node.
#   A leaf is a node with no children.
#
# EXAMPLE:
#       3
#      / \
#     9  20    → min depth = 2 (root→9)
#        / \
#       15   7
#
# IDEA:
#   BFS level by level. Return depth when first leaf is found.
#   BFS guarantees the first leaf found is the shallowest.
#
# Time : O(n)
# Space: O(n)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth  # first leaf found = minimum depth
            if node.left:  queue.append((node.left,  depth+1))
            if node.right: queue.append((node.right, depth+1))

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3, TreeNode(9),
                       TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.minDepth(root) == 2
    assert sol.minDepth(None) == 0
    assert sol.minDepth(TreeNode(1)) == 1
    print("All tests passed ✓")
