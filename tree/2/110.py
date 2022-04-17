# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # O(nlogn)
        # if not root: return True
        # return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 \
        #        and self.isBalanced(root.left) \
        #        and self.isBalanced(root.right)
        
        # O(n)
        self.balanced = True
        def height(root):
            if not root or not self.balanced: return -1
            l = height(root.left)
            r = height(root.right)
            if abs(l-r) > 1:
                self.balanced = False
                return -1
            return max(l, r) + 1
        height(root)
        return self.balanced
    def getDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))