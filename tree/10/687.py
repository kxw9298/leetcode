# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        # self._univaluePath(root)
        self.getPath(root)
        return self.ans
    
    def _univaluePath(self, root):
        if root is None: return 0
        l = self._univaluePath(root.left) if root.left else -1
        r = self._univaluePath(root.right) if root.right else -1
        pl = l + 1 if l >= 0 and root.val == root.left.val else 0
        pr = r + 1 if r >= 0 and root.val == root.right.val else 0
        self.ans = max(self.ans, pl + pr)
        return max(pl, pr)

    def getPath(self, root):
        if not root: return 0
        left = self.getPath(root.left)
        right = self.getPath(root.right)
        pl, pr = 0, 0
        if root.left and root.left.val == root.val: pl = left + 1
        if root.right and root.right.val == root.val: pr = right + 1
        self.ans = max(self.ans, pl + pr)
        return max(pl, pr)