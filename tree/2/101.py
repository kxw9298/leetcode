# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        # def isMirror(root1, root2):
        #     if not root1 and not root2: return True
        #     if not root1 or not root2: return False
        #     return root1.val == root2.val \
        #       and isMirror(root1.left, root2.right) \
        #       and isMirror(root2.left, root1.right)
        # return isMirror(root.left, root.right)
        
        stack = [(root.left, root.right)]
        while stack:
            l,r = stack.pop()
            if not l and not r:
                continue
            if not l or not r or (l.val != r.val):
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True