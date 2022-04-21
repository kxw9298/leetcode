# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float("-inf")
        self._maxPathSum(root)
        return self.ans
    def _maxPathSum(self, root):
        if not root: return float("-inf")
        l = max(0, self._maxPathSum(root.left))
        r = max(0, self._maxPathSum(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l ,r)