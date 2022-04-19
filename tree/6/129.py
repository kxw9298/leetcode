# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = [0]
        self.dfs(root, res, root.val)
        return res[0]
    def dfs(self, root, res, path):
        if not root.left and not root.right:
            res[0] += path
        if root.left:
            self.dfs(root.left, res, path * 10 + root.left.val)
        if root.right:
            self.dfs(root.right, res, path * 10 + root.right.val)