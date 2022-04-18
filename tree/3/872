# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        return self.getLeafs(root1) == self.getLeafs(root2)
    
    def getLeafs(self, root):
        res = []
        if not root: return res
        if not root.left and not root.right: return [root.val]
        res.extend(self.getLeafs(root.left))
        res.extend(self.getLeafs(root.right))
        return res