# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        self.count = collections.Counter()
        self.inOrder(root)
        freq = max(self.count.values())
        res = []
        for item, c in self.count.items():
            if c == freq:
                res.append(item)
        return res
    
    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.count[root.val] +=1
        self.inOrder(root.right)