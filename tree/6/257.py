# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        res = []
        # self.dfs(root, res, str(root.val))
        
        stack = []
        stack.append((root, str(root.val)))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val) ))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
        
        return res
    
    def dfs(self, root, res, path):
        # if not root: return
        if not root.left and not root.right:
            res.append(path)
        if root.left:
            self.dfs(root.left, res, path + '->' + str(root.left.val))
        if root.right:
            self.dfs(root.right, res, path + '->' + str(root.right.val))