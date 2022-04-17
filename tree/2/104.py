# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maxDepth(root) = max(maxDepth(root.left), maxDepth(root.right)) + 1
        # if not root: return 0
        # l = self.maxDepth(root.left)
        # r = self.maxDepth(root.right)
        # return max(l, r) + 1
        depth = 0
        que = collections.deque()
        que.append(root)
        while que:
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node:
                    continue
                que.append(node.left)
                que.append(node.right)
            depth += 1
        return depth -1