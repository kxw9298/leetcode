# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)
                # root node and not covered
                if not par and node not in covered:
                    self.res +=1
                    covered.update({node, par, node.left, node.right})
                # left or right child not covered
                if node.left not in covered or node.right not in covered:
                    self.res +=1
                    covered.update({node, par, node.left, node.right})
        # from leaf up to root        
        self.res = 0
        covered = {None}
        dfs(root)
        return self.res