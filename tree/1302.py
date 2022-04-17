# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dict = {}
        def dfs(node, dict, depth):
            if not node:
                return
            if depth not in dict:
                dict[depth] = 0
            dict[depth] += node.val
            if node.left:
                dfs(node.left, dict, depth + 1)
            if root.right:
                dfs(node.right, dict, depth + 1)
        dfs(root, dict, 0)
        return dict[max(dict.keys())]