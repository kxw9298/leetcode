# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not root.left: return 1 + r
        if not root.right: return 1 + l
        return 1 + min(l,r)
        # que = collections.deque()
        # que.append(root)
        # depth = 1
        # while que:
        #     size = len(que)
        #     for _ in range(size):
        #         node = que.popleft()
        #         if not node: continue
        #         # this means minimum depth
        #         if not node.left and not node.right:
        #             return depth
        #         que.append(node.left)
        #         que.append(node.right)
        #     depth +=1
        # return depth