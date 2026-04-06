# Problem 145 — Binary Tree Postorder Traversal
# Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
# Difficulty: Easy | Topics: Tree, DFS, Stack
#
# PROBLEM:
#   Return postorder traversal: Left → Right → Root
#
# IDEA:
#   Reverse of a modified preorder (Root→Right→Left).
#   Do preorder but push left before right, then reverse result.
#
# Time : O(n)
# Space: O(n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        result = []
        stack  = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:  stack.append(node.left)   # left pushed last
            if node.right: stack.append(node.right)
        return result[::-1]  # reverse to get Left→Right→Root

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    assert sol.postorderTraversal(root) == [3,2,1]
    assert sol.postorderTraversal(None) == []
    print("All tests passed ✓")
