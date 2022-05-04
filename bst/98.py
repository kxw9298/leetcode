# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.valid(root, float('-inf'), float('inf'))
        res = []
        self.inOrder(root, res)
        return res == sorted(res) and len(res) == len(set(res))
    
    def valid(self, root, min, max):
        if not root: return True
        if root.val >= max or root.val <= min:
            return False
        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)
    
    def inOrder(self, root, res):
        if not root: return []
        l = self.inOrder(root.left, res)
        if l: res.extend(l)
        res.append(root.val)
        r = self.inOrder(root.right, res)
        if r: res.extend(r)