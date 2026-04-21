# Problem 257 — Binary Tree Paths
# Link: https://leetcode.com/problems/binary-tree-paths/
# Difficulty: Easy | Topics: Tree, DFS, Backtracking
#
# PROBLEM:
#   Return all root-to-leaf paths in a binary tree as strings "1->2->5".
#
# EXAMPLE:
#     1
#    / \
#   2   3
#    \
#     5
#   Output: ["1->2->5","1->3"]
#
# IDEA:
#   DFS. Build path string as we go down.
#   When we reach a leaf → add complete path to result.
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        result = []
        def dfs(node, path):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                result.append(path)
            else:
                dfs(node.left,  path + "->")
                dfs(node.right, path + "->")
        dfs(root, "")
        return result

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
    assert sorted(sol.binaryTreePaths(root)) == sorted(["1->2->5","1->3"])
    assert sol.binaryTreePaths(TreeNode(1))  == ["1"]
    print("All tests passed ✓")
