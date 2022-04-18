# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # recursive
        # self.levelOrder(root, res, 0)
        
        # bfs
        
        que = collections.deque()
        que.append(root)
        while que:
            levelVal = []
            size = len(que)
            for _ in range(size):
                node = que.popleft()
                if not node: continue
                levelVal.append(node.val)
                que.append(node.left)
                que.append(node.right)
            if levelVal:
                res.append(levelVal)
            
        return reversed(res)
    
    def levelOrder(self, root, res, level):
        if not root: return
        if level >= len(res):
            res.append([])
        res[level].append(root.val)
        self.levelOrder(root.left, res, level+1)
        self.levelOrder(root.right, res, level+1)