# Problem 102 — Binary Tree Level Order Traversal
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium | Topics: Tree, BFS, Queue
#
# PROBLEM:
#   Return values of each level of a binary tree as a list of lists.
#
# EXAMPLE:
#       3
#      / \
#     9  20
#        / \
#       15   7
#   Output: [[3],[9,20],[15,7]]
#
# IDEA:
#   BFS with a queue. Process one level at a time.
#   For each level: record all values, enqueue all children.
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
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        results = []
        queue   = deque([root])

        while queue:
            level_size   = len(queue)  # number of nodes at this level
            level_values = []

            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                if node.left:  queue.append(node.left)
                if node.right: queue.append(node.right)

            results.append(level_values)

        return results

if __name__ == "__main__":
    sol  = Solution()
    root = TreeNode(3, TreeNode(9),
                       TreeNode(20, TreeNode(15), TreeNode(7)))
    assert sol.levelOrder(root) == [[3],[9,20],[15,7]]
    assert sol.levelOrder(None) == []
    print("All tests passed ✓")
