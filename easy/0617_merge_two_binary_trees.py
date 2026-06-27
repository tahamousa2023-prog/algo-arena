# Problem 617 - Merge Two Binary Trees
# Link: https://leetcode.com/problems/merge-two-binary-trees/
# Difficulty: Easy | Topics: Tree, DFS, Recursion
#
# PROBLEM:
#   Merge two trees by overlapping. Overlapping nodes are summed.
#
# IDEA:
#   DFS. Both null -> None. One null -> return other.
#   Both exist -> sum values, recurse on children.
#
# Time : O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val; self.left = left; self.right = right

class Solution:
    def mergeTrees(self, root1, root2):
        if not root1: return root2
        if not root2: return root1
        root1.val  += root2.val
        root1.left  = self.mergeTrees(root1.left,  root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    t2 = TreeNode(2, TreeNode(1), TreeNode(3))
    merged = sol.mergeTrees(t1, t2)
    assert merged.val == 3
    assert merged.left.val == 4
    print("All tests passed v")
