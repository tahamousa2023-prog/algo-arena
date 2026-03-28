# Problem 100 — Same Tree
# Link: https://leetcode.com/problems/same-tree/
# Difficulty: Easy | Topics: Tree, DFS, BFS
#
# PROBLEM:
#   Given roots of two binary trees, check if they are structurally
#   identical with the same node values.
#
# EXAMPLE:
#   [1,2,3] and [1,2,3] → True
#   [1,2]   and [1,null,2] → False
#
# IDEA:
#   Recursion. Two trees are the same if:
#     1. Both are None
#     2. Both have same val AND left subtrees match AND right subtrees match
#
# Time : O(n)
# Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (p.val == q.val and
                self.isSameTree(p.left,  q.left) and
                self.isSameTree(p.right, q.right))

if __name__ == "__main__":
    sol = Solution()
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    t2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(t1, t2) == True

    t3 = TreeNode(1, None, TreeNode(2))
    t4 = TreeNode(1, TreeNode(2))
    assert sol.isSameTree(t3, t4) == False
    print("All tests passed ✓")
