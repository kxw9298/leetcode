# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.ans = 0
        self.getDepth(root)
        return self.ans
    def getDepth(self, root):
        if not root: return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        self.ans = max(self.ans, left + right)
        return 1 + max(left, right)
        