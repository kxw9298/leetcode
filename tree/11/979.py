# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int: 
        def dfs(root, result):
            if not root:
                return 0
            left_edge = dfs(root.left, result) 
            right_edge = dfs(root.right, result)
            result[0] += abs(left_edge) + abs(right_edge)
            return root.val + left_edge + right_edge - 1

        result = [0]
        dfs(root, result)
        return result[0]