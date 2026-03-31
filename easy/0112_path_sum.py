# Problem 112 — Path Sum
# Link: https://leetcode.com/problems/path-sum/
# Difficulty: Easy | Topics: Tree, DFS
#
# PROBLEM:
#   Return True if tree has a root-to-leaf path that sums to targetSum.
#
# EXAMPLE:
#         5
#        / \
#       4   8
#      /   / \
#     11  13   4
#    /  \       \
#   7    2       1
#   targetSum=22 → True  (5→4→11→2)
#
# IDEA:
#   DFS. Subtract node value from target as we go down.
#   At a leaf, check if remaining target == 0.
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        remaining = targetSum - root.val
        if not root.left and not root.right:  # leaf node
            return remaining == 0
        return (self.hasPathSum(root.left,  remaining) or
                self.hasPathSum(root.right, remaining))

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(5,
             TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
             TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
    assert sol.hasPathSum(root, 22) == True
    assert sol.hasPathSum(root, 5)  == False
    assert sol.hasPathSum(None, 0)  == False
    print("All tests passed ✓")
